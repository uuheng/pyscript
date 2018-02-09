import requests
from time import sleep
from bs4 import BeautifulSoup

headers = {
    'referer':'http://blog.csdn.net/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'
}

cnt = [0] * 66

def look(url, index):
    res = requests.get(url, headers=headers)
    print(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    vis_num = soup.find('button', attrs={'class': "btn-noborder"}).find('span').string
    print(vis_num)
    print(cnt[index])
    cnt[index] = int(vis_num)

def getArts():
    base_url = 'http://blog.csdn.net/qq_39091609/article/list/'
    ans_list = []
    arts = []
    for i in range(1, 5):
        url = base_url + str(i)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content, 'html5lib')
        ans_list += soup.find_all('li', attrs={'class': 'blog-unit'})
    #for art in arts:
    #    #print(art.find('a')['href'])
    #    look(art.find('a')['href'])
    #    #sleep(3)
    #print(len(arts))
    for tmp in ans_list:
        arts.append(tmp.find('a')['href'])
    return arts
if __name__ == '__main__':
    items = getArts()
    while True:
        for item in items:
            index = items.index(item)
            look(item, index)
            sleep(2)
        sleep(20)
    #while True:
        #getArt()
        #sleep(10)