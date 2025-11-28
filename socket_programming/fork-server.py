"""
Server side: open a socket on a port, listen for a message from a client,
and send an echo reply; forks a process to handle each client connection;
child processes share parent's socket descriptors; fork is less portable
than threads--not yet on Windows, unless Cygwin or similar installed;
"""

import os, time, sys
from socket import *  # get socket constructor and constants

myHost = ""  # server machine, '' means local host
myPort = 50007  # listen on a non-reserved port number
sockobj = socket(AF_INET, SOCK_STREAM)  # make a TCP socket object
sockobj.bind((myHost, myPort))  # bind it to server port number
sockobj.listen(5)  # allow 5 pending connects


def now():  # current time on server
    return time.ctime(time.time())


activeChildren = []


def reapChildren():  # reap any dead child processes
    while activeChildren:  # else may fill up system table
        pid, stat = os.waitpid(0, os.WNOHANG)  # don't hang if no child exited
        if not pid:
            break
        activeChildren.remove(pid)


def handleClient(connection):  # child process: reply, exit
    time.sleep(5)  # simulate a blocking activity
    while True:  # read, write a client socket
        data = connection.recv(1024)  # till eof when socket closed
        if not data:
            break
        reply = "Echo=>%s at %s" % (data, now())
        connection.send(reply.encode())
    connection.close()
    os._exit(0)


def dispatcher():  # listen until process killed
    while True:  # wait for next connection,
        connection, address = sockobj.accept()  # pass to process for service
        print("Server connected by", address, end=" ")
        print("at", now())
        reapChildren()  # clean up exited children now
        childPid = os.fork()  # copy this process
        if childPid == 0:  # if in child process: handle
            handleClient(connection)
        else:  # else: go accept next connect
            activeChildren.append(childPid)  # add to active child pid list


dispatcher()


# [Cygwin shell window]
# [C:\...\PP4E\Internet\Socekts]$ python fork-server.py
# Server connected by ('127.0.0.1', 58258) at Sat Apr 24 07:50:15 2010
# Server connected by ('127.0.0.1', 58259) at Sat Apr 24 07:50:17 2010
# [Windows console, same machine]
# C:\...\PP4E\Internet\Sockets> python echo-client.py localhost bright side of life
# Client received: b"Echo=>b'bright' at Sat Apr 24 07:50:20 2010"
# Client received: b"Echo=>b'side' at Sat Apr 24 07:50:20 2010"
# Client received: b"Echo=>b'of' at Sat Apr 24 07:50:20 2010"
# Client received: b"Echo=>b'life' at Sat Apr 24 07:50:20 2010"
# [Windows console, same machine]
# C:\...\PP4E\Internet\Sockets> python echo-client.py
# Client received: b"Echo=>b'Hello network world' at Sat Apr 24 07:50:22 2010"
