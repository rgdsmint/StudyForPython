import requests
from bs4 import BeautifulSoup

'''
对新浪新闻的定向爬虫
'''


class getUrlAndTitle:
    newsUrlList = []

    def __init__(self):
        self.main('http://news.sina.com.cn/china/')

    def main(self, url):
        self.getUrl(url)
        self.screenUrl()
        self.printUrl()

    def getUrl(self, url):
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            result = soup.select('.blk12')[0]
            for item1 in range(0, len(result.select('.blk121')[0].select('a'))):
                newsUrl_1 = result.select('.blk121')[0].select('a')[item1]['href']
                self.newsUrlList.append(newsUrl_1)
            for item2 in range(0, len(result.select('.blk122')[0].select('a'))):
                newsUrl_2 = result.select('.blk122')[0].select('a')[item2]['href']
                self.newsUrlList.append(newsUrl_2)
        except:
            print('error')

    def screenUrl_code(self, url):
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            s = BeautifulSoup(r.text, 'html.parser')
            ru = s.select('.main-title')
            if not ru:
                del self.newsUrlList[self.newsUrlList.index(url)]
        except:
            print('error')

    def screenUrl(self):
        for link in self.newsUrlList:
            self.screenUrl_code(link)

    def printUrl(self):
        wr = open('E:\\work_python\\sinaNewsOfChina\\news\\urls.txt', 'a')
        wr.seek(0)
        wr.truncate()
        for link in self.newsUrlList:
            if self.newsUrlList.index(link) == len(self.newsUrlList) - 1:
                wr.write(link)
            else:
                wr.write(link + '\n')
        wr.close()
