

# 获取在线网页信息
def getWebInfo(url):
    import requests#导入工具包
    r=requests.get(url)#向目标网页url发出请求
    r.status_code#查看状态并读取网页内容
    r.encoding = r.apparent_encoding#转换编码方式为"utf-8"
    return r.text #返回网页内容

url='http://www.weather.com.cn/'#目标网址
html_text=getWebInfo(url)#调用方法获取网页信息
print(html_text) #输出网页内容

# 获取本地网页信息函数
def getLocalInfo(url):
    # 打开指定的本地网页文件
    r=open(url,encoding='utf-8')
    html_doc = r.read()# 读取网页脚本
    print(html_doc)#输出网页内容
    return html_doc #返回网页内容
    r.close()#关闭连接

#结构化网页内容
def PrettifyDoc(html_text):
    from bs4 import BeautifulSoup# 导入BeautifulSoup
    soup=BeautifulSoup(html_text,'html.parser')# 将网页信息读入BeautifulSoup中
    prettify_doc = soup.prettify()# 结构化网页信息
    return prettify_doc # 返回结构化后的信息

local_url = 'Html/index.html'#本地网页存放路径
html_text=getLocalInfo(local_url)#调用方法获取网页信息
print(html_text) #输出网页内容
prettify_doc=PrettifyDoc(html_text)
print(prettify_doc)# 输出结构化后的网页信息
