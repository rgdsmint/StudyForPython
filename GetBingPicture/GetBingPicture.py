import requests
import json
from urllib import request
import time

path = "D:\\Pictures\\Bing_Today_Picture"   # 设置图片保存路径
todayTime = time.strftime('%Y-%m-%d')   # 获取当前时间

def getUrl(url):
    """ 请求网页, 得到页面内容并返回 """
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        pass


def parseHtml(html):
    """ 对页面进行解析, 得到图片地址和信息地址并返回 """
    url_list = []
    link_dict = json.loads(html)
    pictureUrl = 'https://cn.bing.com' + link_dict['images'][0]['url']
    url_list.append(pictureUrl)
    result_doc_url = link_dict['images'][0]['copyright']
    url_list.append(result_doc_url)
    return url_list


def downloadPictures(pictureUrl):
    """ 保存图片 """
    request.urlretrieve(pictureUrl[0], '%s\\%s.jpg' % (path, todayTime))


def downloadDoc(docUrl):
    """ 保存图片相关信息 """
    with open('%s\\%s.txt' % (path, todayTime), 'a', encoding='utf-8') as ap:
        ap.write(docUrl[1])


def main():
    """ 控制代码主要流程 """
    print('#', end='')
    url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1529297819631&pid=hp'
    print('#', end='')
    html = getUrl(url)
    print('#', end='')
    urlList = parseHtml(html)
    print('#', end='')
    downloadPictures(urlList)
    print('#', end='')
    downloadDoc(urlList)
    print('#', end='')


if __name__ == '__main__':
    print('#', end='')
    main()
    print('#.')
    with open('%s\\%s.txt' % (path, todayTime), 'r', encoding='utf-8') as ap:
        docInformation = ap.readline()
        print("Get picture information: %s" % (docInformation))
        print("The name of picture and information file are Today's date.")
        print("They are saved under the  %s." % (path))
