from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

log.startLogging(sys.stdout)


def setDone(result):
    print ("Key result:", result)


def bootstrapDone(found, server):
    for x in range(0, 1000000):
        server.set("{}".format(x), "{}".format(x)).addCallback(setDone)

server = Server()
server.listen(8468)
server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)

reactor.run()