
from twisted.internet import reactor
from node.process import child
from twisted.python import log
import sys

log.startLogging(sys.stdout)


def main():
    child()
    reactor.run()


if __name__ == '__main__':
    main()
