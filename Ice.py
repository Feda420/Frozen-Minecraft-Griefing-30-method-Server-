from threading import Thread
from mcstatus import MinecraftServer

import threading
import json, signal, sys
import os
import time

workingservers = 0

print("""


    ▄█   ▄████████    ▄████████ 
    ███  ███    ███   ███    ███ 
    ███▌ ███    █▀    ███    █▀  
    ███▌ ███         ▄███▄▄▄     
    ███▌ ███        ▀▀███▀▀▀     
    ███  ███    █▄    ███    █▄  
    ███  ███    ███   ███    ███ 
    █▀   ████████▀    ██████████ v.0.1

    Dev by FrozenCode
                            
""")
ips = []
inpito = input("[!] IP RANGE [Example: 149.56.242-243.1-255] \n: ")
puertosinput = input("[!] Write the ports or port to check [Define those ports with ',' or just use a port range with '-'] \n: ")
output = input("[!] Write the output's file name: ")

iprange = inpito.split('.')

    

os.system('clear')
print("""


    ▄█   ▄████████    ▄████████ 
    ███  ███    ███   ███    ███ 
    ███▌ ███    █▀    ███    █▀  
    ███▌ ███         ▄███▄▄▄     
    ███▌ ███        ▀▀███▀▀▀     
    ███  ███    █▄    ███    █▄  
    ███  ███    ███   ███    ███ 
    █▀   ████████▀    ██████████ v.0.1

    Dev by FrozenCode
    >Scanning...                          
""")

try:
    threads = int(sys.argv[1])
except:
    print("Add threads! | Usage: python IceScanner.py numberthreads")
    sys.exit(0)

print(" [!] Checking servers... [!]\n")
if '' is output:
    filename = 'Results.txt'
else:
    filename = output+".txt"

puertos = []
started = 0

def CheckServer(server):
    global workingservers
    global started
    global puertos
    global filename
    for puerto in puertos:
        try:
            #print(server+":"+puerto)
            serverb = MinecraftServer.lookup(server+":"+puerto)
            status = serverb.status()
            motd = str(status.description)
            texts = motd.split("'text': '")
            motd = ""
            for x in texts:
                motd += x.split("'")[0].replace("\n", "")
            print("> Working {0} | [{1}/{2}] | {3} - {4}".format(server+":"+puerto, status.players.online, status.players.max, status.version.name, motd.replace("{", "")))
            workingservers+=1
            with open('IceResults.txt','a') as xD:
                xD.write("> Working {0} | [{1}/{2}] | {3} - {4}\n".format(server+":"+puerto, status.players.online, status.players.max, status.version.name, motd.replace("{", "")))
            
        except Exception:
            pass
        started = started - 1

if not ',' in puertosinput and not '-' in puertosinput:
    puertos.append(str(puertosinput))

if ',' in puertosinput and not '-' in puertosinput:
    for comapuerto in puertosinput.split(","):
        puertos.append(str(comapuerto))

if '-' in puertosinput and not ',' in puertosinput:
    puertoinicial = int(puertosinput.split('-')[0])
    puertofinal = int(puertosinput.split('-')[1])
    for i in range(puertoinicial, puertofinal+1):
        puertos.append(str(i))

if '-' in puertosinput and ',' in puertosinput:
    for coma in puertosinput.split(','):
        if '-' in coma:
            puertoinicial = int(coma.split('-')[0])
            puertofinal = int(coma.split('-')[1])
            for c in range(puertoinicial, puertofinal+1):
                puertos.append(str(c))
        else:
            puertos.append(coma)

#print(puertos)

try:
    if '-' in iprange[2]:
        if '-' in iprange[3]:
            for c in range(int(iprange[2].split("-")[0]),int(iprange[2].split("-")[1])+1):
                for t in range(int(iprange[3].split("-")[0]),int(iprange[3].split("-")[1])+1):
                    server = iprange[0]+"."+iprange[1]+"."+str(c)+"."+str(t)
                    #print(server)
                    while True:
                        if started <= threads:
                            thread = Thread(target = CheckServer, args = (server, ))
                            thread.start()
                            started += 1
                            break
    else:
        if '-' in iprange[3]:
            for t in range(int(iprange[3].split("-")[0]),int(iprange[3].split("-")[1])+1):
                server = iprange[0]+"."+iprange[1]+"."+iprange[2]+"."+str(t)
                #print(server)
                while True:
                    if started <= threads:
                        thread = Thread(target = CheckServer, args = (server, ))
                        thread.start()
                        started += 1
                        break
except Exception:
    print('Error '+str(Exception))
    exit()

if threads is 0:
    print("Working Servers found: " + str(workingservers)+ ".")
    exit()