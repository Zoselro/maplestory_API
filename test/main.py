from flask import Flask, request, render_template
from datetime import datetime, timedelta
import maplestory_API.Character_Data_cache_async.Character_basic_data as Character_basic_data
import maplestory_API.Character_Data_cache_async.Character_ocid as Character_ocid
import maplestory_API.Character_Data_cache_async.fetch_dojang_theseed_ranking_data as fetch_dojang_theseed_ranking_data
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
import asyncio
import maplestory_API.Character_Data_cache_async.Main_Character_Serach as Main_Character_Serach
import maplestory_API.Character_Data_cache_async.Character_Stat as Character_Stat
import maplestory_API.Character_Data_cache_async.Character_list_data as Character_list_data
import maplestory_API.enforce_Data.async_cube_data as async_cube_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # HTML 폼에서 전달된 데이터 가져오기
    character_name = request.form['character_name']
    api_key = request.form['api_key']
    difficulty = request.form['difficulty']
    job = request.form['job']
    world_name = request.form['world_name']
    page = request.form['page']
    
    # 현재 날짜로부터 1일 전까지의 날짜 설정
    start_date = datetime(2023, 12, 22)
    end_date = datetime.now() - timedelta(days=1)

    try:
        # Character Data 조회 로직
        character_data = Character_basic_data.get_character_data(character_name, api_key, end_date.strftime('%Y-%m-%d'))
        character_nickname = character_data.get('character_name')
        ocid = Character_ocid.character_ocid(character_nickname, Character_utility.headers_data(api_key))

        if ocid is None:
            return "Error: ocid is None"

        main_Character_nickname = Main_Character_Serach.Union_Character_list(api_key, ocid, end_date.strftime('%Y-%m-%d'))
        character_stat = Character_Stat.get_character_stat(character_name, api_key, end_date.strftime('%Y-%m-%d'))
        character_list = Character_list_data.get_character_list(api_key)
        cube_all_data, cnt_red, cnt_black, cnt_editional, cnt_white_editional = asyncio.run(async_cube_data.get_cube_list(api_key))

        max_dojang_floor, max_theseed_floor = asyncio.run(
            fetch_dojang_theseed_ranking_data.fetch_all_data(
                world_name, ocid, page, api_key, start_date, end_date, difficulty, job
            )
        )

        # 결과 출력
        return f"""
        <p>{character_name} 의 가장 높은 무릉 층수: {max_dojang_floor}</p>
        <p>{character_name} 의 가장 높은 더시드 층수: {max_theseed_floor}</p>
        <p>큐브 돌린 횟수는 레드 : {cnt_red}, 블랙 : {cnt_black}, 에디셔널 : {cnt_editional}, 화에큐 : {cnt_white_editional}</p>
        """
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)    