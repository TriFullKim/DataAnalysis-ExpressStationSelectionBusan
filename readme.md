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
> - [부산교통공사_도시철도 역명정보](https://www.data.go.kr/data/3077187/fileData.do)
> - [부산교통공사_시간대별 승하차인원](https://www.data.go.kr/data/3057229/fileData.do)
> - [부산교통공사_부산도시철도 운행 정보](https://www.data.go.kr/data/15082980/fileData.do)

## `SubwayStation-Code.csv` 생성 후 수정필요.
데이터의 일부를 수정하는 것이 필요함.
1. `"·" -> "."` 
2. `"국제금융센터"->"국제금융"`