from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

log.startLogging(sys.stdout)

def bootstrapDone(found, server):
    server.saveStateRegularly('./state.txt', 20)
    print('load state scheduled for 20 seconds')

    reactor.stop()

server = Server()
server.listen(8468)
server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)

server_two = Server()
server_two.listen(8469)
server_two.bootstrap([('127.0.0.1', 8468)])

reactor.run()