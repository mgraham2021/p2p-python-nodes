
# on message
# create direct connect node
# send message
# have recieving node broadcast the message to other peers

from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT
import time


# Start existing's server direct connection.
node_dht = DHT()
node_direct = Net(passive_bind="192.168.0.45", passive_port=44444, interface="eth0:2",
                  net_type="direct", dht_node=node_dht, debug=1)
node_direct.start()

# Start client direct connect.
client_dht = DHT()
client_direct = Net(passive_bind="192.168.0.44", passive_port=44445, interface="eth0:1",
                    net_type="direct", node_type="active", dht_node=client_dht, debug=1)
client_direct.start()


# Callbacks.
def success(con):
    print("Client successfully connected to Server.")
    con.send_line("Request.")


def failure(con):
    print("Client failed to connect to Server\a")

events = {
    "success": success,
    "failure": failure
}

# Have the client connect to server.
client_direct.unl.connect(node_direct.unl.construct(), events)

# Event loop.
while 1:
    # client get reply.
    for con in client_direct:
        for reply in con:
            print(reply)

    # Server node accept con.
    for con in node_direct:
        x = 1

time.sleep(0.5)
