# second_session
# 네이버 지도

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
    
# webdriver 설정
browser = webdriver.Chrome('./chrome/chromedriver.exe')

# 크롬 브라우저 대기 - 사양 고려
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get('https://nid.naver.com/')
time.sleep(3)

# 아이디입력
id_element = browser.find_element_by_css_selector('input#id.int')
id_element.send_keys('tjdud0123')

# 패스워드입력
pw_element = browser.find_element_by_css_selector('input#pw.int')
pw_element.send_keys('dja2533')

# 로그인클릭
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn_global'))).click()

# 자동방지입력, 패스워드입력
time.sleep(5)
pw_element = browser.find_element_by_css_selector('input#pw.int')
pw_element.send_keys('dja2533')

time.sleep(5)
auto_element = browser.find_element_by_css_selector('input#chptcha.int')
string = input('자동방지 문자입력 : ')
auto_element.send_keys(string)

WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.btn_global'))).click()

# 페이지 이동 후 즐겨찾기 클릭
time.sleep(5)
browser.get('https://map.naver.com/')
time.sleep(5)
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.more'))).click()

#골라내기
soup = BeautifulSoup(browser.page_source, "html.parser")
like_list = soup.select('div.srl_box')

print('<내 즐겨찾기>')
for i, like in enumerate(like_list, 1):
    name = like.select_one('a.srl_a').text.strip()
    location = like.select_one('div.srl_d').text.strip()
    print(name)
    print(location)
    print('---------------------------')
