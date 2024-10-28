import requests
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

file_path = r'D:\Project\python\Character_Data_json\character_ocid_data.json'
def character_ocid(character_name,headers):
    if character_name is None:  # character_name이 None이면 함수 종료
        print("character_name is None")
        return None
    
    #Character_utility.initialize_json_file(file_path)
    urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + character_name
    response = requests.get(urlString, headers = headers, timeout=30)
    ocid = Character_utility.response_ocid(response)
        
    Character_utility.file_mode(file_path, response.json(), 'w+')
    
    return ocid