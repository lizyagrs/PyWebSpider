import requests
from bs4 import BeautifulSoup
import re
#结构化网页内容
def PrettifyDoc(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    prettify_doc = soup.prettify()
    print(prettify_doc)
    return prettify_doc

#获取网页所有文本内容
def getTextFromDoc(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    prettify_doc = soup.prettify()
    HTML_Text = soup.get_text()
    print(HTML_Text)
    return HTML_Text

#获取网页指定标签内容
def getTagContentFromDoc(html_doc,tagName):
    soup = BeautifulSoup(html_doc, 'html.parser')
    prettify_doc = soup.prettify()
    # HTML_title = soup.title
    # print(HTML_title)
    HTML_Text = soup.find_all(tagName)
    print(HTML_Text)
    return HTML_Text

#从网页中获取指定表达式内容数据
def get_data(html,label):
    # print(html)
    table = re.findall(label, html, re.S)
    print(table)
    #获取table数组长度
    ncount_table = len(table)
    #遍历所有数组
    for i in range(ncount_table):
        #取出数据中的数据
        subtable = table[i]
        print(subtable)
    return table


#请求并获取网页内容
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

#主函数
if __name__ == '__main__':
    #目标网站
    url ='http://lishi.tianqi.com/wuhan'
    #返回的网页内容
    HTMLContent = getHTMLContent(url)
    #打印网页内容
    # print(HTMLContent)
    pDoc=PrettifyDoc(HTMLContent)
    # HTML_Text=getTextFromDoc(HTMLContent)
    soup = BeautifulSoup(HTMLContent, 'html.parser')
    title_name = soup.select('.tian_two')
    print(title_name)



