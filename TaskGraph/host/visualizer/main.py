#!/usr/bin/env python
"""
SYNOPSIS:
    Simple framework to do experiment with task graph using sdp mechanism. 
    Created on 2 Nov 2016
    @author: indar.sugiarto@manchester.ac.uk
"""


from PyQt4 import Qt, QtGui
from tgvis import visWidget
import sys
from rig.machine_control import MachineController

#MACHINE_IP = '10.2.225.9'

class mainWidget(QtGui.QWidget):
    def __init__(self, MACHINE_IP, parent=None):
        super(mainWidget, self).__init__(parent)
        self.setGeometry(0,0,640,480)
        self.setWindowTitle("SpiNNaker Chips Visualizer")

        # get info from rig:
        mc = MachineController(MACHINE_IP)
        mc.boot()
        mInfo = mc.get_system_info()
        w = mInfo.width
        h = mInfo.height
        chipList = mInfo.keys()
        self.vis = visWidget(w, h, chipList, self)
        self.vis.setGeometry(0,0,self.width(),self.height())

    def resizeEvent(self, event):
        self.vis.setGeometry(0,0,self.width(), self.height())

if __name__=='__main__':
    if len(sys.argv) < 2:
        print "Please provide the ip address of the target machine!"
    else:
        myApp = Qt.QApplication(sys.argv)
        myMainWidget = mainWidget(sys.argv[1])
        myMainWidget.show()
        sys.exit(myApp.exec_())
