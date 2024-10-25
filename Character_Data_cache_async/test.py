from flask import Flask, request, g

app = Flask(__name__)

@app.route('/test.jsp', methods=['POST'])
def fetch_data():
    g.character_name = request.json.get('character_name')
    g.world_name = request.json.get('world_name')
    g.difficulty = request.json.get('difficulty')
    g.job = request.json.get('job')

    # g를 통해 데이터 사용
    return {"status": "success"}, 200

def main():
    # Flask 애플리케이션과는 별개로 함수를 호출할 경우
    # 요청이 발생하기 전에 이 함수가 호출되어야 합니다.
    print(f"Character Name: {g.character_name}")
    print(f"World Name: {g.world_name}")
    print(f"Difficulty: {g.difficulty}")
    print(f"Job: {g.job}")

if __name__ == '__main__':
    app.run(debug=True)