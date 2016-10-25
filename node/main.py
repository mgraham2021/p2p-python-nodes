
import os
from optparse import OptionParser

from pyp2p.net import *
from pyp2p.unl import UNL
from pyp2p.dht_msg import DHT
import time




import settings


def main(*args, **kwargs):
    # args setup
    parser = OptionParser()
    parser.add_option('-i', '--id', dest='identifier',
                      help='The identifier for this instance; Used when spawning '
                           'mulitple workers that can be load balanced.',
                      type=int,
                      default=0)
    (options, parsed_args) = parser.parse_args()

    newpid = os.fork()