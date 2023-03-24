#coding=utf-8
import json
import re
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def getWebInfo(url):
    r = requests.get(url)
    r.status_code
    r.encoding = r.apparent_encoding
    return r.text

def getInfoFromCMA(url):
    html_text = getWebInfo(url)
    # print(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    # hot_data = soup.find_all(id='HOT')
    hot_tag = soup.select('#HOT')
    # print(hot_tag)

    rank_list = [];
    sname_list = [];
    pname_list = [];
    value_list = [];

    soup_class_hot = BeautifulSoup(str(hot_tag), 'html.parser')
    rank = soup_class_hot.find_all(class_='rank')

    for r in rank:
        if '排名' not in r.text:
            rank_list.append(r.text.strip())
    print(rank_list)

    sname = soup_class_hot.select(' .sname')
    for s in sname:
        if '城市' not in s.text:
            sname_list.append(s.text.strip())
    print(sname_list)

    pname = soup_class_hot.select(' .pname')
    for p in pname:
        if '省份' not in p.text:
            pname_list.append(p.text.strip())
    print(pname_list)

    value = soup_class_hot.select(' .value')
    for v in value:
        if '温度' not in v.text:
            value_list.append(v.text.strip())
    print(value_list)

    p_rank = pd.Series(rank_list)
    print(p_rank)

    p_sname = pd.Series(sname_list)
    print(p_sname)

    p_pname = pd.Series(pname_list)
    print(p_pname)

    p_value = pd.Series(value_list)
    print(p_value)

    data = {'排名': p_rank,
            '城市':p_sname,
            '省份':p_pname,
            '最高温度':p_value
    }



    print(data)
    hot_df = pd.DataFrame(data)
    print(hot_df.head())
    hot_df.to_csv('Data/weatherHotData.csv', encoding='utf_8_sig',index=False)


# 获取动态网站加载数据
def getInfoFromWeatherCOM(url):
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    data = driver.page_source
    driver.close()
    soup = BeautifulSoup(data, 'lxml')
    hot_rank = soup.find_all('ul',class_='on')
    # print(hot_rank)
    rank_soup = BeautifulSoup(str(hot_rank),'lxml')
    rank_column = rank_soup.select("[class~=pi]")
    # print(rank_column)
    for column in rank_column:
        rank_name = column.find(class_="sort").text
        city_name = column.find(class_='city').text
        prov_name = column.find(class_='prov').text
        temp_name = column.find(class_='lastTemp').text
    col_names = [rank_name, city_name, prov_name, temp_name]
    print(col_names)

    rank_span = rank_soup.select(' li > span')
    print(rank_span)
    rank_list = []
    city_list = []
    prov_list=[]
    temp_list=[]
    href_list =[]

    i=0
    for span in rank_span:
        i=i+1
        if '排名' not in span.text and '城市' not in span.text \
                and '所属省' not in span.text and '最高气温(出现时间)' not in span.text\
                and '资料统计' not in span.text:
            print('i:{}'.format(i))
            print('span:{}'.format(span.text))
            if (i- 5) % 4 == 0:
                rank_list.append(span.text)
            if (i - 6) % 4 == 0:
                city_list.append(span.text)
            if (i - 7) % 4 == 0:
                prov_list.append(span.text)
            if (i - 8) % 4 == 0:
                temp_list.append(span.text)

    print(str(len(temp_list)))
    data = {
        "rank": rank_list,
        "sname": city_list,
        "pname": prov_list,
        "value": temp_list
    }

    hot_df = pd.DataFrame(data)
    print(hot_df.head())
    hot_df.to_csv('Data/weatherComHotData.csv', encoding='utf_8_sig')



    # for hot in hot_rank:
    #     if '<li>' in str(hot):
    #         print(hot.get_text('span'))

def getTimedata(url):
    html_text = getWebInfo(url)
    pd_data = pd.read_html(html_text)[0]
    print(pd_data)
    pd_data.to_csv('Data/timeAndDate.csv',encoding=' utf_8_sig')




if __name__ == '__main__':
    url = 'https://weather.cma.cn/'
    getInfoFromCMA(url)

    # url = ' http://www.weather.com.cn/'
    # getInfoFromWeatherCOM(url)

    # url = 'https://www.timeanddate.com/weather/?low=c'  # 目标网址
    # # url = ' https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
    # getTimedata(url)  # 调用方法获取网页信息




