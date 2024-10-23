import requests
import json

def character_ocid(character_name,headers):
    file_path = r'D:\Project\python\Character_Data_json\character_ocid_data.json'
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + character_name
    response = requests.get(urlString, headers = headers)
    ocid = response.json()['ocid']
    response = requests.get(urlString, headers = headers)
    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    
    return ocid