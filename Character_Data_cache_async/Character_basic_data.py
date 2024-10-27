import requests
import json
import Character_ocid
import API_Project.maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

#캐릭터 기본정보 알아내기
file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_data.json'
def get_character_data(characterName, api_key, date_value):
    #json 파일 초기화
    Character_utility.initialize_json_file(file_path)
    headers = Character_utility.headers_data(api_key)
    #캐릭터명의 ocid 알아내기
    ocid = Character_ocid.character_ocid(characterName,headers)
    #내 캐릭터의 정보
    urlString = f"https://open.api.nexon.com/maplestory/v1/character/basic?ocid={ocid}&date={date_value}"
    response = requests.get(urlString, headers = headers, timeout=30)
    
    Character_utility.file_mode(file_path, response.json(), 'r+')
    return response.json()