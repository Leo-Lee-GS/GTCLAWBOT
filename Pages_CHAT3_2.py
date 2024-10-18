import streamlit as st

# 챗봇을 화면 중앙에 배치
st.subheader("저는 :blue[GT&C] 관련 :red[계약 문구 분석봇]입니다. 내용을 알려주시면 GT&C와 비교&분석 해드릴게요! :sunglasses:", divider="grey")

st.components.v1.html(
    """
<iframe
    src="https://udify.app/chatbot/sMwFAxRDJXy7U1HU"
    style="width: 100%; height: 80vh; min-height: 700px"
    frameborder="0"
    allow="microphone">
    </iframe>
    """,
    height=1500  # PDF 뷰어의 예상 높이에 맞춰서 높이 설정
)
