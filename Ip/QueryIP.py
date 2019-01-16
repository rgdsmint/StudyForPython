import requests
from bs4 import BeautifulSoup

def query_IP():
    ip = input('请输入您要查询的ip或域名(输入"exit"可退出):')
    if ip == 'exit':
        exit()
    url = 'http://www.ip138.com/ips138.asp?ip={}'.format(ip)
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        message = r.text
        soup = BeautifulSoup(message, 'html.parser')
        for item in range(0, 3):
            result = soup.select('.ul1')[0].select('li')[item].text.split('：')[1]
            print('参考数据:%s' % (result))
    except:
        print("输入有误")


if __name__ == '__main__':
    while True:
        query_IP()
