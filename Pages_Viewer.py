import streamlit as st
import fitz  # PyMuPDF
from PIL import Image

#st.title("HOME")
st.header("회사 별 :blue[GT&C] Viewer :sunglasses:", divider="blue")
# PDF 페이지를 이미지로 변환하는 함수
def pdf_page_to_image(pdf_path, page_number, zoom=1.5):  # zoom 값 수정
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number)  # 페이지 로드
    # 확대/축소 비율을 설정하여 적절한 크기로 표시
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)  # 확대된 비율로 픽스맵 생성
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img

# PDF 파일 경로 리스트
pdf_files = {
    "BPOI 2015": r"D:\GS_OneDrive\OneDrive - GS칼텍스\CDS_파이썬코드\langchain-kr\99-Projects\03. AI-DEAS\Data\BPOI 2015.pdf",
    "Chevron 2014 Products GTC": r"D:\GS_OneDrive\OneDrive - GS칼텍스\CDS_파이썬코드\langchain-kr\99-Projects\03. AI-DEAS\Data\Chevron2014ProductsGTC.pdf",
    "STASCO 2010 Revised": r"D:\GS_OneDrive\OneDrive - GS칼텍스\CDS_파이썬코드\langchain-kr\99-Projects\03. AI-DEAS\Data\STASCO 2010_revised.pdf"
}

# PDF 파일 선택 박스를 본문 상단에 배치
selected_pdf = st.selectbox("PDF 파일을 선택하세요", ["파일을 선택하세요"] + list(pdf_files.keys()))

if selected_pdf == "파일을 선택하세요":
    st.warning("PDF 파일을 선택하세요.")
else:
    # PDF 파일을 선택하면 해당 경로 가져오기
    pdf_path = pdf_files[selected_pdf]

    # PDF 파일을 열고 총 페이지 수 가져오기
    doc = fitz.open(pdf_path)
    total_pages = doc.page_count

    # 세션 상태로 현재 페이지 번호를 저장
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0

    # 상단 네비게이션 바 (페이지 넘기기)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("이전 페이지"):
            if st.session_state.page_number > 0:
                st.session_state.page_number -= 1
    with col2:
        # 페이지 직접 입력 기능
        page_input = st.number_input(
            "페이지", min_value=1, max_value=total_pages, value=st.session_state.page_number + 1) - 1
        if page_input != st.session_state.page_number:
            st.session_state.page_number = page_input
    with col3:
        if st.button("다음 페이지"):
            if st.session_state.page_number < total_pages - 1:
                st.session_state.page_number += 1

    # 현재 페이지 및 총 페이지 수 표시
    st.write(f"페이지: {st.session_state.page_number + 1} / {total_pages}")

    # 현재 페이지를 이미지로 변환 및 표시 (화면에 맞게 확대/축소 비율 조정)
    image = pdf_page_to_image(pdf_path, st.session_state.page_number, zoom=10)  # zoom 값 조정
    st.image(image, use_column_width=True)  # 이미지를 전체 너비로 표시
    #st.image(image, width=900) 