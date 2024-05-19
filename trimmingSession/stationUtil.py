EXCHANGE_RELATION = [
    (119, 219, True),
    (123, 305, True),
    (125, 402, True),
    (208, 301, True),
    (219, 119, True),
    (233, 313, True),
    (301, 208, True),
    (305, 123, True),
    (309, 401, True),
    (313, 233, True),
    (401, 309, True),
    (402, 125, True),
]


# time은 간선(vertex) startSc---endSc 의 가중치
# stoppingTime은 노드 endSc 의 가중치
# 환승역 일 때의 time 환승 시 소요 시간임.
def fn_export_subway_graph(_df):
    interval_time = _df
    subway_graph = interval_time.loc[
        :, ["exchange", "startSc", "endSc", "stoppingTime", "time","dist"]
    ]
    subway_graph = subway_graph.groupby(by=["startSc", "endSc", "exchange"]).sum()
    print(
        "len(subway_graph) == len(interval_time) : ",
        len(subway_graph) == len(interval_time),
    )

    subway_graph = subway_graph.T.to_dict()
    subway_graph_index = list(subway_graph.keys())

    # This RETURN ( (환승여부,startSc,endSc), (stoppingTime, time) )
    return subway_graph_index, subway_graph


def fn_export_exchange_station_index(idx):
    # 환승정보역 관계를 갖는 index 추출
    exchange_relation_index = []
    for _index in idx:
        _, _, exchange = _index
        if exchange is True:
            exchange_relation_index.append(_index)

    # This RETURN ( (환승여부,startSc,endSc)
    return exchange_relation_index

# stationCode 입력하면, 호선으로 반환함.
# 데이터 특성상 조건을 만듦
def get_line(sCode_x):
    if sCode_x < 200:
        return 1
    elif sCode_x < 300:
        return 2
    elif sCode_x < 400:
        return 3
    elif sCode_x < 500:
        return 4
    else:
        assert False, "MUST sCode_x < 500 (4호선까지 존재 합니다.)"
        
        
def line_range(sCode_x):
    line_num = get_line(sCode_x)
    if line_num==1:
        return range(0, 200)
    elif line_num==2:
        return range(200, 300)
    elif line_num==3:
        return range(300, 400)
    elif line_num==4:
        return range(400, 500)
    else:
        assert False, "MUST sCode_x < 500 (4호선까지 존재 합니다.)"


# 시작점(stationCode_x) 과 끝점(stationCode_y) 사이에 필수적으로 환승이 필요한지 확인하는 함수
def isExchange(sCode_x, sCode_y):
    """경로에서 환승이 일어 났는지 확인하는 함수"""
    assert sCode_x > 0 and sCode_y > 0, ValueError
    _X, _Y = sCode_x // 100, sCode_y // 100
    if _X > 1 and _Y > 1:
        return _X != _Y
    elif _X <= 1 and _Y <= 1:
        return False
    else:
        return True


# 같은 노선에서의 모든 황승역 확인
def find_exchange_inline(sCode: int, exchage=EXCHANGE_RELATION):
    result_arr = []
    for _index in exchage:
        startSc, _, _ = _index
        if startSc in line_range(sCode):
            result_arr.append(startSc)
    return result_arr


# sCode를 포함한 같은 이름을 갖는 다른 역코드를 리스트로 반환함.
def find_same_station(sCode: int, exchage=EXCHANGE_RELATION):  # -> list[Any]:
    _same_stations = []
    for _index in exchage:
        startSc, endSc, _ = _index
        if sCode == startSc:
            _same_stations.append(endSc)
    return _same_stations


# 가장 가까운 환승역 코드(같은 노선의 역코드와 다른 노선의 역코드) 반환
def find_exchange_near(sCode: int):
    _exchange_candidate = find_exchange_inline(sCode)
    _diff = [abs(s - sCode) for s in _exchange_candidate]
    _result_index = _diff.index(min(_diff))
    _near_station = [_exchange_candidate[_result_index]]
    _near_station.extend(find_same_station(_near_station[0]))
    return _near_station


# 같은 노선 중에서 sCode 기준 양쪽 각 방면에 있는 역코드들 반환
def make_RL_Node_inline(sCode: int):
    l_node, r_node = [], []
    for s in find_exchange_inline(sCode):
        print(s, sCode)
        if sCode < s:
            r_node.append(s)
        elif s < sCode:
            l_node.append(s)
    return l_node, r_node
