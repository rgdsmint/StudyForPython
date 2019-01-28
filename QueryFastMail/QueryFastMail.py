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


class SetFile:
    def __init__(self, arg):
        if arg == 2:
            while True:
                numOfFastMail = input("输入要添加的快递编号(输入n可退出):")
                if numOfFastMail == 'n':
                    break
                fastMailMsg = input("输入备注(可为空):")
                self.addFile(numOfFastMail, fastMailMsg)
        else:
            self.showFile()

    def addFile(self, num="", msg=""):
        with open('Wait.json', 'r', encoding='utf-8') as file:
            f = file.read()
            fastMailDic = json.loads(f)
        if num in fastMailDic.keys():
            print('此单号已存在')
            print()
        else:
            fastMailDic[num] = msg
            jsonStr = json.dumps(fastMailDic, indent=4)
            with open('Wait.json', 'w', encoding="utf-8") as jsonFile:
                jsonFile.write(jsonStr)
            print("添加成功")
            print()

    def showFile(self):
        with open('Wait.json', 'r', encoding='utf-8') as file:
            f = file.read()
            fastMailDic = json.loads(f)
        fastMailList = list(fastMailDic)
        while True:
            count = 0
            while count < len(fastMailList):
                print("{}.单号:{}\t备注:{}".format(count + 1, fastMailList[count], fastMailDic[fastMailList[count]]))
                count += 1
            op = int(input("查看(输入0退出):"))
            if op == 0:
                print()
                break
            query = Query(fastMailList[op - 1])


if __name__ == '__main__':
    while True:
        option = int(input("1.直接查询\n"
                           "2.新建查询项(以后直接查看)\n"
                           "3.查看已有查询项\n"
                           "请选择您需要的选项(输入不在选项内的数字退出):"))
        if option == 1:
            while True:
                numOfFastMail = input("请输入快递单号(输入n退出):")
                if numOfFastMail == "n":
                    print()
                    break
                print()
                query = Query(numOfFastMail)
        elif (option == 2) or (option == 3):
            SetFile(option)
        else:
            exit()
