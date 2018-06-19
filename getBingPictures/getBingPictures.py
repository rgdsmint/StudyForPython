import requests
import json
from urllib import request


def getUrl(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        return r.text
    except:
        pass


def parseHtml(html):
    link_dict = json.loads(html)
    result = link_dict['images'][0]['url']
    pictureUrl = 'https://cn.bing.com' + result
    return pictureUrl


def downloadPictures(pictureUrl):
    request.urlretrieve(pictureUrl, 'D:\\today.jpg')


def main():
    url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1529297819631&pid=hp'
    html = getUrl(url)
    pictureUrl = parseHtml(html)
    downloadPictures(pictureUrl)


if __name__ == '__main__':
    main()