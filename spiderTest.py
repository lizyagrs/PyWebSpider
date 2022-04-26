# -*- coding: utf-8 -*-
import urllib.request as req
import re
import numpy as np
import pandas as pd

#获取全部hmtl网页内容
def get_content(url):
    webpage = req.urlopen(url) # 根据超链访问链接的网页
    html = webpage.read() # 读取超链网页数据
    html = html.decode('utf-8') # byte类型解码为字符串
    #print(html)
    return html

#从网页中获取指定标签数据
def get_data(html,label):

    table = re.findall(label, html, re.S)
    #获取table数组长度
    ncount_table = len(table)
    #遍历所有数组
    for i in range(ncount_table):
        #print('-----------取出数据中的第'+str(i+1)+'组数据-----------')
        #取出数据中的数据
        subtable = table[i]
        #print(subtable)
    return table


def getDataFrom(url):
    #目标网站
    #url ='http://www.weather.com.cn/'
    html =get_content(url)

    print('---------------------------label---------------------------')
    label = r'<ul class="on"(.*?)</ul>'
    table =get_data(html,label)
    print('-----------取出全部指定标签数据-----------')
    print(table)

    li_label = r'<li>(.*?)</li>'
    li_data =get_data(table[0],li_label)
    print('-------------------------指定li_label标签中数据------------------------')
    print(li_data)
    #获取table数组长度
    ncount_li_data = len(li_data)

    print('---------------------------span_label---------------------------')
    #指定城市名的标签
    span_city_label = r'<span class="city">(.*?)</span>'
    #指定省名的标签
    span_pro_label = r'<span class="prov">(.*?)</span>'
    #指定温度的标签
    span_wd_label = r'<span class="wd"(.*?)</span>'

    #气象数据列表
    weather_list=[]

    #如果数组不为空
    if len(li_data)>0:
        #遍历所有数组
        for i in range(ncount_li_data):
            #每一行的数据组合
            sub_list = []
            if li_data[i] is not None:
                sub_list.append(i+1)
            #取出数据中的第三组数据
            subtable_city = get_data(li_data[i],span_city_label)
            print('-------------------------指定span_city_label标签中数据：城市名------------------------')
            print(subtable_city)

            #取字段名称的公共标签
            field_label = r'>(.*?)<'

            #如果数组不为空
            if len(subtable_city) > 0:
                city_name = get_data(subtable_city[0],field_label)
                print('城市名：'+str(city_name))
                if city_name[0] is not None:
                    sub_list.append(city_name[0])
            subtable_pro = get_data(li_data[i],span_pro_label)
            print('-------------------------指定span_pro_label标签中数据：省名------------------------')
            print(subtable_pro)
            #如果数组不为空
            if len(subtable_pro)>0:
                pro_name = get_data(subtable_pro[0],field_label)
                print('省名：'+str(pro_name))
                if pro_name[0] is not None:
                    sub_list.append(pro_name[0])

            subtable_wd = get_data(li_data[i],span_wd_label)
            print('-------------------------指定span_wd_label标签中数据：温度------------------------')
            print(subtable_wd)
            #如果数组不为空
            if len(subtable_wd):
                wd_value = get_data(subtable_wd[0],field_label)
                print('温度：'+str(wd_value))
                if wd_value[0] is not None:
                    sub_list.append(wd_value[0])
            weather_list.append(sub_list)
            print(weather_list)
    #准备数据集
    pd_data = pd.DataFrame(weather_list)
    #表格列名，为输出EXCEL做准备
    colunms=['Num','city','prov','wd']
    #添加列名
    pd_data.columns=colunms
    print(pd_data)
    ExcelName=r'Data\WeatherArray.xlsx'
    sheetName='Weather'
    WriteExcel(pd_data,ExcelName,sheetName)


#写入EXCEL
def WriteExcel(pd_data,ExcelName,sheetName):

    writer = pd.ExcelWriter(ExcelName)		# 写入Excel文件
    pd_data.to_excel(writer, sheetName,index=False)		# 写入excel的sheet名
    writer.save()
    writer.close()
    print('Done:'+ExcelName)


if __name__ == '__main__':
    #目标网站
    url ='http://www.weather.com.cn/'
    getDataFrom(url)
