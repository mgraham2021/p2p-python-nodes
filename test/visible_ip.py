from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

log.startLogging(sys.stdout)


def setDone(result, server):
    reactor.stop()


def bootstrapDone(found, server):
    server.inetVisibleIP().addCallback(setDone, server)


server = Server()
server.listen(8468)
server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)

reactor.run()