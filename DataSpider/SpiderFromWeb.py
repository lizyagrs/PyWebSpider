import urllib.request as req
import re

#获取全部hmtl网页内容
def get_content(url):
    #url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    webpage = req.urlopen(url) # 根据超链访问链接的网页
    html = webpage.read() # 读取超链网页数据
    html = html.decode('utf-8') # byte类型解码为字符串
    #print(html)
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
        # 数据清洗，将表中的&nbsp;和空格号去掉
        subtable = subtable.replace('&nbsp;', '')
        #空格
        subtable = subtable.replace(' ', '')
        print(subtable)
    return table

if __name__ == '__main__':
    #目标网站
    url ='https://ncov.dxy.cn/ncovh5/view/pneumonia'
    html =get_content(url)
    #用指定标签取对应内容，较为精准的ID指定
    #label = r'<script id="getAreaStat(.*?)</script>'
    #所有id中包含get的数据
    label = r'<script id="get(.*?)</script>'
    table =get_data(html,label)

    #获取省数据，指定省数据标签
    province_label = r'"provinceName":(.*?)00'
    #分省数据为第三个get的数组，因此这里拆分第三组的分省数据，数组从0开始，因此第三组的索引为2
    province_data = get_data(table[2],province_label)

    #获取各处所有城市数据,指定城市数据标签
    pro_city_label = r'"cities"(.*?)"provin'
    #仍然从分省数据中获取数值
    pro_city_data = get_data(table[2],pro_city_label)

