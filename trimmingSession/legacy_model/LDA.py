import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv("승하차인원.csv", encoding='cp949')

# 필요한 열 선택
df1 = df[['역명', '년월일', '구분', '합계']]

# 날짜 열을 날짜 형식으로 변환
df1['년월일'] = pd.to_datetime(df1['년월일'])

# 주차 정보 추가
df1['주'] = df1['년월일'].dt.isocalendar().week

# 역별 주별 승차인원과 하차인원을 저장할 딕셔너리 생성
승차_dict = {}
하차_dict = {}

# 각 역별 주차별 승차인원과 하차인원을 딕셔너리에 저장
for s in df1['역명'].unique():
    승차_dict[s] = {}
    하차_dict[s] = {}
    for w_n in range(1, 14):
        승차_dict[s][w_n] = df1[(df1['역명'] == s) & (df1['주'] == w_n) & (df1['구분'] == '승차')]['합계'].sum()
        하차_dict[s][w_n] = df1[(df1['역명'] == s) & (df1['주'] == w_n) & (df1['구분'] == '하차')]['합계'].sum()

# 데이터프레임으로 변환
승차_df = pd.DataFrame(승차_dict)
승차 = 승차_df.transpose()
하차_df = pd.DataFrame(하차_dict)
하차 = 하차_df.transpose()

# 1주차 데이터 추출
승차_1 = 승차.iloc[:, 1]
하차_1 = 하차.iloc[:, 1]

# 승차와 하차 데이터프레임 결합
승하차_1주 = pd.concat([승차_1, 하차_1], axis=1)
승하차_1주.columns = ['승차', '하차']

# 원하는 역 이름 리스트
stations = [
    "다대포해수욕장", "다대포항", "낫개", "신장림", "장림", "동매", "신평", "하단", 
    "당리", "사하", "괴정", "대티", "서대신", "동대신", "토성", "자갈치", "남포", 
    "중앙", "부산역", "초량", "부산진", "좌천", "범일", "범내골", "서면", "부전", 
    "양정", "시청", "연산", "교대", "동래", "명륜", "온천장", "부산대", "장전", 
    "구서", "두실", "남산", "범어사", "노포"
]

# 해당 역 이름 필터링
want_station = 승하차_1주.loc[stations]

# LDA 수행
lda = LDA(n_components=1)
X = want_station[['승차', '하차']]
# LDA를 위해 임의의 y 생성
y = [0 if i < len(X) // 2 else 1 for i in range(len(X))]

lda.fit(X, y)

# 가중치 추출
W_1, W_2 = lda.coef_[0]

print(f"W_1: {W_1}, W_2: {W_2}")

# 판별 함수 Z 계산
Z = lda.transform(X)

# Z를 데이터프레임에 추가
want_station['Z'] = Z

def assign_grade(z_value):
    if z_value < -1.0:
        return 5
    elif -1.0 <= z_value < -0.5:
        return 4
    elif -0.5 <= z_value < 0.0:
        return 3
    elif 0.0 <= z_value < 0.5:
        return 2
    else:
        return 1

# Z 값으로 등급 매기기
want_station['등급'] = want_station['Z'].apply(assign_grade)

print(want_station['등급'] <= 1)