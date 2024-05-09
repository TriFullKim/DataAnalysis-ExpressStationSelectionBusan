import pandas as pd
import pickle

PATH_STATION_INFO = "../raw_data/selected/부산교통공사_도시철도 역명정보.csv"
PATH_STATION_INFO_REFINE = "../trimmed_data/stationCodeNameLine.json"

DAYTYPE = ['토요일', '일요일', '공휴일', '평일']
PATH_STATION_SCHEDULE = "../raw_data/selected/부산교통공사_부산도시철도 운행 정보.csv"
PATH_STATION_SCHEDULE_REFINE= "../trimmed_data/stationSchedule.json"
PATH_STATION_SCHEDULE_REFINE_DAYTYPE = [f"../trimmed_data/stationSchedule{day}.json" for day in DAYTYPE]
PATH_STATION_SCHEDULE_SEPERATED_DAYTYPE= [f"../trimmed_data/stationSchedule{day}-SEPERATED.json" for day in DAYTYPE]
PATH_INTER_STATION_SPEND_TIME = "../trimmed_data/IntervalTimeAPI.pickle"
PATH_INTER_STATION_EXCHANGE_TIME = "../trimmed_data/ExchangeTimeAPI.pickle"

PATH_CUSTOMER_IO = "../raw_data/selected/부산교통공사_시간대별 승하차인원.csv"

PATH_SCHEDULE_INTERVAL_MEAN=[f"../trimmed_data/ScheduleIntervalMean{day}.pickle" for day in DAYTYPE]
PATH_WEIGHTED_MEAN_INTERVAL = "../trimmed_data/WeightedIntervalMean.pickle"
# CONST
DVECT_EIGEN = {
    0: [
        "다대포해수욕장노포",
        "신평노포",
    ],
    1: [
        "노포다대포해수욕장",
        "신평다대포해수욕장",
        "노포신평", 
    ],
    3: [
        "구명장산",
        "호포장산",
        "양산장산",
        "양산전포",
    ],
    4: [
        "장산호포",
        "장산양산",
        "장산광안",
        "호포양산",
        "전포양산",
        "광안양산",
    ],
    5: [
        "수영대저",
    ],
    6: [
        "대저수영",
    ],
    7: [
        "안평미남",
    ],
    8: [
        "미남안평",
    ],
}
DVECT_EIGEN_REV = {
    "다대포해수욕장노포": 0,
    "신평노포": 0,
    "노포다대포해수욕장": 1,
    "신평다대포해수욕장": 1,
    "노포신평": 1,
    "구명장산": 2,
    "호포장산": 2,
    "양산장산": 2,
    "양산전포": 2,
    "장산호포": 3,
    "장산양산": 3,
    "장산광안": 3,
    "호포양산": 3,
    "전포양산": 3,
    "광안양산": 3,
    "수영대저": 4,
    "대저수영": 5,
    "안평미남": 6,
    "미남안평": 7,
}



SUBWAY_CODE_PATH = PATH_STATION_INFO_REFINE
def stationCode(_x, code_data:pd.DataFrame=pd.DataFrame(), return_mode="code"):
    result = None
    if pd.DataFrame().__len__() == 0:
        try:
            code_data = pd.read_csv(SUBWAY_CODE_PATH)
        except:
            return FileNotFoundError

    if return_mode == "code":
        assert type(_x) is str, "Input must be str"
        code_data = code_data.set_index(keys="StationName")
        result = code_data.loc[_x, "StationCode"]
    elif return_mode == "name":
        assert type(_x) is int, "Input must be int"
        code_data = code_data.set_index(keys="StationCode")
        result = code_data.loc[_x, "StationName"]

    return result

def savePickle(_dat,path):
    with open(path,mode="wb") as f:
        pickle.dump(_dat,f)

def loadPickle(path):
    with open(path, mode='rb') as f:
        return pickle.load(f)
    
STATION_NameCode = loadPickle("../trimmed_data/stationNameCode.pickel")

def df_mul_DiffColName(df1:pd.DataFrame,df2:pd.DataFrame,op_target:dict) -> pd.DataFrame:
    _vals = list(op_target.values())
    _rev_dict ={val:key for key,val in op_target.items()}
    if list(op_target.keys())[0] in df1.columns:
        _df1 = df1.rename(columns=op_target)
        _df1.loc[:,_vals] = _df1.loc[:,_vals].mul(df2.loc[:,_vals])
        return _df1.rename(columns=_rev_dict)
    
    elif list(op_target.keys())[0] in df2.columns:
        _df2 = df2.rename(columns=op_target)
        _df2.loc[:,_vals] = _df2.loc[:,_vals].mul(df1.loc[:,_vals])
        return _df2.rename(columns=_rev_dict)
    
    else:
        assert False, NotImplementedError
        
def df_div_DiffColName(df1:pd.DataFrame,df2:pd.DataFrame,op_target:dict) -> pd.DataFrame:
    _vals = list(op_target.values())
    _rev_dict ={val:key for key,val in op_target.items()}
    if list(op_target.keys())[0] in df1.columns:
        _df1 = df1.rename(columns=op_target)
        _df1.loc[:,_vals] = _df1.loc[:,_vals].div(df2.loc[:,_vals])
        return _df1.rename(columns=_rev_dict)
    
    elif list(op_target.keys())[0] in df2.columns:
        _df2 = df2.rename(columns=op_target)
        _df2.loc[:,_vals] = _df2.loc[:,_vals].div(df1.loc[:,_vals])
        return _df2.rename(columns=_rev_dict)
    
    else:
        assert False, NotImplementedError