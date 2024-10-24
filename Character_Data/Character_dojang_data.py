import requests
import json
import headers_data
#캐릭터가 2023년 12월 22일부터 datetime.now() 까지 무릉도장 기록이 있는 것만 조회 한 후 가장 높은 층수를 기록하고 있는 데이터를 json 데이터 출력 후 json에 저장

file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_dojang_data.json'    
def get_character_dojang(world_name, difficulty, job, ocid, page_num, api_key, date_value):
    
    headers = headers_data.headers_data(api_key)
    urlString = f"https://open.api.nexon.com/maplestory/v1/ranking/dojang?date={date_value}&world_name={world_name}&difficulty={difficulty}&class={job}&ocid={ocid}&page={page_num}"
    response = requests.get(urlString, headers = headers)
    
    data = response.json()
    data_value = data.get('ranking')
    data_all = []
    
    for data_cache in data_value:
        if(data_cache['date']):
            #print(data_cache['date'])
            data_all.append(data_cache)
            with open(file_path, 'a', encoding='utf-8') as json_file:
                json.dump(data_all, json_file, ensure_ascii=False, indent=4)
                json_file.write('\n')
            return data_all