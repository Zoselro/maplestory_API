import sys
sys.path.append("D:/Project/python/API_Project")
from datetime import datetime, timedelta

import aiohttp
import asyncio
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

file_path = r'D:\Project\python\Character_Data_json\maplestory_api_cube_data'
file_path_type = '.json'
cache = {}
errorNum = 0

async def fetch_cube_data(session, api_key, date, retries=5, backoff_factor=1):
    global errorNum
    
    cache_key = (api_key, date)
    if cache_key in cache:
        return cache[cache_key]
    urlString = f"https://open.api.nexon.com/maplestory/v1/history/cube?count=1000&date={date.strftime('%Y-%m-%d')}&x-nxopen-api-key={api_key}"
    headers = Character_utility.headers_data(api_key)
    
    for attempt in range(retries):
        async with session.get(urlString, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                cache[cache_key] = data
                return data
            
            elif response.status == 429:
                # Too Many Requests, 일정 시간 후에 다시 시도
                wait_time = backoff_factor * (2 ** attempt)  # 지수 백오프
                print(f"cube is Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
                await asyncio.sleep(wait_time)
            elif response.status == 400:
                print("cube is Bad Request: Check the request parameters.")
            elif response.status == 403:
                print("cube is Forbidden: Access is denied.")
            elif response.status == 500:
                print("cube is Internal Server Error: Something went wrong on the server.")
            else:
                # 다른 에러 처리
                print(f"Error {response.status}: {await response.text()}")
                break  # 다른 에러 발생 시 루프 탈출
        errorNum += 1
        print(f"Failed to fetch data for {date} after {retries} attempts.{errorNum}")
        return None  # 모든 재시도 후에도 실패한 경우

async def get_cube_list(api_key, date_value=datetime(2022, 11, 25), end_date=datetime.now() - timedelta(days=1)):
    if date_value > end_date:
        raise ValueError("시작 날짜가 종료 날짜보다 뒤에 있습니다.")
    cache.clear()
    #Character_utility.initialize_json_file(file_path)
    
    cube_list = []
    cnt_red = 0
    cnt_black = 0
    cnt_white_editional = 0
    cnt_editional = 0

    async with aiohttp.ClientSession() as session:
        tasks = []
        current_date = date_value
        while current_date <= end_date:
            tasks.append(fetch_cube_data(session, api_key, current_date))
            current_date += timedelta(days=1)
        
        # 모든 날짜에 대한 비동기 요청 실행
        responses = await asyncio.gather(*tasks)
        
        # 응답 데이터 처리
        for data in responses:
            if data:
                for cube_data in data.get('cube_history', []):
                    if cube_data['cube_type'] == '레드 큐브':
                        cube_list.append(cube_data)
                        cnt_red += 1
                    elif cube_data['cube_type'] in ['블랙 큐브', '카르마 블랙 큐브']:
                        cube_list.append(cube_data)
                        cnt_black += 1
                    elif cube_data['cube_type'] in ['카르마 화이트 에디셔널 큐브', '화이트 에디셔널 큐브']:
                        cube_list.append(cube_data)
                        cnt_white_editional += 1
                    elif cube_data['cube_type'] == '에디셔널 큐브':
                        cube_list.append(cube_data)
                        cnt_editional += 1
    
    # JSON 파일로 저장
    Character_utility.file_mode(file_path + f'_{api_key}' + file_path_type, cube_list, 'w')
    
    return cnt_red, cnt_black, cnt_editional, cnt_white_editional
    