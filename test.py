# a_list = ['사과','배','감']
# b_list = ['철수', '영희']
# a_list.append('딸기')
# a_list.insert(0,'수박')
# a_list.append(b_list)
# print(a_list[5][1])
#
# a_dict = {'name':'pyo','age':25}
# # a_dict['height'] = 200
# print(a_dict)
# print(a_dict['name'])
#
# def sum(a,b):
#     print('hi')
#
#
# result = sum(2,3)
# print(result)


# def is_even(num):
#     if (num % 2 is 0) or (num is 19):
#         return True
#     else:
#         return False
#
# result = is_even(19)
# print(result)
#
# myemail = 'spartacoding@gmail.com'
# domain = myemail.split('@')[1].split('.')[0]
# print(domain)


people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}, {'name': 'john', 'age': 7}]

# for person in people :
#     print(person['name'])
#
# for a in range(0,10):
#     print(a)

# for person in people :
#     print(person)
#     if(person['age'] <20) :
#         print(person['name'])

# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
# print(rjson)
# print (rjson['RealtimeCityAir']['row'][0]['NO2'])
#
#
# rows = rjson['RealtimeCityAir']['row']
#
# for row in rows :
#     if row['IDEX_MVL'] < 50:
#         print(row['MSRSTE_NM'],row['IDEX_MVL'])



import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200129',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################
# select_one 하나만 찾아옴  // select 모두 다 찾아옴(리스트형태)
movies = soup.select('#old_content > table > tbody > tr')
#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
for movie in movies :
    title = movie.select_one('td.title > div > a')
    if title is not None :
        star = movie.select_one('td.point')
        rank = movie.select_one('td:nth-child(1) > img')
        print(rank['alt'],title.text,star.text)


#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img


