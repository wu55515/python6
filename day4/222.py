from socket import *
import select
import sys
tcp_server = socket(AF_INET, SOCK_STREAM)
local_add = ('192.168.3.38', 2000)
tcp_server.bind(local_add)
tcp_server.listen(10)
client_socket,client_addr=tcp_server.accept()

epoll = select.epoll()
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(client_socket.fileno(),select.EPOLLIN)
while True:
    events = epoll.poll(-1,2)
    for fd, event in events:
        if fd == sys.stdin.fileno():
            data=input('请输入数据:')
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():
            recv_data=client_socket.recv(100)
            if not recv_data:
                print('对方断开了')
                exit()
            print(recv_data.decode('utf8'))

client_socket.close()
tcp_server.close()







