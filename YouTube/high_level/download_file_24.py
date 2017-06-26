from urllib import request

# 从网上下载文件
book_url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1495725279&period2=1498403679&interval=1d&events=history&crumb=MC74VOgfcPo"


def download_stock_data(url):
    response = request.urlopen(url)
    book = response.read()
    book_content = str(book)
    book_lines = book_content.split("\\n")
    dest_url = r'goog.csv'

    fx = open(dest_url, 'w')
    for line in book_lines:
        fx.write(line + "\n ")
    fx.close()

#Error ：未授权错误
download_stock_data(book_url)
