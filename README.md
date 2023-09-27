# 멀티캠퍼스 세미프로젝트 (23.09.01 ~ 23.09.26) 
| 교육기간(23.06.26 ~ 23.12.06) 중 처음하는 프로젝트이다.

## 결과 모습
  - 유튜브 링크 : https://www.youtube.com/watch?v=phZRdA8Wsik
  - 서비스 링크 : http://15.152.248.112:8000/
    (서비스 링크의 경우, 잡아먹는 리소스가 너무 커 서버를 계속 켜둘 수 없다. 사용모습은 유튜브로 확인 또는 아래 웹 개발팀원에 연락 필요)
    (웹개발 팀원 : https://kimec995.github.io/)
    

## 주제 : 지하철 혼잡도 예측 및 사용자 분산 서비스
  - 주제선정 배경 : 이태원 참사 이후 군중밀집의 위험성에 대한 인식 상승, 지하철 혼잡에 대한 경각심도 함께 대두 됨. 우리 프로젝트가 혼잡도 문제를 해결하는데 조금은 도움이 되지 않을까 하여 기획 

## 혼잡도란?
  - 국토교통부 예규에서 좌석 54개에 사람이 모두 앉아 있는 것을 34%, 1량 정원 160명을 100%로 기준 삼아 나타내는 수치.
  - 영국 서퍽대학교 군중과학 객원 교수인 Keith Still 교수의 연구에 따르면 1m^2의 공간에 5명부터 군중 밀집 임계점이라고 함.
  - 54명(좌석) + {32.56m^2(열차입석면적평균)x5(임계점)} = 216.8명 => 혼잡도 135.5%
  - 위 처럼 계산해보면 혼잡도가 135.5 이상일 경우 사고가 날 가능성이 높다고 볼 수 있다.

## 데이터 수집
  - 서울열린데이터광장, 공공데이터포털, 기상청에서 데이터 수집

## 변수 선정
  - 1. 월
    2. 요일
    3. 시간대
    4. 기상조건
    5. 추가적인 파생변수 고려
   
## EDA
  - 1. 월 / 월별 승객 수 비교
       ![README_image](README_image/월별승객수.png)

       - 봄,가을에는 증가하는 추세
       - 여름, 겨울에는 감소하는 추세
       - 주기성을 보임 (역마다 주기성이 조금씩 다름)
       - 유의미한 변수로 판단


    2. 요일 / 요일별 승객 수 비교
       ![README_image](README_image/요일별승객수.png)

       - 월요일부터 금요일까지 승객 수 증가
       - 토,일요일에는 승객 수가 급격히 감소
       - 위 그래프는 성신여대입구역을 기준으로 나타낸것, 다른 역들은 또 다른 다양한 변화를 보임
       - 유의미한 변수로 판단

      
    3. 시간대 / 시간대별 승객 수 비교
       ![README_image](README_image/시간대별승객수(1).png)

       ![README_image](README_image/시간대별승객수(2).png)

       - 출/퇴근 시간대에 특히나 많은 이용객이 있는 것을 알 수 있음
       - 반면에 새벽시간대는 거의 없다.
       - 유의미한 변수로 판단
      

    4. 기상조건
       
       ![README_image](README_image/기상조건에따른승객.png)

       ![README_image](README_image/강수량.png)

       ![README_image](README_image/기온&강수량.png)

       - 처음 가설로 설정했던 비가 많이 올 수록, 강수량이 높을 수록 지하철 이용객이 많을 것으로 예상한것과 달리 큰 관련성이 없게 나왔고 기온도 마찬가지로 큰 영향을 주지 못했다.
       - 기상조건 또 한 가설과 다르고 오차범위가 너무 크게 나타났다.
       - 적절한 변수가 되지 못한다.



## 데이터 필터링


# 폴더
### 데이터 정리

### 머신러닝

### 시행착오

### 최종산출물

### 프로젝트 로그
