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
    <td align="center"><img src="https://private-user-images.githubusercontent.com/133230306/419249517-77a8d10c-aa29-4398-af51-2acaff1e118e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzkyNjEsIm5iZiI6MTc0MTEzODk2MSwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjQ5NTE3LTc3YThkMTBjLWFhMjktNDM5OC1hZjUxLTJhY2FmZjFlMTE4ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTQyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NGVlZGE0M2JkN2UyMGZjMDEyMTVlNjJlNWE4YWEyMGMwYTkwZDIxZWVjNmRlNmM1MmUxYjRhZWJhMGE3NTdjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.aIKvzHnvtjItRjwqfxtc2_8dwzGvnjbVTazBUPDGmY0" width="175" height="175"></td>
    <td align="center"><img src="https://private-user-images.githubusercontent.com/133230306/419249369-1b7d25d0-7a5b-4753-ad71-0b6ee999458d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzkyNjEsIm5iZiI6MTc0MTEzODk2MSwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjQ5MzY5LTFiN2QyNWQwLTdhNWItNDc1My1hZDcxLTBiNmVlOTk5NDU4ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTQyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02OThmZDRkOTJjZmM2OWI0MmQ2OTY2MTdjNTEyY2FkMWJmNGNjZjRlZjNlMDVjYTE0ZTIyMDVlNzIyZDAwNzZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.a3CXpgW8yoMoT64YlXMKxFwdvIerMVAfTo37PkUPnPA" width="175" height="175"></td>
    <td align="center"><img src="https://private-user-images.githubusercontent.com/133230306/419249897-af198527-3b28-4c07-9953-3ed7b88de5f2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzkyNjEsIm5iZiI6MTc0MTEzODk2MSwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjQ5ODk3LWFmMTk4NTI3LTNiMjgtNGMwNy05OTUzLTNlZDdiODhkZTVmMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTQyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ZWRiZjBhNDEyNTRjMzZkYWNhNmNkYWFhM2U3ZmIwZGFhZjEwMGI1MDFlMzRkMTcwYjY4ZThhMGU1YTdhNzJiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.yzU4GZ6UhR0uaKNe7wS5QjO0s3AFo_uDBCjyJTt6G98" width="175" height="175"></td>
    <td align="center"><img src="https://private-user-images.githubusercontent.com/133230306/419249796-fc6cab04-415f-41cb-a536-aac4dcc0d490.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzkyNjEsIm5iZiI6MTc0MTEzODk2MSwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjQ5Nzk2LWZjNmNhYjA0LTQxNWYtNDFjYi1hNTM2LWFhYzRkY2MwZDQ5MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTQyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00ZmJkNmVmM2ZlZDUzOWVjZDM4MWFjYTMxMjI0MTY5ZmI5ODI2NjM1YWEyY2U4Njk4YmE3OTc5NDMwYjliMzZkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.HpB96k_oQ59JLOIFQtkq0yC03qCVatGQ4jidLafqrZE" width="175" height="175"></td>
    <td align="center"><img src="https://private-user-images.githubusercontent.com/133230306/419254613-f66681ef-323b-4c8a-ae24-e75e1d3765e1.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzkyNjEsIm5iZiI6MTc0MTEzODk2MSwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjU0NjEzLWY2NjY4MWVmLTMyM2ItNGM4YS1hZTI0LWU3NWUxZDM3NjVlMS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTQyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNmFjOTdhNjVkY2VjZDA5MDI1NTgxM2U3MzIwZmFhNDkxN2NlNTE0MzhjNGY4MjliMmI1ODU5MWE4M2E0NDUyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.pSfyF7pruQ59-CIJkuYgp3kckfgYGqmymSTn7Y3tm3Q" width="175" height="175"></td>
    <td align="center"><img src="https://private-user-images.githubusercontent.com/133230306/419249668-3522df42-2e99-43a0-85bb-a471df72655b.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzkyNjEsIm5iZiI6MTc0MTEzODk2MSwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjQ5NjY4LTM1MjJkZjQyLTJlOTktNDNhMC04NWJiLWE0NzFkZjcyNjU1Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTQyNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMzk2MjhjNTYyNGEzZjUyMDRlNTA2MTQ5NGFmZGQzZTVhODhjMWY4YzQwNjZlMzVlNWRhNWJiNGEzYzJhM2MyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.rcyY0DVQtv2jx85HKpCUDOKcGLmteO0ZS3T-LQ7pAHoL" width="175" height="175"></td>
  </tr>
  <tr>
    <td align="center"><b>팀장</b></td>
    <td align="center" colspan="5"><b>팀원</b></td>
  </tr>
  <tr>
    <td align="center"><b>프로젝트 총괄</b><br>데이터 분석<br>RandomForest, LogisticRegression, XGBoost 모델</td>
    <td align="center">데이터 분석<br>streamlit 화면 개발<br>GitHub 업데이트</td>
    <td align="center">RandomForest, LightGBM, XGBoost 모델 개발<br>모델 성능 분석<br>화면 설계</td>
    <td align="center">LightGBM 모델 개발<br>데이터 분석<br>모델 성능 업그레이드</td>
    <td align="center">LightGBM 모델 개발<br>모델 성능 업그레이드<br>데이터 분석</td>
    <td align="center">Ensemble 모델 개발<br>모델 성능 업그레이드<br>데이터 분석</td>
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

