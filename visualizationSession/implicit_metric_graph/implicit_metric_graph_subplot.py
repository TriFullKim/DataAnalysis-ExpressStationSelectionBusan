import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sorted_implicit_metric1.csv', encoding='cp949')

# def create_bar_plot(line_data, stations, station_numbers, line_name):
#     plt.figure(figsize=(20, 6))
#     plt.bar(stations, line_data.set_index('scode').reindex(stations)['implicit_metric'].fillna(0))
#     plt.xlabel('Station Number')
#     plt.ylabel('Implicit Metric')
#     plt.title(f'Implicit Metric ({line_name})')
#     plt.xticks(stations, station_numbers, rotation=45)
#     plt.tight_layout()

#     # 막대 그래프 상단에 implicit_metric 표시
#     for i, v in enumerate(line_data.set_index('scode').reindex(stations)['implicit_metric'].fillna(0)):
#         plt.text(i + stations[0] - 0.5, v + 0.01, str(round(v, 2)), ha='center', va='bottom')

# line1 = df[df['LineCode'] == 1]
# line2 = df[df['LineCode'] == 2]
# line3 = df[df['LineCode'] == 3]
# line4 = df[df['LineCode'] == 4]

# stations_1 = list(range(95, 135))
# stations_2 = list(range(201, 243))
# stations_3 = list(range(301, 317))
# stations_4 = list(range(401, 414))

# station_numbers_1 = [str(scode) for scode in stations_1]
# station_numbers_2 = [str(scode) for scode in stations_2]
# station_numbers_3 = [str(scode) for scode in stations_3]
# station_numbers_4 = [str(scode) for scode in stations_4]

# # 1호선
# create_bar_plot(line1, stations_1, station_numbers_1, "Line 1")
# plt.show()

# # 2호선
# create_bar_plot(line2, stations_2, station_numbers_2, "Line 2")
# plt.show()

# # 3호선
# create_bar_plot(line3, stations_3, station_numbers_3, "Line 3")
# plt.show()

# # 4호선
# create_bar_plot(line4, stations_4, station_numbers_4, "Line 4")
# plt.show()

def create_bar_plot(ax, line_data, stations, station_numbers, line_name):
    ax.bar(stations, line_data.set_index('scode').reindex(stations)['implicit_metric'].fillna(0))
    ax.set_xlabel('Station Number')
    ax.set_ylabel('Implicit Metric')
    ax.set_xticks(stations)
    ax.set_xticklabels(station_numbers, rotation=45)

    # # 막대 그래프 상단에 implicit_metric 표시
    # for i, v in enumerate(line_data.set_index('scode').reindex(stations)['implicit_metric'].fillna(0)):
    #     ax.text(i + stations[0] - 0.5, v + 0.01, str(round(v, 2)), ha='center', va='bottom')

line1 = df[df['LineCode'] == 1]
line2 = df[df['LineCode'] == 2]
line3 = df[df['LineCode'] == 3]
line4 = df[df['LineCode'] == 4]

stations_1 = list(range(95, 135))
stations_2 = list(range(201, 243))
stations_3 = list(range(301, 317))
stations_4 = list(range(401, 414))

station_numbers_1 = [str(scode) for scode in stations_1]
station_numbers_2 = [str(scode) for scode in stations_2]
station_numbers_3 = [str(scode) for scode in stations_3]
station_numbers_4 = [str(scode) for scode in stations_4]

fig, axs = plt.subplots(2, 2, figsize=(20, 10))
fig.suptitle('Implicit Metric(All Lines)')

# 1호선
create_bar_plot(axs[0, 0], line1, stations_1, station_numbers_1, "Line 1")

# 2호선
create_bar_plot(axs[0, 1], line2, stations_2, station_numbers_2, "Line 2")

# 3호선
create_bar_plot(axs[1, 0], line3, stations_3, station_numbers_3, "Line 3")

# 4호선
create_bar_plot(axs[1, 1], line4, stations_4, station_numbers_4, "Line 4")

plt.tight_layout()
plt.show()