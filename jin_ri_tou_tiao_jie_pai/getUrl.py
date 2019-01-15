import requests
from bs4 import BeautifulSoup
import json


class getUrl:
    def getUrl(self, url):
        try:
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            return r.text
        except:
            pass

    def parseHtml_first(self, html):
        url_dict = json.loads(html)
        picture_url_list = url_dict['data']
        self.imageUrlList = []
        self.imageUrlCount = {}

        for link in picture_url_list:
            imageUrl = link['share_url']
            imageCount = link['image_count']
            self.imageUrlList.append(imageUrl)
            self.imageUrlCount[imageUrl] = imageCount
    
    def parseHtml_second(self):
        r = requests.get(self.imageUrlList[1])
        print(self.imageUrlList[1])
        print(r)
        print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup)
        re = soup.select('.image-item-inner')
        print(re)

    def main(self):
        html = self.getUrl('https://www.toutiao.com/search_content\
/?offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=t\
rue&count=20&cur_tab=2&from=search_tab')
        self.parseHtml_first(html)
        self.parseHtml_second()


if __name__ == '__main__':
    g = getUrl()
    g.main()