import pandas as pd
import sqlite3
import csv

#CSV 파일 로드
df = pd.read_csv("CSVForHeatmapTest.csv")

# DB랑 연결
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "Station" : "CharField"
    , "Line" : "CharField"
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

}

df.to_sql(name='DashBoard_csvforheatmaptest', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")

conn.close()