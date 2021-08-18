from socket import *


addr = (('localhost',8888))
udp_socket = socket(AF_INET, SOCK_DGRAM)

#encode - перекодирует введенные данные в байты, decode - обратно
while True:
    data=input("Type Something(q or Q to exit:)")
    if data.lower()=='q':
        udp_socket.close()
        break
    else:
        udp_socket.sendto(data.encode(),("localhost", 8888))
        data_from_server, addr=udp_socket.recvfrom(1024)
        print(data_from_server.decode())


#google.com
#   142.251.1.102
#ADD google.com:1.1.1.1
#   Added new dns entry
#google.com
#   1.1.1.1
#yandex.ru
#   77.88.55.77
#fff1.1
#   error hostname
#ADD google.com:1.1.1.2
#   Added new dns entry
#google.com
#   1.1.1.2
#ADD yandex.ru 8.8.8.8
#   Dns entry didn't add, repead request like 'ADD HostName:IP'
#ADD yandex.ru:8.8.8/8
#   Dns entry didn't add, error IPv4 format
#ADD yandex.ru:8.8.8.8
#   Added new dns entry
#yandex.ru
#   8.8.8.8