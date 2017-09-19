from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

#有异常处理 获取 bs对象

def getBsObj(url):
    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read(), 'lxml')
    except HTTPError as e:
        return None

    return bsObj



if __name__ == '__main__':
    # print(getBsObj('http://www.pythonscraping.com/pages/page1.html'))
    # html = urlopen('http://www.pythonscraping.com/pages/page3.html')
    bsObj = getBsObj('http://www.pythonscraping.com/pages/page3.html')
    #../img/gifts/img1.jpg
    # if bsObj is not None:
    #     for child in bsObj.findAll('img', {'src' : re.compile(r'\.\./img/gifts/img[0-9]\.jpg')}):
    #         print(child['src'])
    #         print(child.attrs)
    print(bsObj.find(lambda tag : len(tag.attrs) == 2))