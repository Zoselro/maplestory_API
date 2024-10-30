from flask import Flask, request, render_template
import asyncio
import maplestory_API.enforce_Data.async_cube_data as async_cube_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cube_data.html')  # cube_data.html 페이지 렌더링

@app.route('/get_cube_data', methods=['POST'])
def get_cube_data():
    api_key = request.form.get('api_key')

    if not api_key:
        return "API key is required.", 400  # 오류 발생 시 메시지 반환

    try:
        # 큐브 데이터 조회
        cube_all_data, cnt_red, cnt_black, cnt_editional, cnt_white_editional = asyncio.run(async_cube_data.get_cube_list(api_key))

        # 결과를 HTML 형식으로 반환
        return f"""
        <h3>Cube Data Results:</h3>
        <p>Red Cube Count: {cnt_red}</p>
        <p>Black Cube Count: {cnt_black}</p>
        <p>Additional Cube Count: {cnt_editional}</p>
        <p>White Additional Cube Count: {cnt_white_editional}</p>
        """
    except Exception as e:
        # 예외 발생 시 에러 메시지 반환
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)