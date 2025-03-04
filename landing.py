import streamlit as st

# 페이지 제목
st.title("🎨 탈주는 아니될 말이오")

# 셀렉트 박스 (옵션 리스트)
option = st.selectbox("옵션을 선택하세요", ["LightGBM", "XGBoost", "KNN", "RandomForest", "LogisticRegression", "앙상블"])

# 선택한 옵션에 따라 이미지 표시
if option == "LightGBM":
    st.image("dog1.jpg", caption="강아지 1")
    st.image("dog2.jpg", caption="강아지 2")
elif option == "XGBoost":
    st.image("cat1.jpg", caption="고양이 1")
    st.image("cat2.jpg", caption="고양이 2")
elif option == "KNN":
    st.image("nature1.jpg", caption="자연 1")
    st.image("nature2.jpg", caption="자연 2")
elif option == "RandomForest":
    st.image("cat1.jpg", caption="고양이 1")
    st.image("cat2.jpg", caption="고양이 2")
elif option == "LogisticRegression":
    st.image("nature1.jpg", caption="자연 1")
    st.image("nature2.jpg", caption="자연 2")
elif option == "앙상블":
    st.image("nature1.jpg", caption="자연 1")
    st.image("nature2.jpg", caption="자연 2")
