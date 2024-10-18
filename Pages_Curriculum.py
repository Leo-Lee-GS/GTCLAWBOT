import streamlit as st
import fitz  # PyMuPDF
from PIL import Image


# st.title("Case_Study")
st.header(":blue[Chevron GT&C]를 쉽게 공부해보세요! :sunglasses:", divider="gray")



# Tab 생성
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["교육 관련 (General)",
                                        "Ch1. FOB Delivery", 
                                        "Ch2. CFR, CIF 및 DAP Delivery", 
                                        "Ch3. Barge Deliveries", 
                                        "Ch4. General Provisions", 
                                        "Ch5. Schedules (부록)",
                                        "Chevron GT&C 보기"])

# Define the structure with formatted headers, line breaks, and colors.
with tab1:
    with st.container():
        st.markdown("""---

### 주니어 교육 프로그램

**Chevron GT&C**의 주요 섹션을 중심으로 진행되며, 실무에 필요한 핵심 내용을 이해할 수 있도록 설계되었습니다.

---

### 1. 계약 개요 및 기본 용어 이해

**목표:**  
계약서의 전반적인 구조와 기본 용어를 이해하고, 거래에서 자주 사용되는 상업적 조건들을 익힌다.

**내용:**  
- 계약서의 전체 목차 소개  
- **FOB, CFR, CIF** 등 인코텀즈(Incoterms) 설명 (Part One~Five 관련)  
- **리스크와 타이틀** 이전 시점 (Section 3, Section 10)  
- **Laytime과 Demurrage** 개념 (Section 7, Section 16)

**예시:**  
"FOB 조건에서는 리스크가 선적 시점에 구매자에게 이전됩니다."

---

### 2. 건강, 안전 및 환경 규정(REACH)

**목표:**  
REACH 규정과 MSDS 제공 의무를 이해하고 이를 실제 거래에 적용하는 방법을 학습한다.

**내용:**  
- **REACH 규정 설명** (Section 46.1)  
- **MSDS 제공 시점 및 책임 구분** (Section 46.1.3)  
- **구매자의 건강 및 안전 책임** (Section 46.3)

**예시:**  
"FOB 조건에서는 선적 시점에 MSDS를 제공해야 합니다."

---

### 3. 법률 변경 및 새로운 규제 대응

**목표:**  
법률이나 규제가 변경될 경우 가격 또는 계약 조건 재협상 옵션을 이해한다.

**내용:**  
- 새로운 법규나 규제 변화에 따른 **재협상 권리** (Section 50)  
- 협상이 실패할 경우 계약 종료 가능성

**예시:**  
"새로운 세금이 도입되어 판매자에게 경제적으로 불리한 영향을 미칠 경우 가격 재협상을 요청할 수 있습니다."

---

### 4. 부패 방지 및 탈세 방지 조항

**목표:**  
부패 방지와 탈세 방지를 위한 국제적인 법적 요구사항을 숙지하고 준수 방법을 학습한다.

**내용:**  
- **부패 방지 관련 조항 설명** (Section 57)  
- **금전 또는 가치 있는 물품 제공 금지** 대상 명확화  
- 위반 시 계약 해지 가능성

**예시:**  
"정부 공무원에게 뇌물을 제공하거나 약속하는 행위는 엄격히 금지됩니다."

---

### 5. 선박 요건 및 사고 보고 절차

**목표:**  
선박 운송 중 발생할 수 있는 사고 대응 절차와 선박 요건을 숙지한다.

**내용:**  
- **ITOPF 가입 요건** 및 **ISPS 코드 준수** 필요성 (Schedule C Section 1.2~1.3)  
- **Chevron 사고 보고 절차** 설명 (Schedule D)

**예시:**  
"선박이 충돌이나 화재 등의 긴급 상황에 처했을 때는 즉각 Chevron 비상 정보 센터로 연락해야 합니다."

---

### 6. 품질/수량 측정 및 독립 검사

**목표:**  
제품의 품질과 수량 측정을 위한 표준 절차를 이해하고 독립 검사의 중요성을 학습한다.

**내용:**  
- **제품 품질/수량 측정 방법론** 소개 (Section 2.1)  
- **독립 검사관 임명 절차와 역할** (Section 2.2)

**예시:**  
"독립 검사관은 양 당사자가 동의한 후 임명되며 그 결과는 청구서 발행 기준으로 사용됩니다."

---

### 추가 고려 사항

각 섹션마다 실제 사례나 모의 상황을 통해 실습 기회를 제공합니다.  
교육 후에는 퀴즈나 토론 세션 등을 통해 신입 사원의 이해도를 평가합니다.

---

        """, unsafe_allow_html=True)
