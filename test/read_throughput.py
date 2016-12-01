from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

log.startLogging(sys.stdout)


def done(result):
    print ("Key result:", result)


def setDone(result, server):
    for x in range(0, 1000000):
        server.get("a key").addCallback(done)


def bootstrapDone(found, server):
    server.set("a key", "a value").addCallback(setDone, server)

server = Server()
server.listen(8468)
server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)

reactor.run()