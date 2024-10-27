import requests
from datetime import datetime, timedelta
import json
import headers_data
import json_file_clear

file_path = r'D:\Project\python\Character_Data_json\Union_character_List.json'

def Union_Character_list(api_key, ocid, date_value):
    json_file_clear.initialize_json_file(file_path)
    
    headers = headers_data.headers_data(api_key)
    #urlString = f"https://open.api.nexon.com/maplestory/v1/user/union?ocid={ocid}&date={date_value}" #유니온 정보 조회
    #urlString = f"https://open.api.nexon.com/maplestory/v1/user/union-raider?ocid={ocid}&date={date_value}" #유니온 공격대 정보 조회
    #urlString = f"https://open.api.nexon.com/maplestory/v1/user/union-artifact?ocid={ocid}&date={date_value}" #유니온 아티팩트 정보 조회
    urlString = f"https://open.api.nexon.com/maplestory/v1/ranking/union?ocid={ocid}&date={date_value}" #유니온 랭킹 정보 조회 (본캐 조회)
    response = requests.get(urlString, headers = headers)
    
    print("response.status_code : ", response.status_code)

    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

    data = response.json()
    
    return data