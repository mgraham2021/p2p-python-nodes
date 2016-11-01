import os
from twisted.internet import reactor
import settings
from node.process import child

ip_address_counter = 0




def main():
    global ip_address_counter


    # for x in range(settings.local_nodes):
    #     pid = os.fork()
    #     if pid == 0:
    #         ip_address_counter += 1
    child(ip_address_counter)

    print('parent')
    reactor.run()



if __name__ == '__main__':
    main()
