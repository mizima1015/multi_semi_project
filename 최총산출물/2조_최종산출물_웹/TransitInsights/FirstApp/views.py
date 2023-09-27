from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
from datetime import datetime, timedelta
import pandas as pd
import joblib

# Create your views here.

def Start_Page(request):
    return render(request, 'First_Page.html')

# ==============================================================

def Second_Page(request, sw_id):
# --------------------------------------------------------------

    # 노선필터
    SW_Station = ALL_LN_HS_F.objects.filter(LINE=sw_id)

    # 노선 색과 이름 가져오기
    GLC = Get_Line_Code(sw_id)
    SL_Color = GLC[0]
    L_IMG_N = GLC[1]

# --------------------------------------------------------------
    Content = {'SW_Station':SW_Station
               ,'SW_ID':sw_id
               ,'SL_Color':SL_Color
               ,'L_IMG_N':L_IMG_N
               }
    
# --------------------------------------------------------------

    return render(request, 'Second_Page.html', Content)

# ==============================================================

def Third_Page(request):

# -------------------------------------------------------------- 전페이지 가져오기

    request.method == 'POST'

    selected_Start = request.POST.get('selected_Start')
    selected_End = request.POST.get('selected_End')
    selected_DateTime = request.POST.get('selected_DateTime')
    Toggle_SW_Holiday = request.POST.get('Toggle_SW_Holiday','False')
    Line_Select = request.POST.get('Line_Select')
    SL_Color = request.POST.get('SL_Color')

    SW_Station = []
 
# -------------------------------------------------------------- 미기입, 오타 필터

    SW_Station = [i.STATION for i in ALL_LN_HS_F.objects.filter(LINE=Line_Select)]

    if not selected_Start:
        Msg = '출발역이 입력되지 않았습니다.'
    elif not selected_End:
        Msg = '도착역이 입력되지 않았습니다.'
    elif not selected_DateTime:
        Msg = '날짜와 시간이 입력되지 않았습니다.'
    elif selected_Start == selected_End:
        Msg = '동일한 역을 고르셨습니다.'
    elif selected_Start not in SW_Station or selected_End not in SW_Station:
        Msg = f'선택한 역은 {Line_Select}호선에 존재하지 않습니다.'

    if 'Msg' in locals():
        return render(request, 'Warning_Page.html', {'Msg': Msg})
    
# -------------------------------------------------------------- 날짜 시간 쪼개기
    VARDATEConversion = DATEConversion(selected_DateTime,Toggle_SW_Holiday)

    selected_TIME = VARDATEConversion[4]
    selected_YEAR = VARDATEConversion[0]
    selected_MONTH = VARDATEConversion[1]
    selected_DAY = VARDATEConversion[2]
    selected_WeekDay = VARDATEConversion[3]

# -------------------------------------------------------------- 머신러닝 데이터

    df = pd.read_csv("ALL_LN_HS_F.csv")
    list_data = df.values.tolist()
    RESULT_VAL = NansuTo000(int((print_congestion_predictions(selected_Start, selected_End, selected_YEAR, selected_MONTH, selected_WeekDay, int(Line_Select), 'TIME_'+str(selected_TIME), list_data))))

# -------------------------------------------------------------- 

    # 호선이름바꾸기 ex.21=> 성수지선
    L_IMG_N = Get_Line_Code(Line_Select)[1]

    # 혼잡도 분류와 출력
    PHJD = Print_HJD(RESULT_VAL)
    HonJap = PHJD[0]
    HonJap_N = PHJD[1]

# -------------------------------------------------------------- 

    Content03 = {'Line_Select':Line_Select
                    ,'L_IMG_N' : L_IMG_N
                    ,'selected_Start':selected_Start
                    ,'selected_End':selected_End
                    ,'selected_TIME':selected_TIME
                    ,'selected_YEAR':selected_YEAR
                    ,'selected_MONTH':selected_MONTH
                    ,'selected_DAY':selected_DAY
                    ,'selected_WeekDay':selected_WeekDay
                    ,'RESULT_VAL':RESULT_VAL
                    ,'selected_DateTime' :selected_DateTime
                    , 'Toggle_SW_Holiday': Toggle_SW_Holiday
                    ,'HonJap':HonJap
                    ,'SL_Color':SL_Color
                    , 'HonJap_N':HonJap_N
                    }

    return render(request, 'Third_Page.html', Content03)

# ========================================================== 기타 함수

# ---------------------- 날짜 쪼개기
def DATEConversion(request, Toggle_SW_Holiday):
    selected_DATE_ALL = request.split('T')[0]
    YEAR = int(selected_DATE_ALL.split('-')[0])
    MONTH = int(selected_DATE_ALL.split('-')[1])
    DAY = int(selected_DATE_ALL.split('-')[2])

    WD = ['월', '화', '수', '목', '금', '토', '일'][datetime(YEAR,MONTH,DAY).weekday()]
    HOUR = request.split('T')[1][:2]

    if Toggle_SW_Holiday == 'True':
        WD = '일'

    return(YEAR,MONTH,DAY,WD,HOUR)

