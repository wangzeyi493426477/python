from bs4 import BeautifulSoup
import requests
import re
start = 'https://bj.58.com/sale.shtml'
def get_name(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text,'lxml')
    name_data = soup.select('li.ym-tab span.dlb')
    url_last = re.compile(r'href=\"(.*?)\"').findall(str(name_data))
    for link_last in url_last:
        web = 'https://bj.58.com' + link_last
        print(web)
get_name(start)
list = '''
https://bj.58.com/shouji/
https://bj.58.com/tongxunyw/
https://bj.58.com/danche/
https://bj.58.com/diandongche/
https://bj.58.com/diannao/
https://bj.58.com/shuma/
https://bj.58.com/jiadian/
https://bj.58.com/ershoujiaju/
https://bj.58.com/yingyou/
https://bj.58.com/fushi/
https://bj.58.com/meirong/
https://bj.58.com/yishu/
https://bj.58.com/tushu/
https://bj.58.com/wenti/
https://bj.58.com/kaquan/
https://bj.58.com/shebei.shtml
https://bj.58.com/chengren/
'''
