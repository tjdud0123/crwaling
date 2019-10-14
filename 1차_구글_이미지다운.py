# first_session
# 구글 검색 후 이미지 다운로드





import os
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

# 구글 이미지 기본 URL(크롬 개발자 도구)
base1 = "https://www.google.com/search?q="
base2 = "&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiku6zr5fPkAhUMyosBHc55B5IQ_AUIEigB&biw=1536&bih=754"
# 검색어
quote = rep.quote_plus("드래곤 길들이기")
# URL 완성
url = base1 + quote + base2
    
# Request
res = req.urlopen(url)
print(res)

# 이미지 저장 경로)
savePath = "C:\\Users\\user\\Desktop\\dragon\\"  # C:\\imagedown\\

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

# select 사용
img_list = soup.select("img")
print(img_list)

for i, v in enumerate(img_list):
    try:
   
        # 저장 파일명 및 경로
        fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
        
        # 다운로드 요청(URL, 저장경로)
        req.urlretrieve(v['src'], fullFileName)
    except:
        #파일이 없으면 넘어감
        pass
    else:
        # 다운로드 완료 시 출력
        print("download succeeded!")
