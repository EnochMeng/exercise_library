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

        cmd = str(conntent_recv, 'utf8')
        cmd_obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        # 这里就是把命令执行的结果保存在cmd_obj这个对象中，一定要加上stdout这个参数，这个是将结果移动到你的主进程，不然接受不到结果
        cmd_result = cmd_obj.stdout.read()
        # 这里取出命令结果，cmd_reslut是一个通过gbk进行编码的bytes类型,因为我们在windows下执行的命令，默认使用gbk进行编码
        cmd_len = len(cmd_result)
        print(cmd_len)
        # 计算出这个结果的长度，也就是他的字节数，因为这是个bytes类型

        conn.send(bytes(str(cmd_len), 'utf8'))

        conn.recv(1024)
        # 这个加个接受是因为要解决 粘包 现象，粘包就是两个send在一块时，有可能会出现上面一个send把下面一个内容也一起发出去了，缓存区的问题，可以百度一下
        # 其实就是让他中间停顿一下，就不会一起了

        conn.send(cmd_result)
        # send方法输出的内容必须是byte类型，因此这里做转化

sk.close()
# 关闭server端，一般是不会关闭的。pycharm报错unreachable code，执行不到这个代码，哈哈，确实执行不到这里
