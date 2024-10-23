import requests
import json
import Character_ocid
import headers_data

#캐릭터 기본정보 알아내기
def get_character_data(characterName, api_key, date_value):
    #json 파일 초기화
    file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_data.json'
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
    
    headers = headers_data.headers_data(api_key)
    
    #캐릭터명의 ocid 알아내기
    ocid = Character_ocid.character_ocid(characterName,headers)

    #내 캐릭터의 정보
    urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid + "&date=" + date_value
    response = requests.get(urlString, headers = headers)
    
    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    
    return response.json()