with tab2:
    with st.container():
        st.markdown("""---
### 세부 교육 과정: Part One - FOB Deliveries

---

#### 1. Section 1: Delivery (인도)

**목표:**  
FOB 조건에서 제품 인도의 절차와 책임을 명확히 이해한다.

**내용:**  
- 제품은 판매자가 구매자에게 제공한 선박에 적재됨으로써 인도된다.  
- 구매자는 선박을 준비하고, 판매자는 지정된 기간 내에 제품을 적재해야 한다.  
- 인도 시점에서 리스크가 구매자에게 이전됨.

**예시:**  
"FOB 조건에서는 판매자가 제품을 선적하는 순간부터 리스크가 구매자에게 넘어갑니다."

**참고 섹션:** [Part One Section 1]

---

#### 2. Section 2: Measurement and Sampling, Independent Inspection and Certification (측정 및 샘플링, 독립 검사 및 인증)

**목표:**  
제품의 품질과 수량 측정 방법과 독립 검사의 중요성을 이해한다.

**내용:**  
- 동적 미터 또는 탱크 게이지를 사용하여 수량 측정 (Section 2.1).  
- 품질은 Inline 샘플러 또는 탱크 샘플로 결정되며, 검사 결과는 청구서 발행 기준으로 사용됨.  
- 독립 검사관 임명 절차와 역할 설명 (Section 2.2).

**예시:**  
"독립 검사관이 발행한 품질/수량 증명서는 오류나 사기 외에는 양 당사자에게 구속력을 가집니다."

**참고 섹션:** [Part One Section 2]

---

#### 3. Section 3: Risk and Title (리스크 및 소유권)

**목표:**  
리스크와 소유권 이전 시점을 정확히 파악하고 이를 실무에 적용한다.

**내용:**  
- 리스크는 제품이 선적되는 순간 구매자에게 이전됨.  
- 소유권 역시 동일한 시점에 이전되지만, 계약서 상 특별 조항이 있을 경우 예외 가능성 있음.  
- 위험 부담과 소유권 이전의 차이를 명확히 구분함으로써 분쟁 예방 가능.

**예시:**  
"제품이 선적된 후 발생하는 손실이나 손상은 모두 구매자의 책임입니다."

**참고 섹션:** [Part One Section 3]

---

#### 4. Section 4: Laydays

**목표:**  
Laydays 개념과 설정 방법을 학습하고 이를 통해 효율적인 운송 계획을 세운다.

**내용:**  
- Laydays는 구매자가 지명한 선박이 유효한 Notice of Readiness(NOR)를 제출해야 하는 기간임 (Section 4.1).  
- Laydays는 특별 조항(Special Provisions)에 따라 설정되거나 판매자가 통지함 (Section 4.2).  
- Laydays 범위 내에서만 적재가 이루어져야 하며, 이를 벗어나면 추가 비용 발생 가능성 있음.

**예시:**  
"Laydays는 일반적으로 계약서 상 명시된 날짜 범위 내에서 정해지며, 이 기간 동안 NOR 제출이 필수입니다."

**참고 섹션:** [Part One Section 4]

---

#### 5. Section 6: Arrival of Vessel, Loading, Berth (선박 도착 및 적재 절차)

**목표:**  
선박 도착 후 적재 절차와 관련된 규정을 숙지하고 실제 상황에 적용한다.

**내용:**  
- NOR Tener 후 판매자는 즉시 적재 준비를 해야 함 (Section 6.1).  
- 부두 배정 문제나 기타 이유로 인해 지연될 경우 발생할 수 있는 비용 처리 방안 학습.  
- 부두 접근 권리와 관련된 규정 설명 (Berth Clause).

**예시:**  
"NOR Tender 후에도 부두가 준비되지 않으면 그로 인해 발생하는 지연비용은 판매자의 책임일 수 있습니다."

**참고 섹션:** [Part One Section 6]

---

#### 6. Section 7: Laytime, Delays and Demurrage (Laytime 계산 및 체선료 처리)

**목표:**  
Laytime 계산 방식과 체선료(Demurrage)의 발생 원인을 이해하고 관리 방안을 학습한다.

**내용:**  
- Laytime 시작 시점과 종료 시점 정의  
- 허용 시간(Laytime)을 초과할 경우 체선료 발생  
- 지연 원인 분석 및 각 당사자의 책임 구분

**예시:**  
"Laytime 초과로 인해 체선료가 발생하면 이는 일반적으로 구매자가 부담합니다."

---

### 추가 고려 사항

각 섹션마다 실제 사례나 모의 상황을 통해 실습 기회를 제공합니다 (예: 특정 상황에서 NOR 제출 타이밍 맞추기 등).  
교육 후에는 퀴즈나 토론 세션 등을 통해 신입 사원의 이해도를 평가합니다.

---

### 요약

이 커리큘럼은 신입 사원이 Part One의 주요 조항들을 심층적으로 학습하도록 돕습니다. 특히 FOB 거래에서 자주 마주치는 상황들(리스크 이전 시점, Layday 설정 등)을 중심으로 구성되어 있으며 실무 적용 능력을 키우는 데 중점을 둡니다.

---

### 출처

- 인도 관련 내용 (Part One Section 1)  
- 측정 및 샘플링 관련 내용 (Part One Section 2)  
- 리스크 및 타이틀 관련 내용 (Part One Section 3)  
- Layday 설정 관련 내용 (Part One Section 4)  
- 선박 도착 및 적재 절차 (Part One Section 6)  
- 체선료 처리 관련 내용 (Part One Section 7)

---

        """, unsafe_allow_html=True)


