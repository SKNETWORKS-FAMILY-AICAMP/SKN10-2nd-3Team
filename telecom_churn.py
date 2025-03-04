import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, log_loss
from imblearn.over_sampling import SMOTE

# 데이터 로드 및 전처리
df = pd.read_csv("customer_churn_telecom_services.csv")
df.columns = [col.lower() for col in df.columns]

df["churn"] = df["churn"].map({"No": 0, "Yes": 1})
df["totalcharges"] = df["totalcharges"].replace(" ", np.nan).astype(float)
df.loc[:, "totalcharges"] = df["totalcharges"].fillna(df["totalcharges"].median())

label_cols = ["gender", "partner", "dependents", "phoneservice", "paperlessbilling"]
for col in label_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

one_hot_cols = ["multiplelines", "internetservice", "onlinesecurity", "onlinebackup",
                "deviceprotection", "techsupport", "streamingtv", "streamingmovies",
                "contract", "paymentmethod"]
df = pd.get_dummies(df, columns=one_hot_cols, drop_first=True)

# 1년 미만 가입 고객 여부 추가
df["is_short_tenure"] = (df["tenure"] < 12).astype(int)

X = df.drop(columns=["churn"])
y = df["churn"]

smote = SMOTE(sampling_strategy="auto", random_state=42)

# Epoch 횟수 설정
num_epochs = 5  # 🔥 여러 번 학습 (Epoch 개념 적용)

# 모델 초기화 (한 번만 실행)
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(eval_metric="logloss", random_state=42)
}

# 결과 저장을 위한 딕셔너리
results = {name: {"accuracy": [], "precision": [], "recall": [], "f1_score": [], "log_loss": []}
           for name in models.keys()}

# 모델 학습 및 평가 (데이터셋만 변경, 모델 유지)
for epoch in range(num_epochs):
    print(f"\n🔄 Epoch {epoch + 1} / {num_epochs}")

    # 🔥 매 Epoch마다 새로운 데이터 샘플링 (train_test_split을 다시 실행)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2,
                                                        random_state=np.random.randint(0, 10000))

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    for name, model in models.items():
        print(f"\n🔹 Training {name} (Epoch {epoch + 1})...")

        # 🔥 기존 모델 유지 & 새 데이터로 추가 학습
        model.fit(X_train, y_train)  # 모델을 유지한 채 새로운 데이터로 학습

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

        # 🔥 터미널에 결과 출력 추가
        print(f"✅ {name} Results (Epoch {epoch + 1}):")
        print(f"  Accuracy: {acc:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1:.4f}, Log Loss: {loss:.4f}\n")

# 📌 개별 지표별 성능 변화 시각화
metrics = ["accuracy", "precision", "recall", "f1_score", "log_loss"]
for metric in metrics:
    plt.figure(figsize=(10, 6))
    for name in models.keys():
        sns.lineplot(x=range(1, num_epochs + 1), y=results[name][metric], marker='o', linestyle='-', label=f"{name} {metric}")
    
    plt.xlabel("Epochs")
    plt.ylabel(f"{metric.capitalize()} Score")
    plt.title(f"Model {metric.capitalize()} Across Epochs")
    plt.legend()
    plt.grid(True)
    plt.show()

# 📌 Feature Importance 분석 (RandomForest & XGBoost)
feature_importance = {}

for name, model in models.items():
    if hasattr(model, "feature_importances_"):  # RandomForest, XGBoost 지원
        feature_importance[name] = model.feature_importances_

for name in feature_importance:
    sorted_idx = np.argsort(feature_importance[name])[::-1]
    plt.figure(figsize=(10, 6))
    sns.barplot(x=np.array(X.columns)[sorted_idx][:10], y=feature_importance[name][sorted_idx][:10])
    plt.xlabel("Features")
    plt.ylabel("Importance Score")
    plt.title(f"Top 10 Feature Importance ({name})")
    plt.xticks(rotation=45)
    plt.show()

# 📌 SHAP 분석 (XGBoost 모델 사용)
explainer = shap.Explainer(models["XGBoost"], X_train)
shap_values = explainer(X_test)

# 📌 SHAP Summary Plot (Scatter)
shap.summary_plot(shap_values, X_test, feature_names=X.columns.tolist())  # 🔥 Feature 이름 반영

# 📌 SHAP Summary Plot (Bar Chart)
shap.summary_plot(shap_values, X_test, plot_type="bar", feature_names=X.columns.tolist())  # 🔥 Feature 이름 반영

