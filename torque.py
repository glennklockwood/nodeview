#!/usr/bin/env python

import sys
try:
    import xml.etree.ElementTree as ET
except ImportError:
    import elementtree.ElementTree as ET
import subprocess

def _get_subprocess_xml( args ):
    """
    Run a subprocess and convert its output to an ElementTree.Element
    """
    p = subprocess.Popen( args, stdout=subprocess.PIPE )
    o, e = p.communicate()
    exit_code = p.poll()
    if exit_code: sys.stderr.write( e )

    return ET.fromstring( o )

def parse_node_status( status_str ):
    """
    Parse a node's "status" field.  Because the "jobs" key includes commas
    within parentheses, one cannot simply split on commas and instead must
    use a context-aware split.
    """
    parse_state = 0
    new_parts = []
    jobs_part = []
    parts = status_str.split(',')
    for part in parts:
        if parse_state == 0:
            if part.startswith( 'jobs=' ):
                if '(' in part:
                    parse_state += 1
                jobs_part.append( part )
            else:
                new_parts.append( part )
        elif parse_state == 1:
            if ')' in part and '(' in part:
                jobs_part.append( part )
            elif ')' in part:
                parse_state -= 1
                jobs_part.append( part )
            else:
                jobs_part.append( part )

    if len(jobs_part) > 0:
        new_parts.append( ','.join( jobs_part ) )

    status_dict = {}
    for keyval in new_parts:
        k, v = keyval.split('=',1)
        status_dict[k] = v

    return status_dict
        
def _pretty_print_element( e ):
    """
    Pretty print an XML representation of a given ElementTree.Element
    """
    import xml.dom.minidom
    print xml.dom.minidom.parseString( ET.tostring( e ) ).toprettyxml()

def _pretty_print_dict( d ):
    """
    Pretty print a dict (or list) as json
    """
    import json
    print json.dumps( status, sort_keys=True, indent=4 )

def nodeview( args ):
    element = _get_subprocess_xml( [ 'pbsnodes', '-x' ] )

    nodelist = element.findall( './Node' )
    for node in nodelist:
        vals = []

        # get node status
        status = node.find('status')
        if status is not None: 
            status = parse_node_status( status.text )
        else:
            status = {}

        # try to get node name from node status first, then from torque
        if 'name' in status:
            name = status['name']
        elif node.find('name') is not None:
            name = node.find('name').text
        if name is None:
            name = 'unknown'

        # try to get number of cores--from node status first, then try torque
        np = 0
        if 'CPROC' in status:
            np = int(status['CPROC'])
        elif 'ncpus' in status:
            np = int(status['ncpus'])
        elif node.find('np') is not None:
            np = int(node.find('np').text)

        # try to get available cores
        if 'APROC' in status:
            np_avail = int(status['APROC'])
        else:
            np_avail = np

        # try to get total physical memory and avail memory
        if 'availmem' in status:
            availmem_kb = int(status['availmem'].strip('kb'))
        else:
            availmem_kb = 0

        if 'physmem' in status:
            physmem_kb = int(status['physmem'].strip('kb'))
            availmem_pct = 100.0 * (1.0 - float(availmem_kb) / float(physmem_kb))
        else:
            physmem_kb = 0
            availmem_pct = 0

        # node state (generally an arbitrary string)
        if 'state' in status:
            state = status['state']
        else:
            state = ""

        # load on node.  XT nodes do not report this
        if 'loadave' in status:
            load = float( status['loadave'] )
        else:
            load = 0.0

        property_string = [ state ]
        if node.find('properties') is not None:
             property_string = property_string + node.find('properties').text.split(',')

        print "%-14s %4d %4d %7d %3d/%3d %5.1fG %6.1f%% %7.2f %s" % (
            name,
            0,
            0,
            np,
            np-np_avail,
            np,
            physmem_kb / 1024.0 / 1024.0,
            availmem_pct,
            load,
            ':'.join( property_string ).lower() )
# 12345678901234 1234 1234 1234567 1234567 123456 1234567 1234567 123456
# node           jobs rnks cpus    slots   totmem %memuse avgload state

if __name__ == '__main__':
    _pretty_print_element( _get_subprocess_xml( [ 'pbsnodes', '-x' ] ) )


