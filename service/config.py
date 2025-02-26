
import os

BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODEL_DIR = os.path.join(DATA_DIR, 'models')

# 모델 설정
MODEL_VERSION = 'v1_rf'
MODEL_FILENAME = f'model_{MODEL_VERSION}.pkl'
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

DATA_PATH = os.path.join(DATA_DIR, 'raw.csv')
#TEST_PATH = os.path.join(DATA_DIR, 'test.csv')
#SUBMISSION_PATH = os.path.join(DATA_DIR, f'submission_{MODEL_VERSION}.csv')

N_FOLDS = 5
