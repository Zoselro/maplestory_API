from flask import Flask, request, render_template, send_file
import asyncio
import maplestory_API.enforce_Data.async_cube_data as async_cube_data
import maplestory_API.Character_Data_cache_async.Character_utility as Character_utility
import maplestory_API.Character_Data_cache_async.Character_list_data as Character_list_data
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cube_data.html')  # cube_data.html 페이지 렌더링

@app.route('/get_cube_data', methods=['POST'])
def get_cube_data():
    api_key = request.form.get('api_key')

    if not api_key.isascii():
        return "API key는 ASCII 문자만 허용됩니다.", 400
    
    validation_api_key = Character_list_data.get_character_list(api_key)
    #print("Validation : ",validation_api_key) # 캐릭터 목록 조회
    
    if not api_key:
        return "API key is required.", 400  # 오류 발생 시 메시지 반환
    elif validation_api_key is None:
        return "API key is None", 400
    else:
        try:
            # 큐브 데이터 조회
            cnt_red, cnt_black, cnt_editional, cnt_white_editional = asyncio.run(async_cube_data.get_cube_list(api_key))

            # 결과를 HTML 형식으로 반환
            return f"""
            <h3>Cube Data Results:</h3>
            <p>Red Cube Count: {cnt_red}</p>
            <p>Black Cube Count: {cnt_black}</p>
            <p>Additional Cube Count: {cnt_editional}</p>
            <p>White Additional Cube Count: {cnt_white_editional}</p>
            <form action="/download_cube_data" method="get">
                <input type="hidden" name="api_key" value="{api_key}">
                <input type="submit" value="Download Cube Data as JSON">
            </form>
            """

        except Exception as e:
            # 예외 발생 시 에러 메시지 반환
            return f"An error occurred: {e}", 500

@app.route('/download_cube_data', methods=['GET'])
def download_cube_data():
    api_key = request.args.get('api_key')
    if not api_key:
        return "API key is required.", 400

    try:
        # 파일 전송
        return send_file('D:\Project\python\Character_Data_json\maplestory_api_cube_data.json', as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)