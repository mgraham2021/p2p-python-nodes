import os
import asyncio
import settings
from node.process import child

ip_address_counter = 0




def main():
    global ip_address_counter
    # def _main():
    while 1:
        for x in range(settings.local_nodes):
            pid = os.fork()
            if pid == 0:
                ip_address_counter += 1
                child(ip_address_counter)
        os.waitpid(pid, 0)
        print('parent')

    # asyncio.ensure_future(_main())
    # asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
