import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import shap
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, log_loss, confusion_matrix, roc_curve, auc
from imblearn.over_sampling import SMOTE

# 여기에 자신의 .csv경로를 입력하고 타겟 컬럼이름으로 수정해야합니다.
########################################################################################
# 데이터 로드 및 전처리
df = pd.read_csv("my_dataset.csv")  # 데이터 셋 경로

df = df.drop(columns=["Unnamed: 0"])

X = df.drop(columns=["Churn"])  # 타겟 컬럼
y = df["Churn"] # 타겟 컬럼
########################################################################################
# 아래부터는 건들지 않아도 됩니다.
smote = SMOTE(sampling_strategy="auto", random_state=42)

# Epoch 횟수 설정
num_epochs = 10  # 🔥 여러 번 학습 (Epoch 개념 적용)

# 모델 초기화 (한 번만 실행)
models = {
    # "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    # "XGBoost": XGBClassifier(eval_metric="logloss", random_state=42),
    "Logistic Regression": LogisticRegression(),
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
    X_resampled, y_resampled = smote.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2,
                                                        random_state=np.random.randint(0, 10000))

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

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
    plt.figure(figsize=(10, 6))
    for name in models.keys():
        sns.lineplot(x=range(1, num_epochs + 1), y=results[name][metric], marker='o', linestyle='-', label=f"{name} {metric}")
    
    plt.xlabel("Epochs")
    plt.ylabel(f"{metric.capitalize()} Score")
    plt.title(f"Model {metric.capitalize()} Across Epochs")
    plt.legend()
    plt.grid(True)
    plt.show()

# 📌 Feature Importance 분석
feature_importance = {}

for name, model in models.items():
    if hasattr(model, "feature_importances_"):  # RandomForest, XGBoost 지원
        feature_importance[name] = model.feature_importances_
    elif hasattr(model, "coef_"):  # Logistic Regression 지원
        feature_importance[name] = np.abs(model.coef_[0])  # 절댓값으로 중요도 변환

for name in feature_importance:
    sorted_idx = np.argsort(feature_importance[name])[::-1]
    plt.figure(figsize=(10, 6))
    sns.barplot(x=np.array(X.columns)[sorted_idx][:10], y=feature_importance[name][sorted_idx][:10])
    plt.xlabel("Features")
    plt.ylabel("Importance Score")
    plt.title(f"Top 10 Feature Importance ({name})")
    plt.xticks(rotation=45)
    plt.show()

# 📌 혼동 행렬 시각화
plt.figure(figsize=(15, 5))
for i, (name, matrix) in enumerate(conf_matrices.items()):
    plt.subplot(1, len(models), i + 1)
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["No Churn", "Churn"], yticklabels=["No Churn", "Churn"])
    plt.title(f"Confusion Matrix: {name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

plt.tight_layout()
plt.show()

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
plt.show()