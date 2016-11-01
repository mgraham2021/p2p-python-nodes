from kademlia.network import Server
from twisted.internet import reactor


def done(result):
    print ("Key result:", result)
    reactor.stop()


def setDone(result, server):
    server.get("a key").addCallback(done)


def bootstrapDone(found, server):
    server.set("a key", "a value").addCallback(setDone, server)




def child(ip_address_counter):
    port = 8468 + ip_address_counter
    print(port)
    server = Server()
    server.listen(port)
    server.bootstrap([('127.0.0.{}'.format(ip_address_counter),
                           port)]).addCallback(bootstrapDone, server)

