"""
    name2ip // made by kotenok_1337
"""

import socket as libsocket
import blessed as libblessed
import art as libart
import time as libtime

try:
    t = libblessed.Terminal()
    def clear():
        print(t.clear)
    clear()
    logo = f'{libart.text2art("n2ip")}\nby kotenok_1337'
    print(logo)
    print("Welcome!")
    libtime.sleep(1)
    clear()

    print(logo)
    host = str(input('Enter hostname (ex: google.com): '))
    clear()
    print(logo)
    print("Loading...")
    try:
        ip = libsocket.gethostbyname(host)
        print(f'{host} - IP: {t.green(ip)}')
    except libsocket.gaierror as e:
        print(f'{t.red("ERROR:")} Invalid hostname.')
        print(f'{t.blue("DEBUG:")} {e}')
except:
    clear()
    print(logo)
    print(f'{t.red("ERROR:")} Unknown error.')