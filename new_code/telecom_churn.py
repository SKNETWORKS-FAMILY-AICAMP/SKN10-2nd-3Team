import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, log_loss, confusion_matrix, roc_curve, auc

# 데이터 로드 및 전처리
df = pd.read_csv("data/raw.csv")

## drop id
df.drop(columns = 'customerID', inplace = True)

## fill na
df = df.replace(r'^\s*$', np.nan, regex=True)
df['TotalCharges'] = df['TotalCharges'].astype(float)
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())

## label encoding
lab_features = ['StreamingTV', 'StreamingMovies',
                 'OnlineSecurity', 'OnlineBackup','DeviceProtection',]
normal_cols = list(set(df.columns) - set(lab_features))
label_encoders = {}
temp_df = df.copy()
for feature in lab_features:
    label_encoders[feature] = LabelEncoder()
    try:
        # Fit and transform the feature
        temp_df[feature] = label_encoders[feature].fit_transform(temp_df[feature])
    except ValueError as e:
        print(f"Warning: Issue encountered while encoding {feature}")
        print(str(e))
available_cols = sorted([col for col in normal_cols if col in df.columns])
df = temp_df[available_cols + lab_features].copy()

## dummy encoding
dum_features = ['PaymentMethod',
                    'MultipleLines', 'InternetService', 'Contract',
                    'TechSupport']
temp_df = df.copy()
normal_cols = list(set(df.columns) - set(dum_features))
dummies_df = pd.get_dummies(temp_df[dum_features], prefix=dum_features)
available_cols = sorted([col for col in normal_cols if col in df.columns])
df = pd.concat(
        [temp_df[available_cols].reset_index(drop=True), 
         dummies_df.reset_index(drop=True)],
        axis=1
    ).reset_index(drop=True)

## yn encoding
yn_features = ['gender', 'Partner', 'Dependents','PhoneService', 'PaperlessBilling','Churn']
for feature in yn_features:
    df[feature] = df[feature].apply(lambda x: 1 if x in ['Yes','Female'] else 0)


X = df.drop(columns=["Churn"])
y = df["Churn"]


# Epoch 횟수 설정
num_epochs = 10  # 🔥 여러 번 학습 (Epoch 개념 적용)

# 모델 초기화 (한 번만 실행)
models = {
    #"Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(colsample_bytree= 0.9, learning_rate= 0.1, max_depth= 3, n_estimators= 50, subsample= 0.7, random_state=42),
    #"Logistic Regression": LogisticRegression(),
}

# 결과 저장을 위한 딕셔너리
results = {name: {"accuracy": [], "precision": [], "recall": [], "f1_score": [], "log_loss": []}
           for name in models.keys()}

# 혼동 행렬 & ROC-AUC 저장
conf_matrices = {}
roc_curves = {}

# 모델 학습 및 평가 (데이터셋만 변경, 모델 유지)
for epoch in range(num_epochs):
    print(f"\n🔄 Epoch {epoch + 1} / {num_epochs}")

    # 🔥 매 Epoch마다 새로운 데이터 샘플링 (train_test_split을 다시 실행)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=np.random.randint(0, 10000))



    for name, model in models.items():
        print(f"\n🔹 Training {name} (Epoch {epoch + 1})...")

        # 🔥 기존 모델 유지 & 새 데이터로 추가 학습
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]

        acc = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        loss = log_loss(y_test, y_pred_proba)

        results[name]["accuracy"].append(acc)
        results[name]["precision"].append(precision)
        results[name]["recall"].append(recall)
        results[name]["f1_score"].append(f1)
        results[name]["log_loss"].append(loss)

        # 🔥 혼동 행렬 저장
        conf_matrices[name] = confusion_matrix(y_test, y_pred)

        # 🔥 ROC-AUC 저장
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_curves[name] = (fpr, tpr, auc(fpr, tpr))

        print(f"✅ {name} Results (Epoch {epoch + 1}):")
        print(f"  Accuracy: {acc:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1:.4f}, Log Loss: {loss:.4f}\n")

# 📌 개별 지표별 성능 변화 시각화
metrics = ["accuracy", "precision", "recall", "f1_score", "log_loss"]
for metric in metrics:
    plt.figure(figsize=(6, 6))
    for name in models.keys():
        sns.lineplot(x=range(1, num_epochs + 1), y=results[name][metric], marker='o', linestyle='-', label=f"{name} {metric}")
    
    plt.xlabel("Epochs")
    plt.ylabel(f"{metric.capitalize()} Score")
    plt.title(f"Model {metric.capitalize()} Across Epochs")
    plt.legend()
    plt.grid(True)
    plt.savefig('screenshot_xgboost/metrics_xgboost.png')
    #plt.show()

# 📌 Feature Importance 분석
feature_importance = {}

for name, model in models.items():
    if hasattr(model, "feature_importances_"):  # RandomForest, XGBoost 지원
        feature_importance[name] = model.feature_importances_

for name in feature_importance:
    sorted_idx = np.argsort(feature_importance[name])[::-1]
    plt.figure(figsize=(12, 6))
    sns.barplot(x=np.array(X.columns)[sorted_idx][:10], y=feature_importance[name][sorted_idx][:10])
    plt.xlabel("Features")
    plt.ylabel("Importance Score")
    plt.title(f"Top 10 Feature Importance ({name})")
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.2)
    plt.tight_layout()
    plt.savefig('screenshot_xgboost/feature_importance_xgboost.png')
    plt.show()

# 📌 혼동 행렬 시각화
plt.figure(figsize=(5, 5))
for i, (name, matrix) in enumerate(conf_matrices.items()):
    plt.subplot(1, len(models), i + 1)
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["No Churn", "Churn"], yticklabels=["No Churn", "Churn"])
    plt.title(f"Confusion Matrix: {name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

plt.tight_layout()
plt.savefig('screenshot_xgboost/confusion_matrix_xgboost.png')
#plt.show()

# 📌 ROC-AUC Curve 시각화
plt.figure(figsize=(8, 6))
for name, (fpr, tpr, roc_auc) in roc_curves.items():
    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.4f})")

plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC-AUC Curve")
plt.legend()
plt.grid(True)
plt.savefig('screenshot_xgboost/roc_auc_curve_xgboost.png')
#plt.show()