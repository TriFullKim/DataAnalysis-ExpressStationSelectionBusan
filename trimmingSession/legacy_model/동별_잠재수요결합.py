import pandas as pd

# 데이터프레임 불러오기
area = pd.read_csv("HJDONG_AREA_GIS.csv")
people = pd.read_csv("FLUX_METRIC.csv")

# HJDONG_NAME에서 '부산광역시 사하구 '를 제거한 새로운 열 생성
# 구군별 csv 파일을 위해 기장군 -> 남구 -> 해운대구... 로 변환
area['CLEANED_HJDONG_NAME'] = area['HJDONG_NAME'].str.replace('부산광역시 기장군 ', '')

# 데이터프레임 결합
merged_data = pd.merge(area, people, left_on='CLEANED_HJDONG_NAME', right_on='HJDONG', how='left')

# 필요 없는 열 제거
merged_data = merged_data.drop(columns=['CLEANED_HJDONG_NAME'])

merged_data.to_csv("잠재수요_기장군.csv", index = False)