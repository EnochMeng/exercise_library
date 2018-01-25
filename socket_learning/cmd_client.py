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

    cmd_len = int(str(sk.recv(1024), 'utf8'))
    print(cmd_len)

    sk.send(bytes('ok', 'utf8'))
    # 对应server端来解决 粘包 问题

    content_recv = bytes()
    while len(content_recv) != cmd_len:

        content_recv += sk.recv(1024)
    # 在此阻塞，等待接受消息，1024是一次接受消息的大小;上面这个循环主要是解决我们一次无法接受完超过1024字节的数据，因此用这个来不断的接受数据，保证能接受完
    print('---', str(content_recv, 'gbk'))
    # 这里使用gbk进行解码，是因为server端那边是运用gbk进行编码的，因此这边要用gbk进行解码

sk.close()