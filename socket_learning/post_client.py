import socket
import os
sk = socket.socket()
# 创建一个socket对象sk

address = ('127.0.0.1', 8000)
sk.connect(address)
# 连接server端

while True:
    conntent_send = input('>>>').strip()

    if conntent_send == 'exit':
        break
    # 输入exit就退出连接

    elif not conntent_send:
        print('没有内容')
        continue
    # 不能发送None值，就是直接回车，这样server收不到任何消息会一直等到，而client端程序会正常向下执行，因此我在这加了一个判断

    cmd, path = conntent_send.split('|')
    filename = os.path.basename(path)
    # 这里得到需要上传的文件名,
    filesize = os.stat(path).st_size
    # 这里得到上传文件的大小，字节为单位
    filesize = str(filesize)

    file_info = "%s|%s|%s" % (cmd, filename, filesize)
    sk.sendall(bytes(file_info, 'utf8'))
    # send方法输出的内容必须是byte类型，因此这里做转化

    with open(path, 'rb') as f:
        data = 0
        while data != int(filesize):
            content_send = f.read(1024)
            # 这里读出来的是个2进制的content_send，千万不要再去动content_send,将结果发过去。
            # 一定要用data = 0去做循环判断，之前犯过一个错误，导致传输过来的图片，文件都乱码了，就是应为用content_send去做循环中的加法了
            # 一定要记住这个问题，这样写才对
            data += len(content_send)
            sk.sendall(content_send)
    # 这里就是把文件读出来然后一段一段的给发出去

    conntent_recv = sk.recv(1024)
    # 在此阻塞，等待接受消息，1024是一次接受消息的大小
    print('---', str(conntent_recv, 'utf8'))

sk.close()