from datetime import datetime, timedelta
# 날짜 범위 설정
start_date = datetime(2023, 12, 22)
end_date = datetime.now()


i = 0

while start_date <= end_date:
    i += 1
    print(i)
    start_date += timedelta(days=1)

a = [5,4,8,1,2]
b = a[0]  # 리스트의 첫 번째 값을 기본값으로 설정

for i in a:
    if b < i:  # b가 i보다 작으면
        b = i  # b에 i 값을 저장

print(b)