import requests
from bs4 import BeautifulSoup


def PrettifyDoc(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    prettify_doc = soup.prettify()
    print(prettify_doc)
    return prettify_doc


def getHTMLContent(url):
    try:
        r=requests.get(url,timeout=20)
        #请求状态，如果是200，则成功，否则产生HTTP异常
        r.status_code
        #编码方式，默认为"utf-8"
        r.encoding = r.apparent_encoding
        #返回网页的内容
        return r.text
    except:
        return "出现异常！请检查代码或者网页是否有效"

if __name__ == '__main__':
    #目标网站
    url ='https://github.com/lizyagrs'
    #返回的网页内容
    HTMLContent = getHTMLContent(url)
    #打印网页内容
    print(HTMLContent)
    print("----------------------------------------------------------------------------------------------")
    PrettifyDoc(HTMLContent)