import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import easyocr
from selenium.webdriver.common.action_chains import ActionChains
import time


# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("profile-directory=Profile 3")  # 사용하려는 프로필 이름

# ChromeDriver 경로 설정
service = Service(r'D:\python\maplestory_API\chromedriver\chromedriver.exe')

# driver 생성
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_window_size(1900, 1000)
driver.implicitly_wait(3)

# 로그인 페이지 열기
driver.get("https://id.payco.com/oauth2.0/authorize?serviceProviderCode=TKLINK&scope=&response_type=code&state=9720f41a8ff646a8880183daed05f03a&client_id=Z9Ur2WLH9rB59Gy4_cJ3&redirect_uri=https://m.ticketlink.co.kr/auth/callback?selfRedirect=N&userLocale=ko_KR")

userId = driver.find_element(By.ID, 'id')
userId.send_keys('zoselro0328@gmail.com')

userPwd = driver.find_element(By.ID, "pw")
userPwd.send_keys('rhsmok3524@')
userPwd.send_keys(Keys.ENTER)

driver.get("https://www.ticketlink.co.kr/reserve/plan/schedule/1701922691?menuIndex=reserve")

# 부정예매방지문자 OCR 생성
reader = easyocr.Reader(['en'])

# 부정예매방지 문자 이미지 요소 선택
capchaPng = driver.find_element(By.XPATH,'//*[@id="captcha_img"]')


# 부정예매방지문자 입력
result = reader.readtext(capchaPng.screenshot_as_png, detail=0)
capchaValue = result[0].replace(' ', '').replace('5', 'S').replace('0', 'O').replace('$', 'S').replace(',', '')\
    .replace(':', '').replace('.', '').replace('+', 'T').replace("'", '').replace('`', '')\
    .replace('1', 'L').replace('e', 'Q').replace('3', 'S').replace('€', 'C').replace('{', '').replace('-', '')
    
# 입력
#driver.find_element(By.XPATH,'//*[@id="divRecaptcha"]/div[1]/div[3]').click()
chapchaText = driver.find_element(By.XPATH,'//*[@id="ipt_captcha"]')
chapchaText.send_keys(capchaValue)
        
#입력완료 버튼 클릭
driver.find_element(By.XPATH, '//button[@class="btn btn_full"]').click()


# 오류 메시지가 나타나는지 확인
try:
    # 오류 메시지가 나타날 때 .bx_input_txt에 error 클래스가 추가되므로, 이 클래스를 가진 요소 확인
    error_element = driver.find_element(By.CSS_SELECTOR, ".bx_input_txt.error .txt_error")

    # 오류 메시지 텍스트 확인
    if "정확하게 입력해주세요" in error_element.text:
        print("보안문자 다시 입력")

except Exception as e:
    print("오류 메시지 없음.")  # 해당 요소가 없으면 메시지 없음
    # 좌석 정보 가져오기
    seats_info = driver.execute_script("return tk.state.plan.seatMap;")
    seats_sold = driver.execute_script("return tk.state.plan.seatSoldMap;")



    # while(True):
    #     for seat, is_sold in seats_sold.items():
    #         if not is_sold:
    #             seat_available = True
    #             print(f"Available seat found: {seat}")
    #             print("Seat position:", seats_info[seat]["position"])
                
    #             # 좌석의 좌표를 가져오기
    #             seat_position = seats_info[seat]["position"]
                
    #             # 캔버스 요소 가져오기
    #             canvas = driver.find_element(By.TAG_NAME, "canvas")
                
    #             rect = canvas.rect  # 캔버스의 위치와 크기 (좌표는 `rect`로 가져옵니다)
                
    #             # 캔버스의 실제 크기
    #             canvas_width = rect['width']
    #             canvas_height = rect['height']
                
    #             # 좌석 좌표를 캔버스의 상대적 좌표로 변환
    #             x = (seat_position['x'] - rect['x']) * (canvas_width / rect['width'])
    #             y = (seat_position['y'] - rect['y']) * (canvas_height / rect['height'])
                
    #             # 클릭 이벤트 생성
    #             actions = ActionChains(driver)
    #             actions.move_to_element_with_offset(canvas, x, y).click().perform()
    #             print(f"Simulated click at position: ({x}, {y})")
    #             break
        
    #     if seat_available:
    #         print("Seat available. Exiting loop.")
    #         break
    #     else:
    #         print("No seats available. Refreshing...")
            
    #         # 상태 초기화 실행 (JavaScript 함수 실행)
    #         driver.execute_script("""
    #             tk.state.waitingDetail.startLoading('refresh');
    #             tk.state.select.clearSelectedSeats();
    #             tk.state.view.clearSelectedSeats();
    #             tk.event.service.signals.updateAliveGrade.dispatch();
    #             tk.event.service.signals.updateSeatWaitingLinked.dispatch();
    #             tk.event.service.signals.updateReservationSeatData.dispatch();
    #             tk.event.service.signals.updateReservationData.dispatch();
    #             tk.state.waitingDetail.endLoading('refresh');
    #         """)

# 프로그램이 종료되지 않도록 대기
input("종료하려면 Enter 키를 누르세요...")