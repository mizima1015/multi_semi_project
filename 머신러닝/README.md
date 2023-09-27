# 머신러닝 코드

1. ver0.1(23.09.13 최종수정)
   -  train/test: 7 : 3 으로 나누어 학습
   -  Best 평가지표 (MAE: 1.69, RMSE: 2.44, R2: 0.98)
  
2. ver0.2 (23.09.13 최종수정)
   -  train/test: 8 : 2 으로 나누어 학습
   -  Best 평가지표 (MAE: 1.91 ,RMSE: 2.84, R2: 0.97)

3. ver0.3 (23.09.13 최종수정)
   -  train/validation/test: 4 : 3 : 3 으로 나누어 학습
   -  Best 평가지표 (MAE: 2.53, RMSE: 3.60, R2: 0.95)

4. ver0.4 (23.09.13 최종수정)
   -  train/validation/test: 5 : 3 : 2 으로 나누어 학습
   -  Best 평가지표 (MAE: 2.14 ,RMSE: 3.30, R2: 0.96)

5. 하이퍼파라미터튜닝(with ver0.1) (23.09.14 최종수정)
   -  train/test: 7 : 3 으로 나누어 학습
   -  Best 평가지표 (MAE: 1.45 ,RMSE: 2.29, R2: 0.98)

## 모든 버전에서 XGBoost와 LGBM의 성능이 좋았음
   - 추가 데이터 학습 준비중


# 사용 모델
1. [Scikit-learn RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor)
2. [Scikit-learn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression)
3. [LightGBM LGBMRegressor](https://lightgbm.readthedocs.io/en/v3.3.2/pythonapi/lightgbm.LGBMRegressor.html)
4. [XGBoost XGBRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor)


# pkl 파일
1~8호선 각 호선별로 XGBoost를 이용해 학습한 내용을 저장한 파일
.pkl로 저장 시 학습을 한 번 해두면 그 내용을 저장해 혼잡도를 예측할 때 매번 새로 모델을 학습시키지 않아도 된다.

# XGBoost(최종)
- pkl 파일을 만들 때 사용한 머신러닝 파일 최종버전

# 웹머신러닝함수.ipynd
- 웹에서 혼잡도 예측 결과를 보여주기 위한 함수.
  출발역/도착역, 연도, 월, 요일, 호선, 시간대를 input 값으로 받으면 해당 구간의 혼잡도 평균을 알려주는 함수이다.
  2호선의 경우 순환선이기에 시계방향, 반시계방향을 비교하서 더 가까운 방향으로 돌며 혼잡도를 예측하도록 하였고,
  꼬다리 처럼 나온 성수지선과 신정지선 마천지선은 환승역과 마찬가지로 내려서 갈아타야하는 역이기에 별도의 호선으로 처리했다.
  6호선의 경우 한쪽 끝 부분이 단방향 순환선인데, 이는 반대방향으로 설정시 혼잡도가 음수 또는 0으로 나와 구분 가능하도록 했다. 
