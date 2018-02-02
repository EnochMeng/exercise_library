# 实现并发，也就是多个client端可以和我聊天
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('server端启动')
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                client_data = conn.recv(1024)
                print(str(client_data, 'utf8'))
                if str(client_data, 'utf8') == 'exit':
                    break
                conn.sendall(client_data)   # 返回client端发来的数据,主要观察并发
            conn.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    server.serve_forever()

