def make_graph_data():
    from util import (
        loadPickle,
        PATH_WEIGHTED_MEAN_INTERVAL,
        PATH_INTER_STATION_SPEND_TIME,
    )
    from stationUtil import fn_export_subway_graph

    _, subway_graph = fn_export_subway_graph(loadPickle(PATH_INTER_STATION_SPEND_TIME))

    interval = loadPickle(PATH_WEIGHTED_MEAN_INTERVAL)
    new_subway_graph = {}
    for index, value in subway_graph.items():
        value["dispatchingTime"] = interval[index[0]]
        new_subway_graph[index] = value

    return new_subway_graph


new_subway_graph = make_graph_data()
# GPT-4
# Prompt1:인접리스트로 구현한 가중치 그래프를 파이썬으로 구현 해줘
# Prompt2:구현한 그래프로 가중치의 합이 최소가되는 경로를 추출하는 함수를 짜줘
import heapq


class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex in self.adj_list:
            self.adj_list[from_vertex].append((to_vertex, weight))
        else:
            self.adj_list[from_vertex] = [(to_vertex, weight)]

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")

    def find_min_path(self, start_vertex, end_vertex):
        distances = {vertex: float("infinity") for vertex in self.adj_list}
        distances[start_vertex] = 0
        previous_vertices = {vertex: None for vertex in self.adj_list}
        pq = [(0, start_vertex)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex == end_vertex:
                break

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        path, current_vertex = [], end_vertex
        while previous_vertices[current_vertex] is not None:
            path.append(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.append(start_vertex)

        return path[::-1]

    # Prompt 3: ```{Above Lines}``` 위 코드는 인접리스트로 구현된 그래프를 구현한 모습이다. 메서드 find_min_path에서 나온 출력 값(리스트로된 경로)을 이용해 해당경로의 가중치의 총합을 구하는 메서드를 추가로 작성해줘
    def calculate_path_weight(self, path):
        total_weight = 0
        if len(path) < 2:
            return total_weight

        for i in range(len(path) - 1):
            from_vertex = path[i]
            to_vertex = path[i + 1]
            for neighbor, weight in self.adj_list[from_vertex]:
                if neighbor == to_vertex:
                    total_weight += weight
                    break

        return total_weight


# Draw Graph
def time_weight_graph(exclude_list: list = [], new_subway_graph=new_subway_graph):
    graph = WeightedGraph()
    for index, weights in new_subway_graph.items():
        v1, v2, isTransfer = index
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        time_spend = weights["time"]

        # 시나리오 작성 시, 정차하지 않는 역은 정차 시간(stopTime)을 빼고 간선을 추가한다.
        if v1 in exclude_list:
            graph.add_edge(v1, v2, time_spend)
            continue

        time_spend = weights["time"] + weights["stoppingTime"]

        # 환승하는 경우 (최악) 배차시간을 적용. - 최소 환승을 적용하기 위해서임.
        if isTransfer:
            time_spend += weights["dispatchingTime"]

        graph.add_edge(v1, v2, time_spend)

    return graph


def dist_weight_graph(new_subway_graph=new_subway_graph):
    graph = WeightedGraph()
    for index, weights in new_subway_graph.items():
        v1, v2, _ = index
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_edge(v1, v2, weights["dist"])

    return graph


# Applicated Function
def calc_total_path_weight(g: WeightedGraph, sCode_start, sCode_end):
    weight = 1  # 단위를 시간으로 바꾸고 싶으면 1/3600 으로 할것
    """
    calc_weight 최단경로를 지났을 때의 weigt 총합을 반환함.

    Args:
        g (WeightedGraph): 그래프 넣으면됨
        sCode_start (_type_): 시작지점
        sCode_end (_type_): 끝지점

    Returns:
        _type_: 초 단위로 출력함.
    """
    path = g.find_min_path(sCode_start, sCode_end)
    return g.calculate_path_weight(path) * weight


def line_num_to_range(line_num: int):
    path = []
    if line_num == 1:
        path = [*range(95, 134 + 1)]
    elif line_num == 2:
        path = [*range(201, 243 + 1)]
    elif line_num == 3:
        path = [*range(301, 317 + 1)]
    elif line_num == 4:
        path = [*range(401, 414 + 1)]
    return path


def calc_line_speed(line_num: int, g_dist: WeightedGraph, g_time: WeightedGraph):
    UNITFACTOR_P1KM_TO_1KM = 1 / 10
    UNITFACTOR_1SEC_TO_1HOUR = 1 / 3600
    """
    calc_line_speed 표정속도 구하는 함수임.

    Args:
        line_num (int): 호선입력하세요
        g_dist (WeightedGraph): dist graph 입력하세요
        g_time (WeightedGraph): time graph 입력하세요

    Returns:
        float: 표정속도[km/h]
    """
    path = line_num_to_range(line_num)
    return (g_dist.calculate_path_weight(path) * UNITFACTOR_P1KM_TO_1KM) / (
        g_time.calculate_path_weight(path) * UNITFACTOR_1SEC_TO_1HOUR
    )


def calc_line_spend_time(line_num: int, g_time: WeightedGraph):
    """
    calc_line_speed 표정속도 구하는 함수임.

    Args:
        line_num (int): 호선입력하세요
        g_dist (WeightedGraph): dist graph 입력하세요
        g_time (WeightedGraph): time graph 입력하세요

    Returns:
        float: 표정속도[km/h]
    """
    path = line_num_to_range(line_num)
    return g_time.calculate_path_weight(path)
