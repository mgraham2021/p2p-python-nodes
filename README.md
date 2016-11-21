# p2p-python-nodes
Python nodes that use dht to communicate with each other. Twisted
framework allows for asynchronous execution. 

Installation:
1.Install requirements in environment
  e.g. pip install -r requirements.txt

2. Run server cluster:
   e.g. python -m node

3. Run client code:
   e.g. python -m client
   -enter: 1 or 2
   -option 1 allows the user to loop up key/value pairs
   -option 2 allows theusers to enter new key/value pairs


Utilizes a kademlia dht node class that abstracts the network code.
https://github.com/bmuller/kademlia

All instances of clients and server clusters will connect to the same network.  Clients are lightweight
stateless connection interface.  On the other hand, the server nodes save state frequently to
file, as well as on node failure.

Node class methods:
    listen 
    -initializes the port for the node to listen on
    -params: port (int) i.g. 5800
    
    bootstrap
    -connects to existing known peers, or creates new network
    -params: peer list of tuples i.g. ('127.0.0.0', 5800)
 
    bootstrappableNeighbors
    -returns a list of known neighbors
    
    get 
    -searches network for a key that matches
    -params: search term
    
    set
    -sets key/value pair into network
    -params: key, data
    
    
   saveState
   -saves node state to a file
   -params: path to file
   
   loadState
   -initializes node with data and peers
   -params: path to file
   
   saveStateRegularly
   -schedules regular saving of the data
   -params: time, path to file
    
   