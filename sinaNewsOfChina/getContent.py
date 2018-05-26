import requests
from bs4 import BeautifulSoup
import json
from getUrlAndTitle import getUrlAndTitle

'''
获取新闻内容, 如时间、来源、内文、评论等
'''


class getContent:

    def __init__(self, url):
        self.main(url)
        g = getUrlAndTitle()
        g.main('http://news.sina.com.cn/china/')
        self.title = g.newsTitleList
        self.passage = self.date + '\n' + self.source + '\n' + self.article

    def main(self, url):
        self.getDate(url)
        self.getSource(url)
        self.getArticle(url)
        self.getComment(url)

    def getDate(self, url):
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            self.date = soup.select('.date')[0].text
        except:
            print('error')

    def getSource(self, url):
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        self.source = soup.select('.source')[0].text

    def getArticle(self, url):
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            result = soup.select('.article')[0].text.split('\n')
            article = []
            for line in result:
                line = line.strip()
                article.append(line)
            self.article = '\n'.join(article)
        except:
            print('error')

    def getComment(self, url):
        self.commenterNick = []
        self.commenterArea = []
        self.commenterIP = []
        self.commentDate = []
        self.content = []
        temp = url.split('-i')[1].split('.')[0]
        newUrl = 'http://comment5.news.sina.com\
.cn/page/info?version=1&format=js&channel=gn&new\
sid=comos-{}&group=0&compress=0&ie=gbk&oe=gbk&pag\
e=1&page_size=20'.format(temp)
        try:
            r = requests.get(newUrl, verify=False)
            r.encoding = r.apparent_encoding
            comment_dict = json.loads(r.text.strip('var data='))
            for item in range(0, len(comment_dict['result']['cmntlist'])):
                comment_1 = comment_dict['result']['cmntlist'][item]
                self.commenterNick.append(comment_1['nick'])
                self.commenterArea.append(comment_1['area'])
                self.commenterIP.append(comment_1['ip'])
                self.commentDate.append(comment_1['time'])
                self.content.append(comment_1['content'])

            for item in range(0, len(comment_dict['result']['hot_list'])):
                comment_2 = comment_dict['result']['hot_list'][item]
                self.commenterNick.append(comment_2['nick'])
                self.commenterArea.append(comment_2['area'])
                self.commenterIP.append(comment_2['ip'])
                self.commentDate.append(comment_2['time'])
                self.content.append(comment_2['content'])
        except:
            print('error')
