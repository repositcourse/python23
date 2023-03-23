# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
IP = input("Ввыедите адрес (в формате X.X.X.X): ")
local_broadcast = "255.255.255.255"
unassigned ="0.0.0.0"


if int(IP.split(".")[0]) in range(0,224):
    print(f"IP-адрес {IP} имеет типа unicast")
elif int(IP.split(".")[0]) in range(224,240):
    print(f"IP-адрес {IP} имеет типа multicast")
elif IP == local_broadcast:
    print(f"IP-адрес {IP} имеет типа local broadcast")
elif IP == unassigned:
    print(f"IP-адрес {IP} имеет типа unassigned")
else:
    print(f"IP-адрес {IP} имеет типа unused")


