from datetime import datetime, timedelta
# 날짜 범위 설정
start_date = datetime(2023, 12, 22)
end_date = datetime.now()

i = 0

while start_date <= end_date:
    i += 1
    print(i)
    start_date += timedelta(days=1)