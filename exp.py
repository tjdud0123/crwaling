# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class ExpSpider(scrapy.Spider):


    name = 'exp'
    allowed_domains = ['koc.chunjae.co.kr']
    start_urls = ['https://koc.chunjae.co.kr/Dic/dicDetail.do?idx=40025']
    def parse(self, response):
        urls = []
        base = 'https://koc.chunjae.co.kr/Dic/dicDetail.do?idx='
        fistNumber = 40026
        for i in range (149) :
            url = base + str(fistNumber + i)
            urls.append(url)
            for url in urls:
                yield scrapy.Request(response.urljoin(url), self.parse_title)
    
    def parse_title(self, response):
        title = response.xpath('//*[@id="pDetail"]/div[2]/div/div[1]/h4/text()').extract()
        contents = response.xpath('//*[@id="pDetail"]/div[2]/div/div[5]/p/text()').extract()
        print('###################')
        print(title)
        yield {title.pop() : ''.join(contents).strip()}
