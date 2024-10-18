import streamlit as st

# 챗봇을 화면 중앙에 배치
st.subheader("저는 다양한 :blue[Business Case]관련 :red[영문 Letter 작성봇]입니다. 입력하신 내용을 전문적인 영문 레터로 작성해드릴게요! :sunglasses:", divider="blue")

st.components.v1.html(
    """
    <iframe
    src="https://udify.app/chatbot/jhdj4FkD4xXc6qb9"
    style="width: 100%; height: 80vh; min-height: 700px"
    frameborder="0"
    allow="microphone">
    </iframe>
    """,
    height=1000  # PDF 뷰어의 예상 높이에 맞춰서 높이 설정
)