with tab3:
    with st.container():
        st.markdown("""---

### 세부 교육 과정: Part Two - CFR, CIF 및 DAP Deliveries

---

#### 1. Section 8: Delivery (인도)

**목표:**  
CFR, CIF 및 DAP 조건에서 제품 인도의 절차와 각 당사자의 책임을 명확히 이해한다.

**내용:**  
- **CFR/CIF 인도:** 판매자는 제품을 선적하고 지정된 도착항까지 운송해야 하며, 리스크는 선적 시점에 구매자에게 이전됨 (Section 8.1).  
- **DAP 인도:** 판매자는 제품을 지정된 도착지까지 운송하며 리스크는 도착지에서 구매자에게 이전됨 (Section 8.2).  
- 각 조건별로 리스크와 비용 부담의 차이점 설명.

**예시:**  
"CIF 조건에서는 판매자가 보험료를 부담하지만 리스크는 선적 시점에 구매자에게 넘어갑니다."

**참고 섹션:** [Part Two Section 8]

---

#### 2. Section 9: Risk and Title (리스크 및 소유권)

**목표:**  
CFR, CIF 및 DAP 거래에서 리스크와 소유권 이전 시점을 정확히 파악하고 이를 실무에 적용한다.

**내용:**  
- **CFR/CIF 거래:** 리스크는 제품이 선박에 적재되는 순간 구매자에게 이전되지만 소유권은 계약서 상 명시된 대로 따름.  
- **DAP 거래:** 리스크는 제품이 지정된 도착지에 도달한 후 구매자에게 이전됨.  
- 소유권과 리스크가 반드시 동일한 시점에 이전되지 않을 수 있음을 강조.

**예시:**  
"DAP 조건에서는 제품이 목적지에 도착할 때까지 모든 위험은 판매자가 부담합니다."

**참고 섹션:** [Part Two Section 9]

---

#### 3. Section 10: Laydays and Cancelling Date (Laydays 설정 및 취소일)

**목표:**  
Laydays 설정과 취소일(Cancelling Date)의 개념을 이해하고 이를 통해 효율적인 운송 계획을 세운다.

**내용:**  
- Laydays 기간 동안 선박이 준비되지 않으면 계약 취소 가능성 있음 (Section 10.1).  
- 특별 조항(Special Provisions)에 따라 Laydays와 취소일 설정 가능.  
- Laydays 범위 내에서만 적재가 이루어져야 하며 이를 벗어나면 추가 비용 발생 가능성 있음.

**예시:**  
"Laydays 기간 내에 선박이 준비되지 않으면 계약 해지가 가능합니다."

---

#### 4. Section 11: Vessel Nomination and Substitution (선박 지명 및 교체)

**목표:**  
선박 지명 절차와 교체 규정을 숙지하여 원활한 운송 계획을 수립한다.

**내용:**  
- 구매자는 특정 기한 내에 선박 지명을 완료해야 함(48시간 전 통보 등).  
- 지명된 선박이 불가피하게 변경될 경우 교체 절차를 준수해야 함(Section 11.2).  
- 교체 가능한 상황과 그로 인해 발생하는 추가 비용 처리 방안 학습.

**예시:**  
"구매자가 지명한 선박이 변경될 경우 즉시 판매자에게 통보해야 합니다."

---

#### 5. Section 12-13: Loading/Discharge Port Operations (선적/하역 항구 운영)

**목표:**  
항구에서의 적재 및 하역 절차를 이해하고 각 당사자의 역할과 책임을 명확히 한다.

**내용:**  
- 적재 항구에서의 작업은 판매자의 책임이며, 하역 항구에서는 구매자가 주도함 (Section 12 & Section 13).  
- 항구 혼잡이나 기타 이유로 인해 발생하는 지연비용 처리 방안 학습(Laytime 계산 포함).

**예시:**  
"하역 항구에서 발생하는 모든 비용은 일반적으로 구매자가 부담합니다."

---

#### 6. Section 14-15: Demurrage and Despatch Money (체선료 및 조출료)

**목표:**  
체선료(Demurrage)와 조출료(Despatch Money)의 개념을 이해하고 실제 사례를 통해 계산 방법을 익힌다.

**내용:**  
- 허용 시간(Laytime)을 초과하면 체선료가 발생하며 이는 일반적으로 구매자가 부담함 (Section 14).  
- 반대로 허용 시간보다 빨리 작업이 완료되면 조출료 지급 가능성 있음 (Section 15).  
- 체선료/조출료 계산 방식 학습(Laytime 시작/종료 기준 포함).

**예시:**  
"Laytime 초과로 인해 체선료가 발생하면 이는 일반적으로 구매자가 부담합니다."

---

### 추가 고려 사항

각 섹션마다 실제 사례나 모의 상황을 통해 실습 기회를 제공합니다 (예: 특정 상황에서 NOR 제출 타이밍 맞추기 등).  
교육 후에는 퀴즈나 토론 세션 등을 통해 신입 사원의 이해도를 평가합니다.

---

### 요약

이 커리큘럼은 신입 사원이 Part Two의 주요 조항들을 심층적으로 학습하도록 돕습니다. 특히 CFR, CIF, DAP 거래에서 자주 마주치는 상황들(리스크 이전 시점, Layday 설정 등)을 중심으로 구성되어 있으며 실무 적용 능력을 키우는 데 중점을 둡니다.

---

### 출처

- 인도 관련 내용 (Part Two Section 8)  
- 리스크 및 타이틀 관련 내용 (Part Two Section 9)  
- Layday 설정 관련 내용 (Part Two Section 10)  
- 선박 지명 관련 내용 (Part Two Section 11)

---

        """, unsafe_allow_html=True)

