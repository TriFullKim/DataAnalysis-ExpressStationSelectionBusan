mkdir ./raw_data
mkdir ./raw_data/selected
mkdir ./trimmed_data

wget -O "부산교통공사_도시철도 역명정보.csv" "https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002831181&fileDetailSn=1&dataNm=%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%20%EC%97%AD%EB%AA%85%EC%A0%95%EB%B3%B4_20231023"
mv "./부산교통공사_도시철도 역명정보.csv" ./raw_data/selected

wget -O "부산교통공사_시간대별 승하차인원" "https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002902499&fileDetailSn=1&dataNm=%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EC%8B%9C%EA%B0%84%EB%8C%80%EB%B3%84%20%EC%8A%B9%ED%95%98%EC%B0%A8%EC%9D%B8%EC%9B%90_20240331"
mv "./부산교통공사_시간대별 승하차인원.csv" ./raw_data/selected

wget -O "부산교통공사_부산도시철도 운행 정보" "https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002767170&fileDetailSn=1&dataNm=%EB%B6%80%EC%82%B0%EA%B5%90%ED%86%B5%EA%B3%B5%EC%82%AC_%EB%B6%80%EC%82%B0%EB%8F%84%EC%8B%9C%EC%B2%A0%EB%8F%84%20%EC%9A%B4%ED%96%89%20%EC%A0%95%EB%B3%B4_20230710"
mv "./부산교통공사_부산도시철도 운행 정보.csv" ./raw_data/selected

echo "DONE"
rm ./download_data.sh