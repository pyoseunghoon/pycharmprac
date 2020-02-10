from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:/Users/LG/Desktop/spa/Crawling_method/chromedriver')
driver.get('https://www.google.com/search?q=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%EC%A3%BC%EC%8B%9D&rlz=1C1AVFC_enKR855KR855&oq=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%EC%A3%BC%EC%8B%9D&aqs=chrome..69i57j0l5j69i60l2.4498j1j7&sourceid=chrome&ie=UTF-8')

list0 = driver.find_elements_by_css_selector('#knowledge-finance-wholepage__entity-summary > div > div > g-card-section:nth-child(2) > div > div > div > table > tbody > tr > td.JgXcPd')
list1 = driver.find_elements_by_css_selector('#knowledge-finance-wholepage__entity-summary > div > div > g-card-section:nth-child(2) > div > div > div > table > tbody > tr > td.iyjjgb')

# print(list1[0].text)
for tag_num in range(len(list0)):
    print(list0[tag_num].text, list1[tag_num].text)
