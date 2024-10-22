
import requests
from datetime import datetime, timedelta
import json

file_path = r'D:\Project\python\jsonfilelist\maplestory_api_potential_data.json'
with open(file_path, 'w', encoding='utf-8') as json_file:
    json_file.write('')
headers = {
    "x-nxopen-api-key": "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
}

characterName = "리마"
urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + characterName
response = requests.get(urlString, headers=headers)
ocid = response.json()['ocid']

# 10월 1일부터 현재까지의 날짜 계산
start_date = datetime(2024, 1, 25)
end_date = datetime.now()
days_diff = (end_date - start_date).days
set_date = 0
# JSON 파일을 새로 시작
all_data = []
data = []
for i in range(days_diff + 1):
    date_num = (start_date + timedelta(days=set_date)).strftime('%Y-%m-%d')
    urlString = "https://open.api.nexon.com/maplestory/v1/history/potential?ocid=" + ocid + "&count=1000" + "&date=" + date_num
    response = requests.get(urlString, headers=headers)
    data = response.json()
    
    count_value = data.get('count')
    
    # 응답 데이터를 추가
    if data.get('count') == 0:
        pass
    else:
        all_data.append(data)
    
    set_date += 1  # 날짜 증가

# JSON 파일에 전체 데이터를 저장
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)

print("모든 데이터를 'response_data_potential.json' 파일로 저장했습니다.")