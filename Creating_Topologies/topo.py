#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    # build(): the method to override in your topology class
    def build(self, n=2):
        # addSwitch(): adds a switch to a Topo and returns the switch name 
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            # addHost(): adds a host to a Topo and returns to host name 
            host = self.addHost('h%s' % (h + 1))
            # addLink(): adds a bidirectional link to Topo
            self.addLink(host, switch)
    
def simpleTest():
    "Create and test a simple network."
    topo = SingleSwitchTopo(n = 4)
    # Mininet: main class to create and manage a network
    net = Mininet(topo)
    # start(): starts your network
    net.start()
    print("Dumping host connections")
    # dumpNodeConnections(): dumps connections to/from a set of nodes
    dumpNodeConnections(net.hosts) # net.hosts: all the hosts in a network 
    print("Testing network connectivity.")
    # pingAll(): tests connectivity by trying to have all nodes ping each other  
    net.pingAll()
    # stop(): stops your network
    net.stop()

if __name__ == '__main__':
    #Tell mininet to print useful information
    # setLogLevel('info'|'debug'|'output'): set Mininet's default output level
    setLogLevel('info')
    simpleTest()