#Написать сервер, который по запросу имени хоста высылает Ip адрес. Добавить возможность переопределять "днс-запись"
#слушаем порт и принимаем данные по  1024 байта, если переменная начинается с ADD - переопределяем "днс-запись" (есть проверка на корректность фотмата записи при переопредлении, корректность IPv4 формата)
#если нет - возвращаем либо свою днс-запись либо Ip с помощью метода socket.gethostbyname (есть проверка на существование хоста)

# udp client в файле hw19_client.py - там же внизу комментарии без знака табуляции ввод, ниже со знаком табуляции -сообщение от сервера
from socket import *
import ipaddress

udp_socket = socket(AF_INET, SOCK_DGRAM) #создаем udp сокет
udp_socket.bind(("localhost",8888)) #занимаем порт, который будем слушать

my_dns={}
while True:
    hostName, addr = udp_socket.recvfrom(1024)
    hostName=hostName.decode()
    '''add DNS entry'''
    if hostName.startswith("ADD"):
        try:
            my_dns[hostName[3::].replace(" ", "").split(":")[0]] = hostName[3::].replace(" ", "").split(":")[1]
            try:
                ipaddress.ip_address(hostName[3::].replace(" ","").split(":")[1])
                my_dns[hostName[3::].replace(" ","").split(":")[0]]=hostName[3::].replace(" ","").split(":")[1]
                udp_socket.sendto(b"Added new dns entry", addr)
            except:
                udp_socket.sendto(b"Dns entry didn't add, error IPv4 format", addr)
        except:
            udp_socket.sendto(b"Dns entry didn't add, repead request like 'ADD HostName:IP'", addr)

    else:
        '''return IP adress to hostName'''
        if hostName in my_dns:
            udp_socket.sendto(my_dns[hostName].encode(), addr)
        else:
            try:
                ipAddress = gethostbyname(hostName)
            except:
                ipAddress="error hostname"
            udp_socket.sendto(ipAddress.encode(),addr)





