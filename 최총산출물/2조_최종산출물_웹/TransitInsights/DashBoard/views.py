from django.shortcuts import render
from django.http import HttpResponse
import random
from DashBoard.models import *
from statistics import mean
from django.db.models import Avg

# Create your views here.

def DashBoard(request):
    # return HttpResponse("This is DashBoard!!!!")
    return render(request, 'D_First_Page.html')

# def D_Second(request):
    # 히트맵데이터 CSV 불러오기
    heatmap_data = CSVForHeatmapTest.objects.all()
    row_name = []
    col_name = []
    val_name = []
    Result_H = []
    Result_B = []
    Result_BigLine = []
    
    for i in heatmap_data:
        row_name.append(i.Station)

    for j in range(6,24):
        col_name.append(f"Time_{j:02d}")

    for RN in row_name:
        SAM = CSVForHeatmapTest.objects.get(Station=RN)
        for CN in col_name:
            val_name.append(getattr(SAM, CN))

    for i in range(len(row_name)):
        for j in range(len(col_name)):
            l1_item = i
            l2_item = j
            l3_value = val_name[i * len(col_name) + j]
            Result_H.append([l1_item, l2_item, l3_value])

    for RN in row_name:
        SAM = CSVForHeatmapTest.objects.get(Station=RN)
        Result_B.append(SAM.Time_06)

    for CN2 in col_name:
        Result_BigLine.append(getattr(CSVForHeatmapTest.objects.get(Station='한성대입구'), CN2))

    categories = ['Category A', 'Category B', 'Category C']
    data = [42, 67, 29]

    Print_Nansu = NansuTo000(random.randint(1,200))
    
    content = {
        'Print_Nansu':Print_Nansu
        , 'categories':row_name
        , 'data':Result_B
        , 'heatmap_data':heatmap_data 
        , 'val_name' :Result_H
        , 'row_name':row_name
        , 'col_name':col_name
        , 'BigLine_col':col_name
        , 'BigLine_Val':Result_BigLine
        }
    print(Result_BigLine)
    
    return render(request, 'D_Second_Page.html',content)

def D_Third(request):

    # Line_Number = CSVForHeatmapTest.objects.values('Line').distinct()

    Line_Number = [{'Line': str(i)} for i in range(1, 9)]
    # print(type(Line_Number), Line_Number,'--------------------')
    return render(request, 'D_Third_Page.html',{'Line_Number':Line_Number})

def D_Fourth(request):
    # return HttpResponse("FourthPage")
    # return HttpResponse(Line_Select)

#------------------------------------------- 시간대 이름
    col_name = []
    for j in range(5,25):
        col_name.append(f"TIME_{j:02d}")

#------------------------------------------- 시각화용 결과들
    # 테스트
    Result_BigLine = []

    # 상/하선 평균: 선 그래프
    DIRECTION_Line_UP = []
    DIRECTION_Line_DOWN = []

    # 요일별 평균: 파이 그래프
    DAY_Pie_UP =[]
    DAY_Pie_DOWN =[]

    # 전체: 히트맵
    ALL_Result_Heatmap = []

    # 개별역: 선그래프
    One_St_Line_UP = []
    One_St_Line_DOWN = []

#------------------------------------------- 이전 페이지에서 가져올것
    
    request.method == 'POST'
    Selected_Line = request.POST.get('Line_Select')
    Selected_Station = request.POST.get('Station_Select')
    # print('Selected_Station:',Selected_Station, type(Selected_Station),'---------------')

#------------------------------------------- 입력한 노선 DB 불러오기
    
    selected_model = globals()[f'Vi_CSV_NO{int(Selected_Line)}']

#------------------------------------------- 호선 확인 및 오타감지
    
    try:
        INTSL = int(Selected_Line)
        if INTSL not in (1,2,3,4,5,6,7,8, 51):
            Msg = '존재하지 않는 노선입니다.'
            return render(request,'Warning_Page.html',{'Msg':Msg})
        
        elif INTSL == 51:
            Line_Select = selected_model.objects.all()
            Selected_Line = '마천지 5'
            
        else:
            # 호선 확인 후 맞는 모델 불러오기
            Line_Select = selected_model.objects.all()
            # print(Line_Select, type(Line_Select),'---------------')

    except ValueError:
            Msg = '존재하지 않는 노선입니다.'
            return render(request,'Warning_Page.html',{'Msg':Msg})
    # print(Line_Select, type(Line_Select),'---------------')

