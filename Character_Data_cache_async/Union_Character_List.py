import requests
from datetime import datetime, timedelta
import json
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

file_path = r'D:\Project\python\Character_Data_json\Union_character_List.json'

def Union_Character_list(api_key, ocid, date_value):
    #Character_utility.initialize_json_file(file_path)
    
    headers = Character_utility.headers_data(api_key)
    #urlString = f"https://open.api.nexon.com/maplestory/v1/user/union?ocid={ocid}&date={date_value}" #유니온 정보 조회
    #urlString = f"https://open.api.nexon.com/maplestory/v1/user/union-raider?ocid={ocid}&date={date_value}" #유니온 공격대 정보 조회
    #urlString = f"https://open.api.nexon.com/maplestory/v1/user/union-artifact?ocid={ocid}&date={date_value}" #유니온 아티팩트 정보 조회
    urlString = f"https://open.api.nexon.com/maplestory/v1/ranking/union?ocid={ocid}&date={date_value}&page=1&world_name=리부트" #유니온 랭킹 정보 조회 (본캐 조회)
    response = requests.get(urlString, headers = headers, timeout=30)

    Character_utility.file_mode(file_path, response.json(), 'w+')
    data = response.json()
    
    return data