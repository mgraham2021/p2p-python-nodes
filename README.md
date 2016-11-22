# p2p-python-nodes
Python nodes that use dht to communicate 

Installation:
1.Install requirements in environment
  e.g. pip install -r requirements.txt

2. Run server cluster:
   e.g. python -m node

3. Run client code:
   e.g. python -m client


Utilizes a kademlia dht node class that abstracts the network code.
https://github.com/bmuller/kademlia

All instances of clients and server clusters will connect to the same network.  Clients are lightweight
stateless connection interface.  On the other hand, the server nodes save state frequently to
file, as well as on node failure. 