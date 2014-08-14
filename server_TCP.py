#!/usr/bin/env python
'TCP server based on TCP_Server from SocketServer'

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline()))
        
tcpServer = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServer.serve_forever()
