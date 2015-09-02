#!/usr/bin/env python

class Node:
    def __init__( self,
                  name,
                  np,
                  np_avail,
                  physmem_kb=0,
                  availmem_kb=0,
                  load=0.0,
                  state="",
                  properties=[],
                  other_info={} ):
        self.name = name
        self.np = np
        self.np_avail = np_avail
        self.physmem_kb = physmem_kb
        self.availmem_kb = availmem_kb
        if physmem_kb > 0:
            self.availmem_pct = 100.0 * (1.0 - float(availmem_kb) / float(physmem_kb))
        else:
            self.availmem_pct = 0.0
        self.load = load
        self.state = state
        self.properties = properties
        self.other_info = other_info

def print_node_line( node ):
    print "%-14s %4d %4d %7d %3d/%3d %5.1fG %6.1f%% %7.2f %s" % (
        node.name,
        0,
        0,
        node.np,
        node.np - node.np_avail,
        node.np,
        node.physmem_kb / 1024.0 / 1024.0,
        node.availmem_pct,
        node.load,
        ':'.join( node.properties ).lower() )
# 12345678901234 1234 1234 1234567 1234567 123456 1234567 1234567 123456
# node           jobs rnks cpus    slots   totmem %memuse avgload state


