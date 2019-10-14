# first_session
# 멜론플레이리스트 가져오기

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


# 멜론 플레이리스트 URL
url = "https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=420245387"

# 요청 URL 확인
print(url)
    
# Request
res = req.urlopen(url)
print(res)

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# select 사용
songs = soup.select("td:nth-child(5) > div > div.wrap_song_info")
print(songs)

#반복해서 데려오기
for i,song in enumerate(songs, 1):
    title = song.select_one('div.ellipsis.rank01').text.strip()
    artist = song.select_one('div.ellipsis.rank02 > a').text.strip()
  
    # 순위출력
    print(str(i) + '위')
    print('title : ' + title)
    print('artist : ' + artist)
    print('----------------')
