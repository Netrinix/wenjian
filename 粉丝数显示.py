import requests
import time
import os
import re  
def dailichi():
    import random
    daili = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    ]
    dai = random.choice(daili)
    # print(dai)
    head  ={
        'User-Agent':'%s'% dai
    }
    return head

def get_time():
    import datetime
    # now_time = str(datetime.datetime.now())[:10]
    now_time = str(datetime.datetime.now())
    return now_time

    
def main(id):
    url = f'https://api.bilibili.com/x/relation/stat?vmid={id}'
    timee = get_time()
    response = requests.get(url=url,headers=dailichi())
    pep = response.json()['data']['follower']
    return str(timee)+":"+str(pep)


def get_name(id):
    url =f'https://space.bilibili.com/{id}'
    response = requests.get(url=url,headers=dailichi())
    txt = response.text
    name = re.findall('<title>(.*?)的个人空间 - 哔哩哔哩',txt,re.S)[0]
    return name


if __name__ == "__main__":
    id = '546195'
    name = get_name(id)
    # print(name)
    while True:
        # os.system('cls')
        print('\r'+str(name)+'----'+main(id))
        time.sleep(1)
        