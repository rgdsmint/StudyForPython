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
                        "yunda": "韵达快递", "shunfeng": "顺丰快递"}  # 对应快递代码快递名称

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
        self.fastMailPosition.clear()
        self.fastMailTime.clear()


class SetFile:
    fastMailList = []
    fastMailDic = {}

    def __init__(self, arg):
        self.updateFile()
        if arg == 2:
            while True:
                numOfFastMail = input("输入要添加的快递编号(输入n可退出):")
                if numOfFastMail == 'n':
                    print()
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
            self.updateFile()

    def delFile(self, num):
        with open('Wait.json', 'r', encoding='utf-8') as file:
            f = file.read()
            fastMailDic = json.loads(f)
        if num not in fastMailDic.keys():
            print("此单号不存在或已删除")
            print()
        else:
            numOfFastMail = fastMailDic.pop(num)
            jsonStr = json.dumps(fastMailDic, indent=4)
            with open('Wait.json', 'w', encoding="utf-8") as jsonFile:
                jsonFile.write(jsonStr)
            print("删除成功")
            print()
            self.updateFile()

    def showFile(self):
        while True:
            self.printFile()           
            op = int(input("1.查看\n"
                           "2.删除\n"
                           "(输入0退出):"))
            if op == 0:
                print()
                break
            elif op == 2:
                print()
                while True:
                    self.printFile() 
                    print()
                    opNum = int(input("输入要删除快递的序列号(输入0退出):"))
                    if opNum != 0:
                        self.delFile(self.fastMailList[opNum - 1])
                    else:
                        print()
                        break
            else:
                print()
                while True:
                    self.printFile() 
                    opNum = int(input("输入要查看快递的序列号(输入0退出):"))
                    if opNum != 0:
                        query = Query(self.fastMailList[opNum - 1])
                    else:
                        print()
                        break
                        
    def printFile(self):
        if len(self.fastMailList) == 0:
                print("[你没有添加查询项]")
        else:
            count = 0
            while count < len(self.fastMailList):
                print(
                    "[{}]单号:{}\t备注:{}".format(count + 1, self.fastMailList[count],
                                                self.fastMailDic[self.fastMailList[count]]))
                count += 1
        print()
    def updateFile(self):
        with open('Wait.json', 'r', encoding='utf-8') as file:
            f = file.read()
            self.fastMailDic = json.loads(f)
        self.fastMailList = list(self.fastMailDic)


if __name__ == '__main__':
    while True:
        option = int(input("1.直接查询\n"
                           "2.新建查询项(以后直接查看)\n"
                           "3.查看或删除已有查询项\n"
                           "请选择您需要的选项(输入不在选项内的数字退出):"))
        print()
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
