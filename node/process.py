from kademlia.network import Server
from twisted.internet import reactor


nodes = ['node_one', 'node_two', 'node_three', 'node_four']
d = {}

bootstrap_default_data = True


def done(result):
    print ("Key result:", result)
    reactor.stop()


def setDone(result, server):
    server.get("a key").addCallback(done)


def bootstrapDone(found, server):
    global bootstrap_default_data
    print('Node connected to the network')

    if bootstrap_default_data == True:
        server.set(1, [0, 'init'])
        server.set(2, [1, 'hello'])
        server.set(3, [2, 'second'])
        server.set(4, [3, 'datas'])

        bootstrap_default_data = False
        print('Initial data loaded into network')


def set_key(server, key, value):
    server.set(key, value)


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
