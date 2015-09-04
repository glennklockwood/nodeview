#!/usr/bin/env python

import nodeview

import sys
import subprocess

def _get_subprocess_dict( args ):
    """
    Run a subprocess and convert its rows, columns into a list of dicts
    """
    p = subprocess.Popen( args, stdout=subprocess.PIPE )
    o, e = p.communicate()
    exit_code = p.poll()
    if exit_code: sys.stderr.write( e )

    col_names = None
    output = []
    for line in o.splitlines():
        cols = line.split('|')
        if col_names is None:
        #')
            col_names = cols
        else:
            node_dict = {}
            for i, j in enumerate(cols):
                node_dict[col_names[i].strip()] = j.strip()
            output.append( node_dict )
                
    return output

def generate_nodelist( ):
    node_dicts = _get_subprocess_dict( [ 'sinfo', '-o%all' ] )

    node_list = []
    for node_dict in node_dicts:
        import json
        #print json.dumps(node_dict, indent=4, sort_keys=True)
        node_list.append( nodeview.Node( 
            name=       node_dict['HOSTNAMES'],
            np=         int(node_dict['CPUS(A/I/O/T)'].split('/')[3]),
            np_avail=   int(node_dict['CPUS(A/I/O/T)'].split('/')[0]),
            physmem_kb= int(node_dict['MEMORY'])*1024,
            availmem_kb=int(node_dict['FREE_MEM'])*1024,
            load=       float(node_dict['CPU_LOAD']),
            state=      node_dict['STATE'],
            properties= [ node_dict['FEATURES'] ],
            other_info='') )

    return node_list

#AVAIL          up
#CPUS           48
#TMP_DISK       32261
#FREE_MEM       62815
#FEATURES       (null)
#GROUPS         all
#SHARE          EXCLUSIVE
#TIMELIMIT      30:00
#MEMORY         64523
#HOSTNAMES      nid00033
#NODE_ADDR      nid00033
#PRIORITY       20
#ROOT           no
#JOB_SIZE       1-10
#STATE          resv
#USER           root
#VERSION        15.08
#WEIGHT         1
#S:C:T          2:12:2
#NODES(A/I)     0/1 
#MAX_CPUS_PER_NODE UNLIMITED 
#CPUS(A/I/O/T)  0/48/0/48 
#NODES          1 
#REASON         none 
#NODES(A/I/O/T) 0/1/0/1 
#GRES           craynetwork:4 
#TIMESTAMP      Unknown 
#DEFAULTTIME    5:00 
#PREEMPT_MODE   OFF 
#NODELIST       nid00033 
#CPU_LOAD       0.23 
#PARTITION      debug* 
#PARTITION      debug 
#ALLOCNODES     all 
#STATE          reserved 
#USER           root(0) 
#SOCKETS        2 
#CORES          12 
#THREADS        2 


if __name__ == '__main__':
    generate_nodelist()


