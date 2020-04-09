# BeautifulSoup
# BeautifulSoup 사용 wiki 표정보 가져오기

import os
import urllib.parse as rep
import urllib.request as req

from bs4 import BeautifulSoup


while(True):
# 네이버 이미지 기본 URL(크롬 개발자 도구)
    base = "https://ko.wikipedia.org/wiki/"

# 검색어
    query = str(input())
    quote = rep.quote_plus(query)
# URL 완성
    url = base + quote

#요청 URL 확인
#print('Request URL : {}'.format(url))

# Request
    res = req.urlopen(url)

# bs4 초기화
    soup = BeautifulSoup(res, "html.parser")

# select 사용
    table = soup.select_one("table.infobox > tbody")
    row_list = table.find_all('tr')
#print(row_list)

    for r in row_list:
        try:
        #파일 이름 셀렉트로 가져오기(**변경)
          title = r.find('th').text.strip()
          content = r.find('td').text.strip()
        except:
          pass
        else:
            print('title : {}'.format(title))
            print('content : {}'.format(content))
            print('----------------')
