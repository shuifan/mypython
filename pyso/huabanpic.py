import requests
import re



def make_ajax_url(No):
    """ 返回ajax请求的url """
    url = "http://huaban.com/favorite/beauty/?i5p998kw&max=" + No + "&limit=20&wfl=1"
    return downlocadImg(url)


def downlocadImg(pageUrl):
    req = requests.get(url = pageUrl)
    htmlPage = req.content.decode('utf-8')
    print(htmlPage)

    pat = re.compile(r'app\.page\["pins"\].*')
    appPins = pat.findall(htmlPage)
    listLike = appPins[0][19:-1]
    print(listLike)

    #js的null  python中为 None
    null = None
    true = True
    imgDetails = eval(listLike)
    print(imgDetails)

    images = []

    for i in  imgDetails:
        info = {}
        info['id'] = str(i['pin_id'])
        info['url'] = "http://img.hb.aicdn.com/" + i["file"]["key"] + "_fw658"
        info['type'] = i["file"]["type"][6:]
        images.append(info)

    print(images)

    for i in images:
        print(i['url'])
        imgRes = requests.get(i['url'])
        basePath = '/Users/a2017-8-27/Documents/moocimg/'
        imageName = basePath + i['id'] + '.' + i['type']
        with open(imageName, 'wb') as f:
            f.write(imgRes.content)

    make_ajax_url(images[-1]['id'])


if __name__ == '__main__':
    downlocadImg('http://huaban.com/favorite/beauty/')
