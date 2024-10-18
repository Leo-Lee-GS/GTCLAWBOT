import streamlit as st
# 챗봇을 화면 중앙에 배치
st.subheader("저는 :blue[GT&C] 관련 :red[Q&A봇]입니다. 궁금한 사례를 물어보세요! :sunglasses:", divider="blue")
# st.subheader("먼저 질문할 회사의 GTC를 선택하세요!", divider="gray")

# iframe을 전체 화면 너비로 설정
st.components.v1.html(
    """
    <iframe
    src="https://udify.app/chatbot/kUsdbJDTHOAkf9Db"
    style="width: 100%; height: 80vh; min-height: 700px"
    frameborder="0"
    allow="microphone">
    </iframe>
    """,
    height=1500
)

