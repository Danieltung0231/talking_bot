import os
import random
import json

os.system("pip install requests")
os.system("pip install bs4")
import requests
from bs4 import BeautifulSoup

# 下載資料庫
r = requests.get('https://danieltung0231.github.io/library.html')

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')
  # 將文字檔轉成 dictionary
  library = soup.p.string
  lib = json.loads(str(library))

def news() :
    # 下載 Yahoo 首頁內容
    r = requests.get('https://tw.yahoo.com/')
    # 確認是否下載成功
    if r.status_code == requests.codes.ok:
      # 以 BeautifulSoup 解析 HTML 程式碼
      soup = BeautifulSoup(r.text, 'html.parser')

    # 以 CSS 的 class 抓出各類頭條新聞
      stories = soup.find_all('a', class_='story-title')
      for i in range(5):
        # 新聞標題
        print("標題：" + stories[i].text)
        # 新聞網址
        print("網址：" + stories[i].get('href'))

while True :
    k = input("==>")
    sents = k.split('!')
    if len(sents) == 1 :
        if sents[0] in lib :
            if str(type(lib[sents[0]])) == "<class 'list'>":
                print(random.choice(lib[sents[0]]))
            else :
                print(lib[sents[0]])
        else :
            print("我不會這句話···")
    else :
        if sents[0] == "新聞" :
            news()
        elif sents[0] == "遊戲" :
            os.system("pip install requests")
        
