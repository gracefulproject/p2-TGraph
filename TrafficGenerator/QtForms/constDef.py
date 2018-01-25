# For debugging:
SHOW_PARSING_RESULT     = False
SINGLE_SIMULATION       = True
DEF_MIN_TIMER_TICK      = 100               # in microsecond


DEF_MIN_RUNNING_TIME    = 0
DEF_MAX_RUNNING_TIME    = 1000*60*60        # 1 hour max simulation

# Operational
BOOT_MACHINE            = True
DEF_HOST                = '10.2.225.9'
#DEF_HOST                = '192.168.240.1'   # since we need at least 10 chips
#DEF_HOST                = '192.168.240.253'   # since we need at least 10 chips
DEF_MYPC                = '192.168.240.2'
DEF_SEND_PORT           = 17893             # tidak bisa diganti dengan yang lain
DEF_TUBO_PORT           = 17892             # just for your info :)
DEF_TUBO_IPTAG          = 0
DEF_REPORT_PORT         = 17900             # for reading report data from SpiNNaker through iptag-1
DEF_REPORT_IPTAG        = 1                 # put this value in ybug!!!
DEF_SEND_IPTAG          = 0                 # for sending *into* SpiNNaker machine
DEF_SDP_CONF_PORT       = 7                 # Use port-7 for configuration
DEF_SDP_CORE            = 1                 # Let's use core-1 at the moment (future: configurable!)
DEF_SDP_TIMEOUT         = 0.025             # in second
WITH_REPLY              = 0x87
NO_REPLY                = 0x07

APPID_TGSDP		        = 16
APPID_SRCSINK	        = 17
APPID_MONITOR           = 255
TGPKT_CHIP_NODE_MAP     = 0xc01e
TGPKT_DEPENDENCY        = 0xdec1
TGPKT_HOST_ASK_REPORT   = 0x2ead
TGPKT_SOURCE_TARGET		= 0x52ce
TGPKT_START_SIMULATION	= 0x6060
TGPKT_STOP_SIMULATION	= 0x7070
TGPKT_HOST_SEND_TICK	= 0x71c4
TGPKT_PING              = 0x7179

DEF_SOURCE_ID = 0xFFFF
DEF_SOURCE_PORT = 1         # SOURCE will send through port-1
DEF_SINK_ID = 0xFFFF
DEF_SINK_PORT = 2           # SINK will receive through port-2
DEF_APP_CORE = 1
DEF_MON_CORE = 2            # cannot use core-17 because some chips don't have it (broken?)


# Regarding iptag, I found that enabling iptag reduces the throughput considerably
ENABLE_IPTAG = False

"""
Chip list should be generated automatically from machineInfo

# CHIP_LIST_48 contains 1D array of chipID, starting from 0 (==<0,0>) to 47(==<7,7,>)
CHIP_LIST_48 = [[0,0],[1,0],[2,0],[3,0],[4,0],\
                [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],\
                [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],\
                [0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],\
                      [1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],\
                            [2,5],[3,5],[4,5],[5,5],[6,5],[7,5],\
                                  [3,6],[4,6],[5,6],[6,6],[7,6],\
                                        [4,7],[5,7],[6,7],[7,7]]

STATIC_CHIP_LIST_144 = [[0,0],[1,0],[2,0],[3,0],[4,0],\
                        [0,1],[1,1],[2,1],[3,1],[4,1], [5,1],\
                        [0,2],[1,2],[2,2],[3,2],[4,2], [5,2], [6,2],\
                        [0,3],[1,3],[2,3],[3,3],[4,3], [5,3], [6,3], [7,3],\
                              [1,4],[2,4],[3,4],[4,4], [5,4], [6,4], [7,4], [8,4], [9,4], [10,4], [11,4], [12,4],\
                                    [2,5],[3,5],[4,5], [5,5], [6,5], [7,5], [8,5], [9,5], [10,5], [11,5], [12,5], [13,5],\
                                          [3,6],[4,6], [5,6], [6,6], [7,6], [8,6], [9,6], [10,6], [11,6], [12,6], [13,6], [14,6],\
                                                [4,7], [5,7], [6,7], [7,7], [8,7], [9,7], [10,7], [11,7], [12,7], [13,7], [14,7], [15,7],\
                                                [4,8], [5,8], [6,8], [7,8], [8,8], [9,8], [10,8], [11,8], [12,8], [13,8], [14,8], [15,8],\
                                                [4,9], [5,9], [6,9], [7,9], [8,9], [9,9], [10,9], [11,9], [12,9], [13,9], [14,9], [15,9],\
                                                [4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[14,10],[15,10],\
                                                [4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11],[11,11],[12,11],[13,11],[14,11],[15,11],\
                                                       [5,12],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],\
                                                              [6,13],[7,13],[8,13],[9,13],[10,13],[11,13],\
                                                                     [7,14],[8,14],[9,14],[10,14],[11,14],\
                                                                            [8,15],[9,15],[10,15],[11,15]]

#CHIP_LIST_48 = STATIC_CHIP_LIST_144
"""
# Let's generate static mapping from TGnodes to SpiNN-chips
        # SOURCE and SINK send to chip<0,0>, since it is connected to ethernet
        # node-0, send to chip<1,0> == map[1] in the CHIP_LIST_48
        # node-1, send to chip<2,0> == map[2]
        # node-2, send to chip<3,0> == map[3]
        # node-3, send to chip<4,0> == map[4]
        # node-4, send to chip<0,1> == map[5]
        # node-5, send to chip<1,1> == map[6]
        # node-6, send to chip<2,1> == map[7]
        # node-7, send to chip<3,1> == map[8]
        # node-8, send to chip<4,1> == map[9]
        # let's put those in a "map" and "cfg" variables
        # TODO (future): use rig to find out the available chips (undead ones?)
