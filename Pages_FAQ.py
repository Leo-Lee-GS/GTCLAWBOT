import streamlit as st

# FAQ 페이지 타이틀
st.header("기본적으로 알아야 하는 :blue[상식] :sunglasses:", divider="gray")

# FAQ 내용을 포함할 컨테이너 생성
with st.container():
    st.markdown("""
    **<span style="color:blue">1. Q: FOB(Free on Board) 조건에서 Risk는 언제 구매자에게 이전되나요?</span>**  
    A: FOB 조건에서는 물품이 선적 항구에서 선박에 실리는 순간 리스크가 구매자에게 이전됩니다.

    ---  

    **<span style="color:blue">2. Q: CIF와 CFR의 차이점은 무엇인가요?</span>**  
    A: CIF는 판매자가 운송비와 보험을 부담하는 반면, CFR은 운송비만 판매자가 부담하고, 보험은 구매자가 부담합니다.

    ---  

    **<span style="color:blue">3. Q: 'Demurrage'(체선료)는 언제 발생하나요?</span>**  
    A: Demurrage는 선박이 정해진 Laytime(선적/하역 기간)을 초과할 경우, 발생하는 벌금입니다.

    ---  

    **<span style="color:blue">4. Q: 계약서에서 'Risk and Title' 조항은 어떤 의미인가요?</span>**  
    A: Risk(위험)는 물품의 손상 또는 손실에 대한 책임을, Title(소유권)은 물품의 법적 소유권을 의미합니다.

    ---  

    **<span style="color:blue">5. Q: DAP 조건에서 판매자의 책임은 어디까지인가요?</span>**  
    A: DAP(Delivered at Place) 조건에서 판매자는 지정된 목적지까지 물품을 안전하게 운송할 책임이 있으며, 그 이후의 리스크는 구매자에게 이전됩니다.

    ---  

    **<span style="color:blue">6. Q: 'Laytime'은 무엇을 의미하나요?</span>**  
    A: Laytime은 물품을 선적하거나 하역하는 데에 허용된 시간을 의미하며, 이 시간이 초과되면 체선료가 발생할 수 있습니다.

    ---  

    **<span style="color:blue">7. Q: 보험(Insurance) 조항에서 CIF 조건과 DAP 조건의 차이점은 무엇인가요?</span>**  
    A: CIF 조건에서는 판매자가 보험을 책임지고, DAP 조건에서는 구매자가 보험을 책임집니다.

    ---  

    **<span style="color:blue">8. Q: 계약서에서 'Force Majeure' 조항이란 무엇인가요?</span>**  
    A: 'Force Majeure'(불가항력) 조항은 천재지변이나 전쟁 등 예측할 수 없는 상황으로 인해 계약 이행이 불가능할 경우, 책임을 면제받는 조항입니다.

    ---  

    **<span style="color:blue">9. Q: 계약서에서 'Title'이 언제 구매자에게 이전되나요?</span>**  
    A: 계약서에 명시된 조건에 따라, 물품이 특정 지점(예: 선적 항구)에서 구매자에게 소유권이 이전됩니다.

    ---  

    **<span style="color:blue">10. Q: 계약서에서 'Indemnity'(배상) 조항이란 무엇인가요?</span>**  
    A: 'Indemnity' 조항은 한쪽 당사자가 손실을 입을 경우, 상대방이 이를 보상할 의무를 명시하는 조항입니다.

    ---  

    **<span style="color:blue">11. Q: 'Nomination of Vessels'는 무엇을 의미하나요?</span>**  
    A: 'Nomination of Vessels'는 구매자가 운송할 선박을 지명하여 판매자에게 통보하는 절차를 의미합니다.

    ---  

    **<span style="color:blue">12. Q: 'Payment' 조항에서는 어떤 조건을 명시하나요?</span>**  
    A: 'Payment' 조항은 물품 대금을 언제, 어떻게 지불할 것인지, 그리고 지불 지연 시의 페널티를 명시합니다.

    ---  

    **<span style="color:blue">13. Q: 'Termination' 조항은 어떤 상황에서 적용되나요?</span>**  
    A: 'Termination' 조항은 특정한 조건 하에 계약이 종료될 수 있는 상황을 규정하며, 계약 위반이나 불가항력과 같은 이유로 종료될 수 있습니다.

    ---  

    **<span style="color:blue">14. Q: 계약서에 명시된 'Inspection' 절차는 무엇인가요?</span>**  
    A: 'Inspection' 절차는 물품의 품질과 수량을 확인하기 위해 양측이 지정한 검사 기관이 물품을 점검하는 절차입니다.

    ---  

    **<span style="color:blue">15. Q: 'Quality and Claims' 조항은 어떤 역할을 하나요?</span>**  
    A: 이 조항은 물품의 품질과 관련된 불만이 있을 경우, 클레임을 어떻게 처리해야 하는지에 대한 지침을 제공합니다.

    ---  

    **<span style="color:blue">16. Q: 'Assignment' 조항이란 무엇인가요?</span>**  
    A: 'Assignment' 조항은 계약 당사자가 계약상의 권리나 의무를 제3자에게 양도할 수 있는지 여부를 규정합니다.

    ---  

    **<span style="color:blue">17. Q: 'Sanctions and Boycotts' 조항은 어떤 내용을 담고 있나요?</span>**  
    A: 'Sanctions and Boycotts' 조항은 특정 국가나 단체에 대한 제재나 보이콧과 관련된 법적 규제를 준수해야 한다는 내용을 포함합니다.

    ---  

    **<span style="color:blue">18. Q: 'Shifting' 이 발생할 경우 누가 비용을 부담하나요?</span>**  
    A: 판매자가 다른 접안시설로 이동을 요청할 경우 비용은 판매자가 부담하고, 구매자가 요청하거나 구매자의 통제 하에 있는 상황에서는 비용을 구매자가 부담합니다.
    """, unsafe_allow_html=True)
