# 1. 시스템 및 환경 관련 라이브러리
import os
import random

# 2. 데이터 분석 및 처리 라이브러리
import pandas as pd
import numpy as np
import koreanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import easydict

# 3. 머신러닝 관련 라이브러리
from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV,
    StratifiedKFold  # ✅ StratifiedKFold 추가
)
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import roc_curve, auc, confusion_matrix  # ✅ confusion_matrix 추가
from sklearn.model_selection import cross_val_score

# LightGBM 라이브러리
import lightgbm as lgb

# 날짜 및 시간 관련 라이브러리
from datetime import datetime, timezone, timedelta

# 한국 시간대 설정
kst = timezone(timedelta(hours=9))

today = datetime.now(kst).strftime('%m%d')

def reset_seeds(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
def load_data():
    # 데이터 폴더 경로 설정
    data_path = Path("data/")
    file_path = data_path / "customer_churn_telecom_services.csv"  # CSV 파일 경로

    # 파일이 존재하는지 확인
    if not file_path.exists():
        raise FileNotFoundError(f"파일이 존재하지 않습니다: {file_path}")

    # CSV 파일 로드
    df = pd.read_csv(file_path)
    return df  # DataFrame 반환

# ✅ 사용 예시
data = load_data()

args = easydict.EasyDict()

# ✅ 로컬 경로 설정 (VS Code에서는 로컬 PC 경로를 사용)
args.default_path = Path("C:/dev/github/SKN10-2nd-3Team-1/data")  
args.data_csv = args.default_path / "customer_churn_telecom_services.csv"

# ✅ 결과 저장 경로 (로컬 PC에 저장할 경로)
history_results_dir = Path("C:/dev/github/SKN10-2nd-3Team-1/")
history_results_path = history_results_dir / "history_results.csv"

# 기타 설정
args.random_seed = 42
args.results = []  # 결과 저장 리스트

ori_data=pd.read_csv(args.data_csv)

# train 데이터와 test 데이터로 나눔
reset_seeds()
ori_tr, ori_te = train_test_split(ori_data, test_size=0.2, stratify=ori_data['Churn'], random_state=args.random_seed)

# ori_tr을 학습용과 검증용으로 나눔
train, test = train_test_split(ori_tr, test_size=0.2, stratify=ori_tr['Churn'], random_state=args.random_seed)

# 결측치 제거

# ori_te는 나중에 테스트 할 데이터
median_value_ori_te = ori_te["TotalCharges"].median()
ori_te['TotalCharges'].fillna(median_value_ori_te, inplace=True)
# train은 ori_tr중 학습용으로 나눈 데이터
median_value_train = train["TotalCharges"].median()
train['TotalCharges'].fillna(median_value_train, inplace=True)
# test는 ori_tr중 검증용으로 나눈 데이터
median_value_test = test["TotalCharges"].median()
test['TotalCharges'].fillna(median_value_test, inplace=True)

# Fiber optic이면 1, 아니면 0으로 변환 ( Fiber optic 서비스 이용자와 아닌 사람들로 새로 특성 만듦 )
train["Fiber_Optic"] = (train["InternetService"] == "Fiber optic").astype(int)
test["Fiber_Optic"] = (test["InternetService"] == "Fiber optic").astype(int)
ori_te["Fiber_Optic"] = (ori_te["InternetService"] == "Fiber optic").astype(int)

# Fiber_Optic 새로 만들었으므로 기존 컬럼 삭제
train.drop(["InternetService"], axis=1, inplace=True)
test.drop(["InternetService"], axis=1, inplace=True)
ori_te.drop(["InternetService"], axis=1, inplace=True)

train["No_Phoneservice"] = (train["PhoneService"] == 0).astype(int)
test["No_Phoneservice"] = (test["PhoneService"] == 0).astype(int)
ori_te["No_Phoneservice"] = (ori_te["PhoneService"] == 0).astype(int)

train["No_Multiple"] = ((train["PhoneService"] == 1) & (train["MultipleLines"] == "No")).astype(int)
test["Multiple"] = ((test["PhoneService"] == 1) & (test["MultipleLines"] == "Yes")).astype(int)
ori_te["Multiple"] = ((ori_te["PhoneService"] == 1) & (ori_te["MultipleLines"] == "Yes")).astype(int)

# 범주형
cat_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'Churn']
# 연속형
num_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']

