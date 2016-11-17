from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

log.startLogging(sys.stdout)

def bootstrapDone(found, server):
    server.loadState('./state.txt')
    print('state loaded successfully')

    reactor.stop()

server = Server()
server.listen(8468)
server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)


reactor.run()
