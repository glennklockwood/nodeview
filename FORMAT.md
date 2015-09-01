Torque pbsnodes XML format
==========================

Torque's pbsnodes returns a variety of information encoded in XML.  Cray XT
nodes look like this:

    <Node>
        <name>6040</name>
        <state>job-exclusive,busy</state>
        <power_state>Running</power_state>
        <np>24</np>
        <properties>cray_compute</properties>
        <ntype>cluster</ntype>
        <jobs>0-23/3519203.edique02</jobs>
        <status>
            rectime=1441134521,node_index=5469,availmem=0kb,state=BUSY,physmem=67108864kb,totmem=67108864kb,CMEMORY=65536,APROC=0,CPROC=24,CCU=0,name=c7-3c1s6n0,ARCH=XT
        </status>
        <mom_service_port>15002</mom_service_port>
        <mom_manager_port>15003</mom_manager_port>
    </Node>

And login nodes look like this:

<?xml version="1.0" ?>
<Node>
    <name>nid01664</name>
    <state>free</state>
    <power_state>Running</power_state>
    <np>64</np>
    <properties>alps_login</properties>
    <ntype>cluster</ntype>
    <jobs/>
    <status>
        rectime=1441144900,macaddr=00:01:01:00:08:80,cpuclock=Performance:2401MHz,varattr=,jobs=3508074.edique02(cput=1883,energy_used=0,mem=90296kb,vmem=438936kb,walltime=164997) 3509274.edique02(cput=9,energy_used=0,mem=11000kb,vmem=160356kb,walltime=133151) 3512277.edique02(cput=2,energy_used=0,mem=10944kb,vmem=156892kb,walltime=80685) 3513585.edique02(cput=1,energy_used=0,mem=11128kb,vmem=159520kb,walltime=59129) 3514272.edique02(cput=1,energy_used=0,mem=10660kb,vmem=91236kb,walltime=57049) 3517738.edique02(cput=2,energy_used=0,mem=10556kb,vmem=159688kb,walltime=25868) 3518461.edique02(cput=0,energy_used=0,mem=10856kb,vmem=163864kb,walltime=19740,session_id=48466) 3510901.edique02(cput=0,energy_used=0,mem=10576kb,vmem=159420kb,walltime=13580,session_id=31177) 3518929.edique02(cput=1,energy_used=0,mem=10840kb,vmem=94248kb,walltime=13374) 3519493.edique02(cput=0,energy_used=0,mem=10836kb,vmem=160224kb,walltime=7006,session_id=23363) 3517592.edique02(cput=1,energy_used=0,mem=10360kb,vmem=90584kb,walltime=6464,session_id=29103) 3517595.edique02(cput=1,energy_used=0,mem=10360kb,vmem=156120kb,walltime=4575,session_id=2108) 3519940.edique02(cput=1,energy_used=0,mem=10648kb,vmem=156728kb,walltime=2657,session_id=24726) 3518413.edique02(cput=1,energy_used=0,mem=6212kb,vmem=69848kb,walltime=1892,session_id=31263) 3518785.edique02(cput=1,energy_used=0,mem=6188kb,vmem=135380kb,walltime=1523,session_id=37263) 3521144.edique02(cput=0,energy_used=0,mem=7400kb,vmem=161824kb,walltime=407,session_id=49075),state=free,netload=1004344494441,gres=,loadave=0.10,ncpus=48,physmem=66070012kb,availmem=56351776kb,totmem=66070012kb,idletime=14764,nusers=14,nsessions=16,sessions=49075 37263 31263 24726 2108 29103 23363 32525 31177 48466 26308 30249 24142 7124 42105 31655,uname=Linux nid01664 3.0.101-0.35.1_1.0502.8640-cray_ari_s #1 SMP Wed Feb 18 05:08:48 UTC 2015 x86_64,opsys=linux
    </status>
    <mom_service_port>15002</mom_service_port>
    <mom_manager_port>15003</mom_manager_port>
</Node>


The 'state' field in each node's XML output varies based on its function.  These
are Cray XT nodes:

    c0-0c2s5n0
    {
        "APROC": "0", 
        "ARCH": "XT", 
        "CCU": "0", 
        "CMEMORY": "65536", 
        "CPROC": "24", 
        "availmem": "0kb", 
        "name": "c0-0c2s5n0", 
        "node_index": "124", 
        "physmem": "67108864kb", 
        "rectime": "1441143477", 
        "state": "BUSY", 
        "totmem": "67108864kb"
    }
    c8-1c0s7n1
    {
        "APROC": "24", 
        "ARCH": "XT", 
        "CCU": "0", 
        "CMEMORY": "32768", 
        "CPROC": "24", 
        "availmem": "33554432kb", 
        "name": "c8-1c0s7n1", 
        "node_index": "6383", 
        "physmem": "33554432kb", 
        "rectime": "1441142783", 
        "state": "UP", 
        "totmem": "33554432kb"
    }

