BASE_URL = 'http://weixin.sogou.com/weixin?'
KEYWORD = '风景'

HEADERS = {
    'Host': 'weixin.sogou.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'CXID=170B0605F4499ADD0E3B77A6F48D7961; SUV=0003178CB66A623959A956DAD985C699; SUID=39626AB63865860A59A6D7310003F306; IPLOC=CN5101; ABTEST=0|1512207083|v1; SNUID=F8F68DB91510494E301EA8D516ABD3C5; weixinIndexVisited=1; H_USER_ID=f03297ce-6a37-4908-9cb0-aaf355e7f459; ppinf=5|1512226613|1513436213|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxOi58Y3J0OjEwOjE1MTIyMjY2MTN8cmVmbmljazoxOi58dXNlcmlkOjQ0Om85dDJsdVBBSXFheTlWZ1NZbHZ6eGU2OUVzd2tAd2VpeGluLnNvaHUuY29tfA; pprdig=hJD-86mOJ8fyIThplFE0a6F9GVEpcqzxeIO-6B8Vfva907EZsUR3aKsOYOJcRL8afw35QVw4dP8JlV_4cU90_SJzKjBhSwIs-YZru8FB48Vbrf5g4xRhrgWRngi5-VbiS5KWtyVyI9seO3GiZNTpK7DSVHF_m8gPeXnQoiQakOI; sgid=31-32249305-AVoiavzXt8GAv5ESN90p24RQ; SUIR=F8F68DB91510494E301EA8D516ABD3C5; ppmdig=15122906690000003d358424c9069a24714457d9ce7f4fc1; sct=7; JSESSIONID=aaaIZo-Drju2abVG_Rv8v'
}

# ProxyPool
PROXYPOOL_URL = 'http://127.0.0.1:5000/get'

# MongoDB Conf
MONGO_URL = 'localhost'
MONGO_DB = 'wx_articles'
MONGO_TABLE = 'wx_articles'