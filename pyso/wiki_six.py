from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# html = urlopen('https://en.wikipedia.org/wiki/Eric_Idle')
# bsObj = BeautifulSoup(html.read(), 'lxml')
#
# for link in bsObj.find('div',{'id' : 'bodyContent'}).findAll('a', href = re.compile(r'^(/wiki/)((?!:).)*$')):
#     if('href' in link.attrs):
#         print(link['href'])

def getLinks(partUrl):
    html = urlopen('https://en.wikipedia.org' + partUrl)
    bsObj = BeautifulSoup(html.read(), 'lxml')
    return bsObj.find('div',{'id' : 'bodyContent'}).findAll('a', href = re.compile(r'^(/wiki/)((?!:).)*$'))

if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    links = getLinks('/wiki/Eric_Idle')
    while(len(links) > 0):
        randomLink = links[random.randint(0, len(links) - 1)].attrs['href']
        print(randomLink)
        links = getLinks(randomLink)
