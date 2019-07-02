import requests
import re

'''
获取车站对应序号 以及序号对应车站
已将信息存入本目录的 stations.py 文件
无需再次运行
'''


def getMessage():
    url = 'https://kyfw.12306.cn/otn/resources/js/\
framework/station_name.js?station_version=1.9053'
    requests.urllib3.disable_warnings()
    r = requests.get(url, verify=False)
    patter = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = dict(re.findall(patter, r.text))
    temp1 = list(result.keys())
    temp2 = list(result.values())
    result2 = {}
    for a, b in zip(temp1, temp2):
        result2[b] = a


if __name__ == '__main__':
    getMessage()