import pandas as pd
import numpy as np

# 로컬에 데이터셋이 있다면, 아래와 같이 로드합니다.
df = pd.read_csv('./data/my_dataset.csv')

df = df.drop(columns=["Unnamed: 0"])
print(df.head())

# X와 y를 나눠줍니다.
X = df.drop(columns=["Churn"])
y = df["Churn"]


from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import cross_val_score

# 데이터셋을 나눕니다.
x_train, x_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# SMOTE로 클래스 불균형 처리
smt = SMOTE(random_state=42)
x_train_resampled, y_train_resampled = smt.fit_resample(x_train, y_train)

print(x_train_resampled.shape, y_train_resampled.shape)


from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from sklearn.model_selection import KFold

import optuna
from optuna.samplers import TPESampler
optuna.logging.disable_default_handler()

class Objective:
    def __init__(self,x_train,y_train,seed):

        self.x_train = x_train
        self.y_train = y_train
        self.seed = seed
        num_folds=10 # 학습시간을 줄이기 위해 2로 하였다. 일반적으로는 5
        self.cv = KFold(n_splits=num_folds,shuffle=True,random_state=self.seed)

    def __call__(self,trial):

        hp = {
            "max_depth" : trial.suggest_int("max_depth", 1, 10),
            "min_samples_split" : trial.suggest_int("min_samples_split", 2, 5),
            "criterion" : trial.suggest_categorical("criterion",["gini","entropy"]),
            "max_leaf_nodes" : trial.suggest_int("max_leaf_nodes",2,10),
            "n_estimators" : trial.suggest_int("n_estimators",500,1500,50),
            "learning_rate" : trial.suggest_float("learning_rate", 0.01, 0.1),
            "verbose": trial.suggest_categorical("verbose",[-1])
        }
        # model
        model = LGBMClassifier(random_state=self.seed,**hp)
        # cross validation
        scores = cross_val_score(model,self.x_train,self.y_train, cv = self.cv , scoring="roc_auc")
        return np.mean(scores)

sampler = TPESampler(seed=42) # 대체모델 부분

# 스터디 객체
study = optuna.create_study(
    direction = "maximize", # maximize or minimize
    sampler = sampler
)
objective = Objective(x_train_resampled, y_train_resampled, 42)
study.optimize(objective, n_trials=50)

print("Best Score:", study.best_value) # 최고점수
print("Best hp", study.best_params) # 최고점수의 하이퍼파라미터조합

# 최적 하이퍼파라미터로 LGBM 모델 설정 및 학습
model = LGBMClassifier(random_state=42, **study.best_params)
model.fit(x_train_resampled, y_train_resampled)

# 예측 및 성능 평가
y_train_pred = model.predict(x_train_resampled)
y_test_pred = model.predict(x_test)

print("Accuracy Score of Model on Training Data is =>", round(accuracy_score(y_train_resampled, y_train_pred)*100, 2), "%")
print("Accuracy Score of Model on Testing Data is =>", round(accuracy_score(y_test, y_test_pred)*100, 2), "%")

print("F1 Score of the Model is =>", f1_score(y_test, y_test_pred, average="micro"))
print("Recall Score of the Model is =>", recall_score(y_test, y_test_pred, average="micro"))
print("Precision Score of the Model is =>", precision_score(y_test, y_test_pred, average="micro"))


import joblib

# 모델 저장
joblib.dump(model, 'lgbm_model.pkl')

# 모델 로드
loaded_model = joblib.load('lgbm_model.pkl')

# 로드한 모델을 사용하여 예측
y_pred = loaded_model.predict(x_test)
print(f"Prediction on test data: {y_pred}")
