import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://stackoverflow.com/questions/tagged/python',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################
# select_one 하나만 찾아옴  // select 모두 다 찾아옴(리스트형태)
question = soup.select('#questions > .question-summary > .summary > h3 > a')
print(question[0])
for index, qu in enumerate(question):
    hr_link = 'https://stackoverflow.com/'+qu['href']
    python_text = qu.text
    print(str(index + 1)+ ':' + python_text + '\n' + hr_link)
    print('\n')




