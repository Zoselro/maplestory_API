from datetime import datetime, timedelta
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
import requests
import json
file_path = r'D:\Project\python\Character_Data_json\cube_data.json'
api_key = 'live_23a1b1d4734e921eb7e769206e88f1f8d52039d05af824fe944ba9b2cf6e1f7d183da407b7a678747cf6efb59c154129'
#cursor = 'be2b6abfc1bfc0d5222c26fae987a15f86e68d4012202d0434d05f81868f68e3' #count=10
urlString = f"https://open.api.nexon.com/maplestory/v1/history/cube?x-nxopen-api-key={api_key}&count=30&date=2022-11-25"
#urlString = f"https://open.api.nexon.com/maplestory/v1/history/cube?x-nxopen-api-key={api_key}&count=10&cursor={cursor}"

#첫 날 부터 조회 -> 첫 날에 한 번에 1000개씩 조회를 하는데,  26개가 조회 된다면
#예를들어 count = 10 으로 조회, 그 이후 next_cursor 데이터 값이 있다면 그 cursor값으로 그다음 10개 조회 가능 그다음 cusor값이 있다면 그 다음 6개 조회 하고 cursor은 NULL
#이로 인해 총 큐브 돌린 갯수 확인 가능 및 페이징 처리도 원활하게 가능.


headers = Character_utility.headers_data(api_key)

response = requests.get(urlString, headers = headers, timeout=30)
data = response.json()

Character_utility.file_mode(file_path, data, 'w+')

print(data)