# The following will produce: [65535, 0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
smallmap = [-1 for _ in range(48)]
for mapItem in range(9):
    smallmap[mapItem+1] = mapItem    # we start from i+1 because chip<0,0> will be used for SOURCE and SINK
smallmap[0] = DEF_SOURCE_ID

bigmap = [-1 for _ in range(48)]
for mapItem in range(47):
    bigmap[mapItem+1] = mapItem    # we start from i+1 because chip<0,0> will be used for SOURCE and SINK
bigmap[0] = DEF_SOURCE_ID

map25 = [-1 for _ in range(48)]
for mapItem in range(25):
    map25[mapItem+1] = mapItem
map25[0] = DEF_SOURCE_ID

map143 = [-1 for _ in range(144)]
for mapItem in range(143):
    map143[mapItem+1] = mapItem
map143[0] = DEF_SOURCE_ID

# Untuk keperluan eksperimen ambil data:
# map d0_8 untuk 8 nodes
mapexp_d0_8 = bigmap

#map d1_8 untuk 8 nodes
mapexp_d1_8 = [-1 for _ in range(48)]
#mapexp_d1_8 = [65535, 0, -1, 1, -1,-1,-1,-1,-1,-1,-1,2,-1,3,-1,4,-1,5,-1,-1,-1,-1,-1,-1,-1,-1,6,-1,7,-1,...]
mapexp_d1_8[0] = 65535; mapexp_d1_8[1] = 0; mapexp_d1_8[3] = 1; mapexp_d1_8[11] = 2
mapexp_d1_8[13] = 3; mapexp_d1_8[15] = 4; mapexp_d1_8[17] = 5
mapexp_d1_8[26] = 6; mapexp_d1_8[28] = 7; mapexp_d1_8[30] = 8

#map d2_8 untuk 8 nodes
mapexp_d2_8 = [-1 for _ in range(144)]
mapexp_d2_8[0] = 65535; mapexp_d2_8[1] = 0; mapexp_d2_8[4] = 1
mapexp_d2_8[18] = 2; mapexp_d2_8[21] = 3; mapexp_d2_8[24] = 4
#mapexp_d2_8[50] = 5; mapexp_d2_8[54] = 6; mapexp_d2_8[88] = 7; mapexp_d2_8[92] = 8
mapexp_d2_8[64] = 5; mapexp_d2_8[77] = 6; mapexp_d2_8[100] = 7; mapexp_d2_8[123] = 8


tg2spinMap = dict()
# Yang berikut buat eksperimen ambil data
tg2spinMap['d0'] = mapexp_d0_8
tg2spinMap['d1'] = mapexp_d1_8
tg2spinMap['d2'] = mapexp_d2_8
"""

tg2spinMap['9Nodes'] = smallmap;
tg2spinMap['47Nodes'] = bigmap;
tg2spinMap['25Nodes'] = map25
tg2spinMap['143Nodes'] = map143
"""