#------------------------------------------- 상/하선 시간별 선 그래프 데이터

    D_filter = {'DIRECTION': '상선'}
    DIRECTION_Line_UP = ALL_Line_G(selected_model,col_name,**D_filter)

    D_filter = {'DIRECTION': '하선'}
    DIRECTION_Line_DOWN = ALL_Line_G(selected_model,col_name,**D_filter)

#------------------------------------------- 요일별 파이 그래프 데이터

    #파이
    DAY_Pie_UP = Func_for_PIE(Station_Time_AVG_Fu(selected_model,'DAY'))

# ------------------------------------------ 역 별 필터링
    
    # 호선에 맞는 역 이름 가져오기
    row_name = []
    for i in Line_Select:
        row_name.append(i.STATION)
    Station_name = list(set(row_name))

#------------------------------------------- 각 역 / 시간 히트맵

    # 히트맵
    ALL_Result_Heatmap = Func_for_HM(Station_name,col_name,Station_Time_AVG_Fu(selected_model,'STATION'))
    
    # 히트맵 오류용 대비
    row_name_H = Station_name.copy()
    row_name_H.insert(0, 'STN')

#------------------------------------------ 역 선택

    # 오타 확인
    if Selected_Station is not None:
        if Selected_Station not in Station_name:
            Msg = f'{Selected_Line}호선에는 존재하지 않는 역입니다.'
            return render(request, 'Warning_Page.html', {'Msg':Msg})
        else:
            # 역 선택
            for CN2 in col_name:
                MSG02 = f'{Selected_Station}역의 하루 혼잡도입니다.'
    else:
        # 기본역
        for CN3 in col_name:
            Selected_Station = Station_name[0]
            MSG02 = f'기본역은 {Selected_Station}입니다'

#------------------------------------------- 개별역: 선 그래프
    
    S_filter = {'STATION': Selected_Station}

    D_filter = {'DIRECTION': '상선'}
    Com_filter = {**D_filter, **S_filter}
    One_St_Line_UP = ALL_Line_G(selected_model,col_name,**Com_filter)

    D_filter = {'DIRECTION': '하선'}
    Com_filter = {**D_filter, **S_filter}
    One_St_Line_DOWN = ALL_Line_G(selected_model,col_name,**Com_filter)    

#------------------------------------------- 

    content = {
         'Selected_Line':Selected_Line 
        , 'row_name':Station_name
        , 'row_name_H':row_name_H
        , 'col_name':col_name
        , 'DAY_Pie_UP':DAY_Pie_UP
        , 'DAY_Pie_DOWN':DAY_Pie_DOWN
        , 'DIRECTION_Line_UP':DIRECTION_Line_UP
        , 'DIRECTION_Line_DOWN':DIRECTION_Line_DOWN
        , 'ALL_Result_Heatmap':ALL_Result_Heatmap
        , 'One_St_Line_UP':One_St_Line_UP
        , 'One_St_Line_DOWN':One_St_Line_DOWN
        , 'Selected_Station':Selected_Station
        , 'MSG02':MSG02
        }
    
    return render(request, 'D_Fourth_Page.html',content)

def D_Fivth(request):

    #------------------------------------------- 시간대 이름
    col_name = []
    for j in range(5,25):
        col_name.append(f"TIME_{j:02d}")

    #------------------------------------------- 시각화용 결과들

    # 개별역: 선그래프
    One_St_Line_UP = []
    One_St_Line_DOWN = []

    #------------------------------------------- 이전 페이지에서 가져올것
    
    request.method == 'POST'
    Selected_Line = request.POST.get('Line_Select')
    Selected_Station = request.POST.get('Station_Select')
    MSG02 = request.POST.get('MSG02')

    #------------------------------------------- 라인정리

    if Selected_Line == '마천지 5' or Selected_Line == 51:
        Selected_Line = 51
        Line_Name = '마천지 5'
    else:
        Line_Name = str(Selected_Line)

    #------------------------------------------- 입력한 노선 DB 불러오기
    
    selected_model = globals()[f'Vi_CSV_NO{int(Selected_Line)}']

    # ------------------------------------------ 역 별 필터링
    
    Line_Select = selected_model.objects.all()
    # 호선에 맞는 역 이름 가져오기
    row_name = []
    for i in Line_Select:
        row_name.append(i.STATION)
    Station_name = list(set(row_name))

    #------------------------------------------- 개별역: 선 그래프
    
    S_filter = {'STATION': Selected_Station}

    D_filter = {'DIRECTION': '상선'}
    One_St_Line_UP = ALL_Line_G(selected_model,col_name,**{**D_filter, **S_filter})

    D_filter = {'DIRECTION': '하선'}
    One_St_Line_DOWN = ALL_Line_G(selected_model,col_name,**{**D_filter, **S_filter})    

    #------------------------------------------- 메시지

    content = {
    'Selected_Line':Selected_Line 
    ,'Line_Name':Line_Name
    ,'Station_name':Station_name
    , 'col_name':col_name
    , 'One_St_Line_UP':One_St_Line_UP
    , 'One_St_Line_DOWN':One_St_Line_DOWN
    , 'Selected_Station':Selected_Station
    }
    return render(request, 'D_Fivth_Page.html',content)

