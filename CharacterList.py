import requests
from datetime import datetime, timedelta
import json
file_path = r'D:\Project\python\json\response_data_character_list.json'
with open(file_path, 'w', encoding='utf-8') as json_file:
    json_file.write('')

headers = {
    "x-nxopen-api-key": "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
}

characterName = "리마"
urlString = "https://open.api.nexon.com/maplestory/v1/character/list?character_name=" + characterName
response = requests.get(urlString, headers = headers)

with open(file_path, 'r+', encoding='utf-8') as json_file:
    json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

print("응답 데이터를 'response_data.json' 파일로 저장했습니다.")
print(response.json())