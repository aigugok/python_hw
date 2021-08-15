import ipaddress


class router:
    '''Route class that has add/del/print ip adresses and same methods for routes'''
    def __init__(self):
        '''initialization of the list of ip addresses and dict of routes - {Network:gateway}'''
        self.ip_adresses=[]
        self.ip_routes={}
    def add_ip_address(self,ip):
        '''Add ip adresses method - add to list of IP adresses new IP adress if it isn't in this list and add route to network through IP'''
        try:
            ipaddress.IPv4Interface(ip)
        except (ipaddress.AddressValueError,ipaddress.NetmaskValueError):
            return f"Your ip adress {ip} is wrong in IPv4 "
        if ipaddress.IPv4Interface(ip) not in self.ip_adresses:
            self.ip_adresses.append(ipaddress.IPv4Interface(ip))
            self.ip_routes[ipaddress.IPv4Interface(ip).network]=ip


    def delete_ip_address(self,ip):
        '''Delete ip adresses method - delete IP adress on the list of IP adresses if it ia in this list'''
        try:
            ipaddress.IPv4Interface(ip)
        except (ipaddress.AddressValueError,ipaddress.NetmaskValueError):
            return f"Your ip adress {ip} is wrong in IPv4 "
        if  ipaddress.IPv4Interface(ip) in self.ip_adresses:
            self.ip_adresses.remove(ipaddress.IPv4Interface(ip))

    def print_ip_address(self):
        '''Print IP adresses list'''
        print(f"IP adresses: {', '.join([str(x) for x in [*self.ip_adresses]])}")


    def add_ip_route(self,scr,dest):
        '''Add route in dict if we have route to the network through gateway'''
        try:
            scr = ipaddress.ip_address(scr)
        except ipaddress.AddressValueError:
            return f"Your ip adress {scr} is wrong in IPv4 "
        try:
            dest = ipaddress.IPv4Interface(dest).network
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            return f"Your ip adress {dest} is wrong in IPv4 "

        #для каждой сети проверяем принаджежит ли ip (scr) к этой сети, если да - добавляем новое значение в словрь (если такая сеть уже была, делаем словарь из ip), если нет - пишем "исключение"
        for i in self.ip_routes:
            if (scr in i):
                if (dest in self.ip_routes):
                    self.ip_routes[dest] = list(self.ip_routes[dest].split())
                    if scr not in self.ip_routes[dest]:
                        self.ip_routes[dest].append(format(scr))
                else:
                    self.ip_routes[dest]=format(scr)
                break
        else:
            print (f"You can't add route to {dest} through {scr}")


    def del_ip_route(self, scr, dest):
        '''Delete route in dict'''
        try:
            scr = ipaddress.ip_address(scr)
        except ipaddress.AddressValueError:
            return f"Your ip adress {scr} is wrong in IPv4 "
        try:
            dest = ipaddress.IPv4Interface(dest).network
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            return f"Your ip adress {dest} is wrong in IPv4 "

        #если сеть есть в ключах словаря и ip в значениях по этому ключу, смотрим если у нас список больше 1 элемента удалчем только значение, если нет и ключ, и значение
        if dest in self.ip_routes and str(scr) in self.ip_routes[dest]:
            if type(self.ip_routes[dest])==list and len(self.ip_routes[dest])>1:
                self.ip_routes[dest].remove(str(scr))
            else:
                self.ip_routes.pop(dest, scr)
        else:
            print(f"You want to delete a nonexistent route to the network {dest} through {scr}")



    def print_ip_route(self):
        '''Print IP routes dict'''
        for i in self.ip_routes:
            print(f"Route to the network {i} through {self.ip_routes[i]}")






# my_router=router()
# my_router.add_ip_address('192.168.5.14/24')
# my_router.print_ip_address()
# my_router.print_ip_route()
# print()
# my_router.add_ip_address('192.168.5.20/24')
# my_router.print_ip_address()
# my_router.print_ip_route()
# print()
# my_router.delete_ip_address('192.168.5.20/24')
# my_router.print_ip_address()
# my_router.print_ip_route()
# print()
#
#
# my_router.add_ip_route("192.168.5.1",'172.16.0.0/16')
# my_router.add_ip_route("192.168.8.3",'172.24.0.0/16')
# my_router.add_ip_route("192.168.5.2",'172.16.0.0/16')
# my_router.add_ip_route("172.16.8.1",'172.24.0.0/16')
# print()
# my_router.print_ip_route()
# print()
# my_router.del_ip_route("192.168.5.2",'172.16.0.0/16')
# my_router.del_ip_route("192.168.5.1",'172.16.0.0/16')
# my_router.del_ip_route("172.16.8.1",'172.25.0.0/16')
# my_router.print_ip_route()