with tab4:
    with st.container():
        st.markdown("""---
### 세부 교육 과정: Part Three - Barge Deliveries

---

### 1. Section 17 & Section 25: Applicability (적용 범위)

**목표:**  
Part Three가 적용되는 상황과 지역을 명확히 이해한다.

**내용:**  
- Part One 및 Part Two의 조항이 적절한 경우 적용되며, 별도로 명시된 경우에는 Part Three의 규정이 우선함.  
- **북서유럽(North-West Europe):** FOB, CFR 및 CIF 조건으로 바지선을 통해 제품이 인도됨 (Section 17).  
- **미국 국내(U.S. Domestic):** FOB, CFR, CIF 및 DAP 조건으로 바지선을 통해 제품이 인도됨 (Section 25).

**예시:**  
"북서유럽에서는 주로 FOB와 CFR/CIF 조건으로 거래가 이루어지고 미국 내에서는 DAP까지 포함됩니다."

**참고 섹션:**  
[Part Three(A) Section 17], [Part Three(B) Section 25]

---

### 2. Section 24 & Section 34: Part Cargo (부분 화물 처리)

**목표:**  
여러 당사자가 동일한 바지선을 사용할 때 발생하는 비용 분담 방식을 이해한다.

**내용:**  
- 여러 당사자가 동시에 또는 순차적으로 화물을 적재하거나 하역할 경우 체선료(Demurrage)를 어떻게 분배하는지 학습.  
- 동시 적재/하역 시 총 화물량에 비례하여 체선료를 분배함 (Section 24.1.1 / Section 34.1.1).  
- 순차적 적재/하역 시 각 당사자는 자신의 화물 처리 시간만큼 책임짐 (Section 24.1.2 / Section 34.1.2).  
- 여러 항구에서 적재/하역할 경우 각 항구별로 체선료 계산 후 비례 배분 (Section 24.1.3 / Section 34.1.3).

**예시:**  
"동시에 여러 당사자의 화물이 적재될 경우 전체 화물량에 따라 체선료가 나누어집니다."

**참고 섹션:**  
[Part Three(A) Section 24], [Part Three(B) Section 34]

---

### 3. Section 26: Measurement and Sampling, Independent Inspection and Certification (측정 및 샘플링, 독립 검사 및 인증)

**목표:**  
바지선을 통한 제품 운송 시 품질과 수량 측정 방법을 이해하고 독립 검사의 중요성을 학습한다.

**내용:**  
- FOB/CFR/CIF/DAP 거래 모두에서 제품의 품질과 수량은 선적 또는 하역 시점에서 독립적인 검사관에 의해 측정됨 (Section 26).  
- 측정 기준은 API나 ASTM 등 국제적으로 인정된 표준을 따름.  
- 검사 결과는 청구서 발행 기준으로 사용되며 오류나 사기 등의 특별한 상황 외에는 구속력을 가짐.

**예시:**  
"독립 검사관이 발행한 보고서는 양 당사자에게 구속력이 있으며 청구서 발행 기준으로 사용됩니다."

**참고 섹션:**  
[Part Three(B) Section 26]

---

### 4. Section 29 & Section 27: Nominations in Respect of DAP and FOB Deliveries (DAP 및 FOB 인도 관련 지명 절차)

**목표:**  
DAP와 FOB 거래에서 선박 지명(Nomination)의 절차와 요구사항을 숙지한다.

**내용:**  
- 판매자는 선박 도착 예정 시간(ETA)을 기준으로 최소한 48시간 전 통보해야 함, 단 공휴일 제외 (Section 29 / Section 27).  
- 지명 내용에는 바지선 이름과 등록 번호, 이전 화물 기록 등 필수 정보가 포함되어야 함 (Section 29 / Section 27).  
- 지명이 변경될 경우 새로운 지명으로 간주되며 다시 통보해야 함 (Section 29 / Section 27).

**예시:**  
"FOB 거래에서는 구매자가 선박 ETA를 최소한 영업일 기준으로 이틀 전에 통보해야 합니다."

**참고 섹션:**  
[Part Three(B) Sections 29 & 27]

---
        """, unsafe_allow_html=True)

