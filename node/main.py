from twisted.internet import reactor
from node.process import child

def main():
    child()

    print('parent')
    reactor.run()


if __name__ == '__main__':
    main()