#=========================================== 기타 함수

def NansuTo000 (request):
    Nansu = request
    Nan_List = [0, 0, 0]
    Nan_List[0] = Nansu // 100
    Nan_List[1] = (Nansu // 10) % 10
    Nan_List[2] = Nansu % 10
    Nan_Result = ''.join(map(str,Nan_List))
    return Nan_Result

#=========================================== 시각화용 함수

#------------------------------------------- 선 그래프

def ALL_Line_G(selected_model, col_name, **kwargs):
    One_Dir = selected_model.objects.filter(**kwargs)
    LINE_GS = []
    for i in col_name:
        average = round(mean([getattr(record, i) for record in One_Dir]), 2)
        LINE_GS.append(average)

    return LINE_GS

#------------------------------------------- 시간별 평균내는거

def Station_Time_AVG_Fu(selected_model,FILTER):
    station_averages = selected_model.objects.values(FILTER).annotate(
    avg_TIME_05=Avg('TIME_05'),
    avg_TIME_06=Avg('TIME_06'),
    avg_TIME_07=Avg('TIME_07'),
    avg_TIME_08=Avg('TIME_08'),
    avg_TIME_09=Avg('TIME_09'),
    avg_TIME_10=Avg('TIME_10'),
    avg_TIME_11=Avg('TIME_11'),
    avg_TIME_12=Avg('TIME_12'),
    avg_TIME_13=Avg('TIME_13'),
    avg_TIME_14=Avg('TIME_14'),
    avg_TIME_15=Avg('TIME_15'),
    avg_TIME_16=Avg('TIME_16'),
    avg_TIME_17=Avg('TIME_17'),
    avg_TIME_18=Avg('TIME_18'),
    avg_TIME_19=Avg('TIME_19'),
    avg_TIME_20=Avg('TIME_20'),
    avg_TIME_21=Avg('TIME_21'),
    avg_TIME_22=Avg('TIME_22'),
    avg_TIME_23=Avg('TIME_23'),
    avg_TIME_24=Avg('TIME_24')
    )
    return station_averages

#------------------------------------------- 히트맵

def Func_for_HM(Station_name,col_name,station_averages_H):
    station_name_dict = {station_name: i for i, station_name in enumerate(Station_name, start=1)}
    col_name_dict = {col_name: j for j, col_name in enumerate(col_name, start=1)}
    Result = []

    # 리스트 만들기
    for item in station_averages_H:
        if item is not None:
            station_num = station_name_dict.get(item['STATION'])
        else:
            station_num = 0
        # print(station_num,type(station_num),'================================')
        for col in col_name:
            time_num = col_name_dict.get(col)
            # print(time_num,'================================')
            # avg_value = round(item[f'avg_{col}'], 2)
            if item[f'avg_{col}'] is not None:
                avg_value = round(item[f'avg_{col}'], 2)
            else:
                avg_value = 12.12
            Result.append([time_num, station_num, avg_value])
    return Result

#------------------------------------------- 파이그래프

def Func_for_PIE(station_averages_PI):
    # 데이터 형식 변환
    Result = []
    for entry in station_averages_PI:
        day = entry['DAY']
        y_value = 'y'
        y_data = round(mean([entry[f'avg_TIME_{hour:02}'] for hour in range(5, 25)]), 2)
        Result.append({'name': day, y_value: y_data})
    return Result