NULL값채움 : TotalCharges (mean으로 채움)<br/>
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

### 2.1 문제인식 및 해결 방법

**문제점**

- 다양한 모델을 사용하여 예측을 해보았지만 낮은 예측율 및 스코어값 산출<br/>

**해결방안**

- 개별 모델 생성후, 동일한 데이터 셋에서 복원 추출로 다른 Train 데이터셋을 여러번 산출해 반복학습하여 모델의 성능 향상<br/>

![image](https://private-user-images.githubusercontent.com/133230306/419249336-92ab8a61-05a2-4088-b69b-e71f3b4fbe6d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExMzg2MjYsIm5iZiI6MTc0MTEzODMyNiwicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjQ5MzM2LTkyYWI4YTYxLTA1YTItNDA4OC1iNjliLWU3MWYzYjRmYmU2ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMTMyMDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jOThmNzVlNjlkZjgwNTkyZDk4NTRlNTA5ZDE1ZDUyZmFiZTc0MDZkNDlkOWM3M2U3MTY3ZmI0YWJlZDZmNzY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6hmhSyZqQcKcSbvcFr03K15cwTLdH0xwzGJbt9FziGg)<br/>



## 3 분석 및 학습 결과

### 3.1 화면 개발 과정
![image](https://private-user-images.githubusercontent.com/133230306/419259804-b85ed2c0-9083-4db9-96c4-fe05842ccae8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDExNDAzOTMsIm5iZiI6MTc0MTE0MDA5MywicGF0aCI6Ii8xMzMyMzAzMDYvNDE5MjU5ODA0LWI4NWVkMmMwLTkwODMtNGRiOS05NmM0LWZlMDU4NDJjY2FlOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwNVQwMjAxMzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03NTJlMWU4MGUyOTczOTNkMDc0NDFjZjYzZTBkZDY1ZTAxMDY3ZmFjMTM4MGU4NDgxNTlmYTEzMTdjMTRlNjI3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.MDLkuyJvd3-cQmEB07T4Ct1d30zv9KlKPVRtiUuRFqA)<br/>



## 4 결과 및 결론

- 가장 score(precision)값이 높은 모델:<br/>
<br/>
"모델별 precision 최고점수"<br/>
|---------------|<br/>
| Random Forest | "0.837"<br/>
| XGBoost | "0.74"<br/>
| Logistic Regression | "0.914" ==> 최고 precision score<br/>
| LightGBM | "0.676"<br/>
| Ensemble | "0.843"<br/>

<br/>

- 가장 loss값이 낮은 모델:<br/>
"모델별 loss 최저점수"<br/>
|---------------|<br/>
| Random Forest | "0.56"<br/>
| XGBoost | "0.393"<br/>
| Logistic Regression | "0.265" ==> 최저 log loss값<br/>
| LightGBM | "0.687"<br/>
| Ensemble | "0.368"<br/>

<br/>


가장 고객 이탈율에 영향을 주는 feature:<br/>
XGBoost 모델<br/>
<br/> "Contranct_Month-to-month" => <br/> "월별계약"

RandomForest <br/>
<br/> "is_Short_Contract_No" => <br/> "단기계약이 아닌 고객"

LightGBM<br/>
<br/> "PaperlessBilling_no" 

Logistic<br/>
<br/> "PaperlessBilling_no" 





## 5. 참여도중 문제점과 해결점

**신정우** :<br/>문제점 : 데이터셋을 전처리를 잘하는것만이 모델의 스코어 값을 올리는건 아니었습니다. 다른 종류의 모델을 실행해봐도 일정 점수 이상의 스코어가 나오는 경우가 없었습니다.<br/> 
해결점: 모델을 생성하면, 학습을 한번으로 끝내는것이 아니라 데이터셋에서 다른 데이터를 랜덤 추출해서 문제집을 반복해서 풀듯이 반복학습으로 해결했습니다.<br/> 

**홍승표** :<br/>문제점 : eda도 gpt가 해주긴하는데 그 수준이 낮아서 아무리 맡겨도 학습에 큰 영향이 없었습니다. 그러면 나 스스로가 eda를 잘해야하는데 아직 공부가 부족해서 gpt한테 시키는것도 잘 못했다. 그래서 부랴부랴 eda에 대해 다시 공부해야했다. 사실 지금도 잘 모르겠다. 큰일났다.<br/>

**최수헌** :<br/>

**남궁승원** :<br/> 데이터 전처리 과정에서 미숙함으로 인해 epoch 적용을 못했고, 전처리 과정에서 체계적으로 하기 보단 떠오르는대로 너무 막 해서 과정이 기억에 잘 안남고 깔끔하지 않고 지저분하게 됐다. 전처리와 EDA 관련 추가 학습과 더 많은 경험을 통해 해결해야 할 것 같다<br/> 

**박예슬** :<br/>문제점 : EDA를 통해 떠올릴 수 있었던 데이터 전처리 기법을 적용했을 때 좋은 결과가 나오지 않는 경우가 있었다.<br/>
해결 : 시행착오를 통해 좋은 결과를 내는 전처리 기법만을 적용했다.<br/>

**김재혁** :<br/>여러 머신러닝 모델들을 합쳐서 앙상블 모델을 만들었는데 기존 모델들보다 성능이 더 떨어졌습니다. 그래서 앙상블 모델 내부의 머신러닝 모델들의 하이퍼파라미터를 각각 조정해가며 꽤 괜찮은 성능이 나오는 앙상블 모델을 만들었습니다.<br/>


<br/>
<br/>

## 프로젝트 후기

**신정우** :<br/>이런 못난 게으르고 능력없는 팀장을 따라와준 팀원들에게 무수히많은 감사를 드립니다. 처음으로 팀장이란걸 해봤는데, 다른 누군가와 함께하고 그 단체를 이끌어 간다는것이 굉장히 중요한 위치에 있다는걸 이번에 제대로 느꼈습니다. 다들 요구사항이 복잡했을텐데도 정말 잘해내주셔서 너무 감사하고 팀장이라는 이름의 무게를 알게되었습니다.

**홍승표** :<br/>ai를 온전히 내 힘으로 돌려본게 이번이 처음이라 매우 어려웠다. gpt라는 친구가 없었다면 불가능했을 것이다. 내가 많이 부족해서 ai를 개발하는데 ai를 쓰는 모순이 일어난 것 같아 마음이 좋지 않았다. gpt 없이 온전히 내 손으로 코드를 쓸 수 있을 때까지 공부해야겠다는 생각이 들었다.<br/> 

**최수헌** :<br/>

**남궁승원** :<br/> 부족한 실력으로 좀 부족한 결과물이 나왔지만, 팀장님과 다른 팀원들의 도움으로 마무리 할 수 있었고, 좀 더 학습해서 체계적이고 깔끔하게 분석하는쪽으로 발전 해야한다고 느꼈다.<br/> 

**박예슬** :<br/>팀원들이 모델을 하나씩 만들고 공유함으로써 다양한 전처리 및 모델링 기법을 간접 경험할 수 있는 좋은 기회였다.<br/> 

**김재혁** :<br/>처음에 그냥 팀내 경진대회처럼 누구의 모델이 점수(성능)이 잘 나오는지 했었는데 내심 내 모델이 제일 성능이 좋길 바랐습니다. 그래서 여러가지 모델을 합쳐서 앙상블 모델을 만들어보기도 하고 하이퍼파라미터도 계속 조정했습니다. 하지만 더 높은 점수가 나오는 모델들이 있었고 그 이유가 모델 이전의 EDA와 Feature engineering이라고 느꼈습니다. 따라서 EDA와 Feature engineering의 중요성을 느낄 수 있었던 프로젝트였습니다.<br/>