This is a Cray login node (from which job scripts run):

    nid05416
    {
        "availmem": "27833764kb", 
        "cpuclock": "Fixed", 
        "gres": "", 
        "idletime": "605351", 
        "jobs": "13081629.hopque01(cput=8,energy_used=0,mem=6208kb,vmem=70092kb,walltime=244194) 13084590.hopque01(cput=32,energy_used=0,mem=6448kb,vmem=135840kb,walltime=166630) 13086850.hopque01(cput=8,energy_used=0,mem=6624kb,vmem=136152kb,walltime=116718) 13087052.hopque01(cput=9,energy_used=0,mem=6612kb,vmem=70612kb,walltime=116049) 13087251.hopque01(cput=2,energy_used=0,mem=6156kb,vmem=135604kb,walltime=114906) 13087511.hopque01(cput=3,energy_used=0,mem=6672kb,vmem=70492kb,walltime=111058) 13087899.hopque01(cput=4,energy_used=0,mem=8720kb,vmem=136180kb,walltime=104707) 13088044.hopque01(cput=4,energy_used=0,mem=6720kb,vmem=136180kb,walltime=104235) 13088110.hopque01(cput=2,energy_used=0,mem=8468kb,vmem=149152kb,walltime=103689) 13088147.hopque01(cput=4,energy_used=0,mem=6704kb,vmem=70400kb,walltime=102741) 13092510.hopque01(cput=18,energy_used=0,mem=10952kb,vmem=136416kb,walltime=75884) 13092609.hopque01(cput=15,energy_used=0,mem=6712kb,vmem=136012kb,walltime=70564) 13092234.hopque01(cput=3,energy_used=0,mem=8728kb,vmem=88556kb,walltime=68796) 13092257.hopque01(cput=2,energy_used=0,mem=8728kb,vmem=88556kb,walltime=35043) 13093222.hopque01(cput=1,energy_used=0,mem=5800kb,vmem=135052kb,walltime=31765) 13093390.hopque01(cput=1,energy_used=0,mem=6028kb,vmem=69912kb,walltime=31622) 13093710.hopque01(cput=1,energy_used=0,mem=6032kb,vmem=135448kb,walltime=26361) 13094208.hopque01(cput=1,energy_used=0,mem=6876kb,vmem=247904kb,walltime=25138) 13094398.hopque01(cput=29,energy_used=0,mem=12008kb,vmem=251596kb,walltime=21485) 13094387.hopque01(cput=3,energy_used=0,mem=6760kb,vmem=136096kb,walltime=20602) 13095056.hopque01(cput=3,energy_used=0,mem=6704kb,vmem=135932kb,walltime=15200) 13098036.hopque01(cput=5,energy_used=0,mem=6456kb,vmem=135708kb,walltime=8526) 13096680.hopque01(cput=0,energy_used=0,mem=7620kb,vmem=126948kb,walltime=8321) 13094746.hopque01(cput=17,energy_used=0,mem=17896kb,vmem=164756kb,walltime=4373,session_id=20564) 13098869.hopque01(cput=2,energy_used=0,mem=6408kb,vmem=70128kb,walltime=2943,session_id=27883)", 
        "loadave": "0.31", 
        "macaddr": "00:01:01:00:38:50", 
        "ncpus": "24", 
        "netload": "1122221155742", 
        "nsessions": "25", 
        "nusers": "18", 
        "opsys": "linux", 
        "physmem": "33080176kb", 
        "rectime": "1441142759", 
        "sessions": "27883 20564 9961 6798 22079 23572 12098 30264 15321 15922 14180 2997 23106 29060 24714 28493 23670 19812 14738 12259 28398 22758 17735 14334 31287", 
        "state": "free", 
        "totmem": "33080176kb", 
        "uname": "Linux nid05416 3.0.101-0.31.1_1.0502.8394-cray_gem_s #1 SMP Wed Sep 10 03:56:55 UTC 2014 x86_64", 
        "varattr": ""
    }

Nodeview Output
===============

The original nodeview had columnar output as follows:

    node           jobs rnks cpus    slots   totmem %memuse avgload state          
    gcn-2-11          1    8   16    16/16    65.0G    6.9%   27.91 overload       
    gcn-2-12          1    8   16    16/16    65.0G    6.7%   37.36 overload       
    gcn-2-13          1    8   16    16/16    65.0G    6.7%   36.01 overload       
    gcn-2-14          1    8   16    16/16    65.0G    6.6%   31.69 overload       
    gcn-2-15          1   16   16    16/16    65.0G   37.5%   16.02                
    gcn-2-16          1    8   16    16/16    65.0G    6.6%   37.20 overload       
    ...
    Total Nodes      :    912
    Total Cores      :  14832
    Total Jobs       :    427
    Total Ranks      :  13753
    Total Load       : 10926.7
    Total SUs Running: 672995
    Total SUs Queued : 693117
    Node Availability:    905/   916 ( 98.8%)
    CPU Utilization  : 10926.7/ 14832 ( 73.7%)
    Core Utilization :  13753/ 14832 ( 92.7%)
    Slot Utilization :  13880/ 14896 ( 93.2%)
    Avail Slot Util  :  13880/ 14720 ( 94.3%)
    Mem Utilization  :  5.8TB/58.7TB (  9.9%)
