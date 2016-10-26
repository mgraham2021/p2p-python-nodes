
import os
from optparse import OptionParser

from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT
import time
import settings

def child():
    print('child')



def main(*args, **kwargs):
    # args setup
    parser = OptionParser()
    parser.add_option('-i', '--id', dest='identifier',
                      help='The identifier for this instance; Used when spawning '
                           'mulitple workers that can be load balanced.',
                      type=int,
                      default=0)
    (options, parsed_args) = parser.parse_args()

    for x in range(3):
        pid = os.fork()
        if pid == 0:
            child()
    os.waitpid(pid, 0)
    print('parent')
