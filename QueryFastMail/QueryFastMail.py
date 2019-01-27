import requests
import json

class Query:
    numOfFastMail = ""
    fastMailHost = ""
    queryHostUrl = "http://www.kuaidi100.com/autonumber/autoComNum?text="  # 查询快递运输公司的接口
    queryFastMailMsgUrl = ""
    fastMailTime = []
    fastMailPosition = []
    def __init__(self, numOfFastMail):
        self.numOfFastMail = numOfFastMail
        # print(numOfFastMail)
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
        count = 0
        while count < len(self.fastMailTime) :
            print(self.fastMailPosition[count])
            print(self.fastMailTime[count])
            print()
            count += 1
if __name__ == '__main__':
    numOfFastMail = input("请输入快递单号: ")
    print()
    query = Query(numOfFastMail)
