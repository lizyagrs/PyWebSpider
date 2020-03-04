import urllib.request as req
import re

#获取全部hmtl网页内容
def get_content(url):
    webpage = req.urlopen(url) # 根据超链访问链接的网页
    html = webpage.read() # 读取超链网页数据
    html = html.decode('utf-8') # byte类型解码为字符串
    print(html)
    return html

#从网页中获取指定标签数据
def get_data(html,label):

    table = re.findall(label, html, re.S)
    print('-----------取出全部数据-----------')
    print(table)
    #获取table数组长度
    ncount_table = len(table)
    #遍历所有数组
    for i in range(ncount_table):
        print('-----------取出数据中的第'+str(i+1)+'组数据-----------')
        #取出数据中的第三组数据
        subtable = table[i]
        print(subtable)
    return table

if __name__ == '__main__':
    #目标网站
    url ='http://www.weather.com.cn/'
    html =get_content(url)

    label = r'<ul class="on"(.*?)</ul>'
    #table =get_data(html,label)

    li_label = r'<li>(.*?)</li>'
    #li_data =get_data(table[0],li_label)
    #获取table数组长度
    #ncount_li_data = len(li_data)

    # span_label = r'<span(.*?)</span>'
    # #遍历所有数组
    # for i in range(ncount_li_data):
    #     #取出数据中的第三组数据
    #     subtable = get_data(li_data[i],span_label)
