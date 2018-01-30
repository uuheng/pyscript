import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from selenium import webdriver

save_path = 'i:\\pyscript\\imgs\\zhihu\\'
base_url = 'https://www.zhihu.com/people/zhang-jia-wei/followers?page='
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}


def get_img(img_url, name):
    if img_url == 'https://pic2.zhimg.com/da8e974dc_im.jpg':
        return
    fname = save_path + str(name) + '.jpg'
    img_url = img_url.replace('_im', '')
    print(img_url)
    res = requests.get(img_url, headers=headers)
    if res.status_code == 200:
        with open(fname, 'wb') as fd:
            fd.write(res.content)
    else:
        print(res.status_code)
    return

def main():
    d = webdriver.Chrome()
    for page in range(2, 101):
        start_name = 20*(page-1) + 1
        url = base_url + str(page)
        d.get(url)
        sleep(2)
        data = d.page_source
        soup = BeautifulSoup(data, 'html5lib')
        fans = soup.find(attrs={'id': 'Profile-following'})
        name = start_name
        for pic in fans.find_all('img'):
            #print(pic['src'])
            sleep(2)
            get_img(pic['src'], name)
            name += 1
    d.quit()

if __name__ == '__main__':
    main()