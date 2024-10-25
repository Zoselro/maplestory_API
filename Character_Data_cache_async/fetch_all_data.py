import headers_data
import json
import aiohttp
import asyncio
import json_file_clear
from datetime import datetime, timedelta

# API 캐시를 위한 딕셔너리
cache = {}

# JSON 파일 경로
theseed_file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_theseed2_data.json'
dojang_file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_dojang2_data.json'
# 더시드 데이터를 비동기 방식으로 가져오는 함수
async def get_character_theseed_async(session, world_name, ocid, page_num, api_key, date_value, retries=5, backoff_factor=1):
    json_file_clear.initialize_json_file(theseed_file_path)
    json_file_clear.initialize_json_file(dojang_file_path)
    cache_key = (world_name, ocid, date_value)
    if cache_key in cache:
        return cache[cache_key]
    
    urlString = f"https://open.api.nexon.com/maplestory/v1/ranking/theseed?date={date_value}&world_name={world_name}&ocid={ocid}&page={page_num}"
    headers = headers_data.headers_data(api_key)
    
    for attempt in range(retries):
        async with session.get(urlString, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                cache[cache_key] = data
                return data
            
            elif response.status == 429:
                # Too Many Requests, 일정 시간 후에 다시 시도
                wait_time = backoff_factor * (2 ** attempt)  # 지수 백오프
                print(f"theseed is Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
                await asyncio.sleep(wait_time)
            elif response.status == 400:
                print("theseed is Bad Request: Check the request parameters.")
            elif response.status == 403:
                print("theseed is Forbidden: Access is denied.")
            elif response.status == 500:
                print("theseed is Internal Server Error: Something went wrong on the server.")  
            else:
                # 다른 에러 처리
                print(f"Error {response.status}: {await response.text()}")
                break  # 다른 에러 발생 시 루프 탈출
    return None  # 모든 재시도 후에도 실패한 경우



# 무릉도장 데이터를 비동기 방식으로 가져오는 함수
async def get_character_dojang_async(session, world_name, difficulty, job, ocid, page_num, api_key, date_value, retries=5, backoff_factor=1):
    json_file_clear.initialize_json_file(dojang_file_path)
    cache_key = (world_name, ocid, difficulty, job, date_value)
    if cache_key in cache:
        return cache[cache_key]
    
    urlString = f"https://open.api.nexon.com/maplestory/v1/ranking/dojang?date={date_value}&world_name={world_name}&difficulty={difficulty}&class={job}&ocid={ocid}&page={page_num}"
    headers = headers_data.headers_data(api_key)
    
    for attempt in range(retries):
        async with session.get(urlString, headers=headers) as response:    
            if response.status == 200:
                data = await response.json()
                cache[cache_key] = data
                return data
            
            elif response.status == 429:
                # Too Many Requests, 일정 시간 후에 다시 시도
                wait_time = backoff_factor * (2 ** attempt)  # 지수 백오프
                print(f"dojang is Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
                await asyncio.sleep(wait_time)
            elif response.status == 400:
                print("dojang is Bad Request: Check the request parameters.")
            elif response.status == 403:
                print("dojang is Forbidden: Access is denied.")
            elif response.status == 500:
                print("dojang is Internal Server Error: Something went wrong on the server.")  
            else:
                # 다른 에러 처리
                print(f"Error {response.status}: {await response.text()}")
                break  # 다른 에러 발생 시 루프 탈출
    return None  # 모든 재시도 후에도 실패한 경우

# 전체 데이터 수집 작업을 비동기 방식으로 실행
async def fetch_all_data(world_name, ocid, page_num, api_key, start_date, end_date, difficulty, job):
    max_dojang_floor = 0
    max_theseed_floor = 0

    async with aiohttp.ClientSession() as session:
        tasks_dojang = []
        tasks_theseed = []
        data_all_dojang = []
        data_all_theseed = []
        current_date = start_date

        # 날짜별로 비동기 처리할 API 호출을 준비
        while current_date <= end_date:
            date_value = current_date.strftime('%Y-%m-%d')
            tasks_dojang.append(get_character_dojang_async(session, world_name, difficulty, job, ocid, page_num, api_key, date_value))
            tasks_theseed.append(get_character_theseed_async(session, world_name, ocid, page_num, api_key, date_value))
            current_date += timedelta(days=1)
        # 비동기로 API 호출 처리
        dojang_results = await asyncio.gather(*tasks_dojang)
        theseed_results = await asyncio.gather(*tasks_theseed)
        
        # 무릉도장 데이터 처리
        for dojang_data in dojang_results:
            if dojang_data:
                for entry_dojang in dojang_data.get('ranking'):
                    # 가장 높은 무릉 층수 갱신
                    if entry_dojang['dojang_floor']:
                        if entry_dojang['dojang_floor'] > max_dojang_floor:
                            data_all_dojang.append(entry_dojang)
                            max_dojang_floor = entry_dojang['dojang_floor']
                    
    # 데이터 저장
    with open(dojang_file_path, 'a', encoding='utf-8') as json_file:
        json.dump(list(data_all_dojang), json_file, ensure_ascii=False, indent=4)
        json_file.write('\n')

        # 더시드 데이터 처리
        for theseed_data in theseed_results:
            if theseed_data:
                for entry_theseed in theseed_data.get('ranking'):
                    # 가장 높은 더시드 층수 갱신
                    if entry_theseed['theseed_floor']:
                        data_all_theseed.append(entry_theseed)
                        if entry_theseed['theseed_floor'] > max_theseed_floor:
                            max_theseed_floor = entry_theseed['theseed_floor']
                    
    # 데이터 저장
    with open(theseed_file_path, 'a', encoding='utf-8') as json_file:
        json.dump(list(data_all_theseed), json_file, ensure_ascii=False, indent=4)
        json_file.write('\n')
                            
    return max_dojang_floor, max_theseed_floor