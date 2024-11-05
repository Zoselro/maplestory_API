import requests
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility

#본인이 갖고있는 캐릭터 list
file_path = r'D:\Project\python\Character_Data_json\maplestory_api_Character_list.json'
def get_character_list(api_key):
    headers = Character_utility.headers_data(api_key)
    urlString = f"https://open.api.nexon.com/maplestory/v1/character/list?x-nxopen-api-key={api_key}"
    response = requests.get(urlString, headers = headers, timeout=30)
    max_level = 0
    character_list = []
    
    
    #레벨이 가장 높은 캐릭터의 월드 뽑고 난 후, 그 월드에 있는 캐릭터 list 뽑기
    if response.status_code == 200:
        for data in response.json()['account_list']:
            for data_character_list in data['character_list']:
                if data_character_list['character_level'] > max_level:
                    max_level = data_character_list['character_level']
                    world_name = data_character_list['world_name'] #레벨이 가장 높은 월드 추출
        
        for data_character in response.json()['account_list']:
            for data_character_world in data_character['character_list']:
                if data_character_world['world_name'] == world_name:
                    character_list.append(data_character_world) # 리스트로 추출
        
        Character_utility.file_mode(file_path, character_list, 'w+')
        return character_list
    else:
        return None