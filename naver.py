# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class NaverSpider(scrapy.Spider):
    
    #검색어받기
    query = str(input('검색어를 입력하세요 : '))

    # webdriver 설정(Chrome, Firefox 등) --경로설정
    browser = webdriver.Chrome('C:\\Users\\user\\Desktop\\여름_랩실인턴\\python_crawl\\naver100\\naver100\\spiders\\chromedriver.exe')

    # 크롬 브라우저 내부 대기
    browser.implicitly_wait(5)

    # 브라우저 사이즈
    browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

    # 페이지 이동
    browser.get('https://terms.naver.com')

    # 검색창 input 선택
    element = browser.find_element_by_css_selector('input#term_query')

    # 검색어 입력
    element.send_keys(query)

    # 검색(Form Submit)
    element.submit()

    #클릭
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content > div:nth-child(3) > div.more_link > a'))).click()


    name = 'naver'
    allowed_domains = ['terms.naver.com']
    currentUrl = browser.current_url
    print('>>>>>>>>>>>>>>>>')
    print(currentUrl)
    start_urls = [currentUrl]

     #브라우저 종료
    browser.quit()

    def parse(self, response):
        for url in response.css('div.subject > strong > a::attr("href")').getall():
            print(url)
            #url 보다 urljoin 사용
            yield scrapy.Request(response.urljoin(url), self.parse_title)
    
    def parse_title(self, response):    
        contents = response.xpath('//*[@id="size_ct"]/p/text()').extract()
        print('###################')
        print(contents)
        yield {'네이버백과내용': ''.join(contents)}