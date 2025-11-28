import sys
from parallel_system_tools.launchmodes import QuietPortableLauncher

numclients = 8


def start(cmdline):
    QuietPortableLauncher(cmdline, cmdline)()


# start('echo-server.py')              # spawn server locally if not yet started
args = " ".join(sys.argv[1:])  # pass server name if running remotely
for i in range(numclients):
    start("echo-client.py %s" % args)  # spawn 8? clients to test the server


# To run this script, pass no arguments to talk to a server listening on port 50007 on the
# local machine; pass a real machine name to talk to a server running remotely.
