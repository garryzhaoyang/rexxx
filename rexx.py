#导入re库文件
import re

f = open('re_html.html','r',encoding='utf-8')
html = f.read()
f.close()
title = re.search('<title>(.*?)- SuperVan - 博客园</title>',html,re.S).group(1)
print("网页标题为：{0}".format(title))

#爬取链接
text_fied = re.findall('<ul id="navList">(.*?)</ul>',html,re.S)[0]
href = re.findall('href="(.*?)</a>',text_fied,re.S)
print(href)
