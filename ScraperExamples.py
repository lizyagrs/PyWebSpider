#coding:utf-8
import re
from bs4 import BeautifulSoup# 导入BeautifulSoup
import requests#导入工具包
import pandas as pd

# 获取在线网页信息
def getWebInfo(url):
    r=requests.get(url)#向目标网页url发出请求
    r.status_code#查看状态并读取网页内容
    r.encoding = r.apparent_encoding#转换编码方式为"utf-8"
    return r.text #返回网页内容

#结构化网页内容
def PrettifyDoc(html_text):
    soup=BeautifulSoup(html_text,'html.parser')# 将网页信息读入BeautifulSoup中
    prettify_doc = soup.prettify()# 结构化网页信息
    return prettify_doc # 返回结构化后的信息

if __name__ == '__main__':

    # 1.获取网页信息
    url='https://www.timeanddate.com/weather/'#目标网址
    html_text=getWebInfo(url)#调用方法获取网页信息
    # print(html_text) #输出网页内容
    # 结构化网页信息测试
    # print(20*'-----')
    # prettify_doc=PrettifyDoc(html_text)
    # print(prettify_doc)# 输出结构化后的网页信息

    # 2.获取指定区域内容【标签或者CSS样式类】
    print('---获取指定区域内容【标签或者CSS样式类】--------')
    # 将网页信息读入BeautifulSoup中
    soup=BeautifulSoup(html_text,'html.parser')
    # 获取  <table> 标签所有内容
    table_on_label = soup.find_all('table')
    # print(table_on_label)
    # 将网页信息读入BeautifulSoup中
    soup_table=BeautifulSoup(str(table_on_label),'html.parser')
    prettify_doc = soup_table.prettify()# 结构化网页信息
    print(prettify_doc)# 输出结构化后的网页信息

    # 3.获取表格当中的内容
    print('--------获取表格当中的内容------')

    # 获取城市名列表
    city_name_label_list=soup_table.select('td > a')
    # print(city_name_label_list)
    city_list=[]
    for city_name in city_name_label_list:
        city_list.append(city_name.text)
    print(city_list)

    # 获取时间数值列表,td[id]表示在td标签中是否有id
    # 也可以使用soup.find_all(id=True)
    time_label_list=soup_table.select('td[id]')
    # print(time_label_list)
    time_list=[]
    for time_label in time_label_list:
        time_list.append(time_label.text)
    print(time_list)

    # 获取图片链接列表,img ，并且获取天气类型名称
    img_label_list=soup_table.find_all('img')
    # print(img_label_list)
    src_list=[]
    weatherType_list=[]
    for img in img_label_list:
        src_list.append('https:'+img['src'])
        weatherType_list.append(img['alt'])
        # print('图片网址：https:'+img['src']+':::天气类型：'+img['alt'])
    print(src_list)
    print(weatherType_list)
    # 获取温度数值列表
    temp_label_list = soup_table.find_all('td',class_='rbi')
    # print(temp_label_list)
    temp_list=[]
    for temp in temp_label_list:
        temp_list.append(temp.text.replace('\xa0', ''))
    print(temp_list)

    # print('---------------------------获取表中的数据区域信息---------------------------')

    # data = [city_list,time_list,src_list,weatherType_list,temp_list]
    data = {
        'City':city_list,
        'Date':time_list,
        'Src':src_list,
        'weatherType':weatherType_list,
        'Temperature':temp_list
    }
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('Data/Temperature.csv',encoding='GB18030')





