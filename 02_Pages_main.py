import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import streamlit.components.v1 as components

# 페이지 설정 (최초 실행 시)
st.set_page_config(layout="wide")

st.sidebar.markdown("# 🗝️Unlock the Future 🔓")
st.sidebar.markdown("### 🏆 Smart Thinking to Great Success!")
st.sidebar.markdown("")  
st.sidebar.markdown("🤖 Our Service: **I am your Lawbot**")
st.sidebar.markdown("💻 made by **S&Tech(세라/상원/석호)**")
st.sidebar.markdown("🎯 Goal: Global Business 역량 강화")
st.sidebar.markdown("💡 How: 계약 관련 업무 및 학습 지원")
st.sidebar.markdown("")  
st.sidebar.markdown("---")  
st.sidebar.markdown("📌 **Shell, Chevron, BP 등의 General Terms and Conditions**(이하 GT&C)는 석유 거래의 기본 조건을 규정하며, 주로 인도, 결제, 위험 이전 등을 다룹니다.")
st.sidebar.markdown("개별 계약서에서 별도로 합의된 사항이 있을 경우 그 조건이 GT&C보다 우선합니다. GT&C는 기본 틀을 제공하고, 구체적인 내용은 개별 계약서에서 조정됩니다.")
# st.set_page_config(layout="centered")
# 암호 기능을 위한 세션 상태
if 'access_granted' not in st.session_state:
    st.session_state['access_granted'] = False

# 질문에 대한 답 체크 함수
def check_answer():
    if st.session_state["answer"] == "31":
        st.session_state['access_granted'] = True
        st.success("접속 허용!")
    else:
        st.error("틀린 답변입니다. 다시 시도하세요.")

# # Query parameters로부터 세션 유지
# # query_params = st.query_params

# # 세션이 유지되지 않은 경우 URL에서 상태 복원
# if 'access_granted' in query_params and query_params['access_granted'] == 'True':
#     st.session_state['access_granted'] = True

# 암호 입력 전에는 페이지 접근 불가
if not st.session_state['access_granted']:
    st.text_input("S&T는 몇 층입니까? 숫자만 입력하세요!", key="answer")
    if st.button("제출", on_click=check_answer):
        # 올바른 답을 입력한 경우, URL에 세션 상태를 저장
        if st.session_state['access_granted']:
            st.set_query_params(access_granted='True')
else:
    # 네비게이션 설정
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav)
    add_page_title(pg)

    # 페이지 실행
    pg.run()



