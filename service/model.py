
from lightgbm import LGBMClassifier, plot_importance
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from utils import reset_seeds

# 모델 생성 후 리턴
@reset_seeds
def get_model(hp:dict=None, model_nm:str=None):
    if not hp:
        hp = {"verbose":-1} # warning 로그 제거

    if not model_nm:
        return XGBClassifier()
    elif model_nm == "LGBMClassifier":
        return LGBMClassifier(**hp)
    elif model_nm == "RandomForestClassifier":
        return RandomForestClassifier(verbose = False, max_depth = 10, min_samples_split = 10)
    elif model_nm == "XGBoost":
        return XGBClassifier()
