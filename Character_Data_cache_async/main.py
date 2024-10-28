import Character_basic_data
import Character_ocid
import fetch_dojang_theseed_ranking_data
from datetime import datetime, timedelta
import Character_utility
import asyncio
import sys
import Union_Character_List

api_key = "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
character_name = "팬슈" #대 소문자를 구분지어야 된다.
world_name = "리부트"
difficulty = "1"
job = "팬텀-전체 전직"
page = "1"
start_date = datetime(2023, 12, 22)
end_date = datetime.now() - timedelta(days=1)

# 캐릭터 기본 정보 조회(현재 기준)
character_data = Character_basic_data.get_character_data(character_name, api_key, end_date.strftime('%Y-%m-%d'))
character_nickname = character_data.get('character_name')
ocid = Character_ocid.character_ocid(character_nickname, Character_utility.headers_data(api_key))
Union_Character_List.Union_Character_list(api_key, ocid, end_date.strftime('%Y-%m-%d'))

if ocid is None:
    print("ocid is None")
    sys.exit()
try:
    max_dojang_floor, max_theseed_floor = asyncio.run(fetch_dojang_theseed_ranking_data.fetch_all_data(world_name, ocid, page, api_key, start_date, end_date, difficulty, job))
    print(f"{character_name} 의 가장 높은 무릉 층수: {max_dojang_floor}")
    print(f"{character_name} 의 가장 높은 더시드 층수: {max_theseed_floor}")
except Exception as e:
    print(f"An error occurred : {e}")
finally:
    print("This will always execute.")
