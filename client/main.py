from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys

from utils.defaults import intial_node

log.startLogging(sys.stdout)


def done(result):
    print ("Key result:", result)
    reactor.stop()


def result(result):
    print ("Key result:", result)
    reactor.stop()


def setDone(result, server, key):
    server.get(key).addCallback(done)


def bootstrapDone(found, server, key, data):
    server.set(key, data).addCallback(setDone, server, key)


def bootstrap(found, server, key):
    server.get(key).addCallback(result)


def main():
    option = raw_input("Options (1) lookup  // (2) add data: \n")
    if option == '1':

        key = raw_input("Enter key: ")
        print ("you entered key: {}".format(key))
        server = Server()
        server.listen(8500)
        server.bootstrap(intial_node).addCallback(bootstrap, server, key)
    elif option == '2':
        key = raw_input("Enter key: ")
        print ("you entered key: {}".format(key))

        data = raw_input("Enter data: ")
        print ("you entered key: {}".format(data))

        server = Server()
        server.listen(8500)
        server.bootstrap(intial_node).addCallback(bootstrapDone, server, key, data)

    reactor.run()
