import requests
from bs4 import BeautifulSoup


class top_fiveHundred:
    def getUrl(self, url):
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        enterprises = soup.select('tbody')[0]
        return enterprises

    def parseHtml(self, enterprises):
        # 排名
        self.ranking = []

        # 上年排名
        self.lastYear_ranking = []

        # 公司名称
        self.name = []

        # 营业收入(百万美元)
        self.Turnover = []

        # 利润(百万美元)
        self.profit = []

        # 所属国家
        self.Owned_Country = []

        for item in range(1, 501):
            content = enterprises.select('tr')[item].select('td')

            self.ranking.append(content[0].text)

            self.lastYear_ranking.append(content[1].text)

            self.name.append(content[2].text)

            self.Turnover.append(content[3].text)

            self.profit.append(content[4].text)

            self.Owned_Country.append(content[5].text)

    def write_doc(self):
        with open('E:\\pythonDemo\\top500\\ranking.txt', 'a+', encoding='utf-8') as f:
            for item in self.ranking:
                f.write(item + '\n')
        with open('E:\\pythonDemo\\top500\\lastYearRanking.txt', 'a+', encoding='utf-8') as f:
            for item in self.lastYear_ranking:
                f.write(item + '\n')
        with open('E:\\pythonDemo\\top500\\name.txt', 'a+', encoding='utf-8') as f:
            for item in self.name:
                f.write(item + '\n')
        with open('E:\\pythonDemo\\top500\\turnover.txt', 'a+', encoding='utf-8') as f:
            for item in self.Turnover:
                f.write(item + '\n')
        with open('E:\\pythonDemo\\top500\\profit.txt', 'a+', encoding='utf-8') as f:
            for item in self.profit:
                f.write(item + '\n')
        with open('E:\\pythonDemo\\top500\\ownedCountry.txt', 'a+', encoding='utf-8') as f:
            for item in self.Owned_Country:
                f.write(item + '\n')

    def __init__(self, url):
        enterprises = self.getUrl(url)
        self.parseHtml(enterprises)
        self.write_doc()

if __name__ == '__main__':
    t = top_fiveHundred(
        'http://tech.sina.com.cn/it/2018-07-19/doc-ihfnsvzc0219285.shtml?source=cj&dv=2'
    )
