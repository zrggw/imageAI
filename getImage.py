import re
import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie':'BIDUPSID=60AB8858690C9490497B054126608C85; PSTM=1571381343; BAIDUID=A658AD722926CC3E71620AA95A2973FC:SL=0:NR=10:FG=1; '
            'BDUSS=2tvVnJaWlg5cE5rSVN-NWJwSDBjNHM3amRhQlpDbmUwMXIwNHB5Q280c2FOR0JnRVFBQUFBJCQAAAAAAAAAAAEAAADpJPcuuPjE43jJz8nPx6kAAAAAA'
            'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABqnOGAapzhgN; BDUSS_BFESS=2tvVnJaWlg5cE5rSVN-NWJwSDBjNHM3amRhQlpDbmUwMXIwNHB5Q280c'
            '2FOR0JnRVFBQUFBJCQAAAAAAAAAAAEAAADpJPcuuPjE43jJz8nPx6kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABqnOGAapzhgN; MCITY=-:; '
            '__yjs_duid=1_b41f80774f4a5ca4e122147a7b9ca4411619777099951; BAIDUID_BFESS=47FB065C13B0BEF7B729E985F3FA8351:FG=1; H_PS_PSSID=34099_33971_33848_338'
            '55_33607_26350; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=cn.bing.com; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_ZmVlYzgzY2FjOTdlZjg5ZmYyODIyMDg1'
            'YmYwNGVhYWMyMzQ0N2VjNDNiOGY4NDM4NGMyZTI0M2NmMDVkODRjYjM1ZjI2YTliZWEwODc3YTQ1Y2FhNWU3YWJlODFmNjllNjU0NzlhNGQyNGE3YzVmMGVhYWI4YjI1MDQyNGEwYWQ1ZDdlMjU4Mjk'
            '2Y2IwYWQ3ZTZhNjYwZWIyNzEyODc4ZTk4MTYzYzcxZmNjZTE3NzVlMTQ0ZmFlMWYzNDdiMGQ3'
    # 'Cookie':'MUID=0A81BA82A58260491A52B77FA18266C7; SRCHD=AF=NOFORM; MUIDB=0A81BA82A58260491A52B77FA18266C7; SRCHUID=V=2&GUID=4F07879ABF3A4DC4B48'
    #          'C7CCE8ADB8019&dmnchg=1; PPLState=1; KievRPSSecAuth=FABaARRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACEdKOPoYRMpzGAHRcz7PetzXxJCesh8e+Ela2TnKOcB'
    #          '6LjOGr/c2gdEO8YvUoP5C/+8tETXMWh6mzt0pBA4c3L/nfEI7oJ2qA91wmE3PxpHCrEEOn3ArSKkS2aRxdDH2OSg6g4DSp0tSvFmBF1bUVB4L0eD3m99zHOWwPqd7QdWzQj1jOR7ou'
    #          'AyObhlKOh8vDmlrfBaaZXjMUUK1qcKVMPsBnHWpq8HVBdO3oR3U3kWLkTepC930m8Lxi/x/oab79e77SGyZdoxcV/3VH/v7HO97bnNQpN5H7c7/164yYfcjJYf4celjwIk6FRewk1Kfmwz'
    #          'h6wd9XwXwe0ATRH94PEbUuo1/yhi3zAH+F/lV+jCMkZxggYe1Jm/fZisFnFDFr3r8FAAevyF9JY7fI2MtkKL5ifgptjZDGg==; ULC=P=11378|1:1&H=11378|1:1&T=11378|1:1; A'
    #          'NON=A=A4FBF10FE588E1E50CEC3111FFFFFFFF&E=1866&W=1; MUIDB=0A81BA82A58260491A52B77FA18266C7; _EDGE_V=1; _RwBf=mtu=0&g=0&cid=&o=2&p=&c=&t=0&'
    #          's=0001-01-01T00:00:00.0000000+00:00&ts=2021-05-23T14:24:53.6883658+00:00&ssg=0; _TTSS_IN=hist=WyJldCIsInpoLUhhbnMiLCJlbiIsImF1dG8tZGV0ZWN0Il0=;'
    #          ' _TTSS_OUT=hist=WyJhZiIsInpoLUhhbnMiLCJlbiJd; _tarLang=default=en; SerpPWA=RegSWM=1; ABDEF=ABDV=11&MRNB=1623341763274&MRB=0&V=1; WLS=C='
    #          '28a19eb244005f67&N=浩斌; SRCHS=PC=U531; _EDGE_S=SID=395C94796914682F0039842A683A69C8&ui=zh-cn; _ITAB=STAB=TR; _SS=SID=395C94796914682F0039842A6'
    #          '83A69C8&PC=U531&bIm=966966; SRCHUSR=DOB=20200317&T=1623422977000; ipv6=hit=1623426578969&t=4; SNRHOP=I=&TS=; _U=10pwHuqPvBbd0EemrnIfnGWWfIlz'
    #          '5BDAgOGyF1vChtrK8prWk748huPBtJgYeJhH8PNriD29eFDZnr0_RT_QiwgxAp9ZB1QEaORfdmDrXkX9xjO9iLIxRqJuueqMZo1dbAskFr-6Dx8qDx36Mu2F5QeSVoW_ep7cAERr62CkE'
    #          'P6TTW4B7MIOHvJHupQqSMlaFJvdjgs1YTyET9cUXY3R6lA; SRCHHPGUSR=CW=944&CH=737&DPR=1.25&UTC=480&WTS=63722386038&HV=1623423877&DM=0&BRW=HTP&BRH='
    #          '&BZA=0&PLTL=1066&PLTA=1337&PLTN=346&EXLTT=31&SRCHLANG=zh_CHS&SRCHLANGV2=zh-Hans'
}
num = 0
url=[]
def one(keyword,page):
    global url
    for i in range(1,page+1):
        url1 = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={}&pn={}'.format(keyword, page)
        # url1 = 'https://cn.bing.com/images/search?q={}&pn={}'.format(keyword, page)
        data = requests.get(url1,headers=headers)
        pat = '"objURL":"https://(.*?)"'
        link = re.compile(pat).findall(data.text)
        url = link+url
    print(len(url))
       # yield url

def tow(keyword):
    global url,num
    if keyword not in os.listdir('C:/Users/黄浩斌/Desktop/train/img'):#如果桌面没有此文件夹，创建对应的文件夹
        os.makedirs(f"C:/Users/黄浩斌/Desktop/train/img\{keyword}")
       # os.makedirs(f"C:/Users/黄浩斌/Desktop/train/img\{keyword}" )
    for i in url:
        image_url = 'https://'+i#补全链接
        print('正在下载：'+image_url)
        data = requests.get(image_url, headers=headers)
        num = num+1
        # with open('C:/Users/黄浩斌/Desktop/train/img'+keyword + '/' + str(num) + '.jpg', 'wb') as file:
        with open('C:/Users/黄浩斌/Desktop/train/img'+'/' + str(num) + '.jpg', 'wb') as file:
            file.write(data.content)
        print(f'已下载{num}张图片')
        if(num%60==0):
            print('*' * 600)

if __name__ == "__main__":
    keyword = input('输入要下载的内容：')
    n = input('下载页数：')
    one(keyword,int(n))
    tow(keyword)
    print('下载完成！！！')
