from kademlia.network import Server
from twisted.internet import reactor

from utils.defaults import intial_node
from utils.init_data import load_initial_data, return_initial_data

nodes = ['node_one', 'node_two', 'node_three', 'node_four']
d = {}

bootstrap_default_data = True


def done(result):
    print('Kill the distrubuted network')
    reactor.stop()


def setDone(result, server):
    print('Key and value added to dht')


def bootstrapDone(found, server):
    global bootstrap_default_data
    print('Node connected to the network')
    neighbors = server.bootstrappableNeighbors()
    print('This is the neighbors {0}'.format(neighbors))

    if bootstrap_default_data:
        load_initial_data(server)
        bootstrap_default_data = False
        print('Initial data loaded into network')


def set_key(server, key, value):
    server.set(key, value)


def get_key(server, key):
    server.get(key).addCallback(done)


def child():
    server = Server()
    server.listen(8467)
    server.bootstrap(intial_node).addCallback(bootstrapDone, server)

    ip_address_counter = 2
    for node in nodes:
        port = 8468 + ip_address_counter
        print(node + ' listening on port ' + str(port))
        d[node] = Server()
        d[node].listen(port)
        d[node].bootstrap(intial_node).addCallback(bootstrapDone, d[node])
        d[node].saveStateRegularly('./state.txt', 20)

        ip_address_counter += 1
