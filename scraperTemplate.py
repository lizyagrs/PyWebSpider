from bs4 import BeautifulSoup# 导入BeautifulSoup

# 获取在线网页信息
def getWebInfo(url):
    import requests#导入工具包
    r=requests.get(url)#向目标网页url发出请求
    r.status_code#查看状态并读取网页内容
    r.encoding = r.apparent_encoding#转换编码方式为"utf-8"
    return r.text #返回网页内容

#结构化网页内容
def PrettifyDoc(html_text):
    soup=BeautifulSoup(html_text,'html.parser')# 将网页信息读入BeautifulSoup中
    prettify_doc = soup.prettify()# 结构化网页信息
    return prettify_doc # 返回结构化后的信息

# 获取本地网页信息函数
def getLocalInfo(url):
    # 打开指定的本地网页文件
    r=open(url,encoding='utf-8')
    html_doc = r.read()# 读取网页脚本
    return html_doc #返回网页内容
    r.close()#关闭连接

if __name__ == '__main__':
    local_url = 'Html/index.html'#本地网页存放路径
    #调用网页请求函数获取网页信息
    html_text=getLocalInfo(local_url)
    # 将网页信息读入BeautifulSoup中
    soup=BeautifulSoup(html_text,'html.parser')
    img_tag = soup.select('img')#查找所有img标签内容
    print('img标签中的src属性值为:')
    for img_line in img_tag:#遍历img标签数组中所有内容
        print(img_line['src']) #取出每条img标签中的src属性





    # p_tag = soup.find_all('p')#获取所有P标签的脚本
    # p_text=p_tag[2].get_text()#获取p_tag索引号为2的内容
    # print('P标签的文本：\n',p_text)

    # #遍历P标签中每一行内容
    # for p_line in p_tag:
    #     print(p_line)
    #     print('   索引号为：',p_tag.index(p_line))

    # p_text=soup.find('p').text
    # print('p标签的文本：\n',p_text)



    #
    # h2_text=soup.find('h2').text
    # print('h2标签的文本：\n',h2_text)

    # 获取html对象中的所有文本内容
    # all_text = soup.get_text()
    # print('所有title标签的文本：\n',all_text.strip())
    # #查找所有title标签的脚本
    # title_tag = soup.find_all('title')
    # print('所有title标签的脚本：\n',title_tag)
    # #查找所有img标签的脚本
    # all_img_tag = soup.select('img')
    # print('所有img标签的脚本：\n',all_img_tag)


    # # print(html_text) #输出网页内容
    # prettify_doc=PrettifyDoc(html_text)
    # print(prettify_doc)# 输出结构化后的网页信息



    # url='http://www.weather.com.cn/'#目标网址
    # html_text=getWebInfo(url)#调用方法获取网页信息
    # print(html_text) #输出网页内容
