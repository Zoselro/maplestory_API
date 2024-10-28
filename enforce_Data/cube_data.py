import requests
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
from datetime import datetime, timedelta
import asyncio
import aiohttp

file_path = r'D:\Project\python\Character_Data_json\maplestory_api_cube_data.json'

def get_cube_list(api_key, start_date, end_date):
    # 문자열을 datetime 객체로 변환
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    current_date = start_date
    cube_data_count_list = []
    cnt_red = 0
    cnt_black = 0
    cnt_white_editional = 0
    cnt_editional = 0
    
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        urlString = f"https://open.api.nexon.com/maplestory/v1/history/cube?x-nxopen-api-key={api_key}&count=1000&date={date_str}"
        headers = Character_utility.headers_data(api_key)
        response = requests.get(urlString, headers=headers, timeout=30)
        cube_data = response.json().get('cube_history')
        for cube_data_count in cube_data:
            if(cube_data_count['cube_type'] == '레드 큐브'):
                cube_data_count_list.append(cube_data_count)
                cnt_red += 1
            elif(cube_data_count['cube_type'] == '블랙 큐브'):
                cube_data_count_list.append(cube_data_count)
                cnt_black += 1
            elif(cube_data_count['cube_type'] == '카르마 화이트 에디셔널 큐브') or cube_data_count['cube_type'] == '화이트 에디셔널 큐브':
                cube_data_count_list.append(cube_data_count)
                cnt_white_editional += 1
            elif(cube_data_count['cube_type'] == '에디셔널 큐브'):
                cube_data_count_list.append(cube_data_count)
                cnt_editional += 1
        current_date += timedelta(days=1)
    Character_utility.file_mode(file_path, cube_data_count_list, 'w+')
    return cube_data, cnt_red, cnt_black, cnt_editional, cnt_white_editional
