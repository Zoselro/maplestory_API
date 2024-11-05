from datetime import datetime, timedelta
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
import requests
file_path = r'D:\Project\python\Character_Data_json\cube_data.json'
api_key = 'test_454c2b1ff9fd60b4ab2ee265c9f236baf2e7f5b4b6c4da1b3f334d882436e97defe8d04e6d233bd35cf2fabdeb93fb0d'
cursor = '49d7f60b87e603cf65b9c756d103d8a7fd842dab14be2a956555625b37c97bff'
urlString = f"https://open.api.nexon.com/maplestory/v1/history/potential?count=1000&cursor={cursor}"

headers = Character_utility.headers_data(api_key)

response = requests.get(urlString, headers = headers, timeout=30)
data = response.json()

Character_utility.file_mode(file_path, data, 'w+')