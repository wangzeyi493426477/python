from bs4 import BeautifulSoup
from tkinter import *
import requests
import urllib.request
import urllib.parse
import json
from tkinter.scrolledtext import ScrolledText
import re
from tkinter import messagebox
global val
global a
import webbrowser
def run():
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Cookie' : 'BAIDUID=99DAFEEFD296D1DE601CF4D870AF5883:FG=1; BIDUPSID=99DAFEEFD296D1DE601CF4D870AF5883; PSTM=1541565742; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E5%94%AF%E5%BF%83%E4%B8%BB%E4%B9%89%22%5D%7D; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1541565792; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1541565792; delPer=0; PSINO=7; BDRCVFR[PaHiFN6tims]=9xWipS8B-FspA7EnHc1QhPEUf; H_PS_PSSID='
    }
    look = val.get()
    url1 = 'https://baike.baidu.com/item/' + look
    wb_data = requests.get(url1,headers=headers)
    wb_data.encoding = wb_data.apparent_encoding
    soup = BeautifulSoup(wb_data.text,'lxml')
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
    data = {}
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['client'] = 'fanyideskweb'
    data['doctype'] = 'json'
    data['from'] = 'AUTO'
    data['i'] = look
    data['keyfrom'] = 'fanyi.web'
    data['salt'] = '1533990875380'
    data['sign'] = 'd819545177a604a7a5ef381a1c98c91a'
    data['smartresult'] = 'dict'
    data['to'] = 'AUTO'
    data['typoResult'] = 'true'
    data['version'] = '2.1'
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    #print('翻译结果：%s'%(target['translateResult'][0][0]['tgt']))
    data = str(target['translateResult'][0][0]['tgt'])
    data_end = data + '\n'
    text1.insert(END,str(data_end))
    text = str(soup.select('div.lemma-summary'))
    a = re.compile(r'>(.*?)<').findall(text)
    b = str(''.join(a))
    text2.insert(END,str(b))
def b():
    look = val.get()
    url1 = 'https://baike.baidu.com/item/' + look
    if messagebox.askquestion(title = '信息',message = '确定打开网页吗？') == 'yes':
        print(webbrowser.open(url1))

def P():
    text1.delete('1.0','end')
    text2.delete('1.0','end')

window = Tk()
window.title("简单的查找程序")
window.geometry('600x420')
frame1 = Frame(window)
frame1.pack()
label1 = Label(frame1,text = "请输入查找对象",font=('Arial', 16),width = 16 )
val = StringVar()
entryVal = Entry(frame1,bd = 5,width = 40,textvariable = val)
label1.pack(side = LEFT)
entryVal.pack(side = LEFT)
frame2 = Frame(window)
frame2.pack()
bt1 = Button(frame2, text="查找",font=('Arial', 16), width=16, bg='MintCream', command = run)
bt1.pack()
frame3 = Frame(window)
frame3.pack()
text1 = ScrolledText(frame3,width = 80, height = 10)
text1.pack()
frame4 = Frame(window)
frame4.pack()
text2 = ScrolledText(frame4,width = 80, height = 10)
text2.pack()
frame = Frame(window)
frame.pack()
frame = Frame(window)
frame.pack()
bt = Button(frame, text = "查看更多",font = ('Arial', 16), width = 16, bg = 'MintCream', command = b)
bt.pack()
rebt = Button(frame, text ="我知道了",font=('Arial', 16), width = 16, bg='MintCream', command = P)
rebt.pack()
window.mainloop()
