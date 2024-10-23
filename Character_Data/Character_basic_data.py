import requests
from datetime import datetime, timedelta
import json

#캐릭터 기본정보 알아내기
def get_character_data(characterName,api_key):
    #json 파일 초기화
    file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_data.json'
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
    
    headers = {
        "x-nxopen-api-key": api_key
    }
    #캐릭터명의 ocid 알아내기
    characterName = "리마"
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + characterName
    response = requests.get(urlString, headers = headers)
    ocid = response.json()['ocid']

    #내 캐릭터의 정보
    new_time = datetime.now() - timedelta(days=1)
    formatted_new_time = new_time.strftime('%Y-%m-%d')
    urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid + "&date=" + formatted_new_time
    response = requests.get(urlString, headers = headers)
    
    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    
    return response.json()