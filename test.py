import requests
import re
class spider(object):
    def __init__(self):
        print("开始爬取页面……")
    #获取地址集合
    def changeurl(self,url,total_page):
        now_page=int(re.search('page_(\d+)',url,re.S).group(1))
        page_group=[]
        for i in range(now_page,total_page+1):
            link = re.sub('page_(\d+).html','page_{0}.html'.format(i),url,re.S)
            page_group.append(link)
        return page_group
    # 获取源码
    def getsource(self,url):
        html=requests.get(url)
        return html.text
    # 先抓大
    def getclass(self,source):
        everyclass=re.findall('<div class="reed">(.*?)</div>',source,re.S)
        return everyclass
    def getinfo(self,eachclass):
        info ={}
        info['标题'] = re.search('rel="bookmark">(.*?)</a>',eachclass,re.S).group(1)
        info['时间']=re.search('<i class="fa fa-clock-o"></i>(.*?)<i class="fa fa-folder-open">',eachclass,re.S).group(1)
        info['链接'] =re.search('<a target="_blank" href="(.*?)" title="',eachclass,re.S).group(1)
        return info
if __name__=='__main__':
    _url ='http://www.zf826.com/page_1.html'
    mspider = spider()
    all_link = mspider.changeurl(_url,20)
    for link in all_link:
        print('正在处理页面：{0}'.format(link))
        html=mspider.getsource(link)
        eachclass = mspider.getclass(html)
        for each in eachclass:
            info = mspider.getinfo(each)
            for inf in info:
                print("{0}:{1}".format(inf,info[inf]))