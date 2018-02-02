# 实现并发；client端
import socket

ip_port = ('127.0.0.1', 8080)
sk = socket.socket()
sk.connect(ip_port)
print('client端启动了')

while True:
    inp = input('请输入：')
    sk.sendall(bytes(inp, 'utf8'))
    if inp == 'exit':
        break
    server_response = sk.recv(1024)
    print(str(server_response, 'utf8'))

sk.close()
