import requests
from datetime import datetime, timedelta
import json
import headers_data
import json_file_clear

file_path = r'D:\Project\python\Character_Data_json\Union_character_List.json'

def Union_Character_list(api_key, ocid, date_value):
    json_file_clear.initialize_json_file(file_path)
    
    headers = headers_data.headers_data(api_key)
    urlString = f"https://open.api.nexon.com/maplestory/v1/user/union-raider?ocid={ocid}&date={date_value}"
    print(urlString)
    response = requests.get(urlString, headers = headers)

    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)

    data = response.json()
    
    print(data)
    
    return data