
import os
from optparse import OptionParser

from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT
import time
import settings


# Callbacks.
def success(con):
    print("successfully connected")
    con.send_line("Sup Bob.")


def failure(con):
    print("connection failure")


events = {
    "success": success,
    "failure": failure
}




def child():
    print('child')
    node_dht = DHT()
    node = Net(passive_bind="192.168.0.45", passive_port=44444, interface="eth0:2", net_type="passive",
                       dht_node=node_dht, debug=1)
    node.start()
    node.bootstrap()
    node.advertise()

    while 1:
        for con in node:
            con.send_line("test")

def main(*args, **kwargs):
    # args setup
    parser = OptionParser()
    parser.add_option('-i', '--id', dest='identifier',
                      help='The identifier for this instance; Used when spawning '
                           'mulitple workers that can be load balanced.',
                      type=int,
                      default=0)
    (options, parsed_args) = parser.parse_args()

    for x in range(settings.local_nodes):
        pid = os.fork()
        if pid == 0:
            child()
    os.waitpid(pid, 0)
    print('parent')
