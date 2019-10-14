# second_session
# 네이버 웹툰 베댓

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# webdriver 설정
browser = webdriver.Chrome('./chrome/chromedriver.exe')

# 크롬 브라우저 대기 - 사양 고려
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
my_webtoon = 'https://comic.naver.com/webtoon/list.nhn?titleId=695796&weekday=sun'
browser.get(my_webtoon)
time.sleep(3)

# 링크 저장
baseurl = 'https://comic.naver.com'
soup = BeautifulSoup(browser.page_source, "html.parser")
links = soup.select("td.title > a")
print(links)
next_url=[]
for link in links:
    next_url.append(baseurl + link['href'])
print(next_url)

# 댓글 출력
def print_reple(reples):
    for reple in reples:
        try:
            print('-' + reple.select_one('span.u_cbox_contents').text.strip())
        except:
            pass

#각 화에 들어가서 댓글들 추출
for url in next_url:

    # 몇 화인지 프린트
    start_index = int(url.index('no')) + 3
    last_index = int(url.rindex('&'))
    print(url[start_index : last_index] + '화 베댓 추출')

    #링크 이동 후 댓글 프레임 가져오기
    browser.get(url)
    time.sleep(5)
    browser.switch_to.frame('commentIframe')
    soup = BeautifulSoup(browser.page_source, "html.parser")

    #댓글들 추출, 댓글출력call
    reples = soup.select('div.u_cbox_text_wrap')
    print_reple(reples)
    print('-------------------------------')

    
