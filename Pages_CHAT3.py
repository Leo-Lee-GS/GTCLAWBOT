import streamlit as st

# 챗봇을 화면 중앙에 배치
st.subheader("저는 :blue[GT&C] 관련 :red[계약 문구 작성봇]입니다. 내용을 알려주시면 영문 계약 문구를 작성해드릴게요! :sunglasses:", divider="blue")

st.components.v1.html(
    """
    <iframe
    src="https://udify.app/chatbot/GXexupnEeNJk4YEZ"
    style="width: 100%; height: 80vh; min-height: 700px"
    frameborder="0"
    allow="microphone">
    </iframe>
    """,
    height=1500  # PDF 뷰어의 예상 높이에 맞춰서 높이 설정
)
