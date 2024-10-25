import Character_basic_data
import Character_ocid
import fetch_dojang_theseed_ranking_data
import headers_data
from datetime import datetime, timedelta
import asyncio

# 메인 함수
api_key = "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
character_name = "끄롱"
world_name = ""#"리부트123123"
difficulty = "1"
job = "모험가-전체 전직"
page = "1"
start_date = datetime(2023, 12, 22)
end_date = datetime.now()

# 캐릭터 기본 정보 조회
character_data = Character_basic_data.get_character_data(character_name, api_key, start_date.strftime('%Y-%m-%d'))
character_nickname = character_data.get('character_name')
ocid = Character_ocid.character_ocid(character_nickname, headers_data.headers_data(api_key))
max_dojang_floor, max_theseed_floor = asyncio.run(fetch_dojang_theseed_ranking_data.fetch_all_data(world_name, ocid, page, api_key, start_date, end_date, difficulty, job))

print(f"{character_name} 의 가장 높은 무릉 층수: {max_dojang_floor}")
print(f"{character_name} 의 가장 높은 더시드 층수: {max_theseed_floor}")
