import requests
from bs4 import BeautifulSoup
class fanyi:
    def __init__(self,shuru):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
        }
        self.data = {
            'inputtext':shuru,
            'type':'AUTO'
        }
    # def request(self):
    #     r = requests.post('http://m.youdao.com/translate',headers=self.headers,data=self.data )
    #     return r
    def run(self):
        r = requests.post('http://m.youdao.com/translate',headers=self.headers,data=self.data )
        a = BeautifulSoup(r.text,'lxml')
        print(a.select('div.generate li'))
if __name__=='__main__':
    a = fanyi('book')
    a.run()
