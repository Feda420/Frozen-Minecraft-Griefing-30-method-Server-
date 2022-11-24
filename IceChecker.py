from mcstatus import MinecraftServer
from threading import Thread

import threading
import json, signal, sys
import os
import time

workingservers = 0

print("""
                
                            __   ___  ____
                            ||  //   ||   
                            || ((    ||== 
                            ||  \\__  ||___
               
  /$$$$$$  /$$                           /$$                          
 /$$__  $$| $$                          | $$                          
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$      
|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
 \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/   v.0.5   
                                                                      
                                                                      
""")
inpito = input("[!] Write the txt name: ")
puertosinput = input("[!] Write the ports or port to check [Define those ports with ',' or just use a port range with '-'] \n: ")
output = input("[!] Write the output's file name: ")
os.system('clear')
print("""
                
                            __   ___  ____
                            ||  //   ||   
                            || ((    ||== 
                            ||  \\__  ||___
               
  /$$$$$$  /$$                           /$$                          
 /$$__  $$| $$                          | $$                          
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$      
|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
 \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/   v.0.5    
                            Scanning...                                        
                                                                      
""")

try:
    threads = int(sys.argv[1])
except:
    print("Add threads! | Usage: python checker.py numberthreads")
    sys.exit(0)
with open(inpito+".txt") as f:
    servers = f.readlines()
servers = [x.strip() for x in servers]
started = 0
print(" [!] Checking servers... [!]\n")
if '' is output:
    fh = open('Results.txt', "w")
else:
    fh = open(output+'.txt', "w")

puertos = []

def CheckServer(server):
    global workingservers
    global started
    global puertos
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
            fh.write("> Working {0} | [{1}/{2}] | {3} - {4}\n".format(server+":"+puerto, status.players.online, status.players.max, status.version.name, motd.replace("{", "")))
            workingservers+=1
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

for server in servers:
    while True:
        if started <= threads:
            thread = Thread(target = CheckServer, args = (server, ))
            thread.start()
            started += 1
            break

fh.close()
print("Done! Working servers found: " + str(workingservers))
