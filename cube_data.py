import requests
from datetime import datetime, timedelta
import json

file_path = r'D:\Project\python\API_Project\maplestory_API\json\maplestory_api_cube_data.json'

with open(file_path, 'w', encoding='utf-8') as json_file:
    json_file.write('')

headers = {
    "x-nxopen-api-key": "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
}

characterName = "리마"
urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + characterName
response = requests.get(urlString, headers=headers)
ocid = response.json()['ocid']

# 날짜 범위 설정
start_date = datetime(2022, 12, 22)
end_date = datetime(2024, 1, 23)
days_diff = (end_date - start_date).days
set_date = 0

# JSON 파일을 새로 시작
all_data = []
data_cache = {}

for i in range(days_diff + 1):
    date_num = (start_date + timedelta(days=set_date)).strftime('%Y-%m-%d')
    
    # 이미 캐시된 데이터가 있는 경우 재사용
    if date_num in data_cache:
        data = data_cache[date_num]
    else:
        urlString = f"https://open.api.nexon.com/maplestory/v1/history/cube?ocid={ocid}&count=1000&date={date_num}"
        response = requests.get(urlString, headers=headers)
        data = response.json()
        data_cache[date_num] = data  # 가져온 데이터를 캐시
    
    count_value = data.get('count')
    
    # count가 0이 아닐 때만 데이터 저장
    if count_value != 0:
        if 'cube_history' in data:
            for history in data['cube_history']:
                if history['cube_type'] == "블랙 큐브":
                    print(data)
                    all_data.append(data)
    set_date += 1  # 날짜 증가

# JSON 파일에 전체 데이터를 저장
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)
print("모든 데이터를 'response_data_cube.json' 파일로 저장했습니다.")