import requests
import json
file_path = r'D:\Project\python\Character_Data_json\character_ocid_data.json'
def character_ocid(character_name,headers):
    if character_name is None:  # character_name이 None이면 함수 종료
        print("character_name is None")
        return None
    
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + character_name
    response = requests.get(urlString, headers = headers)
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
    
    response = requests.get(urlString, headers = headers)
    with open(file_path, 'r+', encoding='utf-8') as json_file:
        json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
    
    return ocid