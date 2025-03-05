import streamlit as st

# 페이지 제목
st.title("🎨 탈주는 아니될 말이오")

# 셀렉트 박스 (옵션 리스트)
option = st.selectbox("옵션을 선택하세요", ["LightGBM", "XGBoost", "RandomForest", "LogisticRegression", "Ensemble"])

# 선택한 옵션에 따라 이미지 표시
if option == "LightGBM":
    st.image("fucking/accuracy.png", caption="적중률")
    st.image("fucking/confusion_matrix.png", caption="혼동 행렬")
    st.image("fucking/f1_score.png", caption="f1 스코어")
    st.image("fucking/feature_importance.png", caption="변수 중요도")
    st.image("fucking/log_loss.png", caption="loss 값")
    st.image("fucking/precision.png", caption="예측값")
    st.image("fucking/recall.png", caption="재현률")
    st.image("fucking/roc_auc.png", caption="roc_auc 값")

elif option == "XGBoost":
    st.image("ye/accuracy.png", caption="적중률")
    st.image("ye/confusion_matrix.png", caption="혼동 행렬")
    st.image("ye/f1_score.png", caption="f1 스코어")
    st.image("ye/feature_importance.png", caption="변수 중요도")
    st.image("ye/log_loss.png", caption="loss 값")
    st.image("ye/metrics.png", caption="측정결과")
    st.image("ye/precision.png", caption="예측값")
    st.image("ye/recall.png", caption="재현률")
    st.image("ye/roc_auc_curve.png", caption="roc_auc 값")

elif option == "RandomForest":
    st.image("jungwoo/accuracy.png", caption="적중률")
    st.image("jungwoo/confusion_matrix.png", caption="혼동 행렬")
    st.image("jungwoo/epoch.png", caption="학습 횟수")
    st.image("jungwoo/f1_score.png", caption="f1 스코어")
    st.image("jungwoo/feature_importance.png", caption="변수 중요도")
    st.image("jungwoo/log_loss.png", caption="loss 값")
    st.image("jungwoo/precision.png", caption="예측값")
    st.image("jungwoo/recall.png", caption="재현률")
    st.image("jungwoo/roc_auc.png", caption="roc_auc 값")

elif option == "LogisticRegression":
    st.image("jungwoo2/accuracy.png", caption="적중률")
    st.image("jungwoo2/confusion_matrix.png", caption="혼동 행렬")
    st.image("jungwoo2/epoch.png", caption="학습횟수")
    st.image("jungwoo2/f1_score.png", caption="f1 스코어")
    st.image("jungwoo2/feature_importance.png", caption="변수 중요도")
    st.image("jungwoo2/log_loss.png", caption="loss 값")
    st.image("jungwoo2/precision.png", caption="예측값")
    st.image("jungwoo2/recall.png", caption="재현률")
    st.image("jungwoo2/roc_auc.png", caption="roc_auc 값")

elif option == "Ensemble":
    st.image("jae/accuracy.png", caption="적중률")
    st.image("jae/confusion_matrix.png", caption="혼동 행렬")
    st.image("jae/f1_score.png", caption="f1 스코어")
    st.image("jae/log_loss.png", caption="loss 값")
    st.image("jae/precision.png", caption="예측값")
    st.image("jae/recall.png", caption="재현률")
    st.image("jae/roc_auc.png", caption="roc_auc 값")