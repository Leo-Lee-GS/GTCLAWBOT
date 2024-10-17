import streamlit as st
import fitz  # PyMuPDF
from PIL import Image


# st.title("Case_Study")
st.header(":blue[Chevron, Shell, BP GT&C]를 한 눈에 쉽게 비교해 보세요! :sunglasses:", divider="gray")



# Tab 생성
tab1, tab2, tab3 = st.tabs([
                            "FOB Delivery", 
                            "CFR & CIF Delivery", 
                            "공통 사항", 
                            ])


with tab1:
    with st.container():
        st.markdown("""---
### FOB Deliveries

| **Section**                     | **Chevron**                                                    | **Shell**                                            | **BP**                                                      |
|----------------------------------|----------------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------|
| **Delivery**                     | "The Product shall be delivered by the Seller to the Buyer, in bulk FOB at the Loading Terminal onto Vessel(s) provided or procured by the Buyer."| "The Product shall be delivered by the Seller to the Buyer, in bulk FOB at the Loading Terminal onto Vessel(s) provided or procured by the Buyer."| "The Crude Oil or Product shall be delivered by the Seller to the Buyer, in bulk FOB at the Loading Terminal."|
| **Measurement and Sampling**     | **Quantity**: Determined using proven dynamic meters, or if unavailable, manual shore tank gauges. If shore tank gauges are inaccurate or the floating roof is not in the critical zone, Vessel's figures (with VEFL) shall be used. **Quality**: Testing through proven inline sampler or shore tank sample. | "Measurement and sampling" follow standard practice at the Loading Terminal. Certificates of quantity and quality are binding unless there's manifest error or fraud.| "Measurement of quantities and sampling for quality follow standard practice at the Loading Terminal. Independent inspection is possible upon agreement."|
| **Independent Inspection**       | Either party may appoint an inspector, shared cost. In absence of agreement, either can appoint their representative.| Similar to Chevron, either party can appoint an inspector. The costs are shared equally.| Inspection is handled similarly; shared costs for independent inspectors.|
| **Risk and Property**            | Risk and title transfer as the product passes the Vessel’s hose connection. Buyer is liable for loss/damage caused by the Vessel.| Same: Risk and title transfer at the Vessel’s hose connection. Buyer is liable for damages caused by the Vessel.| Risk and property transfer at the Vessel’s hose connection, with the Buyer responsible for any losses during loading.|
| **Laydays**                      | Laydays as specified in Special Provisions, or communicated by Seller 12 days before, or by the 20th of the prior month.| Similar layday specification, with notification at least 12 days before, or by the 20th day of the previous month.| Similar layday structure with notification procedures.|
| **Nomination of Vessels**        | Buyer nominates Vessel, specifying key details. Substitutions allowed with prior notice, subject to size and layday limits.| Buyer nominates Vessel with required details. Substitutions are allowed under similar conditions as Chevron.| Buyer nominates Vessel with specifications. Substitutions allowed with Seller’s consent and similar limitations.|
| **Berth and Loading**            | Buyer’s Vessel must report ETA 72, 48, and 24 hours before arrival. Loading to commence as soon as practical after NOR.| Same ETA reporting structure and similar obligations regarding commencement of loading.| Buyer’s Vessel must report 72, 48, and 24 hours prior. Loading starts after NOR.|
| **Demurrage**                    | Demurrage calculation based on running hours, with specific exclusions for delays caused by the Buyer or the Vessel.| Demurrage terms are similar, with detailed provisions on when time does not count, such as Vessel-related delays.| Demurrage terms are based on running hours, with exclusions for Buyer or Vessel-caused delays.|

**Key Differences:**
- **Measurement and Sampling**: Chevron relies on dynamic meters or vessel figures if shore measurements fail, while Shell and BP rely on the standard terminal practice without specific backup procedures for measurement accuracy.
- **Independent Inspection**: The procedures are similar across all three companies, with shared costs and the option for independent inspectors.
- **Demurrage Conditions**: Chevron, Shell, and BP generally follow similar demurrage structures, but the exact timing of when running hours begin and cease varies slightly between companies. Chevron provides a bit more detail on specific causes like vessel failures impacting demurrage. 
---

### FOB Deliveries 한글 비교

| **항목**                        | **Chevron**                                                    | **Shell**                                            | **BP**                                                      |
|----------------------------------|----------------------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------|
| **인도**                         | "제품은 매수인이 제공하거나 준비한 선박에 매도인이 FOB 조건으로 로딩 터미널에서 벌크 형태로 매수인에게 인도된다".| "제품은 매수인이 제공하거나 준비한 선박에 매도인이 FOB 조건으로 로딩 터미널에서 매수인에게 인도된다".| "원유 또는 제품은 로딩 터미널에서 매도인이 매수인에게 FOB 조건으로 벌크 형태로 인도된다".|
| **측정 및 샘플링**              | **수량**: 동적 미터(dynamic meters)로 측정. 동적 미터가 없을 경우, 육상 탱크 측정기를 사용하며, 정확하지 않을 경우 VEFL이 적용된 선박의 데이터를 사용. **품질**: 인라인 샘플러로 샘플링, 없을 경우 육상 탱크에서 샘플 추출. | "로딩 터미널의 표준 절차에 따라 제품의 수량과 품질이 측정 및 샘플링 된다. 발행된 증명서는 명백한 오류 또는 사기가 아닌 한 양 당사자를 구속한다".| "로딩 터미널의 표준 관행에 따라 수량과 품질을 측정 및 샘플링하며, 독립 검사인도 합의에 따라 지정 가능".|
| **독립 검사**                   | 양 당사자가 독립 검사를 요청할 수 있으며, 비용은 반반씩 부담. 합의되지 않을 경우 각 당사자는 대리인을 지정 가능.| Chevron과 유사하며, 양측이 독립 검사인을 임명할 수 있으며 비용은 반반씩 부담.| 독립 검사인 임명과 관련한 절차는 비슷하며, 비용은 양측이 분담.|
| **위험 및 소유권**               | 제품이 선박의 호스 연결부를 지나면서 위험과 소유권이 매수인에게 이전됨. 선박으로 인해 발생하는 손해는 매수인이 책임.| 동일하게, 선박의 호스 연결부를 지나면서 위험과 소유권이 매수인에게 이전되며, 선박으로 인한 손해는 매수인이 책임.| 제품이 선박의 호스 연결부를 지나면 위험 및 소유권이 매수인에게 이전되며, 로딩 중 발생하는 손실은 매수인의 책임.|
| **정박일(Laydays)**             | 특별 조항에 명시된 날짜 또는 매도인이 12일 전 또는 전월 20일까지 매수인에게 통보한 날짜.| 유사하게 특별 조항에 따라 정박일이 설정되며, 통보는 12일 전 또는 전월 20일까지 해야 함.| 유사한 정박일 구조 및 통보 절차.|
| **선박 지명**                   | 매수인은 선박을 지명하며, 주요 세부 사항을 명시해야 함. 대체 선박은 사전 통보 후 허용되며, 크기와 정박일 제한이 적용.| 매수인은 선박을 지명하며, 대체 선박은 유사한 조건 하에 허용됨.| 매수인은 선박을 지명하고 사양을 제출해야 하며, 대체 선박은 매도인의 동의가 필요.|
| **정박 및 로딩**                | 매수인의 선박은 72, 48, 24시간 전에 ETA(예정 도착 시간)를 보고해야 하며, NOR이 제출된 후 가능한 빨리 로딩을 시작.| Chevron과 같은 ETA 보고 구조 및 NOR 제출 후 로딩 의무.| 매수인의 선박은 ETA를 72, 48, 24시간 전에 보고해야 하며, NOR 이후 로딩 시작.|
| **체선료(Demurrage)**           | 체선료는 실시간(running hours) 기준으로 계산되며, 매수인 또는 선박의 문제로 인한 지연은 제외.| 체선료 조건은 유사하며, 선박 관련 지연의 경우 시간 계산에서 제외.| 실시간 기준으로 체선료 계산되며, 매수인이나 선박 문제로 인한 지연은 제외.|

**Key Differences:**
- **측정 및 샘플링**: Chevron은 동적 미터와 선박의 데이터를 사용해 정확성을 보장하는 반면, Shell과 BP는 로딩 터미널의 표준 관행을 따르며, 별도의 백업 절차를 명시하지 않음.
- **독립 검사**: 세 회사 모두 독립 검사를 허용하고 비용을 반반 부담하나 절차는 거의 동일.
- **체선료 조건**: Chevron, Shell, BP 모두 체선료 구조는 비슷하지만, 세부 사항에서 약간의 차이가 있음. Chevron은 선박 문제로 인한 지연에 대한 구체적인 조건을 더 상세히 명시.
---
        """, unsafe_allow_html=True)
