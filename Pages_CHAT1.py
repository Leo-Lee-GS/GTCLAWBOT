import streamlit as st

# 챗봇을 화면 중앙에 배치
st.subheader("저는:blue[GT&C] 관련 :red[학습봇]입니다. 질문을 통해 쉽게 배워보세요! :sunglasses:", divider="grey")
# st.subheader("먼저 질문할 회사의 GTC를 선택하세요!", divider="gray")
st.components.v1.html(
    """
    <iframe
    src="https://udify.app/chatbot/F6hy3SxP96uYuwon"
    style="width: 100%; height: 70vh; min-height: 700px"
    frameborder="0"
    allow="microphone">
    </iframe>
    """,
    height=1500  # PDF 뷰어의 예상 높이에 맞춰서 높이 설정
)
