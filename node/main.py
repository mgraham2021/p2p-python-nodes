
import os
from optparse import OptionParser

import asyncio
from pyp2p.net import *

import time
import settings

ip_address_counter = 0


# maybe use the direct connections to set that a broadcast needs to happen to the network
# want to test before this




def main():
    def _main():
        for x in range(settings.local_nodes):
            pid = os.fork()
            if pid == 0:
                child()
        os.waitpid(pid, 0)
        print('parent')

    asyncio.ensure_future(_main())
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
