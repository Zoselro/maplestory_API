from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome 옵션 설정
chrome_options = Options()

service = Service('C:\Program Files\Google\Chrome\Application\chrome.exe')  # chromedriver의 경로 입력
# ChromeDriver 실행
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(3)

# 로그인 페이지 열기
driver.get("https://m.ticketlink.co.kr/home")

# 사용자명과 비밀번호 입력 (여기서는 예시로 "username"과 "password"를 사용)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("your_username")
password.send_keys("your_password")
password.send_keys(Keys.RETURN)  # 로그인 버튼 클릭

# 로그인 후 충분히 기다리기
time.sleep(5)

# 로그인 후 페이지 작업
driver.get("https://example.com/after_login_page")