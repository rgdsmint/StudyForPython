import requests
from bs4 import BeautifulSoup
import json
import random
class getUrl():
    def __init__(self):
        self.rateList = []
        self.titleList = []
        self.urlList = []
        self.getUrl()
        for r,t,u in zip(self.rateList, self.titleList, self.urlList):
            print(type(r), '\t', t, '\t', u)

    def getUrl(self):
        flag = 0
        # 用不同IP去访问要爬去的网站

        # 在https://proxy.coderbusy.com/找到的IP地址（不停刷新即可）
        pro = ['122.152.196.126', '114.215.174.227', '119.185.30.75']
        # 头信息
        head = {
            'user-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64 x64)AppleWebkit/537.36(KHTML,like Gecko) chrome/58.0.3029.110 Safari/537.36'
        }
        # 用随机生成的一个IP去访问这个网页
        while True:
            url = 'https://movie.douban.com\
/j/search_subjects?type=movie&tag=%E7%83%AD\
%E9%97%A8&page_limit=1&page_start={}'.format(flag)
            try:
                r = requests.get(url, proxies={'http': random.choice(pro)}, headers=head)
                r.encoding = r.apparent_encoding
                print(r.status_code)
                print(r.text)
                dic = json.loads(r.text)['subjects'][0]
                movie_rate = dic['rate']
                movie_title = dic['title']
                movie_url = dic['url']
                self.rateList.append(movie_rate)
                self.titleList.append(movie_title)
                self.urlList.append(movie_url)
                flag += 1
            except:
                break

if __name__ == '__main__':
    gu = getUrl()
