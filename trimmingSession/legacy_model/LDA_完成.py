import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt

df = pd.read_csv("승하차인원.csv", encoding='cp949')

df1 = df[['역명', '년월일', '구분', '합계']]

df1['년월일'] = pd.to_datetime(df1['년월일'])

df1['주'] = df1['년월일'].dt.isocalendar().week

승차_dict = {}
하차_dict = {}

for s in df1['역명'].unique():
    승차_dict[s] = {}
    하차_dict[s] = {}
    for w_n in range(1, 14):
        승차_dict[s][w_n] = df1[(df1['역명'] == s) & (df1['주'] == w_n) & (df1['구분'] == '승차')]['합계'].sum()
        하차_dict[s][w_n] = df1[(df1['역명'] == s) & (df1['주'] == w_n) & (df1['구분'] == '하차')]['합계'].sum()

승차_df = pd.DataFrame(승차_dict)
승차 = 승차_df.transpose()
하차_df = pd.DataFrame(하차_dict)
하차 = 하차_df.transpose()

data = pd.read_csv('StationNameCode1.csv', encoding='cp949')

stations_1 = data[data['LineCode'] == 1][['StationName', 'Code']]
stations_2 = data[data['LineCode'] == 2][['StationName', 'Code']]
stations_3 = data[data['LineCode'] == 3][['StationName', 'Code']]
stations_4 = data[data['LineCode'] == 4][['StationName', 'Code']]
station_names = stations_4['StationName'].tolist()
# station_names = station_1, 2, 3, 4로 각 주별, 호선별 Z값과 등급 환산


def grades(week):

    승차_week = 승차.iloc[:, week]
    하차_week = 하차.iloc[:, week]
    
    승하차_week = pd.concat([승차_week, 하차_week], axis=1)
    승하차_week.columns = ['승차', '하차']
    
    want_station = 승하차_week.loc[station_names].dropna()
    
    # LDA 수행
    lda = LDA(n_components=1)
    X = want_station[['승차', '하차']]
    
    y = [0 if i < len(X) // 2 else 1 for i in range(len(X))]
    
    lda.fit(X, y)
    
    W_1, W_2 = lda.coef_[0]
    
    print(f"Week {week}: W_1: {W_1}, W_2: {W_2}")
    
    # 판별 함수 Z 계산
    Z = lda.transform(X)
    
    want_station['Z'] = Z
    
    # 아래의 등급은 임의대로 threshold를 임의대로 지정함.
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
    
    want_station['등급'] = want_station['Z'].apply(assign_grade)
    
    return want_station.sort_values(by="Z", ascending=False)

for week in range(1, 12):
    result = grades(week)
    print(f"Week {week} Results:")
    print(result)

# 1주차 데이터
result_1주 = grades(1)
print(result_1주)