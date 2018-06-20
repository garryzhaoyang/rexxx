#www.jikexueyuan.com/course/?pageNum=1

import re
import requests

class Spider(object):
    def __init__(self):
        print("开始爬取内容：")
    def changepage(self,url,total_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group=[]
        for i in range(now_page,total_page+1):
            link = re.sub('pageNum=\d+','pageNum={0}'.format(i),url,re.S)
            page_group.append(link)
        return page_group


if __name__== '__main__':
    url = "http://www.jikexueyuan.com/course/?pageNum=1"
    momoSpider = Spider()
    all_links = momoSpider.changepage(url,20)
    print(all_link)