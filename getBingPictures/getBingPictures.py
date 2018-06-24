import requests
import json
from urllib import request


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
    result_picture_url = link_dict['images'][0]['url']
    pictureUrl = 'https://cn.bing.com' + result_picture_url
    url_list.append(pictureUrl)
    result_doc_url = link_dict['images'][0]['copyright']
    url_list.append(result_doc_url)
    return url_list


def downloadPictures(pictureUrl):
    """ 保存图片 """
    request.urlretrieve(pictureUrl[0],
                        'D:\\Pictures\\Bing_Today_Picture\\day_6.jpg')


def downloadDoc(docUrl):
    """ 保存图片相关信息 """
    with open(
            'D:\\Pictures\\Bing_Today_Picture\\day_6.txt', 'a',
            encoding='utf-8') as ap:
        ap.write(docUrl[1])


def main():
    """ 控制代码主要流程 """
    url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1529297819631&pid=hp'
    html = getUrl(url)
    urlList = parseHtml(html)
    downloadPictures(urlList)
    downloadDoc(urlList)


if __name__ == '__main__':
    main()