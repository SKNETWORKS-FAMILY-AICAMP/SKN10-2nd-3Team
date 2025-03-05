import streamlit as st

# 페이지 제목
st.title("🎨 탈주는 아니될 말이오")

# 셀렉트 박스 (옵션 리스트)
option = st.selectbox("옵션을 선택하세요", ["LightGBM", "XGBoost", "RandomForest", "LogisticRegression"])

# 선택한 옵션에 따라 이미지 표시
if option == "LightGBM":
    st.image("fucking/accuracy.png", caption="고양이 1")
    st.image("fucking/confusion_matrix.png", caption="고양이 2")
    st.image("fucking/f1_score.png", caption="고양이 2")
    st.image("fucking/feature_importance.png", caption="고양이 1")
    st.image("fucking/log_loss.png", caption="고양이 2")
    st.image("fucking/precision.png", caption="고양이 1")
    st.image("fucking/recall.png", caption="고양이 2")
    st.image("fucking/roc_auc.png", caption="고양이 2")

elif option == "XGBoost":
    st.image("ye/accuracy.png", caption="고양이 1")
    st.image("ye/confusion_matrix.png", caption="고양이 2")
    st.image("ye/f1_score.png", caption="고양이 2")
    st.image("ye/feature_importance.png", caption="고양이 1")
    st.image("ye/log_loss.png", caption="고양이 2")
    st.image("ye/metrics.png", caption="고양이 2")
    st.image("ye/precision.png", caption="고양이 1")
    st.image("ye/recall.png", caption="고양이 2")
    st.image("ye/roc_auc_curve.png", caption="고양이 2")

elif option == "RandomForest":
    st.image("jungwoo/accuracy.png", caption="고양이 1")
    st.image("jungwoo/confusion_matrix.png", caption="고양이 2")
    st.image("jungwoo/epoch.png", caption="고양이 1")
    st.image("jungwoo/f1_score.png", caption="고양이 2")
    st.image("jungwoo/feature_importance.png", caption="고양이 1")
    st.image("jungwoo/log_loss.png", caption="고양이 2")
    st.image("jungwoo/precision.png", caption="고양이 1")
    st.image("jungwoo/recall.png", caption="고양이 2")
    st.image("jungwoo/roc_auc.png", caption="고양이 2")

elif option == "LogisticRegression":
    st.image("jungwoo2/accuracy.png", caption="고양이 1")
    st.image("jungwoo2/confusion matrix.png", caption="고양이 2")
    st.image("jungwoo2/epoch.png", caption="고양이 1")
    st.image("jungwoo2/f1_score.png", caption="고양이 2")
    st.image("jungwoo2/log_loss.png", caption="고양이 2")
    st.image("jungwoo2/precision.png", caption="고양이 1")
    st.image("jungwoo2/recall.png", caption="고양이 2")
    st.image("jungwoo2/roc_auc.png", caption="고양이 2")