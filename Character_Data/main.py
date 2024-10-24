import Character_basic_data
import Character_ocid
import Character_dojang_data
import headers_data
import Character_theseed_data

from datetime import datetime, timedelta #파라미터로 날짜를 받기위함

api_key = "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
character_name = "도난"
world_name = "리부트"
difficulty = "1" #통달
job = "팬텀-전체 전직" #직업
page = "1"
date_value = datetime(2023, 12, 22).strftime('%Y-%m-%d')  #2023년 12월 22일날 캐릭터 정보 / 무릉도장 랭킹 조회 #datetime.now().strftime('%Y-%m-%d')


#캐릭터 정보 조회
character_data = Character_basic_data.get_character_data(character_name, api_key, date_value)
#캐릭터 정보중, 닉네임만 조회
character_nickname = character_data.get('character_name')
#캐릭터의 고유값 ocid 조회(ocid를 통해 다양한 정보를 알 수 있다.)
ocid = Character_ocid.character_ocid(character_name, headers_data.headers_data(api_key))

#무릉도장 2023-12-22일자부터 현재까지의 기록을 저장하기 위한 date변수
start_date = datetime(2023, 12, 22)
end_date = datetime.now()
current_date = start_date

max_dojang_floor = 0 #무릉도장 가장 높은 층수
max_theseed_floor = 0 # 더시드 가장 높은 층수
#무릉도장 json 파일 초기화
with open(Character_dojang_data.file_path, 'w', encoding='utf-8') as json_file:
    json_file.write('')
#더 시드 json 파일 초기화
with open(Character_theseed_data.file_path, 'w', encoding='utf-8') as json_file:
    json_file.write('')

while current_date <= end_date:
    date_value = current_date.strftime('%Y-%m-%d')   
     # 각 날짜에 대해 무릉 데이터를 조회 및 저장
    dojang_data = Character_dojang_data.get_character_dojang(world_name, difficulty, job, ocid, page, api_key, date_value)
    theseed_data = Character_theseed_data.get_character_theseed(world_name, ocid, page, api_key, date_value)
    current_date += timedelta(days=1)
    
    if dojang_data:
        for entry_dojang in dojang_data:
            #print(f"날짜: {entry['date']}, 무릉 층수: {entry['dojang_floor']}")
            if entry_dojang['dojang_floor'] > max_dojang_floor:
                max_dojang_floor = entry_dojang['dojang_floor']
    
    if theseed_data:
        for entry_theseed in theseed_data:
            if entry_theseed['theseed_floor'] > max_theseed_floor:
                max_theseed_floor = entry_theseed['theseed_floor']
    
print(f"가장 높은 무릉 층수: {max_dojang_floor}")
print(f"가장 높은 더시드 층수: {max_theseed_floor}")