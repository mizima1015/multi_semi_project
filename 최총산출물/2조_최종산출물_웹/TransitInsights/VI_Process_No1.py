import pandas as pd
import sqlite3
import csv

#CSV 파일 로드
df = pd.read_csv("Vi_CSV_NO1.csv")

# DB랑 연결
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "MONTH" : "IntegerField"
    , "DAY" : "CharField"
    ,"Station" : "CharField"
    , "DIRECTION" : "CharField"
    , "Time_05" : "FloatField"
    , "Time_06" : "FloatField"
    , "Time_07" : "FloatField"
    , "Time_08" : "FloatField"
    , "Time_09" : "FloatField"
    , "Time_10" : "FloatField"
    , "Time_11" : "FloatField"
    , "Time_12" : "FloatField"
    , "Time_13" : "FloatField"
    , "Time_14" : "FloatField"
    , "Time_15" : "FloatField"
    , "Time_16" : "FloatField"
    , "Time_17" : "FloatField"
    , "Time_18" : "FloatField"
    , "Time_19" : "FloatField"
    , "Time_20" : "FloatField"
    , "Time_21" : "FloatField"
    , "Time_22" : "FloatField"
    , "Time_23" : "FloatField"
    , "Time_24" : "FloatField"

}

df.to_sql(name='DashBoard_vi_csv_no1', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")

conn.close()