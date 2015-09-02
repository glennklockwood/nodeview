#!/usr/bin/env python

import nodeview

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
    _SPECIAL_FIELDS = [ 'jobs', 'message' ]
    parse_state = 0
    new_parts = []
    special_part = []
    special_parts = []
    parts = status_str.split(',')
    for part in parts:
        # not currently parsing a special field
        if parse_state == 0:
            is_special_field = False
            # is this field one that must be parsed specially?
            for special_field in _SPECIAL_FIELDS:
                if part.startswith( special_field + '=' ) and '(' in part:
                    parse_state += 1
                    special_part.append( part )
                    is_special_field = True
                    break
            if not is_special_field:
                new_parts.append( part )
        # currently parsing a special field
        elif parse_state == 1:
            if ')' in part and '(' in part:
                special_part.append( part )
            elif ')' in part:
                parse_state -= 1
                special_part.append( part )
                special_parts.append( special_part )
                special_part = []
            else:
                special_part.append( part )

    for parts in special_parts:
        if len( parts ) > 0:
            new_parts.append( ','.join( parts ) )

    status_dict = {}
    for keyval in new_parts:
        if '=' in keyval:
            k, v = keyval.split('=',1)
        else:
            k = ""
            v = keyval
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

def generate_nodelist( ):
    element = _get_subprocess_xml( [ 'pbsnodes', '-x' ] )

    node_list = []
    node_elements = element.findall( './Node' )
    for node in node_elements:
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
        else:
            physmem_kb = 0

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

        if node.find('properties') is not None:
            properties = node.find('properties').text.split(',')
        else:
            properties = []

        node_list.append( nodeview.Node( 
            name=name,
            np=np,
            np_avail=np_avail,
            physmem_kb=physmem_kb,
            availmem_kb=availmem_kb,
            load=load,
            state=state,
            properties=properties,
            other_info=status) )

    return node_list

if __name__ == '__main__':
    _pretty_print_element( _get_subprocess_xml( [ 'pbsnodes', '-x' ] ) )