with tab2:
    with st.container():
        st.markdown("""---
### CFR/CIF Deliveries

| Section | Chevron | Shell | BP |
|---------|---------|-------|----|
| **Delivery (CFR/CIF)** | The Seller delivers the product in bulk at the Loading Terminal and ships it CFR or CIF to the agreed Discharge Port. | Product is delivered in bulk at the Loading Terminal and shipped CFR or CIF to the Discharge Port. | The Seller places the product on board the vessel for CFR or CIF delivery from the Loading Terminal to the Discharge Terminal. |
| **Measurement and Sampling** | Measurement of quantity is determined by proven dynamic meters at the Loading Terminal. If unavailable, manual shore tank gauges are used. Quality is determined by inline samplers or composite shore tank samples. | Measurement and sampling are based on standard practice at the Loading Terminal. Independent inspectors may be appointed by either party, with costs shared. | Measurement and sampling are performed by either the terminal’s own inspectors or independent inspectors if agreed. Costs for independent inspectors are shared equally. |
| **Risk and Property Transfer** | Risk and title pass to the Buyer at the Vessel’s permanent hose connection at the Loading Terminal. | Risk and property pass to the Buyer at the Vessel’s permanent hose connection at the Loading Terminal. | Risk passes when the product passes the Vessel’s hose connection at the Loading Terminal. |
| **Insurance (CFR)** | Responsibility for securing insurance rests wholly with the Buyer. | The Buyer is responsible for insurance. | No obligation to secure insurance for either party. |
| **Insurance (CIF)** | Seller procures marine insurance for 110% of shipment value. Insurance covers marine risks. | Seller provides insurance for 110% of the shipment value against marine risks. | Seller provides insurance for 110% of shipment value against marine risks. |
| **Laydays** | Laydays are the period during which the Seller’s vessel must tender a NOR at the Loading Terminal. | Laydays are specified, and the vessel must tender NOR at the Loading Terminal. | Laydays are specified, and the vessel must tender NOR at the Loading Terminal. |
| **Nomination of Vessels** | The Seller nominates the vessel at least 5 days prior to the first Layday or ETA. | Vessel nomination is made 5 days before Laydays for Products and 8 days for Crude Oil. | The Seller nominates vessels 5 days for Products and 8 days for Crude Oil before Laydays. |
| **Independent Inspection** | Either party may appoint a mutually acceptable independent inspector. If they fail to agree, each party can appoint its own inspector. | Either party may appoint an independent inspector, with costs shared. | Independent inspectors are appointed by mutual agreement. If not, each party may appoint its own inspector. |

**Key Differences:**
- **Insurance (CFR)**: Chevron and Shell both place the responsibility for securing insurance on the Buyer, while BP explicitly states that neither party is obligated to secure insurance for CFR deliveries.
- **Measurement and Sampling**: Chevron uses dynamic meters or manual gauges and inline samplers for quality, while Shell and BP rely on standard terminal practices and shared costs for independent inspectors.
- **Nomination of Vessels**: All three companies require vessel nomination in advance, but Chevron specifies nominations 5 days prior to Laydays, while Shell and BP mention 5 days for Products and 8 days for Crude Oil.
---

### CFR/CIF Deliveries 한글 비교                  

| 항목 | Chevron | Shell | BP |
|---------|---------|-------|----|
| **인도 방식 (CFR/CIF)** | 판매자는 제품을 선적지에서 대량으로 인도하고, CFR 또는 CIF 조건으로 도착 항구까지 운송. | 제품은 선적지에서 대량으로 인도되고, CFR 또는 CIF 조건으로 도착 항구까지 운송. | 판매자는 선적지에서 제품을 선박에 적재하여 CFR 또는 CIF 조건으로 도착 항구까지 운송. |
| **계측 및 샘플링** | 제품의 수량은 선적지에서 검증된 동적 계량기를 사용해 결정. 계량기가 없을 경우 수동 탱크 게이지 사용. 품질은 인라인 샘플러 또는 저장 탱크의 복합 샘플로 결정. | 선적지의 표준 절차에 따라 제품의 수량과 품질을 결정. 각 당사자는 독립 검사원을 지정할 수 있으며, 비용은 반반 부담. | 선적 터미널에서 판매자의 검사원이 계측 및 샘플링을 수행하며, 필요 시 독립 검사원이 지정됨. 비용은 양 당사자가 균등하게 부담. |
| **위험 및 소유권 이전** | 위험과 소유권은 선적지에서 제품이 선박의 영구 호스 연결부를 통과할 때 구매자에게 이전. | 위험과 소유권은 제품이 선적지에서 선박의 영구 호스 연결부를 통과할 때 구매자에게 이전. | 제품이 선적지에서 선박의 호스 연결부를 통과할 때 위험이 구매자에게 이전됨. |
| **보험 (CFR)** | 보험을 확보할 책임은 전적으로 구매자에게 있음. | 보험 책임은 구매자에게 있음. | 어느 당사자도 보험을 확보할 의무가 없음. |
| **보험 (CIF)** | 판매자는 선적 가액의 110%에 해당하는 해상 보험을 확보하며, 보험은 해상 위험을 포함. | 판매자는 선적 가액의 110%에 해당하는 해상 위험 보험을 제공. | 판매자는 선적 가액의 110%에 해당하는 해상 위험 보험을 제공. |
| **Laydays (적재 기간)** | Laydays는 판매자가 지정한 선박이 선적지에서 적재할 수 있는 날 또는 기간을 의미. | Laydays는 특정 기간으로 정의되며, 선박이 선적지에서 NOR을 제시해야 함. | Laydays는 특정 기간으로 정의되며, 선박이 선적지에서 NOR을 제시해야 함. |
| **선박 지명** | 판매자는 Laydays 첫날 또는 ETA 5일 전에 선박을 지명해야 함. | 제품의 경우 Laydays 5일 전, 원유의 경우 8일 전에 선박을 지명. | 제품의 경우 Laydays 5일 전, 원유의 경우 8일 전에 선박을 지명. |
| **독립 검사** | 양 당사자는 서로 합의한 독립 검사원을 지정할 수 있으며, 합의에 실패할 경우 각 당사자는 자체 검사원을 지명할 수 있음. | 양 당사자는 독립 검사원을 지정할 수 있으며, 비용은 반반 부담. | 독립 검사원은 합의에 의해 지정되며, 합의에 실패할 경우 각 당사자가 자체 검사원을 지정할 수 있음. |

**Key Differences:**
- **보험 (CFR)**: Chevron과 Shell은 보험 책임이 구매자에게 있다고 명시한 반면, BP는 CFR 인도 시 보험을 확보할 의무가 없다고 규정.
- **계측 및 샘플링**: Chevron은 동적 계량기 또는 수동 게이지를 사용하고 품질은 인라인 샘플러로 결정하는 반면, Shell과 BP는 터미널의 표준 절차를 따르고 독립 검사원 비용을 공동 부담.
- **선박 지명**: 세 회사 모두 선박 지명 시점에 대해 규정하고 있으나, Chevron은 Laydays 5일 전에, Shell과 BP는 제품은 5일, 원유는 8일 전 지명을 요구.
---
 """, unsafe_allow_html=True)


