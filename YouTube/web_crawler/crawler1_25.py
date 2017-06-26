# 查看beautifulsoup4是？ request模块是？

import requests
from  bs4 import BeautifulSoup


#获取京东悬疑推理书籍
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://list.jd.com/list.html?cat=1713,3258,3304&page='+str(page)+'&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
        # print()
        source_code = requests.get(url)
        # print(source_code)
        plain_text = source_code.text
        # print(plain_text)
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('a'):
            print(link.get('href'))
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for item_name in soup.findAll('div',{'class':'i-name'}):
        print(item_name.string)

trade_spider(1)