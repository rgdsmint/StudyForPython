import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


class UniversityRanking:
    def __init__(self):
        self.main()
    def main(self):
        self.University()
        self.getRanking(self.getUrl())

    def getUrl(self):
        university = input('请输入您想查询的信息:')
        url = 'http://www.zuihaodaxue.cn/{}'.format(self.UniversityDict[university])
        return url

    def getRanking(self, url):
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        pt = PrettyTable()
        title = '排名 校名 所在地区 总分 生源质量 毕业生就业率 社会捐赠收入·千元 科研规模 科研质量 顶尖成果 顶尖人才 科研经费·千元 技术转让收入·千元 留学生比例'.split()
        pt._set_field_names(title)
        for item in soup.select('.alt'):
            ranking = item.find_all('td')[0].text
            name = item.find_all('td')[1].text
            area = item.find_all('td')[2].text
            score = item.find_all('td')[3].text
            students_score = item.find_all('td')[4].text
            rateOfEmployment = item.find_all('td')[5].text
            socialDonationIncome = item.find_all('td')[6].text
            numberOfPapers = item.find_all('td')[7].text
            qualityOfPapers = item.find_all('td')[8].text
            topResults = item.find_all('td')[9].text
            topTalent = item.find_all('td')[10].text
            scientificResearchFunds = item.find_all('td')[11].text
            technologyTransferIncome = item.find_all('td')[12].text
            internationalizationOfStudents = item.find_all('td')[13].text
            self.list = [
                ranking,
                name,
                area,
                score,
                students_score,
                rateOfEmployment,
                socialDonationIncome,
                numberOfPapers,
                qualityOfPapers,
                topResults,
                topTalent,
                scientificResearchFunds,
                technologyTransferIncome,
                internationalizationOfStudents
            ]
            pt.add_row(self.list)
        print(pt)

    def University(self):
        self.UniversityDict = {'2018中国最好大学排名': 'zuihaodaxuepaiming2018.html',
                               '2018生源质量排名': 'shengyuanzhiliangpaiming2018.html',
                               '2018培养结果排名': 'biyeshengjiuyelv2018.html',
                               '2018社会声誉排名': 'shehuishengyupaiming2018.html',
                               '2018科研规模排名': 'keyanguimopaiming2018.html',
                               '2018科研质量排名': 'keyanzhiliangpaiming2018.html',
                               '2018顶尖成果排名': 'dingjianchengguopaiming2018.html',
                               '2018顶尖人才排名': 'dingjianrencaipaiming2018.html',
                               '2018科技服务排名': 'kejifuwupaiming2018.html',
                               '2018成果转化排名': 'chengguozhuanhuapaiming2018.html',
                               '2018学生国际化排名': 'xueshengguojihuapaiming2018.html',
                               }




if __name__ == '__main__':
    u = UniversityRanking()
