from getUrlAndTitle import getUrlAndTitle
from getContent import getContent
import re


class printNews:
    def __init__(self, url):
        self.gc = getContent(url)
        self.main()

    def main(self):
        self.writeNews()

    def writeNews(self):
        fileName = re.sub('[\\\/:*?"<>|]', ' ', self.gc.newsTitle)
        wr = open('E:\\work_python\\sinaNewsOfChina\\news\\%s.txt' % (fileName), 'a', encoding='utf-8')
        wr.write(self.gc.passage + '\n\n-----------------------------\n评论如下:\n\n------------------------\n')
        for n, a, i, d, c in zip(self.gc.commenterNick, self.gc.commenterArea, self.gc.commenterIP, self.gc.commentDate,
                                 self.gc.content):
            wr.write('昵称:' + n + '\n')
            wr.write('故乡:' + a + '\n')
            wr.write('ip地址:' + i + '\n')
            wr.write('评论时间:' + d + '\n')
            wr.write('评论:' + c + '\n-------------------------------------\n')
        wr.close()


if __name__ == '__main__':
    guat = getUrlAndTitle()

    with open('E:\\work_python\\sinaNewsOfChina\\news\\urls.txt', 'r') as rf:
        urls = []
        for line in rf:
            urls.append(str(line).split('\n')[0])

    for item in urls:
        pn = printNews(item)
