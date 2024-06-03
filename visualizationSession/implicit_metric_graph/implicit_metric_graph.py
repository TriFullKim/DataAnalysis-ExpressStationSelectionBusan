import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드
s = pd.read_csv('sorted_implicit_metric1.csv', encoding='cp949')

df = pd.DataFrame(s, columns=["scode", "implicit_metric"])
implicit_metric = df.sort_values(by="scode").reset_index(drop=True)
implicit_metric = implicit_metric.set_index("scode")

max = implicit_metric["implicit_metric"].max() * 1.15

plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax1 = implicit_metric.loc[95:134, :].plot.bar()
fig1 = ax1.get_figure()
ax1.set_ylim(0, max)

plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax2 = implicit_metric.loc[201:243, :].plot.bar()
fig2 = ax2.get_figure()
ax1.set_ylim(0, max)

plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax3 = implicit_metric.loc[301:317, :].plot.bar()
fig3 = ax3.get_figure()
ax1.set_ylim(0, max)

plt.rcParams["figure.figsize"] = (39 * 3, 10)
ax4 = implicit_metric.loc[401:414, :].plot.bar()
fig4 = ax4.get_figure()
ax1.set_ylim(0, max)

# Save File
figs = [-1, fig1, fig2, fig3, fig4]
for idx, f in enumerate(figs):
    if f == -1:
        continue
    f.savefig(f"line{idx}_implicit_metric_SUM.svg", format="svg")