# first_session
# 교보문고 순위 가져오기

import urllib.parse as rep
import urllib.request as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
# Header 정보 삽입
req.install_opener(opener)


# 교보문고 종합순위 URL
url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79"

# 요청 URL 확인
print(url)
    
# Request
res = req.urlopen(url)
print(res)

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# select 사용
books = soup.select("div.detail")
print(books)

#반복해서 데려오기
for i,book in enumerate(books, 1):
    title = book.select_one('div.title strong').text.strip()
    price = book.select_one('div.price > strong').text.strip()
  
    # 순위출력
    print(str(i) + '위')
    print('책제목 : ' + title)
    print('가격 : ' + price)
    print('----------------')
