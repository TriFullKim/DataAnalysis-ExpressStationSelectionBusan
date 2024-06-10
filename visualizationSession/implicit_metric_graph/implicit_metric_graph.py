import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드
s = pd.read_csv('sorted_implicit_metric1.csv', encoding='cp949')

# 읽어온 데이터를 scode와 implicit_metric 컬럼만 있는 데이터프레임으로 만듦.
df = pd.DataFrame(s, columns=["scode", "implicit_metric"])

# scode 기준으로 데이터를 정렬하고, 인덱스를 리셋한 후, scode를 데이터프레임의 인덱스로 설정.
implicit_metric = df.sort_values(by="scode").reset_index(drop=True)
implicit_metric = implicit_metric.set_index("scode")

# implicit_metric 컬럼의 최대값을 구하고, 그 값에 1.15를 곱하여 max 변수에 저장
max = implicit_metric["implicit_metric"].max() * 1.15

# 첫 번째 그래프의 크기를 설정, scode가 95부터 134까지의 데이터를 막대 그래프로 그림.
plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax1 = implicit_metric.loc[95:134, :].plot.bar()
fig1 = ax1.get_figure()
ax1.set_ylim(0, max)

# 두 번째 그래프의 크기를 설정, scode가 201부터 243까지의 데이터를 막대 그래프로 그림.
plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax2 = implicit_metric.loc[201:243, :].plot.bar()
fig2 = ax2.get_figure()
ax1.set_ylim(0, max)

# 세 번째 그래프의 크기를 설정, scode가 301부터 317까지의 데이터를 막대 그래프로 그림.
plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax3 = implicit_metric.loc[301:317, :].plot.bar()
fig3 = ax3.get_figure()
ax1.set_ylim(0, max)

# 네 번째 그래프의 크기를 설정, scode가 401부터 414까지의 데이터를 막대 그래프로 그림.
plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax4 = implicit_metric.loc[401:414, :].plot.bar()
fig4 = ax4.get_figure()
ax1.set_ylim(0, max)

# 그래프들을 SVG 파일로 저장. figs 리스트에 그래프 객체들을 저장, 각 그래프를 순차적으로 SVG 파일로 저장.
# 인덱스가 0인 요소는 건너뛰고, 나머지 그래프는 line{idx}_implicit_metric_SUM.svg 형식의 파일명으로 저장.
figs = [-1, fig1, fig2, fig3, fig4]
for idx, f in enumerate(figs):
    if f == -1:
        continue
    f.savefig(f"line{idx}_implicit_metric_SUM.svg", format="svg")