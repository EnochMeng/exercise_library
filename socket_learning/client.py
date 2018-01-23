import socket

sk = socket.socket()
# 创建一个socket对象sk

address = ('127.0.0.1', 8000)
sk.connect(address)
# 连接server端

while True:
    conntent_send = input('>>>')
    if conntent_send == 'exit':
        break
    # 输入exit就退出连接

    elif not conntent_send:
        print('没有内容')
        continue
    # 不能发送None值，就是直接回车，这样server收不到任何消息会一直等到，而client端程序会正常向下执行，因此我在这加了一个判断

    sk.send(bytes(conntent_send, 'utf8'))
    # send方法输出的内容必须是byte类型，因此这里做转化

    conntent_recv = sk.recv(1024)
    # 在此阻塞，等待接受消息，1024是一次接受消息的大小
    print('---', str(conntent_recv, 'utf8'))

sk.close()