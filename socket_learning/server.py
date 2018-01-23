import socket
import subprocess
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
        try:
            conntent_recv = conn.recv(1024)
            # 在此阻塞，等待接受消息，1024是一次接受消息的大小
        except Exception as e:
            print('client端异常关闭')
            break
        # 这里的捕获异常用来防止，当client端直接关闭程序时，server端会报错导致server端无法正常运行，这里捕获到异常然后跳出while，让server端可以正常重新连接其他client端

        if not conntent_recv:
            print('client端关闭连接')
            break
        # 这里是因为当client端sk.close()正常关闭连接时，server端会接收到一个None值，因此做判断。

        print('---', str(conntent_recv, 'utf8'))

        if str(conntent_recv, 'utf8') == 'cmd':
            cmd_conntent = conn.recv(1024)
            cmd_reslut = subprocess.Popen(cmd_conntent, shell=True, stdout=subprocess.PIPE)
            cmd_rcmd_reslut.stdout.read()
        # 这里用来做cmd ssh的远程命令控制台，还没写完

        conntent_send = input('>>>')
        conn.send(bytes(conntent_send, 'utf8'))
        # send方法输出的内容必须是byte类型，因此这里做转化

sk.close()
# 关闭server端，一般是不会关闭的。pycharm报错unreachable code，执行不到这个代码，哈哈，确实执行不到这里
