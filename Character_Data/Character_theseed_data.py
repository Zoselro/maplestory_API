import requests
import json
import headers_data

file_path = r'D:\Project\python\Character_Data_json\maplestory_api_character_theseed_data.json'    
def get_character_theseed(world_name, ocid, page_num, api_key, date_value):
    
    headers = headers_data.headers_data(api_key)
    urlString = f"https://open.api.nexon.com/maplestory/v1/ranking/theseed?date={date_value}&world_name={world_name}&ocid={ocid}&page={page_num}"
    response = requests.get(urlString, headers = headers)
    data = response.json()
    
    data_value = data.get('ranking')
    data_all = []
    if(response.status_code == 200):
        for data_cache in data_value:
            if(data_cache['date']):
                #print(data_cache['date'])
                data_all.append(data_cache)
                with open(file_path, 'a', encoding='utf-8') as json_file:
                    json.dump(data_all, json_file, ensure_ascii=False, indent=4)
                    json_file.write('\n')
                return data_all
    elif(response.status_code == 400):
        print("Bad Request")
    elif(response.status_code == 403):
        print("Forbidden")
    elif(response.status_code == 429):
        print("Too Many Requests")
    elif(response.status_code == 500):
        print("Internal Server Error")
    else:
        print("Unknown error")