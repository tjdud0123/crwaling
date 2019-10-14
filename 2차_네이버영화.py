# second_session
# 네이버 영화

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#검색어받기
query = str(input('검색어를 입력하세요 : '))
    
# webdriver 설정
browser = webdriver.Chrome('./chrome/chromedriver.exe')

# 크롬 브라우저 대기 - 사양 고려
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get('https://movie.naver.com/')

# 검색창 input 선택
element = browser.find_element_by_css_selector('input#ipt_tx_srch')

# 검색어 입력
element.send_keys(query)

# 검색클릭
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn_srch'))).click()

#기다려주기
time.sleep(3)

# 검색클릭
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li:nth-child(1) > dl > dt > a'))).click()

# soup 초기화
soup = BeautifulSoup(browser.page_source, "html.parser")

# 평점 출력
net_score = soup.select_one('div.netizen_score div.sc_view em').text.strip()
print('네티즌, 관람객 평점 : ' + net_score)

spe_score = soup.select_one('div.special_score div.sc_view em').text.strip()
print('기자, 평론가 평점 : ' + spe_score)

#리뷰 출력
review_list = soup.select('div.obj_section:nth-child(5) div.score_reple')
print('<리뷰>')
for i, review in enumerate(review_list, 1):
    reple = review.select_one('p').text.strip()
    print(str(i) + '. ' + reple)
browser.quit()
