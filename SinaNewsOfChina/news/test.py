import requests
from bs4 import BeautifulSoup
import re

def setFileTitle(title):
    notRight = '\/:*?"<>|'
    fileName = re.sub('[\\\/:*?"<>|]', '', title)
    return fileName# 去掉非法字符
print(setFileTitle('\/:*fgdfs?"<>gs|'))