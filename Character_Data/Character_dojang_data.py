import requests
import json
import headers_data

#캐릭터의 무릉도장 정보 알아내기(마지막으로 쳤던 것)
def get_character_dojang(world_name, difficulty, job, ocid, page_num, api_key, date_value):
    file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_dojang_data.json'
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
    
    headers = headers_data.headers_data(api_key)
    
    urlString = "https://open.api.nexon.com/maplestory/v1/ranking/dojang?date=" + date_value + "&world_name=" + world_name + "&difficulty=" + difficulty + "&class=" + job + "&ocid=" + ocid + "&page=" + page_num
    
    response = requests.get(urlString, headers = headers)
    
    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    
    return response.json()