import re
import urllib3

http = urllib3.PoolManager()
# page = http.request('get', 'https://huaban.com/boards/299704/')
page = http.request('get', 'http://www.imooc.com/')
print(page.data)

# '-' 这个应该放在 【】 中的两侧
picList = re.findall(r'http://[\.\w/-]+jpg', page.data.decode('utf-8'))
print(picList)
print(len(picList))