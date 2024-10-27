import requests
import json
import API_Project.maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

file_path = r'D:\Project\python\Character_Data_json\character_ocid_data.json'
def character_ocid(character_name,headers):
    if character_name is None:  # character_name이 None이면 함수 종료
        print("character_name is None")
        return None
    
    Character_utility.initialize_json_file(file_path)
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + character_name
    response = requests.get(urlString, headers = headers, timeout=30)
    if response.status_code == 200:
        ocid = response.json()['ocid']
    elif response.status_code == 400:
        print("Bad Request")
        return None
    elif response.status_code == 403:
        print("Forbidden")
        return None
    elif response.status_code == 429:
        print("too many Requests")
        return None
    elif response.status_code == 500:
        print("Internal Server Error")
        return None

    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    
    return ocid