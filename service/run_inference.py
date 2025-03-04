import pickle
import pandas as pd
from dataset import preprocess_dataset
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from config import MODEL_PATH


def load_model():
    """저장된 모델을 로드합니다."""
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        print(f"모델을 {MODEL_PATH}에서 로드했습니다.")
        return model
    except Exception as e:
        print(f"모델 로드 실패: {e}")
        return None


def predict_and_submit():
    """테스트 데이터에 대한 예측을 수행하고 제출 파일을 생성합니다."""
    # 데이터 전처리
    _, _, _, _, X_test, y_test = preprocess_dataset()

    # 모델 로드
    model = load_model()
    if model is None:
        return False

    # 예측 수행
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)

    print(f'test f1 score : {f1}')
    print(f'test acc score : {acc}')

    # confusion matrix
    cm = confusion_matrix(y_test,y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=['Stay','Churn'])
    disp.plot()
    plt.title('XGBoost Confusion Matrix')
    plt.savefig('cm.png')
    plt.show()



    return True

if __name__ == "__main__":
    predict_and_submit()
