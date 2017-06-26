import random
import urllib.request
# 下载网络图片
def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2232375209,863244903&fm=26&gp=0.jpg")