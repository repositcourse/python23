# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
local_broadcast = "255.255.255.255"
unassigned ="0.0.0.0"
IP = " "
ip_correct = False
while not ip_correct:
    IP = input("Ввыедите адрес (в формате X.X.X.X): ")
    octets = IP.split(".")
    if len(octets) == 4:
        for octet in octets:
            if octet.isdigit() and int(octet) in range(0, 256):
                ip_correct = True
                continue
            else:
                ip_correct = False
                print("Неправильный IP-адрес")
                break

if ip_correct:
    if int(IP.split(".")[0]) in range(1,224):
        print(f"IP-адрес {IP} имеет типа unicast")
    elif int(IP.split(".")[0]) in range(224,240):
        print(f"IP-адрес {IP} имеет типа multicast")
    elif IP == local_broadcast:
        print(f"IP-адрес {IP} имеет типа local broadcast")
    elif IP == unassigned:
        print(f"IP-адрес {IP} имеет типа unassigned")
    else:
        print(f"IP-адрес {IP} имеет типа unused")
    ip_wrong = True

