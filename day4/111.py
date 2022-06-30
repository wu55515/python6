from socket import *
import select
import sys
tcp_client = socket(AF_INET, SOCK_STREAM)
dest_add = ('192.168.3.38', 2000)
tcp_client.connect(dest_add)

epoll = select.epoll()
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(tcp_client.fileno(),select.EPOLLIN)
while True:
    events = epoll.poll(-1,2)
    for fd, event in events:
        if fd == sys.stdin.fileno():
            data=input('请输入数据:')
            tcp_client.send(data.encode('utf8'))
        elif fd == tcp_client.fileno():
            recv_data=tcp_client.recv(100)
            if not recv_data:
                print('对方断开了')
                exit()
            print(recv_data.decode('utf8'))

tcp_client.close()