# object 데이터들을 category로 변환
for df in [train, test, ori_te]:
    df[cat_features] = df[cat_features].astype('category')

# 인코딩 하면서 Auto끼리 묶고 check 끼리 묶어줌
train['AutoPayment'] = train['PaymentMethod'].replace({
    'Credit card (automatic)': 1,
    'Bank transfer (automatic)': 1,
    'Electronic check': 0,
    'Mailed check': 0
})
test['AutoPayment'] = test['PaymentMethod'].replace({
    'Credit card (automatic)': 1,
    'Bank transfer (automatic)': 1,
    'Electronic check': 0,
    'Mailed check': 0
})

ori_te['AutoPayment'] = ori_te['PaymentMethod'].replace({
    'Credit card (automatic)': 1,
    'Bank transfer (automatic)': 1,
    'Electronic check': 0,
    'Mailed check': 0
})
# monthtomonth 컬럼 만들면서 1년,2년짜리들은 묶어버림
train["MonthToMonth"] = (train["Contract"] == "Month-to-month").astype(int)
test["MonthToMonth"] = (test["Contract"] == "Month-to-month").astype(int)
ori_te["MonthToMonth"] = (ori_te["Contract"] == "Month-to-month").astype(int)

train["No_Phoneservice"] = (train["PhoneService"] == 0).astype(int)
test["No_Phoneservice"] = (test["PhoneService"] == 0).astype(int)
ori_te["No_Phoneservice"] = (ori_te["PhoneService"] == 0).astype(int)

y_tr = train['Churn']
X_tr = train.drop(['Churn'], axis=1)

y_te = test['Churn']
X_te = test.drop(['Churn'], axis=1)
ori_te = ori_te.drop('Churn', axis=1)

reset_seeds()

model_name = 'model_lgbm_V2'

parameters = {
    'random_state' : args.random_seed
}

model_lgbm_V2 = lgb.LGBMClassifier(**parameters)

print(f'{model_lgbm_V2} : {X_tr.shape} / {y_tr.shape}')
model_lgbm_V2.fit(X_tr, y_tr)

reset_seeds()

# Light GBM 모델
# - Train data
score_tr_lgbm = model_lgbm_V2.score(X_tr, y_tr)
# - Test data
score_te_lgbm = model_lgbm_V2.score(X_te, y_te)

print(f'{model_lgbm_V2} : {score_tr_lgbm}, {score_te_lgbm}')

# 1️⃣ 모델 예측 확률 가져오기
y_pred = model_lgbm_V2.predict_proba(X_te)[:, 1]  # 1일 확률 (이탈 확률)

y_te = y_te.map({'No': 0, 'Yes': 1})
# 2️⃣ AUC 계산
fpr, tpr, thresholds = roc_curve(y_te, y_pred)
auc_te = auc(fpr, tpr)
print(f'{model_lgbm_V2}: AUC = {auc_te:.4f}')

# 3️⃣ Threshold 조정 후 새로운 예측값 생성
threshold = 0.4  # 기본 0.5에서 0.4로 조정
y_pred_class = (y_pred >= threshold).astype(int)

# 4️⃣ 혼동행렬 계산
norm_conf_mx = confusion_matrix(y_te, y_pred_class, normalize="true")

# 5️⃣ 혼동행렬 시각화
plt.figure(figsize=(7, 5))
sns.heatmap(norm_conf_mx, annot=True, cmap="coolwarm", linewidth=0.5, fmt=".2f")

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title(f'Confusion Matrix (Threshold = {threshold})')
plt.show()