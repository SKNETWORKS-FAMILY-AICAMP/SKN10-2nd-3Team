
import numpy as np
import pandas as pd
import pickle
import os

from sklearn.model_selection import KFold, StratifiedKFold, GridSearchCV
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

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
    accuracy_lst = []
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
      acc = np.round(accuracy_score(valid_y, y_pred),4)
      accuracy_lst.append(acc)
      print(f'{n_iter} 번째 K-fold F1: {f1}, Acc: {acc}, 학습데이터 크기: {train_x.shape}, 검증데이터 크기: {valid_x.shape}')


    return np.mean(accuracy_lst)

def run_grid_search(base_model, x_train, y_train, param_grid, cv, scoring='f1'):
    """
    GridSearchCV를 사용하여 하이퍼파라미터 튜닝을 수행합니다.
    
    Args:
        base_model: 기본 모델
        x_train: 학습 데이터
        y_train: 학습 라벨
        param_grid: 탐색할 파라미터 그리드
        cv: 교차 검증 객체
        scoring: 최적화할 평가 지표
    
    Returns:
        최적화된 모델
    """
    grid_search = GridSearchCV(
        estimator=base_model,
        param_grid=param_grid,
        cv=cv,
        scoring=scoring,
        n_jobs=-1,
        verbose=2
    )
    
    grid_search.fit(x_train, y_train)
    
    print("Best parameters:", grid_search.best_params_)
    print("Best score:", grid_search.best_score_)
    
    return grid_search.best_estimator_

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
    
    # 기본 모델 생성
    base_model = get_model()
    
    # GridSearch를 위한 파라미터 그리드 정의
    # 예시: RandomForest 모델용 파라미터 그리드 (실제 모델에 맞게 수정 필요)
    param_grid = {
        #random forest
        #'n_estimators': [100, 200, 300],
        #'max_depth': [None, 10, 20, 30],
        #'min_samples_split': [2, 5, 10],
        #'min_samples_leaf': [1, 2, 4]
      
        #xgboost
        'learning_rate': [0.05, 0.1, 0.15],         # Centered around current best 0.1
        'max_depth': [2, 3, 4],                     # Centered around current best 3
        'n_estimators': [50, 100, 150],             # Centered around current best 100
        'subsample': [0.7, 0.8, 0.9],               # Centered around current best 0.8
        'colsample_bytree': [0.7, 0.8, 0.9] 

        #lgbm
        #'learning_rate': [0.01, 0.1],
        #'num_leaves': [31, 63],
        #'n_estimators': [100, 200],
        #'max_depth': [5, 10, -1] 
    }
    
    # 교차 검증 객체 생성
    is_Regression = False
    my_cv = get_cross_validation(is_kfold=is_Regression)
    
    # GridSearchCV를 통한 하이퍼파라미터 최적화
    print("GridSearchCV를 통한 하이퍼파라미터 최적화를 시작합니다...")
    optimized_model = run_grid_search(
        base_model=base_model,
        x_train=X_train,
        y_train=y_train,
        param_grid=param_grid,
        cv=my_cv,
        scoring='accuracy'
    )
    
    # 최적화된 모델로 교차 검증 수행
    print("최적화된 모델로 교차 검증을 수행합니다...")
    acc = run_cross_validation(optimized_model, X_train, y_train, my_cv, is_kfold=is_Regression)

    # 피쳐 중요도
    print_feature_importance(optimized_model, X_train)

    # 테스트 데이터 예측
    y_pred_main = optimized_model.predict(X_test)

    # 모델 저장
    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(optimized_model, f)

    print(f"모델이 {MODEL_PATH}에 저장되었습니다.")

    return accuracy_score(y_test, y_pred_main)

if __name__=="__main__":
  result = main()
  print(f"테스트 스코어는 {result}")
