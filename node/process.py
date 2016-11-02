from kademlia.network import Server
from twisted.internet import reactor


nodes = ['node_one', 'node_two', 'node_three', 'node_four']
d = {}

def done(result):
    print ("Key result:", result)
    reactor.stop()


def setDone(result, server):
    server.get("a key").addCallback(done)


def bootstrapDone(found, server):
    server.set("a key", "a value").addCallback(setDone, server)


def child():
    ip_address_counter = 1
    for node in nodes:
        port = 8468 + ip_address_counter
        print(port)
        print(node)
        d[node] = Server()
        d[node].listen(port)
        d[node].bootstrap([('127.0.0.{}'.format(ip_address_counter), port)]).addCallback(bootstrapDone, d[node])

        ip_address_counter += 1