with tab5:
    with st.container():
        st.markdown("""---

### 세부 교육 과정: General Provisions

---                  

### 1. Section 46: Health, Safety and Environment (건강, 안전 및 환경)

**목표:**  
REACH 규정과 MSDS 제공 의무를 이해하고 이를 실제 거래에 적용하는 방법을 학습한다.

**내용:**  
- **REACH 규정 준수 의무(Section 46.1):** EEA(유럽 경제 지역) 내에서 제품이 물리적으로 도입될 때 판매자와 구매자는 REACH 규정을 준수해야 함.  
- **MSDS(Material Safety Data Sheet) 제공 시점(Section 46.1.3):** 인도 조건에 따라 MSDS를 제공해야 하는 시점이 다름(FCA/FOB/CIF/DAP 등).  
- **구매자의 건강 및 안전 책임(Section 46.3):** 구매자는 제품 취급 시 직원들에게 적절한 정보와 교육을 제공해야 함.

**예시:**  
"FOB 조건에서는 선적 시점에 MSDS를 제공해야 하며, DAP 조건에서는 제품이 도착할 때까지 MSDS가 제공되어야 합니다."

**참고 섹션:**  
[Part Six Section 46]

---

### 2. Section 50: New and Changed Regulations (법률 변경 및 새로운 규제 대응)

**목표:**  
법률이나 규제가 변경될 경우 가격 또는 계약 조건 재협상 옵션을 이해한다.

**내용:**  
- 새로운 법규나 규제 변화로 인해 판매자가 경제적으로 불리한 영향을 받을 경우 가격 재협상 요청 가능 (Section 50.2).  
- 협상이 실패할 경우 계약 종료 가능성 있음.

**예시:**  
"새로운 세금이나 관세가 도입되어 판매자에게 불리한 영향을 미칠 경우 가격 재협상을 요청할 수 있습니다."

**참고 섹션:**  
[Part Six Section 50]

---

### 3. Section 56: Sanctions and Boycotts (제재 및 보이콧 관련 조항)

**목표:**  
국제 제재나 보이콧 상황에서 계약 이행의 제한 사항을 이해하고 이를 실무에 반영한다.

**내용:**  
- **EU, UN 또는 미국의 무역 제재나 외국 무역 통제법 위반 시** 계약 의무 이행 면제 가능 (Section 56.1).  
- 제재로 인해 의무 이행이 불가능해질 경우 상대방에게 서면으로 통보 후 해당 의무를 일시 중단하거나 계약 해지 가능 (Section 56.2).  
- 특정 국가나 지역으로의 수출 금지 또는 제한 사항 설명.

**예시:**  
"만약 특정 국가가 UN 제재 대상이라면 그 국가로의 제품 수출은 금지됩니다."

**참고 섹션:**  
[Part Six Section 56]

---

### 4. Section 57: Anti-Corruption and Anti-Facilitation of Tax Evasion (부패 방지 및 탈세 방지)

**목표:**  
부패 방지와 탈세 방지를 위한 국제적인 법적 요구사항을 숙지하고 준수 방법을 학습한다.

**내용:**  
- **부패 방지 관련 조항 설명(Section 57):** FCPA(미국 해외부패방지법), UK Bribery Act 등 주요 국제법 준수 필요성 강조.  
- **구체적인 행동 지침 설명(Section 57.2):** 정부 공무원에게 뇌물 제공 금지와 같은 행동 지침.  
- **위반 시 계약 해지 가능(Section 57.4):** 위반 시 즉각적인 계약 해지 가능.

**예시:**  
"정부 공무원에게 뇌물을 주거나 약속하는 행위는 엄격히 금지되며 위반 시 즉각적으로 계약이 해지될 수 있습니다."

**참고 섹션:**  
[Part Six Section 57]

---

### 5. Sections 53 & 58: Termination or Suspension / Arbitration and Small Claims (계약 종료/중단 및 중재 절차)

**목표:**  
계약 종료 사유와 분쟁 발생 시 해결 절차를 이해하고 이를 실무에 적용한다.

**내용:**  
- **계약 종료(Section 53):** 한쪽 당사자가 파산하거나 채권자들과 합의를 할 경우 다른 당사자는 즉시 계약을 종료하거나 인도를 중단할 권리가 있음.  
- **분쟁 해결 절차(Section 58):** 모든 분쟁은 런던 국제중재법원(LCIA)의 규칙에 따라 중재로 해결하며 소액 청구는 LMAA 소액 청구 절차를 따름.  
- 체선료 관련 분쟁은 별도의 LMAA 체선료 관련 절차를 따름 (Section 58.3).

**예시:**  
"분쟁 발생 시 런던 국제중재법원의 규칙에 따라 중재가 진행되며 소액 청구는 별도의 간소화된 절차로 처리됩니다."

**참고 섹션:**  
[Part Six Sections 53 & 58]

---

### 6. Section 60: Governing Law and Sovereign Immunity Waiver (준거법 및 주권 면책 포기)

**목표:**  
해당 계약서에서 적용되는 준거법과 주권 면책 포기의 의미를 이해한다.

**내용:**  
- **본 계약서는 영국법에 의해 해석되고 집행됨(English Law)** (Section 60.1).  
- **유엔 국제물품매매계약협약(CISG)은 적용되지 않음** (Section 60.2).  
- **주권 면책 권리 포기(Section 60.3):** 각 당사자는 상업적 목적으로 본 계약을 체결했으며 주권 면책 권리를 포기함.

**예시:**  
"본 계약서는 영국법 하에서 해석되며 각 당사자는 상업적 목적으로 주권 면책 권리를 포기합니다."

**참고 섹션:**  
[Part Six Section 60]

---

### 추가 고려 사항

각 섹션마다 실제 사례나 모의 상황을 통해 실습 기회를 제공합니다 (예: 제재 상황에서 거래 중단 결정하기 등).  
교육 후에는 퀴즈나 토론 세션 등을 통해 신입 사원의 이해도를 평가합니다.

---

### 요약

이 커리큘럼은 신입 사원이 Part Six의 주요 일반 조항들을 심층적으로 학습하도록 돕습니다. 특히 건강/안전/환경 규정(REACH), 부패 방지, 제재 대응 등의 중요한 법적 요구사항과 분쟁 해결 절차 등을 중심으로 구성되어 있으며 실무 적용 능력을 키우는 데 중점을 둡니다.

---

### 출처

- 건강/안전/환경 관련 내용 [Part Six Section 46]  
- 법률 변경 대응 [Part Six Section 50]  
- 제재 및 보이콧 관련 내용 [Part Six Section 56]  
- 부패 방지 조항 [Part Six Section 57]  
- 분쟁 해결 절차 [Part Six Sections 53 & 58]  
- 준거법 및 주권 면책 포기 [Part Six Section 60]

---

        """, unsafe_allow_html=True)
        
