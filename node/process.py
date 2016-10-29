
from pyp2p.dht_msg import DHT
from pyp2p.net import *

def child():
    print('child')
    global ip_address_counter
    ip_address_counter += 1
    node_dht = DHT()
    node = Net(passive_bind="192.168.0.4{}".format(ip_address_counter), passive_port=44444, interface="eth0:2",
               net_type="passive", dht_node=node_dht, debug=1)
    node.start()
    node.bootstrap()
    node.advertise()
    while 1:
        node.dht_messages = 'hello'
        for con in node:
            con.send_line("test")