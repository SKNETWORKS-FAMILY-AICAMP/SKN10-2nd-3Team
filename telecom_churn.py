import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier, StackingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix, precision_recall_curve

# 1. 데이터 로드 및 전처리 (Feature Engineering 추가)
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.loc[:, 'TotalCharges'] = df['TotalCharges'].fillna(0)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # Feature Engineering: tenure 구간화 및 새로운 변수 추가
    df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 36, 72], labels=["Short", "Medium", "Long"])
    df['MonthlyCharge_group'] = pd.cut(df['MonthlyCharges'], bins=[0, 30, 70, 120], labels=["Low", "Medium", "High"])
    df['AvgMonthlyCharge'] = df['TotalCharges'] / (df['tenure'] + 1)
    
    df_encoded = pd.get_dummies(df, columns=[
        'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 
        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 
        'PaymentMethod', 'tenure_group', 'MonthlyCharge_group'
    ], drop_first=True)
    
    scaler = MinMaxScaler()
    df_encoded[['tenure', 'MonthlyCharges', 'TotalCharges', 'AvgMonthlyCharge']] = scaler.fit_transform(
        df_encoded[['tenure', 'MonthlyCharges', 'TotalCharges', 'AvgMonthlyCharge']]
    )
    return df_encoded

# 2. 데이터 분할 및 SMOTE 적용
def split_and_balance_data(df_encoded):
    X = df_encoded.drop(columns=['Churn'])
    y = df_encoded['Churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    smote = SMOTE(sampling_strategy=0.8, random_state=42)  # SMOTE 강도 조정
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    
    # Feature Selection: 변수 중요도 분석 후 하위 1%만 제거 (Precision 개선)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_resampled, y_train_resampled)
    feature_importance = rf.feature_importances_
    important_features = X_train.columns[np.argsort(feature_importance)[-int(len(feature_importance) * 0.99):]]
    
    return X_train_resampled[important_features], X_test[important_features], y_train_resampled, y_test

# 3. 하이퍼파라미터 최적화 (RandomizedSearchCV 사용)
def hyperparameter_tuning(X_train, y_train):
    rf_params = {
        'n_estimators': [200, 300, 400],
        'max_depth': [7, 10, 15],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'class_weight': [{0: 1, 1: 3}]  # 이탈 고객 감지 강화
    }
    rf_grid = RandomizedSearchCV(RandomForestClassifier(random_state=42), rf_params, n_iter=10, cv=5, scoring='f1', n_jobs=-1, random_state=42)
    rf_grid.fit(X_train, y_train)
    best_rf = rf_grid.best_estimator_
    
    xgb_params = {
        'n_estimators': [300, 400, 500],
        'max_depth': [6, 8, 10],
        'learning_rate': [0.01, 0.03, 0.05],
        'subsample': [0.7, 0.9, 1.0]
    }
    xgb_grid = RandomizedSearchCV(XGBClassifier(random_state=42), xgb_params, n_iter=10, cv=5, scoring='f1', n_jobs=-1, random_state=42)
    xgb_grid.fit(X_train, y_train)
    best_xgb = xgb_grid.best_estimator_
    
    return best_rf, best_xgb

# 4. 최적의 Stacking + Voting 앙상블 모델 학습 및 Threshold 최적화
def train_stacking_voting(X_train, X_test, y_train, y_test, best_rf, best_xgb):
    stacking_clf = StackingClassifier(
        estimators=[
            ('Random Forest', best_rf),
            ('XGBoost', best_xgb),
            ('SVM', SVC(kernel='rbf', probability=True, random_state=42))
        ],
        final_estimator=XGBClassifier(n_estimators=400, max_depth=8, learning_rate=0.03, random_state=42)
    )
    
    voting_clf = VotingClassifier(
        estimators=[('Stacking', stacking_clf), ('XGBoost', best_xgb), ('Random Forest', best_rf)],
        voting='soft',
        weights=[1, 2, 2]  # 랜덤 포레스트와 XGBoost 균형 조정
    )
    
    voting_clf.fit(X_train, y_train)
    y_probs = voting_clf.predict_proba(X_test)[:, 1]
    precision, recall, thresholds = precision_recall_curve(y_test, y_probs)
    best_threshold = thresholds[np.argmin(np.abs(precision - recall))]  # Precision과 Recall 균형 유지
    y_pred_adjusted = (y_probs >= best_threshold).astype(int)
    
    return {
        'Accuracy': accuracy_score(y_test, y_pred_adjusted),
        'Precision': precision_score(y_test, y_pred_adjusted),
        'Recall': recall_score(y_test, y_pred_adjusted),
        'F1 Score': f1_score(y_test, y_pred_adjusted),
        'Confusion Matrix': confusion_matrix(y_test, y_pred_adjusted),
        'Classification Report': classification_report(y_test, y_pred_adjusted)
    }

# 실행 코드
if __name__ == "__main__":
    file_path = r"C:\\dev\\python\\파이썬 미니 프로젝트2\\customer_churn_telecom_services.csv"
    df_encoded = load_and_preprocess_data(file_path)
    X_train, X_test, y_train, y_test = split_and_balance_data(df_encoded)
    
    print("\n🚀 하이퍼파라미터 튜닝 진행 중...")
    best_rf, best_xgb = hyperparameter_tuning(X_train, y_train)
    
    print("\n🔥 최적의 Stacking + Voting 모델 평가")
    ensemble_results = train_stacking_voting(X_train, X_test, y_train, y_test, best_rf, best_xgb)
    for metric, value in ensemble_results.items():
        print(f"{metric}: {value}")
