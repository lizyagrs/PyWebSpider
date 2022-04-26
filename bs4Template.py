# 打开指定的本地网页文件
r=open('Html/index.html',encoding='utf-8')
# 读取网页脚本
html_text = r.read()
#输出网页内容
print(html_text)
r.close()

# 结构化前后对比分隔线
print(3*'------------------------结构化后-------------------------')
#结构化网页内容
def PrettifyDoc(html_text):
    from bs4 import BeautifulSoup# 导入BeautifulSoup
    soup=BeautifulSoup(html_text,'html.parser')# 将网页信息读入BeautifulSoup中
    prettify_doc = soup.prettify()# 结构化网页信息
    return prettify_doc # 返回结构化后的信息

prettify_doc=PrettifyDoc(html_text)
print(prettify_doc)# 输出结构化后的网页信息