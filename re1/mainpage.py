# Home.py

import streamlit as st

def main():
    st.title("Streamlit Home Page")

    # 텍스트와 마크다운 출력
    st.write("Welcome to the Streamlit Home Page!")
    st.markdown("This is a *markdown* section.")
    st.markdown("텍스트와 마크다운 출력테스트")

    # 사용자 입력
    st.markdown("변수에 input을 할당할 수 있다")
    name = st.text_input("Enter your name:")

    # 버튼 클릭 시 작동
    if st.button("Greet"):
        st.write(f"Hello, {name}!")

    # 조건부 메시지 출력
    if name:
        st.success(f"Welcome, {name}!")
    else:
        st.info("Please enter your name above.")

    # 슬라이더를 사용한 숫자 입력
    age = st.slider("Select your age", 0, 100, 25)
    st.write("Your age is:", age)

if __name__ == "__main__":
    main()
