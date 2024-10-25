1. jsp를 통해 py파일로 데이터 값 전달 요청 (구현)
데이터 요청 : api-key, 캐릭터 명, 날짜, count, 스타포스?큐브?잠재설정?

2. 전달 받은 값을 통해 python으로 API 요청 후 Json 파일로 변환

3. Json 파일로 변환한 것을 java controller를 사용하여 ajax로 값을 jsp에 전달 받고 출력

------------------------------------------------------------------------------------------

1. API 호출: Python을 사용하여 외부 API를 호출하고 데이터를 받아오기 (python)

2. 데이터 가공: 받아온 데이터를 필요한 형태로 가공하기 (python)

3. 데이터베이스 관리: 가공한 데이터를 데이터베이스에 저장

4. Java Controller 생성 (DB를 활용하여 data를 java controller에 보내는 역할)

5. API 제공: Java에서 만든 API를 통해 클라이언트에 데이터를 전송 (Spring Controller)
