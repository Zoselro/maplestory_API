from datetime import datetime, timedelta
import sys
sys.path.append("D:/Project/python/API_Project")

import maplestory_API.Character_Data_cache_async.Character_basic_data as Character_basic_data
import maplestory_API.Character_Data_cache_async.Character_ocid as Character_ocid
import maplestory_API.Character_Data_cache_async.fetch_dojang_theseed_ranking_data as fetch_dojang_theseed_ranking_data
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
import asyncio
import maplestory_API.Character_Data_cache_async.Main_Character_Serach as Main_Character_Serach
import maplestory_API.Character_Data_cache_async.Character_Stat as Character_Stat
import maplestory_API.Character_Data_cache_async.Character_list_data as Character_list_data
import maplestory_API.enforce_Data.async_cube_data as async_cube_data


api_key = "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"   
character_name = "리마" #대 소문자를 구분지어야 된다.
world_name = "리부트"
difficulty = "1"
job = "팬텀-전체 전직"
page = "1"
start_date = datetime(2023, 12, 22)
end_date = datetime.now() - timedelta(days=1)

character_data = Character_basic_data.get_character_data(character_name, api_key, end_date.strftime('%Y-%m-%d')) # 캐릭터 기본 정보 조회
character_nickname = character_data.get('character_name') #json에서 character_name 만 추출
ocid = Character_ocid.character_ocid(character_nickname, Character_utility.headers_data(api_key))
main_Character_nickname = Main_Character_Serach.Union_Character_list(api_key, ocid, end_date.strftime('%Y-%m-%d'))
character_stat = Character_Stat.get_character_stat(character_name, api_key, end_date.strftime('%Y-%m-%d'))
character_list = Character_list_data.get_character_list(api_key)
cnt_red, cnt_black, cnt_editional, cnt_white_editional = asyncio.run(async_cube_data.get_cube_list(api_key))

if ocid is None:
    print("ocid is None")
    sys.exit()
try:
    max_dojang_floor, max_theseed_floor = asyncio.run(fetch_dojang_theseed_ranking_data.fetch_all_data(world_name, ocid, page, api_key, start_date, end_date, difficulty, job))
    print(f"{character_name} 의 가장 높은 무릉 층수: {max_dojang_floor}")
    print(f"{character_name} 의 가장 높은 더시드 층수: {max_theseed_floor}")
    print('큐브 돌린 횟수는 ','레드 : ' ,cnt_red,'블랙 : ' ,cnt_black,'에디셔널 : ' ,cnt_editional,'화에큐 : ' ,cnt_white_editional)
except Exception as e:
    print(f"An error occurred : {e}")
finally:
    print("This will always execute.")
