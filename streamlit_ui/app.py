# streamlit_ui/app.py - UI demo cho Qwen Coding Use Case
import streamlit as st
import requests

st.title("Qwen Coding Multiple Choice QA Demo")

question = st.text_area("Nhập câu hỏi coding:")
choices = st.text_area("Nhập các lựa chọn (mỗi dòng 1 lựa chọn):")

if st.button("Dự đoán đáp án"):
    if question and choices:
        choices_list = [c.strip() for c in choices.splitlines() if c.strip()]
        data = {"question": question, "choices": choices_list}
        try:
            resp = requests.post("http://localhost:8000/predict", json=data)
            if resp.status_code == 200:
                st.success(f"Đáp án mô hình chọn: {resp.json()['answer']}")
            else:
                st.error(f"Lỗi: {resp.text}")
        except Exception as e:
            st.error(f"Không kết nối được API: {e}")
    else:
        st.warning("Vui lòng nhập đủ câu hỏi và lựa chọn!")
