import streamlit as st
import random

st.title("🧮 수학 퀴즈")

questions = [
    ("2 x 3", "6"),
    ("4 x 5", "20"),
    ("7 x 6", "42"),
    ("9 x 2", "18"),
    ("3 x 3", "9")
]

q, a = random.choice(questions)
user = st.text_input(f"{q} = ")

if user:
    if user == a:
        st.success("✅ 정답입니다!")
    else:
        st.error(f"❌ 틀렸어요! 정답은 {a}입니다.")
