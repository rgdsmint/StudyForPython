import requests
import json


class Query:
    """
    查询快递
    """
    numOfFastMail = ""  # 快递单号
    fastMailHost = ""  # 快递运输公司名称
    queryHostUrl = "http://www.kuaidi100.com/autonumber/autoComNum?text="  # 查询快递运输公司的接口
    queryFastMailMsgUrl = ""  # 包含快递信息的网页
    fastMailTime = []  # 快递时间相关信息
    fastMailPosition = []  # 快递所在地相关信息
    fastMailHostDict = {"zhongtong": "中通快递", "yuantong": "圆通速递", "jd": "京东快递", "shentong": "申通快递", "ems": "邮政EMS",
                        "yunda": "韵达速递"}  # 对应快递代码快递名称

    def __init__(self, numOfFastMail):
        self.numOfFastMail = numOfFastMail
        self.queryHost(self.getWebPage(self.queryHostUrl + self.numOfFastMail))
        self.queryFastMailMsgUrl = "http://www.kuaidi100.com/query?type={}&postid={}" \
            .format(self.fastMailHost, self.numOfFastMail)
        self.querySpeedOfProcess(self.getWebPage(self.queryFastMailMsgUrl))
        self.printFastMailMsg()

    def getWebPage(self, url):
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print("获取页面错误!")

    def queryHost(self, webPage):
        self.fastMailHost = json.loads(webPage)['auto'][0]['comCode']  # 找到快递运送服务公司名称

    def querySpeedOfProcess(self, webPage):
        speedOfProcessList = json.loads(webPage)["data"]
        for item in speedOfProcessList:
            self.fastMailTime.append(item["time"])
            self.fastMailPosition.append(item["context"])

    def printFastMailMsg(self):
        if self.fastMailHost in self.fastMailHostDict.keys():
            print("此快递由[{}]护送".format(self.fastMailHostDict[self.fastMailHost]), end="\n\n")
        else:
            print("此快递由[{}]护送".format(self.fastMailHost), end="\n\n")
            print(self.fastMailHost)
        count = 0
        while count < len(self.fastMailTime):
            print(self.fastMailPosition[count])
            print(self.fastMailTime[count], end="\n\n")
            count += 1


if __name__ == '__main__':
    while True:
        numOfFastMail = input("请输入快递单号(输入n退出):")
        if numOfFastMail == "n":
            exit()
        print()
        query = Query(numOfFastMail)
