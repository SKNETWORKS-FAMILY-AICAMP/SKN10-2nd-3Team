
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from utils import reset_seeds
from config import DATA_PATH
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


# 트레인 데이터 로드
def __load_data() -> pd.DataFrame:
    data = pd.read_csv(DATA_PATH)
    data = data.replace(r'^\s*$', np.nan, regex=True)
    return data

def __process_drop(train, val, test):
    drop_cols = ['customerID', ]

    train.drop(drop_cols, axis=1, inplace=True) # 모델이 학습하는데 사용하는 데이터
    val.drop(drop_cols, axis=1, inplace=True) # 모델의 학습을 평가(잘했는지?? 못했는지??)하기 위한 데이터
    test.drop(drop_cols, axis=1, inplace=True)

def __fill_na(train, val, test):
    null_cols = ['TotalCharges']
    for df in [train, val, test]:
      for col in null_cols:
        df[col] = df[col].astype(float)
        df[col] = df[col].fillna(df[col].mean())
    return train, val, test

def __preprocess_resample(train, val, test):
    print("__preprocess_resample start")
    print(f"train.shape: {train.shape} / test.shape: {val.shape}")
    X_train, y_train = (train.drop(['Churn'], axis=1), train['Churn'])
    X_val, y_val = (val.drop(['Churn'], axis=1), val['Churn'])
    X_test = test.drop(['Churn'], axis=1)
    y_test = test['Churn']

    print("__preprocess_resample end")
    print(f"X_train.shape: {X_train.shape} / X_test.shape: {X_val.shape}")
    return X_train, X_val, y_train, y_val, X_test, y_test

def __preprocess_label_encoding(train, val, test):
    results = []

    cat_features = ['StreamingTV', 'StreamingMovies',
                 'OnlineSecurity', 'OnlineBackup','DeviceProtection',]

    # Remove categorical features from normal columns
    normal_cols = list(set(train.columns) - set(cat_features))

    # Initialize dictionary to store label encoders
    label_encoders = {}

    # Fit label encoders on training data and transform all datasets
    encoded_features = {}
    for feature in cat_features:
        label_encoders[feature] = LabelEncoder()
        # Fit on training data
        encoded_features[feature] = label_encoders[feature].fit_transform(train[feature])

    pd_list = [train, val, test]
    for i, df in enumerate(pd_list):
        # Create a copy of the dataframe
        temp_df = df.copy()

        # Transform categorical features
        for feature in cat_features:
            try:
                temp_df[feature] = label_encoders[feature].transform(df[feature])
            except ValueError as e:
                # Handle unseen categories in validation/test set
                print(f"Warning: Found unseen labels in {feature} for dataset {i+1}")
                # Get unique values in current dataset
                unique_vals = df[feature].unique()
                # Find values not in training set
                unseen_vals = [x for x in unique_vals if x not in label_encoders[feature].classes_]
                if unseen_vals:
                    print(f"Unseen values in {feature}: {unseen_vals}")
                    # Replace unseen values with the most frequent value from training
                    most_frequent = train[feature].mode()[0]
                    temp_df.loc[df[feature].isin(unseen_vals), feature] = most_frequent
                    # Transform again after replacing unseen values
                    temp_df[feature] = label_encoders[feature].transform(temp_df[feature])

        # Only select columns that exist in current dataframe
        available_cols = sorted([col for col in normal_cols if col in df.columns])

        # Combine all features
        result_df = temp_df[available_cols + cat_features].copy()
        results.append(result_df.reset_index(drop=True))

    return results[0], results[1], results[2]


def __preprocess_dummy_encoding(train, val, test):
    results = []

    cat_features = [
                 'PaymentMethod',
                    'MultipleLines', 'InternetService', 'Contract',
                    'TechSupport', ]

    # Remove target from normal_cols calculation
    normal_cols = list(set(train.columns) - set(cat_features))

    # Get dummy variables for categorical features in training set
    dummies_train = pd.get_dummies(train[cat_features], prefix=cat_features)

    # Get dummy column names from training set for consistent columns across sets
    dummy_columns = dummies_train.columns

    pd_list = [train, val, test]
    for i, df in enumerate(pd_list, start=1):
        # Create dummies with only columns that were in training data
        dummies_df = pd.get_dummies(df[cat_features], prefix=cat_features)

        # Ensure all dummy columns from training are present
        for col in dummy_columns:
            if col not in dummies_df.columns:
                dummies_df[col] = 0

        # Keep only dummy columns from training (in case test has categories not in train)
        dummies_df = dummies_df[dummy_columns]

        # Only select columns that exist in current dataframe
        available_cols = sorted([col for col in normal_cols if col in df.columns])

        # Concatenate original features with dummy variables
        results.append(
            pd.concat(
                [df[available_cols].reset_index(drop=True), dummies_df.reset_index(drop=True)],
                axis=1
            ).reset_index(drop=True)
        )


    return results[0], results[1], results[2]

def __preprocess_bin(train, val, test) : 
  bin_categories = []
  for category in bin_categories:
    train[category] = train[category].apply(lambda x: x//1000)
    val[category] = val[category].apply(lambda x: x//1000)
    test[category] = test[category].apply(lambda x: x//1000)

  return train, val, test

def __preprocess_yn (train, val, test):
  yn_categories = ['gender', 'Partner', 'Dependents','PhoneService', 'PaperlessBilling','Churn']
  for category in yn_categories:
    train[category] = train[category].apply(lambda x: 1 if x in ['Yes','Female'] else 0)
    val[category] = val[category].apply(lambda x: 1 if x in ['Yes','Female'] else 0)
    test[category] = test[category].apply(lambda x: 1 if x in ['Yes','Female'] else 0)

  return train, val, test


def __preprocess_data(train, val, test):
    print(f'before: {train.shape} / {test.shape}')
    # 필요없는 컬럼 제거
    __process_drop(train, val, test)
    train, val, test = __fill_na(train,val,test)

    # 범주형 처리
    train, val, test = __preprocess_label_encoding(train, val, test)
    train, val, test = __preprocess_dummy_encoding(train, val, test)

    # bin 처리
    train, val, test = __preprocess_bin(train, val, test)

    return train, val, test


@reset_seeds
def preprocess_dataset():
    # 데이터 로드
    df_raw = __load_data()
    # 데이터 분리
    train_val, test = train_test_split(df_raw, test_size=0.1, stratify=df_raw['Churn'])
    train, val = train_test_split(train_val, test_size=0.1, stratify=train_val['Churn'])
    # 데이터 전처리
    train, val, test = __preprocess_yn(train, val, test)
    train, val, test = __preprocess_data(train, val, test)

    # features, target 분리
    return __preprocess_resample(train, val, test)
