
import numpy as np
import pandas as pd
import pickle
import os

from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import f1_score

from dataset import preprocess_dataset
from model import get_model
from utils import reset_seeds
from config import MODEL_PATH, MODEL_DIR, N_FOLDS

def get_cross_validation(shuffle:bool=True, is_kfold:bool=True, n_splits:int=N_FOLDS):
    if is_kfold:
      return KFold(n_splits=n_splits, shuffle=shuffle)
    else:
      return StratifiedKFold(n_splits=n_splits, shuffle=shuffle)

def run_cross_validation(my_model, x_train, y_train, cv, is_kfold:bool=True):
    n_iter = 0
    f1_lst = []
    if is_kfold:
        cross_validation = cv.split(x_train)
    else:
        cross_validation = cv.split(x_train, y_train)

    for train_index, valid_index in cross_validation:
      n_iter += 1
      # 학습용, 검증용 데이터 구성
      train_x, valid_x = x_train.iloc[train_index], x_train.iloc[valid_index]
      train_y, valid_y = y_train.iloc[train_index], y_train.iloc[valid_index]
      # 학습
      my_model.fit(train_x, train_y)
      # 예측
      y_pred = my_model.predict(valid_x)
      # 평가
      f1 = np.round(f1_score(valid_y, y_pred), 4)
      f1_lst.append(f1)
      print(f'{n_iter} 번째 K-fold F1: {f1}, 학습데이터 크기: {train_x.shape}, 검증데이터 크기: {valid_x.shape}')

    return np.mean(f1_lst)

def print_feature_importance(my_model, data):
  feature_importance = my_model.feature_importances_
  indices = np.argsort(feature_importance)[::-1]
  print("Feature Ranking")
  for f in range(data.shape[1]):
    print(f"{data.columns[indices][f]} : {feature_importance[indices][f]}")

@reset_seeds
def main():
    # 데이터 로드 및 분류
    X_train, X_test, y_train, y_test, _, _ = preprocess_dataset()
    # 모델 생성
    my_model = get_model()
    # 교차 검증
    is_Regression = False
    my_cv = get_cross_validation(is_kfold=is_Regression)
    # 모델 학습
    f1 = run_cross_validation(my_model, X_train, y_train, my_cv, is_kfold=is_Regression)

    # 피쳐 중요도
    print_feature_importance(my_model, X_train)

    # 테스트 데이터 예측
    y_pred_main = my_model.predict(X_test)

    # 모델 저장
    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(my_model, f)

    print(f"모델이 {MODEL_PATH}에 저장되었습니다.")

    return f1_score(y_test, y_pred_main)

if __name__=="__main__":
  result = main()
  print(f"테스트 스코어는 {result}")
