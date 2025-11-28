"""
Server side: open a TCP/IP socket on a port, listen for a message from
a client, and send an echo reply; this is a simple one-shot listen/reply
conversation per client, but it goes into an infinite loop to listen for
more clients as long as this server script runs; the client may run on
a remote machine, or on same computer if it uses 'localhost' for server
"""

from socket import *  # get socket constructor and constants

myHost = ""  # '' = all available interfaces on host
myPort = 50007  # listen on a non-reserved port number
sockobj = socket(AF_INET, SOCK_STREAM)  # make a TCP socket object
sockobj.bind((myHost, myPort))  # bind it to server port number
sockobj.listen(5)  # listen, allow 5 pending connects
while True:  # listen until process killed
    connection, address = sockobj.accept()  # wait for next client connect
    print("Server connected by", address)  # connection is a new socket
    while True:
        data = connection.recv(1024)  # read next line on client socket
        if not data:
            break  # send a reply line to the client
        connection.send(b"Echo=>" + data)  # until eof when socket closed
    connection.close()


# C:\...\PP4E\Internet\Sockets> python echo-client.py
# Client received: b'Echo=>Hello network world'
# C:\...\PP4E\Internet\Sockets> python echo-client.py localhost spam Spam SPAM
# Client received: b'Echo=>spam'
# Client received: b'Echo=>Spam'
# Client received: b'Echo=>SPAM'
# C:\...\PP4E\Internet\Sockets> python echo-client.py localhost Shrubbery
# Client received: b'Echo=>Shrubbery'


# C:\...\PP4E\Internet\Sockets> ftp learning-python.com
# Connected to learning-python.com.
# User (learning-python.com:(none)): xxxxxxxx
# Password: yyyyyyyy
# ftp> mkdir scripts
# ftp> cd scripts
# ftp> put echo-server.py
# ftp> quit


# login as: xxxxxxxx
# XXXXXXXX@learning-python.com's password: yyyyyyyy
# Last login: Fri Apr 23 07:46:33 2010 from 72.236.109.185
# [...]$ cd scripts
# [...]$ python echo-server.py &
# [1] 23016


# C:\...\PP4E\Internet\Sockets> python echo-client.py learning-python.com
# Client received: b'Echo=>Hello network world'
# C:\...\PP4E\Internet\Sockets> python echo-client.py learning-python.com ni Ni NI
# Client received: b'Echo=>ni'
# Client received: b'Echo=>Ni'
# Client received: b'Echo=>NI'
# C:\...\PP4E\Internet\Sockets> python echo-client.py learning-python.com Shrubbery
# Client received: b'Echo=>Shrubbery'


# C:\...\PP4E\Internet\Sockets> ping learning-python.com
# Pinging learning-python.com [97.74.215.115] with 32 bytes of data:
# Reply from 97.74.215.115: bytes=32 time=94ms TTL=47
# Ctrl-C
# C:\...\PP4E\Internet\Sockets> python echo-client.py 97.74.215.115 Brave Sir Robin
# Client received: b'Echo=>Brave'
# Client received: b'Echo=>Sir'
# Client received: b'Echo=>Robin'
