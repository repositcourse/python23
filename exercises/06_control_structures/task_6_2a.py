# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
IP = input("Ввыедите адрес (в формате X.X.X.X): ")
local_broadcast = "255.255.255.255"
unassigned ="0.0.0.0"

ip_wrong = False
octets = IP.split(".")
if len(octets) == 4:
    for octet in octets:
        if octet.isdigit() and int(octet) in range(0, 256):
            continue
        else:
            ip_wrong = True
            break
else:
    ip_wrong = True

if ip_wrong:
    print("Неправильный IP-адрес")

while not ip_wrong:
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
