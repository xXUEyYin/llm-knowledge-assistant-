import streamlit as st
from rag import get_answer

st.set_page_config(page_title="AI知识库助手")

st.title("🧠 AI知识库助手")

query = st.text_input("请输入你的问题")

if st.button("发送"):
    if query:
        answer = get_answer(query)

        st.markdown("### 🤖 AI回答")
        st.write(answer)