# multi_semi_project
멀티 캠퍼스 세미프로젝트

- 경로: 대중교통혼잡 > sample_data > 서울교통공사_지하철혼잡도정보 (2017, 2019, 2021, 2022)
  - 출처: [공공데이터포털](https://www.data.go.kr/data/15071311/fileData.do)
- 경로: 기상조건_대중교통 > data > 서울_기온및강수량분석
  - 출처: [기상청 기상자료개발포털] [기온분석](https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70) [강수량분석](https://data.kma.go.kr/stcs/grnd/grndRnList.do?pgmNo=69)
- 경로: 기상조건_대중교통 > data > 서울_지하철_호선별역별_승하차인원
  - 출처: [서울열린데이터광장](https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do)
- 경로 : 특일정보 > 한국천문연구원_특일정보
  - 출처 : [공공데이터포털](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012690) 
- 경로: 기상조건_대중교통 > data > 서울_통근·통학시 이용하는 교통수단 통계(2022)
  - 출처: [서울열린데이터광장](https://data.seoul.go.kr/dataList/10283/S/2/datasetView.do)  

---

- drop_line = '경춘선', '경강선', '우이신설선', '공항철도 1호선', '수인선', '중앙선', '경의선', '분당선'
- 1호선-(서울역~청량리)
- 경인선-1호선 끝(인천~구일)
- 경원선-1호선 끝(소요산~외대앞) 회기역은???????
- 장항선-1호선 끝(봉명-쌍용-아산-배방-온양온천-신창-탕정)
- 2호선 - 완성
- 3호선 - (지축~오금) //3호선 + 일산선 = 지하철 노선도 내 3호선 완성
- 일산선-3호선 끝(대화-주엽-장발산-마두-백석-대곡-화정-원당-원흥-삼송-지축)
- 4호선- (남태령~당고개)
- 과천선-4호선 (범계-평촌-인덕원-정부과천청사-과천-대공원-경마공원-선바위)
- 안산선-4호선 끝(오이도-정왕-신길온천-안산-초지-고잔-중앙-한대앞-상록수-반월-대야미-수리산-산본)
- 5호선 - 완성
- 6호선 - 완성
- 7호선 - 석남, 산곡역 없음
- 8호선 - 완성
- 9호선 + 9호선2~3단계 = 지하철 노선도 내 9호선 완성
> 어느 호선 버리고 취할지 정해야 할 듯 합니다. [호선별역별승하차인원](https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do)데이터에서 확인한 결과입니다.
