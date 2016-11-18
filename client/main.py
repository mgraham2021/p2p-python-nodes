from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

from utils.defaults import intial_node

log.startLogging(sys.stdout)


def done(result):
    print ("Key result:", result)
    reactor.stop()


def setDone(result, server, key):
    server.get(key).addCallback(done)


def bootstrapDone(found, server, key, data):
    server.set(key, data).addCallback(setDone, server, key)


def main():
    key = raw_input("Enter key: ")
    print ("you entered key: {}".format(key))

    data = raw_input("Enter data: ")
    print ("you entered key: {}".format(data))

    server = Server()
    server.listen(8500)
    server.bootstrap(intial_node).addCallback(bootstrapDone, server, key, data)

    reactor.run()
