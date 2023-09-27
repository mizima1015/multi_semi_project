import pandas as pd
import sqlite3
import csv

#CSV 파일 로드
df = pd.read_csv("TestCsv_Subway.csv")

# DB랑 연결
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "SW_ID" : "IntegerField"
    , "SW_Station" : "CharField"
    , "SW_Num" : "IntegerField"
}

df.to_sql(name='FirstApp_testcsv_subway', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")

conn.close()