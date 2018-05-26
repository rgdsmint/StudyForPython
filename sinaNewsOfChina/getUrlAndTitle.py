import requests
from bs4 import BeautifulSoup

'''
对新浪新闻的定向爬虫
'''


class getUrlAndTitle:
    newsUrlList = []
    newsTitleList = []

    def main(self, url):
        self.getUrl(url)
        self.getTitle()

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
        # 删除无效链接
        for item in self.newsUrlList:
            if not self.getTitle_code(item):
                pass

    def getTitle_code(self, url):
        try:
            requests.urllib3.disable_warnings()
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
        except:
            print('error')
        try:
            result = soup.select('.main-title')[0].text
            return result
        except:
            # 删除无效链接
            del self.newsUrlList[self.newsUrlList.index(url)]
            return None

    def printUrl(self):
        wr = open('E:\\work_python\\sinaNewsOfChina\\news\\urls.txt', 'a')
        wr.truncate()
        for link in self.newsUrlList:
            if self.newsUrlList.index(link) == len(self.newsUrlList) - 1:
                wr.write(link)
            else:
                wr.write(link + '\n')
        wr.close()

    def getTitle(self):
        for item in self.newsUrlList:
            if self.getTitle_code(item):
                self.newsTitleList.append(self.getTitle_code(item))
