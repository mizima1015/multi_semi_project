# 머신러닝 코드

1. ver0.1(23.09.13 최종수정)
   -  train/test: 7 : 3 으로 나누어 학습
   -  Best 평가지표 (MAE: 1,69, RMSE: 2.44, R2: 0.98)
  
2. ver0.2 (23.09.13 최종수정)
   -  train/test: 8 : 2 으로 나누어 학습
   -  Best 평가지표 (MAE: 1.91 ,RMSE: 2.84, R2: 0.97)

3. ver0.3 (23.09.13 최종수정)
   -  train/validation/test: 4 : 3 : 3 으로 나누어 학습
   -  Best 평가지표 (MAE: 2.53, RMSE: 3.60, R2: 0.95)

4. ver0.4 (23.09.13 최종수정)
   -  train/validation/test: 5 : 3 : 2 으로 나누어 학습
   -  Best 평가지표 (MAE: 2.14 ,RMSE: 3.30, R2: 0.96)

# 모든 버전에서 XGBoost와 LGBM의 성능이 좋았음
   - 두 모델에 대하여 최적화 진행 중


# 사용 모델
1. [Scikit-learn RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor)
2. [Scikit-learn LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression)
3. [LightGBM LGBMRegressor](https://lightgbm.readthedocs.io/en/v3.3.2/pythonapi/lightgbm.LGBMRegressor.html)
4. [XGBoost XGBRegressor](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRegressor)
