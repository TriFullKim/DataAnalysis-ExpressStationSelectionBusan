# Dataset Download
```bash
sh download_data.sh
```
> 실행 후 자동 삭제됨.

## API key to get data
[부산교통공사_부산도시철도 운행 정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15001019) 에서 API 키를 발급 받습니다.\
아래와 같이 파일을 구성합니다.
```
./
|___ security.yaml
```
```yaml
API_KEY: YOUR_KEY
```


# Issue
## bash file을 실행할 수 없을 경우
아래와 같이 파일구조를 만들어 줍니다
```
./
|___ raw_data
|      |___ selected
|___ trimmed_data
|
...

```
> 아래의 데이터를 다운받아서 `./raw_data/selected` 에 넣어줍니다.
> - [국가철도공단_부산1호선_역위치](https://www.data.go.kr/data/15041165/fileData.do)
> - [국가철도공단_부산2호선_역위치](https://www.data.go.kr/data/15041166/fileData.do)
> - [국가철도공단_부산3호선_역위치](https://www.data.go.kr/data/15041167/fileData.do)
> - [국가철도공단_부산4호선_역위치](https://www.data.go.kr/data/15041168/fileData.do)
> - [부산교통공사_도시철도 역명정보](https://www.data.go.kr/data/3077187/fileData.do)
> - [부산교통공사_시간대별 승하차인원](https://www.data.go.kr/data/3057229/fileData.do)
> - [부산교통공사_부산도시철도 운행 정보](https://www.data.go.kr/data/15082980/fileData.do)

## `SubwayStation-Code.csv` 생성 후 수정필요.
데이터의 일부를 수정하는 것이 필요함.
1. `"·" -> "."` 
2. `"국제금융센터"->"국제금융"`

# QGIS 처리
- Github에 올라와 있는 [행정동 경계 파일](https://github.com/vuski/admdongkor/tree/master/ver20230701)을 사용하였음
- QGIS상의 데이터 처리를 편리하게 하기 위해 역위치 데이터를 [Python을 이용하여](./trimmingSession/07-station-absolute-pos.ipynb) `EPSG:4326` 에서 `EPSG:5179` 형식으로 변경하였음.
1. Buffer를 이용해 지하철 역의 반경 1km 구역을 나타냄.
2. 행정동 경계와 Buffer와의 경계를 교차영역 기능으로 만들었음.
3. 각각의 행정도의 영역크기, 행정동과 Buffer와의 교차영역의 크기를 계산함.