with tab6:
    with st.container():
        st.markdown("""---
### 세부 교육 과정: Schedules (부록)

---                  
### 1. Schedule E: Supplement in Respect of LPG (LPG 관련 보충 규정)

**목표:**  
LPG 거래 시 적용되는 특별한 규정을 이해하고 이를 실무에 반영한다.

**내용:**  
- Part One 및 Part Two의 조항이 기본적으로 적용되지만, LPG 거래에서는 일부 수정된 규정이 적용됨 (Section 1.1).  
- **FOB 인도 시 지명(Nomination) 절차:** 선박의 적재 온도와 이전 3개의 화물 기록을 추가로 제공해야 함 (Section 2.1).  
- **Laytime 계산 방식 변경:** 일반적인 36시간 대신 LPG 거래에서는 24시간으로 단축됨 (Section 2.2).

**예시:**  
"FOB 조건에서 LPG를 거래할 때는 선박의 적재 온도와 이전 화물 기록을 반드시 제출해야 합니다."

**참고 섹션:**  
[Schedule E Sections 1-2]

---

### 2. Schedule D: Chevron Incident Reporting Procedure (Chevron 사고 보고 절차)

**목표:**  
사고 발생 시 즉각적인 대응 및 보고 절차를 숙지하여 비상 상황에서 신속하게 대처할 수 있다.

**내용:**  
- Chevron 그룹과 관련된 선박에서 사고가 발생하면 즉시 Chevron 비상 정보 센터로 전화 통보 후 이메일로 서면 보고서를 제출해야 함 (Section D).  
- 이메일 제목에는 반드시 "INCIDENT REPORTING"이라는 문구가 포함되어야 하며, 사고 내용, 위치, 피해 규모 등을 상세히 기재해야 함.  
- 만약 사고가 항구 내에서 발생했다면 해당 항구의 에이전트에게도 복사본을 보내야 함.

**예시:**  
"선박 충돌이나 유출 사고가 발생하면 즉시 Chevron 비상 정보 센터로 연락하고 서면 보고서를 제출해야 합니다."

**참고 섹션:**  
[Schedule D Section]

---

### 3. Schedule C: Vessel Requirements (선박 요건)

**목표:**  
계약서 상 명시된 선박 요건을 이해하고 이를 통해 안전한 운송을 보장한다.

**내용:**  
- 모든 선박은 **ITOPF(International Tanker Owners Pollution Federation)**에 가입되어 있어야 하며, 이는 오염 사건 발생 시 신속한 대응을 위한 필수 조건임 (Section C1.2).  
- **ISPS 코드 준수 의무:** 모든 선박은 국제 해양 보안 코드(ISPS Code)를 준수해야 하며, 이는 테러리즘 및 기타 위협으로부터 보호하기 위한 국제 표준임 (Section C1.3).  
- 이러한 요건을 충족하지 못하는 경우 판매자는 선적 거부 권리를 가질 수 있음.

**예시:**  
"모든 선박은 ITOPF에 가입되어 있어야 하며 ISPS 코드를 준수하지 않으면 운송이 거부될 수 있습니다."

**참고 섹션:**  
[Schedule C Section]

---

### 4. Schedule B & A: Quality and Quantity Determination (품질 및 수량 결정 방법)

**목표:**  
제품 품질과 수량 측정 방법론을 학습하고 이를 실무에 적용한다.

**내용:**  
- 품질/수량 측정은 **API 또는 ASTM 기준**에 따라 이루어지며, 독립 검사관이 임명될 경우 그 결과는 양 당사자에게 구속력을 가짐 (Schedule B & A).  
- **동적 미터(Dynamic Metering System)**를 사용하거나 **탱크 게이지(Tank Gauging)**를 통해 정확한 측정을 수행함.  
- 검사 결과는 청구서 발행 기준으로 사용되며 오류나 사기 등의 특별한 상황 외에는 구속력을 가짐.

**예시:**  
"독립 검사관이 발행한 품질/수량 증명서는 오류나 사기 외에는 양 당사자에게 구속력을 가집니다."

**참고 섹션:**  
[Schedule B & A Section]

---

### 5. Schedule F: Special Provisions for Specific Products or Regions (특정 제품 또는 지역별 특별 조항)

**목표:**  
특정 제품이나 지역별로 적용되는 특별 조항들을 이해하고 이를 실무에 반영한다.

**내용:**  
- 특정 제품(LPG 등) 또는 특정 지역(EU 등)에 대해 별도로 명시된 법적 요구사항이나 규제 설명 (Schedule F).  
- 예를 들어 **EU 내 REACH 규정** 준수를 위해 필요한 추가 서류나 인증 요구사항 등이 있을 수 있음.

**예시:**  
"EU 내에서 REACH 규정을 준수하기 위해서는 추가적인 인증서와 서류가 필요합니다."

---

### 추가 고려 사항

각 섹션마다 실제 사례나 모의 상황을 통해 실습 기회를 제공합니다 (예: 사고 발생 시 보고 절차 수행하기 등).  
교육 후에는 퀴즈나 토론 세션 등을 통해 신입 사원의 이해도를 평가합니다.

---

### 요약

이 커리큘럼은 신입 사원이 Part Seven의 주요 부록들을 심층적으로 학습하도록 돕습니다. 특히 **LPG 거래**, **사고 보고 절차**, **선박 요건** 등의 중요한 특수 상황과 관련된 법적 요구사항과 운영 방침 등을 중심으로 구성되어 있으며 실무 적용 능력을 키우는 데 중점을 둡니다.

---

### 출처

- LPG 관련 보충 규정 [Schedule E]  
- Chevron 사고 보고 절차 [Schedule D]  
- 선박 요건 [Schedule C]  
- 품질 및 수량 결정 방법 [Schedules B & A]

---

        """, unsafe_allow_html=True)





with tab7:
 # st.header("회사 별 :blue[GT&C] Viewer :sunglasses:", divider="blue")
    # PDF 페이지를 이미지로 변환하는 함수
    def pdf_page_to_image(pdf_path, page_number, zoom=1.5):  # zoom 값 수정
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_number)  # 페이지 로드
        # 확대/축소 비율을 설정하여 적절한 크기로 표시
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)  # 확대된 비율로 픽스맵 생성
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return img

    # 기본 PDF 파일 경로
    default_pdf_path = "Chevron 2014.pdf"

    # PDF 파일을 열고 총 페이지 수 가져오기
    doc = fitz.open(default_pdf_path)
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
    image = pdf_page_to_image(default_pdf_path, st.session_state.page_number, zoom=10)  # zoom 값 조정
    st.image(image, use_column_width=True)  # 이미지를 전체 너비로 표시
