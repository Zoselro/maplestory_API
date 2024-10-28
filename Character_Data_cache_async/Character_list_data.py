import requests
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

#본인이 갖고있는 캐릭터 list
file_path = r'D:\Project\python\Character_Data_json\maplestory_api_Character_list.json'
def get_character_list(api_key):
    headers = Character_utility.headers_data(api_key)

    urlString = f"https://open.api.nexon.com/maplestory/v1/character/list?x-nxopen-api-key={api_key}"
    response = requests.get(urlString, headers = headers, timeout=30)
    
    Character_utility.file_mode(file_path, response.json(), 'w+')
    return response.json()