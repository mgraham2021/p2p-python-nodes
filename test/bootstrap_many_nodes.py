from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys
from random import randint

log.startLogging(sys.stdout)


def done(result):
    print ("Key result:", result)

    # reactor.stop()


def setDone(result, server, key):
    server.get("{}".format(key)).addCallback(done)


def bootstrapDone(found, server):
    key = randint(0, 999)
    server.set("{}".format(key), "a value").addCallback(setDone, server, key)

server = Server()
server.listen(8468)
server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)
server.bootstrap([('127.0.0.2', 8469)]).addCallback(bootstrapDone, server)
server.bootstrap([('127.0.0.3', 8470)]).addCallback(bootstrapDone, server)

reactor.run()