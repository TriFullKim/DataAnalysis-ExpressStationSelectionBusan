import pandas as pd

# CSV 파일 불러오기
d = pd.read_csv("merged_data.csv", encoding='cp949')

# 같은 동(HJDONG_NAME)으로 그룹화하고 각 동의 잠재수요특성(E/D) 값의 합계 계산
gd = d.groupby(['LineCode', 'StationName'])['각 동의 잠재수요특성'].sum().reset_index()

gd.to_csv("역별_잠재수요특성_합계.csv", index=False)