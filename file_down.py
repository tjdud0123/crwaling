# BeautifulSoup
# BeautifulSoup 블로그 체험학습 파일 다운로드

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent

from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
# Header 정보 삽입
req.install_opener(opener)

# 기본 URL(**사이트 변경시 이곳 변경)
url = "https://m.blog.naver.com/PostView.nhn?blogId=bestmom8&logNo=103886028&proxyReferer=https%3A%2F%2Fwww.google.com%2F"
#url = "http://blog.naver.com/PostView.nhn?blogId=susungone&logNo=150027540038"


# 요청 URL 확인
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로(**경로 맞게 변경 \두개필수)
savePath = "C:\\Users\\user\\Desktop\\file_list2\\"  # C:\\imagedown\\

# 폴더 생성 예외처리 (문제 발생 시 프로그램 종료)
try:
    # 기존 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
        # 에러 내용
        print("folder creation failed!")
        print("folder name : {}".format(e.filename))
        
        # 런타임 에러 raise
        raise RuntimeError('System Exit!')
else:
    # 폴더 생성 정상일 경우 실행
    print('folder is created!')

# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# select 사용(**변경)
file_list = soup.select("a[_foo*=con_link]")


# 파일 한개씩 다운로드
for v in file_list:
    try:
        #파일 이름 셀렉트로 가져오기(**변경)
        name = v.find('font').string.strip()
        # 저장 파일명 및 경로
        fullFileName = os.path.join(savePath, savePath + name)
        # 파일명 출력 
        print('full name : {}'.format(fullFileName))
        
        # 다운로드 요청(URL, 저장경로)
        req.urlretrieve(v['href'], fullFileName)
    except:
        #파일이 없으면 넘어감
        pass
    else:
        # 다운로드 완료 시 출력
        print("download succeeded!")
     
