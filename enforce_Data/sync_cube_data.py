import sys
sys.path.append("D:/Project/python/API_Project")

import requests
import json
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
from datetime import datetime, timedelta

file_path = r'D:\Project\python\Character_Data_json\maplestory_api_cube_data.json'
def get_cube_list(api_key,date_value = datetime(2022, 11, 25), end_date = datetime.now()-timedelta(days = 1)):
    if date_value > end_date:
        raise ValueError("시작 날짜가 종료 날짜보다 뒤에 있습니다.")
    
    Character_utility.initialize_json_file(file_path)
    headers = Character_utility.headers_data(api_key)
    one_day = date_value
    cube_list = []
    cnt_red = 0
    cnt_black = 0
    cnt_white_editional = 0
    cnt_editional = 0
    
    while one_day <= end_date:
        urlString = f"https://open.api.nexon.com/maplestory/v1/history/cube?x-nxopen-api-key={api_key}&count=1000&date={one_day.strftime('%Y-%m-%d')}"
        
        try:
            response = requests.get(urlString, headers = headers)
            if response.status_code == 200:    
                data = response.json()
            else:
                print(f"Error {response.status_code}: {response.text}")
                continue
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue
        
        for cube_data in data.get('cube_history'):
            if(cube_data['cube_type'] == '레드 큐브'):
                cube_list.append(cube_data)
                cnt_red += 1
            elif(cube_data['cube_type'] == '블랙 큐브'):
                cube_list.append(cube_data)
                cnt_black += 1
            elif(cube_data['cube_type'] == '카르마 화이트 에디셔널 큐브') or cube_data['cube_type'] == '화이트 에디셔널 큐브':
                cube_list.append(cube_data)
                cnt_white_editional += 1
            elif(cube_data['cube_type'] == '에디셔널 큐브'):
                cube_list.append(cube_data)
                cnt_editional += 1
        one_day += timedelta(days=1)
    Character_utility.file_mode(file_path, cube_list, 'a+')
    
    return cube_list,cnt_red, cnt_black, cnt_editional, cnt_white_editional