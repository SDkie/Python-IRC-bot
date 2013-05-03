import sys
import socket
import string

HOST="irc.freenode.net"
PORT=6667
NICK="sdkie"
IDENT="sdkie"
REALNAME="sdkie"
CHANNEL="#etherboot"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
print "send:"+"NICK %s\r\n" % NICK
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))#check this
print "send:"+"USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME)
s.send("JOIN %s\r\n" % (CHANNEL))
print  "send:JOIN %s\r\n" % (CHANNEL)
while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
	print line
