from bs4 import BeautifulSoup
import requests
import re
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
test1 = client['test2']
url = test1['url_list3']
info = test1['info_list3']
def get_link(name,page,who=0):
    ##https://bj.58.com/shouji/0/pn2/
    urls=[]
    link_view = '{}{}/pn{}'.format(name,str(who),str(page))
    data = requests.get(link_view)
    soup = BeautifulSoup(data.text,'lxml')
    time.sleep(1)
    if soup.find('td','t'):
        for link in soup.select('td.t a.t.ac_linkurl'):
            urls.append(link.get('href'))
            url.insert_one({'url':urls[-1]})
    else:
        pass
def get_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = wb_data.apparent_encoding
    soup = BeautifulSoup(wb_data.text,'lxml')
    # shifou = '404' in soup.find('script',"text/javascript").get('sre').split('/')
    #
    # if shifou:
    #     pass
    # else:
    title = re.compile(r'<title>(.*?)</title>').findall(str(soup))
    price1 = soup.select('div.infocard__container__item__main span')
    # print(price1.text)
    # ##不加.text则显示<>内的内容，加上.stripped_strings则可消除空格和换行
    # price = re.compile(r'[0-9]').findall(price1) + "元"
    time1 = str(soup.select('div.detail-title__info__text'))
    time = ''.join(re.compile(r'\">(.*?)<').findall(time1))
    place1 = str(soup.select('div.infocard__container__item__main'))
    place = re.compile(r'blank">(.*?)</a>').findall(place1)
    place = ''.join(place)
    data = {
        '地区' : place,
        '标题' : title,
        '时间' : time
    }
    info.insert_one(data)
get_link('https://bj.58.com/shouji/',2)
get_info('https://bj.58.com/shouji/37354545784720x.shtml')
