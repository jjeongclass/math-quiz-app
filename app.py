import streamlit as st
import random

st.set_page_config(page_title="수학 퀴즈", page_icon="🧮")
st.title("🧮 수학 퀴즈")

# 문제 리스트
questions = [
    ("2 x 3", "6"),
    ("4 x 5", "20"),
    ("7 x 6", "42"),
    ("9 x 2", "18"),
    ("3 x 3", "9")
]

# 1️⃣ 문제를 session_state에 저장
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "answered" not in st.session_state:
    st.session_state.answered = False

q, a = st.session_state.current_question

# 2️⃣ 사용자 입력
user = st.text_input(f"{q} = ", key="answer")

# 3️⃣ 제출 버튼 → 정답 확인
if st.button("제출"):
    if user:
        st.session_state.answered = True
        if user.strip() == a:
            st.success("✅ 정답입니다!")
        else:
            st.error(f"❌ 틀렸어요! 정답은 {a}입니다.")

# 4️⃣ 다음 문제 버튼
if st.session_state.answered:
    if st.button("다음 문제"):
        st.session_state.current_question = random.choice(questions)
        st.session_state.answered = False
        st.session_state.answer = ""  # 입력값 초기화
