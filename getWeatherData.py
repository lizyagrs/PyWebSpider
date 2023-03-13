#coding=utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd

def getWebInfo(url):
    r = requests.get(url)
    r.status_code
    r.encoding = r.apparent_encoding
    return r.text


if __name__ == '__main__':
    url = 'https://weather.cma.cn/'
    html_text = getWebInfo(url)
    #print(html_text)
    soup = BeautifulSoup(html_text,'html.parser')
    #hot_data = soup.find_all(id='HOT')
    hot_tag = soup.select('#HOT')
    #print(hot_tag)

    rank_list=[]; sname_list=[];pname_list=[];value_list=[];

    soup_class_hot = BeautifulSoup(str(hot_tag),'html.parser')
    rank = soup_class_hot.find_all(class_='rank')
    for r in rank:
        rank_list.append(r.text.strip())
    print(rank_list)
    print(10 * '---------')
    sname = soup_class_hot.select(' .sname')
    for s in sname:
        sname_list.append(s.text.strip())
    print(sname_list)
    print(10 * '---------')
    pname = soup_class_hot.select(' .pname')
    for p in pname:
        pname_list.append(p.text.strip())
    print(pname_list)
    print(10 * '---------')
    value = soup_class_hot.select(' .value')
    for v in value:
        value_list.append(v.text.replace('\xa0', '').strip())
    print(value_list)

    data={
        "rank":rank_list,
        "sname":sname_list,
        "pname":pname_list,
        "value":value_list
    }
    print(data)
    hot_df = pd.DataFrame(data)
    print(hot_df.head())
    hot_df.to_csv('Data/weatherHotData.csv', encoding='utf_8_sig')



