import requests
import re
url = 'https://www.crowdfunder.com/?q=filter&page=3'

# print(html.text)

html = requests.get(url)
title = re.findall('<div class="card-title">(.*?)</div>',html.text,re.S)
print(title)
