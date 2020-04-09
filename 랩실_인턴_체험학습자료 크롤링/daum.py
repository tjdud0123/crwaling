#-*- coding: utf-8 -*-
import scrapy
import urllib.parse as rep
import urllib.request as req


class DaumSpider(scrapy.Spider):
    
    base = "https://100.daum.net/search/entry?q="
    # 검색어
    query = str(input())
    quote = rep.quote_plus(query)
    # URL 완성
    firsturl = base + quote

    name = 'daum'
    allowed_domains = ['100.daum.net']
    start_urls = [firsturl]

    #메인 페이지 순회
    def parse(self, response):
        """
        :param : response
        :return: Request
        """

        for url in response.css('a.link_register::attr("href")').getall():
            # print(url)
            # url 보다 urljoin 사용
            yield scrapy.Request(response.urljoin(url), self.parse_title)

    #상세 페이지 순회
    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param response: 
        :return Contents Text :
        """
        contents = response.css('p.desc_section::text').extract()
        yield {'다음백과내용': ''.join(contents)}
    
        
    