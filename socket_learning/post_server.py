import socket
import os
sk = socket.socket()
# 创建一个socket对象sk

address = ('127.0.0.1', 8000)
sk.bind(address)
# bind方法绑定server端的ip和端口号

sk.listen(3)
# listen方法监听端口，3表示最大的连接等待数量，比如一个client正在和server聊天，此时可以再连接3个client上来但不能和server聊天要等前面那个聊完才行，第四个就无法连接上来了会报错，这就是限制连接等待数量
print('waiting...')

while True:
    conn, addr = sk.accept()
    # 在此阻塞，等待client来连接，然后再向下运行
    print(conn, addr)
    # conn对象就是client端的socket对象，addr就是client端的ip和端口号

    while True:
        conntent_recv = conn.recv(1024)
        # 在此阻塞，等待接受消息，1024是一次接受消息的大小
        conntent_recv = str(conntent_recv, 'utf8')
        cmd, filename, filesize = conntent_recv.split('|')
        data_path = r"H:\mlc_python_practice\exercise_library\socket_learning\data"
        path = os.path.join(data_path, filename)
        f = open(path, 'ab')
        # 在server端要放文件的地方，把这个文件创建出来
        filesize = int(filesize)
        data = 0
        while data != filesize:
            conntent_recv = conn.recv(1024)
            data += len(conntent_recv)
            # 和那个client端一样，要注意，不能犯同样的错误
            f.write(conntent_recv)
            f.flush()
            # f.flush是用来清空缓存
        f.close()
        # 这里就是一段一段的把文件接收过来

        conn.send(bytes('success', 'utf8'))
        # send方法输出的内容必须是byte类型，因此这里做转化

sk.close()
# 关闭server端，一般是不会关闭的。pycharm报错unreachable code，执行不到这个代码，哈哈，确实执行不到这里
