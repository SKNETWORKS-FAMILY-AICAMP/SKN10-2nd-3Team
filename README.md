# SKN10-2nd-3Team
# [가입 고객 이탈 예측](https://www.kaggle.com/code/bbksjdd/telco-customer-churn)

![Image](https://github.com/user-attachments/assets/51c829fe-ac31-471b-aa5d-092e4ad45a12)

## 프로젝트 주제

**가입 고객 이탈 예측 조회 시스템**

## 프로젝트 목표

이용 고객의 이탈율 확인 및 영향 변수 특정 & 이탈을 막기 위해 조정해야할 요소 산출

<br/>
<br/>
## 📅 프로젝트 기간
**2025.02.19(수요일) ~ 2025.03.05(수요일)** (총 10일) <br/>
<br/>
<br/>

## 팀 소개
<table>
  <tr>
    <th>신정우</th>
    <th>홍승표</th>
    <th>박예슬</th>
    <th>최수헌</th>
    <th>남궁승원</th>
    <th>김재혁</th>
  </tr>
  <tr>
    <td align="center"><img src="https://github.com/user-attachments/assets/1d56cc60-e0d5-401b-b365-3f38f25bed43" width="175" height="175"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/4d97616d-34b6-4495-aa18-dc1bb2733d4a" width="175" height="175"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/1d56cc60-e0d5-401b-b365-3f38f25bed43" width="175" height="175"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/1d56cc60-e0d5-401b-b365-3f38f25bed43" width="175" height="175"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/1d56cc60-e0d5-401b-b365-3f38f25bed43" width="175" height="175"></td>
    <td align="center"><img src="https://github.com/user-attachments/assets/1d56cc60-e0d5-401b-b365-3f38f25bed43" width="175" height="175"></td>
  </tr>
  <tr>
    <td align="center"><b>팀장</b></td>
    <td align="center"><b>팀원</b></td>
    <td align="center"><b>팀원</b></td>
    <td align="center"><b>팀원</b></td>
    <td align="center"><b>팀원</b></td>
    <td align="center"><b>팀원</b></td>
  </tr>
  <tr>
    <td align="center">
      <b>프로젝트 총괄</b><br>
      <b>데이터 분석</b><br>
      <b>RandomForest, LogisticRegression, XGBoost 모델</b>
    </td>
    <td align="center">
      <b>데이터 분석</b><br>
      <b>streamlit 화면 개발</b><br>
      <b>GitHub 업데이트</b>
    </td>
    <td align="center">
      <b>RandomForest, LightGBM, XGBoost 모델 개발</b><br>
      <b>모델 성능 분석</b><br>
      <b>화면 설계</b>
    </td>
    <td align="center">
      <b>LightGBM 모델 개발</b><br>
      <b>데이터 분석</b><br>
      <b>모델 성능 업그레이드</b>
    </td>
    <td align="center">
      <b>LightGBM 모델 개발</b><br>
      <b>모델 성능 업그레이드</b><br>
      <b>데이터 분석</b>
    </td>
    <td align="center">
      <b>Ensemble 모델 개발</b><br>
      <b>모델 성능 업그레이드</b><br>
      <b>데이터 분석</b>
    </td>
  </tr>
</table>

## 📌기술스택
![Image](https://github.com/user-attachments/assets/2ff90937-1572-4922-8117-42ec1958e8a2)
![Image](https://github.com/user-attachments/assets/f4f74fee-a6ec-4916-98a7-87372c233494)
![Image](https://github.com/user-attachments/assets/954f356b-b234-4fdc-a4de-be4678532cdb)
![Image](https://github.com/user-attachments/assets/5e72d28a-8895-4ab3-acdb-d1be87b53374)
![Image](https://github.com/user-attachments/assets/5c3399ed-c375-4793-ad36-35c69da77dd6)


<br/>

---


## 1 데이터셋 개요

- Column수 20개

- Row수  7043개

- Churn(가입 해지율) 비율
- [Unchurn 73%, Churn 27%]

- 데이터 출처 = https://www.kaggle.com/datasets/kapturovalexander/customers-churned-in-telecom-services
<br/>
<br/>

### 1.1 데이터 분석 및 전처리
**신정우** : 

TotalCharges median 값으로 결측치 제거<br/>
Label Encoding : "gender", "partner", "dependents", "phoneservice", "paperlessbilling"<br/>
OneHot Encoding : "multiplelines", "internetservice", "onlinesecurity", "onlinebackup",<br/>
                    "deviceprotection", "techsupport", "streamingtv", "streamingmovies",<br/>
                    "contract", "paymentmethod"<br/>
1년 미만 가입 고객 여부 추가<br/>
"df["is_short_tenure"] = (df["tenure"] < 12).astype(int)"<br/>

|--------------------------------------------------------------------------------------|<br/>

**최수헌** :<br/>
데이터 클리닝(널값 채우기, 중복 행 제거)<br/>
 -> EDA(타겟과 상관관계가 없는 컬럼은 제거, 수치형데이터를 범주형데이터로 변환 등)<br/>
 -> 업샘플링(Chern이 적으므로 SMOTE 업샘플링)<br/>
 -> LGBM 하이퍼파라미터 최적화(RandomSearch, optuna사용)<br/>

LGBM 모델: train(0.8602), test(0.7794), F1(0.7824), Recall(0.7793), Precision(0.7867) <br/>


|--------------------------------------------------------------------------------------|<br/>

**남궁승원** : <br/>

TotalCharges median 값으로 결측치 제거<br/>
AutoPayment 컬럼 만들어서 결제 방법이 AUTO인걸 1, 아닌걸 0으로 인코딩<br/>
OBJECT 를 카테고리 데이터로 수정<br/>
PhoneService 컬럼 원핫 인코딩으로 No_Phoneservice, No_Multiple,Multiple로 나눔<br/>
MonthToMonth 만들어서 1년 계약이랑 2년 계약 합치면서 0이랑 1로 인코딩<br/>

|--------------------------------------------------------------------------------------|<br/>

**박예슬** : <br/>

널값채움 : TotalCharges (mean으로 채움)<br/>
라벨인코딩 : <br/>
'StreamingTV', 'StreamingMovies', 'OnlineSecurity', 'OnlineBackup','DeviceProtection' -> 원핫인코딩 했을때보다 라벨인코딩 했을때 값이 좋았음<br/>
'gender', 'Partner', 'Dependents','PhoneService', 'PaperlessBilling','Churn' -> 칼럼값이 2개여서 라벨인코딩함<br/>
원핫인코딩(더미) : 'PaymentMethod', 'MultipleLines', 'InternetService', 'Contract', 'TechSupport'<br/>

|--------------------------------------------------------------------------------------|<br/>

**김재혁** : <br/>

결측값 처리 (TotalCharges 변환 및 채우기)<br/>
연속형 변수 분포 확인 (tenure, MonthlyCharges 등 히스토그램, Boxplot 분석)<br/>
범주형 변수 분석 (InternetService, Contract 등 Churn Rate 분석)<br/>
상관관계 분석 (Heatmap으로 주요 변수 간 관계 확인)<br/>
Feature Engineering (가입 기간 그룹화, 청구 금액 그룹화)<br/>
총 청구 금액을 가입 개월 수로 나누어 AvgMonthlyCharge(평균 월 청구 금액) 생성<br/>
<br/>
<br/>

## 2 분석 방향 및 초기 계획

- 데이터 셋을 정한 후, 각 팀원들이 개별 모델을 개발하여 자유롭게 예측 및 학습<br/>
- 전처리 과정후 가장 좋은 전처리 과정을 수행한 팀원의 방식을을 다른 팀원들과 동일하게 적용 예정<br/>
<br/>
<br/>

### 2.1 문제인식 및 해결 방법

**문제점**

- 다양한 모델을 사용하여 예측을 해보았지만 낮은 예측율 및 스코어값 산출<br/>

**해결방안**

- 개별 모델 생성후, 동일한 데이터 셋에서 복원 추출로 다른 Train 데이터셋을 여러번 산출해 반복학습하여 모델의 성능 향상<br/>

![image](https://github.com/user-attachments/assets/419250089-8a32e5ae-4488-40ef-ab8a-d8962b2bca3d)<br/>


