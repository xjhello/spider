import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):  # self.request相当于conn
        # print(self.request.recv(1024).decode('utf-8'))
        while True:
            res = self.request.recv(1024).decode('utf-8')
            print(res)
            info = input('>>>')
            self.request.send(info.encode('utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8989), MyServer)
    server.serve_forever()