with tab3:
    with st.container():
        st.markdown("""---
### 공통사항 비교

| **Section**                                | **Chevron**                                                                                                                                            | **Shell**                                                                                                                                           | **BP**                                                                                                                                                |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Quality**                                | Product quality must not be inferior to the specification in Special Provisions. Neither typicals nor delivery time stipulations form part of the description or fitness . | Product quality is defined by the Special Provisions. Typicals and time of delivery do not form part of the description .      | Quality should not be inferior to the specification. Typicals or delivery times do not constitute part of the product’s description  .|
| **Claims in respect of quality/quantity**   | Claims must be made within 60 days (FOB, CFR, CIF). Full documentation should follow within 90 days. No claim allowed for quantity differences ≤0.5% (for quantities ≤200,000 barrels) . | Claims must be made within 60 days (FOB, CFR, CIF). Documentation required within 90 days. No claim accepted for quantity differences ≤0.2% . | Claims should be submitted within 45 days of completion of discharge, supported with evidence. No claim accepted if quantity difference is ≤0.5%  . |
| **Health, Safety, and Environment (REACH)** | Chevron and Buyer must comply with REACH regulations for products delivered in EEA. MSDS provided at the point of delivery. No warranty provided on REACH information  . | Shell and Buyer will comply with REACH regulations within the EEA. MSDS provided to Buyer at time of delivery. No liability accepted for reliance on MSDS accuracy . | BP and Buyer will comply with REACH. Seller provides substance identifiers and current Safety Data Sheets (SDS). No liability for inaccurate substance info . |
| **Material Safety Data Sheet (MSDS)**      | MSDS provided at the point of delivery. Buyer must provide MSDS to relevant personnel .                                            | MSDS is provided. Buyer must provide MSDS or equivalent to employees and other relevant persons .                               | Seller provides SDS at the time of delivery. Buyer must provide it to employees and other responsible persons .                    |
| **Liability**                              | No responsibility for losses due to inherent hazards in the product .                                                             | Seller not responsible for losses caused by hazards in the nature of the product .                                            | BP is not responsible for any loss or injury resulting from the hazards inherent in the product .                                  |

**Key Differences:**
- **Claims Deadlines**: Chevron and Shell provide a 60-day window for filing claims for quality and quantity discrepancies, while BP has a shorter 45-day window.
- **Quantity Tolerance**: Chevron allows for a 0.5% discrepancy for loaded quantities ≤200,000 barrels, whereas Shell allows only up to 0.2%. BP's tolerance is 0.5% for all cases.
- **Health, Safety, and REACH Compliance**: All three require REACH compliance, but Chevron explicitly mentions it provides no warranty on the accuracy of REACH-related information, while Shell and BP include similar clauses about their limitations on REACH data liability.
- **Liability for Hazards**: All three companies absolve themselves of responsibility for any inherent hazards in the products delivered.
---
### 공통사항 한글 비교

| **항목**                                  | **Chevron**                                                                                                                                            | **Shell**                                                                                                                                           | **BP**                                                                                                                                                |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **품질**                                  | 제품 품질은 특별 조건에 명시된 사양을 충족해야 하며, typicals(전형적 특성)이나 인도 시간은 제품의 설명 또는 적합성에 포함되지 않음. | 제품 품질은 특별 조건에 명시된 사양을 따라야 하며, typicals나 인도 시간은 제품의 설명이나 품질에 포함되지 않음. | 품질은 특별 조건에 명시된 사양보다 떨어지지 않아야 하며, typicals나 인도 시간은 제품의 설명이나 품질에 포함되지 않음. |
| **품질 및 수량 클레임**                    | FOB, CFR, CIF 인도의 경우 클레임은 60일 내에 제기해야 하며, 90일 내에 문서가 제출되어야 함. 20만 배럴 이하인 경우 수량 차이가 0.5% 이하일 때는 클레임 불가. | FOB, CFR, CIF 인도의 경우 클레임은 60일 내에 제기, 90일 내 문서 제출. 수량 차이가 0.2% 이하일 경우 클레임 불가. | 수량 차이가 0.5% 이하일 경우 클레임 불가. 클레임은 인도 완료 후 45일 내에 제기해야 하며, 증거를 첨부해야 함. |
| **건강, 안전, 환경 (REACH 준수)**          | EEA 내에서 인도되는 제품에 대해 REACH 규정을 준수해야 하며, MSDS(물질 안전 데이터 시트)는 인도 시 제공됨. REACH 정보의 정확성에 대한 보증은 없음. | EEA 내에서 REACH 규정을 준수해야 하며, MSDS는 인도 시 제공됨. MSDS 정확성에 대한 책임은 없음. | REACH 규정을 준수하며, 물질 식별자와 SDS(안전 데이터 시트)를 제공함. 제공된 정보의 부정확성에 대한 책임은 없음. |
| **물질 안전 데이터 시트 (MSDS)**           | MSDS는 인도 시 제공되며, 구매자는 이를 관련 인력에게 전달해야 함.                                                                       | MSDS는 제공되며, 구매자는 직원과 관련자에게 이를 제공해야 함.                                                                     | SDS는 인도 시 제공되며, 구매자는 이를 직원 및 관련 인력에게 제공해야 함.                                                                  |
| **책임**                                  | 제품의 고유한 위험으로 인한 손실에 대한 책임 없음.                                                                                         | 제품의 고유한 위험으로 인한 손실에 대한 책임 없음.                                                                                     | 제품 고유의 위험으로 인한 손실 또는 부상에 대한 책임 없음.                                                                                 |

**Key Differences:**
- **클레임 제출 기한**: Chevron과 Shell은 클레임 제출 기한이 60일이지만, BP는 45일로 더 짧습니다.
- **수량 허용 오차**: Chevron은 20만 배럴 이하의 경우 0.5% 오차를 허용하지만, Shell은 0.2%만 허용합니다. BP는 0.5%까지 허용합니다.
- **REACH 준수**: 세 회사 모두 EEA 내 제품에 대해 REACH 규정을 준수할 것을 요구하지만, Chevron은 REACH 관련 정보의 정확성에 대한 보증을 명시적으로 부인하고 있으며, Shell과 BP도 유사한 제한을 두고 있습니다.
- **고유 위험에 대한 책임**: 세 회사 모두 제품의 고유한 위험으로 인한 손실에 대해 책임을 지지 않습니다.
---   
        """, unsafe_allow_html=True)

