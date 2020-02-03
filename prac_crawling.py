import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://finance.naver.com/item/main.nhn?code=005930',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
#############################
# (입맛에 맞게 코딩)
#############################
# select_one 하나만 찾아옴  // select 모두 다 찾아옴(리스트형태)
#_cs_root > div.ar_cont > div.cont_dtcon > div > ul.lst
#_cs_root > div.ar_cont > div.cont_dtcon > div > ul.lst > li.pcp
das = soup.select_one('#chart_area > div.rate_info > table')
print(das)
# for da in das :
#     title = da.select_one('td.JgXcPd')
#     amount = da.select_one('td.iyjjgb')
#     print(title, amount)


# from urllib.request import urlopen
#
# from urllib.error import HTTPError
#
# from bs4 import BeautifulSoup
#
#
# def getTitle(url):
#     try:
#
#         html = urlopen(url)
#
#     except HTTPError as e:
#         return None
#
#     try:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
#
#
# title = getTitle("https://www.google.com/search?q=%EC%82%BC%EC%84%B1%EC%A3%BC%EC%8B%9D&rlz=1C1AVFC_enKR855KR855&oq=%EC%82%BC%EC%84%B1%EC%A3%BC%EC%8B%9D&aqs=chrome..69i57j69i59j0l6.1128j1j4&sourceid=chrome&ie=UTF-8")
#
# if title == None:
#
#     print("Title could not be found")
#
# else:
#
#     print(title)