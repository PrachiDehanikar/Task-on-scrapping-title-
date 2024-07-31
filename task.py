import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qurl = 'https://books.toscrape.com/'

qheader = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36'
}

qresp = rq.get(url = qurl, headers= qheader)

bsoup = BeautifulSoup(qresp.content , 'html.parser')


def removenavigablestring(value):
    return list(filter(lambda x : type(x)!= NavigableString , value))

ochild=removenavigablestring( bsoup.ol.children)
# print(ochild[0].h3.getText())

titles =[ol.h3.getText() for ol in ochild]

print(titles[4:10])