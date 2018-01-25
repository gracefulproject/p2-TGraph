from rig.machine_control import MachineController
import sys
import random

if len(sys.argv) < 2:
    print "Usage: python gen_tgmap.py <MACHINE_IP>"
    sys.exit(1)

mc = MachineController(sys.argv[1])
mInfo = mc.get_system_info()
chips_org = mInfo.keys()
chips_srt = mInfo.keys()
chips_srt.sort()
chips_rnd = mInfo.keys()
random.shuffle(chips_rnd)

if len(chips_org) != 144:
    print "Dead chip(s) detected...!"
    sys.exit(1)

# then select some chips and assign the id to them
# Node ID from 0 to 119

# tgmap 1
with open("map_srt.tgmap", "w") as f1:
    i = 0
    f1.write("(0,0)=65535\n")
    for c in chips_srt:
        if i==120:
            break
        if c != (0,0):
            str = "({},{})={}\n".format(c[0],c[1],i)
            f1.write(str)
            i += 1

# tgmap 2
with open("map_org.tgmap", "w") as f2:
    i = 0
    f2.write("(0,0)=65535\n")
    for c in chips_org:
        if i==120:
            break
        if c != (0,0):
            str = "({},{})={}\n".format(c[0],c[1],i)
            f2.write(str)
            i += 1

# tgmap 3
with open("map_rnd.tgmap", "w") as f3:
    i = 0
    f3.write("(0,0)=65535\n")
    for c in chips_rnd:
        if i==120:
            break
        if c != (0,0):
            str = "({},{})={}\n".format(c[0],c[1],i)
            f3.write(str)
            i += 1

