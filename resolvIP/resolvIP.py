import socket
from threading import Thread
roomNum = str(input("Please enter the room number at RSC: "))
addresses = []

def getIP(hostname):
    try:
        ip_addr = hostname + ":" + str(socket.gethostbyname(hostname.strip()))
    except:
        return print(hostname + ": is down")

    addresses.append(ip_addr)
    return

for num in range(0,100):
    if num < 10:
        num = "0"+str(num)

    hostname = "BS-"+roomNum+"-LAB"+str(num)

    Thread(target = getIP, args = (hostname,)).start()
for i in addresses:
    host = i.split(":")[0]
    ip = i.split(":")[1]
    with open("TARGETS.txt", "a") as file:
        file.write(host+":"+ ip +"\n")
