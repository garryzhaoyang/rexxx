from lxml import etree
import requests
url='http://www.zf826.com/'
html=requests.get(url)
Selector = etree.HTML(html.text)
content=Selector.xpath('//div[@class="reed"]')
for each in content:
    title = each.xpath('h2/a/text()')[0]
    fubiaoti=each.xpath('h6/text()')[0]
    category=each.xpath('h6/a/text()')[0]
    href=each.xpath('div[@class="reednr"]/a/@href')[0]
    summary=each.xpath('div[@class="reednr"]/a/p/text()')[0]
    print("标题：{0}".format(title))
    print("时间:{0}".format(fubiaoti))
    print("分类：{0}".format(category))
    print("链接:{0}".format(href))
    print("摘要:{0}".format(summary))