# ---------------------- 세 자리 만들기
def NansuTo000 (request):
    Nansu = request
    Nan_List = [0, 0, 0]
    Nan_List[0] = Nansu // 100
    Nan_List[1] = (Nansu // 10) % 10
    Nan_List[2] = Nansu % 10
    Nan_Result = ''.join(map(str,Nan_List))
    return Nan_Result

# ---------------------- 노선 이름과 색깔 따오기
def Get_Line_Code(sw_id):
    if int(sw_id) == 1:
        SL_Color = '#0052A4'
        L_IMG_N = '1호선'
    elif int(sw_id) == 2:
        SL_Color = '#00A84D'
        L_IMG_N = '2호선'
    elif int(sw_id) == 21:
        SL_Color = '#00A84D'
        L_IMG_N = '성수지선'
    elif int(sw_id) == 22:
        SL_Color = '#00A84D'
        L_IMG_N = '신정지선'
    elif int(sw_id) == 3:
        SL_Color = '#EF7C1C'
        L_IMG_N = '3호선'
    elif int(sw_id) == 4:
        SL_Color = '#00A4E3'
        L_IMG_N = '4호선'
    elif int(sw_id) == 5:
        SL_Color = '#996CAC'
        L_IMG_N = '5호선'
    elif int(sw_id) == 51:
        SL_Color = '#996CAC'
        L_IMG_N = '마천지선'
    elif int(sw_id) == 6:
        SL_Color = '#CD7C2F'
        L_IMG_N = '6호선'
    elif int(sw_id) == 7:
        SL_Color = '#747F00'
        L_IMG_N = '7호선'
    else :
        SL_Color = '#E6186C'
        L_IMG_N = '8호선'
    return SL_Color,L_IMG_N

# ---------------------- 혼잡도 분류+출력
def Print_HJD(RESULT_VAL):
    if int(RESULT_VAL) <= 24:
        HonJap = '착석가능.'
        HonJap_N = '1'
    elif int(RESULT_VAL) <= 58:
        HonJap = '여유공간.'
        HonJap_N = '2'
    elif int(RESULT_VAL) <= 100:
        HonJap = '혼잡증가.'
        HonJap_N = '3'
    elif int(RESULT_VAL) <= 150:
        HonJap = '정부권고.'
        HonJap_N = '4'
    else:
        HonJap = '호흡불가.'
        HonJap_N = '5'
    return HonJap, HonJap_N

# ========================================================== 머신러닝 코드

def shortest_path_2ho(start_idx, end_idx, stations):
    direct_path = abs(end_idx - start_idx)
    if direct_path <= len(stations) / 2:
        if start_idx < end_idx:
            return start_idx , end_idx , "상선"
        else :
            start_idx, end_idx = end_idx + 1, start_idx + 1
            return start_idx , end_idx , "하선"

    else:
        if start_idx < end_idx:
            start_idx,end_idx = start_idx + 1, end_idx + 1
            return end_idx, start_idx + len(stations), "하선"
        else: 
            return start_idx, end_idx + len(stations), "상선"

def print_congestion_predictions(start_station, end_station, input_YEAR, input_MONTH, input_DAY, input_LINE, input_TIME, station_data):
    stations = [item[2] for item in station_data if item[1] == input_LINE]
    start_idx, end_idx = stations.index(start_station), stations.index(end_station)
    
    is_line_2 = input_LINE == 2
    if is_line_2:
        start_idx, end_idx, direction = shortest_path_2ho(start_idx, end_idx, stations)
    else:
        direction = "상선" if start_idx < end_idx else "하선"
        if direction == "하선":
            start_idx, end_idx = end_idx + 1 , start_idx + 1

    if input_LINE in [21,22]:
        input_LINE = 2

    if input_LINE in [51]:
        input_LINE = 5

    model = joblib.load(f'XGB_reg_num{input_LINE}.pkl')

    input_datas = []
    for idx in range(start_idx , end_idx):
        station = stations[idx % len(stations)]
        input_datas.append({
            'YEAR': input_YEAR,
            'MONTH': input_MONTH,
            'DAY': input_DAY,
            'STATION': station,
            'DIRECTION': direction,
            'TIME_00': input_TIME
        })

    df_input = pd.DataFrame(input_datas)
    predictions = model.predict(df_input)

    # for station, pred in zip(df_input['STATION'], predictions):
    #     print(f"역: {station}, 예측 혼잡도: {pred:.2f}")
    # print(direction)
    avg_congestion = predictions.mean()
    # print(f"평균 혼잡도: {avg_congestion:.2f}")
    return avg_congestion