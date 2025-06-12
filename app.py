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

# 세션 상태 초기화
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "input_key" not in st.session_state:
    st.session_state.input_key = 0  # 입력창 초기화를 위한 키
if "correct_total" not in st.session_state:
    st.session_state.correct_total = 0
    st.session_state.total_questions = 0

# 현재 문제
q, a = st.session_state.current_question

# 사용자 입력
user = st.text_input(f"{q} = ", key=f"answer_{st.session_state.input_key}")

# 제출 버튼
if st.button("제출"):
    if user:
        st.session_state.answered = True
        st.session_state.total_questions += 1

        if user.strip() == a:
            st.success("✅ 정답입니다!")
            st.session_state.correct_total += 1
        else:
            st.error(f"❌ 틀렸어요! 정답은 {a}입니다.")

# 다음 문제 버튼
if st.session_state.answered:
    if st.button("다음 문제"):
        st.session_state.current_question = random.choice(questions)
        st.session_state.answered = False
        st.session_state.input_key += 1  # 입력 필드 초기화

# 정답률 표시
if st.session_state.total_questions > 0:
    st.caption(f"📊 지금까지 {st.session_state.correct_total} / {st.session_state.total_questions} 문제 정답")
