import pandas as pd

# 데이터 불러오기
df = pd.read_csv("승하차인원.csv", encoding='cp949')

# 필요한 열 선택
df1 = df[['역명','년월일', '구분', '합계']]

# 데이터 복사
df2 = df1.copy()

# 날짜 열을 날짜 형식으로 변환
df2['년월일'] = pd.to_datetime(df2['년월일'])

# 주차 정보 추가
df2['주'] = df2['년월일'].dt.isocalendar().week

# 역별 주별 승하차 인원 데이터 딕셔너리로 저장
w = {}
for s in df2['역명'].unique():
    w[s] = {}
    for w_n in range(1, 14):
        w[s][w_n] = df2[(df2['역명'] == s) & (df2['주'] == w_n)]

# 각 역별 주차별 승차인원과 하차인원 합산하여 출력
for s, w_d in w.items():
    # print(f"역명: {s}")
    for w_n, data in w_d.items():
        승차 = data[data['구분'] == '승차']['합계'].sum()
        하차 = data[data['구분'] == '하차']['합계'].sum()
        # print(f"Week {w_n}:")
        # print(f"총 승차 인원: {승차}")
        # print(f"총 하차 인원: {하차}")

# s = station, w = station_weekly_data, w_d = weekly_data, w_n = week_num

print(w['다대포해수욕장'])