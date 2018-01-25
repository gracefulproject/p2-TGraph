from PyQt4 import QtGui, QtCore
import sys
import QtMainWindow
from tgxmlParser import tgxmlHandler
import xml.sax
#from tgsdpvis import visWidget
from visualizer.tgvis import visWidget
from sdpComm import sdpComm
import time

from constDef import *
from helper import *
from rig.machine_control import MachineController


class tgViever(QtGui.QWidget):
    def __init__(self, gviewer, okToClose=False, parent=None):
        super(tgViever, self).__init__(parent)
        self.gviewer = gviewer
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.gviewer)
        self.setLayout(layout)
        self.okToClose = okToClose

    def closeEvent(self, e):
        if self.okToClose:
            e.accept()

    @QtCore.pyqtSlot(list)
    def updateHist(self, xy):
        """
        This Slot should be connected to sdp.histUpdate
        """
        self.gviewer.updateHist(xy)

    def animate(self):
        self.gviewer.sceneTimer.start(500)

    def deanimate(self):
        self.gviewer.sceneTimer.stop()


class MainWindow(QtGui.QMainWindow, QtMainWindow.Ui_qtMainWindow):
    def __init__(self, cli_param, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.mdiArea)
        self.statusTxt = QtGui.QLabel("")
        self.dagFile = QtGui.QLabel("")
        self.statusBar().addWidget(self.dagFile)
        self.statusBar().addWidget(self.statusTxt)

        # connect to the machine
        if len(cli_param) > 1:
            ip = cli_param[1]
            if len(cli_param) > 2:
                self.myPC = cli_param[2]
            else:
                self.myPC = DEF_MYPC
        else:
            ip, ok = QtGui.QInputDialog.getText(None, "Connect to SpiNNaker", "Please specify machine IP",
                                                QtGui.QLineEdit.Normal, DEF_HOST)
            if ok is False:
                ip = ''
        print "Using machine at",ip
        self.mc = MachineController(ip)
        if BOOT_MACHINE is True:
            if self.mc.boot() is True:
                print "Machine is now booted..."
            else:
                print "Machine is already booted..."

        # then use machineInfo to build the map
        self.mInfo = self.mc.get_system_info()
        wMachine = self.mInfo.width
        hMachine = self.mInfo.height
        self.chipList = self.mInfo.keys()
        print "Found",len(self.chipList), "active chips:"
        """
        self.mc.iptag_set(0,'192.168.240.2',17892,0,0) # prepare iptag for myTub, because boot in rig doesn't provide this
        if DEF_HOST=='192.168.240.1':
            self.statusTxt.setText("Using SpiNN-5 board at {}".format(DEF_HOST))
        else:
            self.statusTxt.setText("Using SpiNN-3 board at {}".format(DEF_HOST))
        """

        #self.vis = visWidget(wMachine, hMachine, self.chipList, self.mdiArea)
        # for known dead chips on certain boards
        knownDeadChips = []
        if (len(self.chipList) % 48) != 0:
            # dead chip is detected
            lst = QtGui.QInputDialog.getText(self, "Dead chip is detected",
                                                 "Please provide chip coordinate in () separated by space",
                                                 QtGui.QLineEdit.Normal, "(0,2)")
            knownDeadChips = getDeadChipList(lst)
        self.tgvisWidget = visWidget(wMachine, hMachine, self.chipList, knownDeadChips)
        self.vis = tgViever(self.tgvisWidget)
        #self.vis.setGeometry(0,0,1024,1024)
        #self.vis.scale(0.5,0.5) # put in half size

        self.vis.hide()
        self.action_Visualiser.setCheckable(True)
        #self.action_Visualiser.setChecked(False)

        self.connect(self.action_Quit, QtCore.SIGNAL("triggered()"), QtCore.SLOT("Quit()"))
        self.connect(self.action_Load_XML, QtCore.SIGNAL("triggered()"), QtCore.SLOT("loadXML()"))
        self.connect(self.action_Visualiser, QtCore.SIGNAL("triggered()"), QtCore.SLOT("showVisualiser()"))
        self.connect(self.action_Send_and_Init, QtCore.SIGNAL("triggered()"), QtCore.SLOT("sendAndInit()"))
        self.connect(self.actionInspect_SpinConf, QtCore.SIGNAL("triggered()"), QtCore.SLOT("testSpin1()"))
        self.connect(self.actionSet_Tick, QtCore.SIGNAL("triggered()"), QtCore.SLOT("getSimulationTick()"))
        self.connect(self.actionStart, QtCore.SIGNAL("triggered()"), QtCore.SLOT("startSim()"))
        self.connect(self.actionStop, QtCore.SIGNAL("triggered()"), QtCore.SLOT("stopSim()"))

        # 22 March 2017 - 11:48 - Buat experiment ambil data untuk paper
        self.timer = QtCore.QTimer(self)
        #self.timer.setInterval(60000) # one minute experiment
        self.timer.timeout.connect(self.timeout)

        # Simulation parameters
        self.simTick = 1000000      # default value that yield 1second resolution
        self.runningTime = 0        # 0 means runs forever
        self.dag = None          # this is a list of list of dict that contains target dependency data
        """
        self.srcTarget = dict()     # this similar to self.dag, but just contains target for SOURCE node
                                    # (as a dict of a list), e.g: from dag0020, srcTarget = {0: [4,3,2]}
        """
        self.srcTarget = list()     # now scrTarget becomes simpler, because we don't send the trigger's payload
        self.sdp = sdpComm(self.chipList, ip)
        self.sdp.histUpdate.connect(self.vis.updateHist)
        self.setGeometry(0,0,1024,1024)



    @QtCore.pyqtSlot()
    def timeout(self):
        """
        Ini buat ambil data. Setelah jalan 1 menit, otomatis stop. Kemudian lihat iobuf dari srcsink node!
        :return:
        """
        self.stopSim()
        self.timer.stop()

    def closeEvent(self, e):
        self.vis.close()
        e.accept()

    @QtCore.pyqtSlot()
    def Quit(self):
        # TODO: clean up...
        self.close()

    @QtCore.pyqtSlot()
    def showVisualiser(self):
        if self.action_Visualiser.isChecked() is True:
            #self.vis = visWidget(self.mdiArea)     # cuman buat sejarah kalau dulu aku letakkan di sini!
            #self.vis.setGeometry(0,0,1024,1024)
            self.vis.animate()
            #self.vis.sceneTimer.start(500)
            self.vis.show()
        else:
            self.vis.deanimate()
            self.vis.hide()
            #self.vis.sceneTimer.stop()

    def buildMap(self):
        """
        Let's build map correctly
        :input: self.dag
        :output: self.TGmap
        """

    def readTGmap(self, fname, chipList, numNode):
        """
        Read TGmap configuration from the given fname
        :param fname: .tgmap configuration file
        :param chipList: a dict() that contains all active chip coordinate in the machine
        :return: list() if success, otherwise None
        """
        result = None
        ok = False
        with open(fname, 'r') as fid:
            dct = dict()
            nodeFound = 0
            for line in fid:
                #print "line:", line
                idFromXY = getChipIDfromXY(line)
                if idFromXY is not None:
                    dct.update(idFromXY)
                    nodeFound += 1
            if len(dct) > 0:
                print "Found", nodeFound, "nodes (including SRC/SINK)"
                result = [-1 for _ in range(len(chipList))]
                for i in range(len(chipList)):
                    try:
                        result[i] = dct[chipList[i]]
                    except KeyError:
                        result[i] = -1
                if nodeFound==numNode+1:
                    ok = True
        return result, ok

    @QtCore.pyqtSlot()
    def loadXML(self):
        print "Loading XML..."
        fullPathFileName = QtGui.QFileDialog.getOpenFileName(self, "Open XML file", "./", "*.xml")
        if not fullPathFileName:
            print "Cancelled!"
        else:

            fi = QtCore.QFileInfo()
            fi.setFile(fullPathFileName)
            fn = fi.fileName()
            self.dagFile.setText("Using {}".format(fn))
            print "Processing ", fullPathFileName
            parser = xml.sax.make_parser()

            # turn off namespace
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)

            # override the default ContextHandler
            Handler = tgxmlHandler()
            parser.setContentHandler(Handler)
            parser.parse(str(fullPathFileName))


            if SHOW_PARSING_RESULT:
                showParsingResult(Handler)

            """ Let's put the c-like struct as a list:
                Let's create a variable cfg, which is a list of a dict.
                Then, let's create a variable dag, which is a list of cfg. Hence, dag is a list of a list of a dict.
            """
            dag = list()
            for nodes in Handler.Nodes:
                cfg = list()
                srcPayload = list()
                srcFound = False
                for target in nodes.Target:
                    dct = dict()
                    dct['nodeID'] = nodes.Id
                    dct['destID'] = target.destId
                    dct['nPkt'] = target.nPkt
                    dct['nDependant'] = target.nDependant
                    for d in range(target.nDependant):
                        srcIDkey = "dep{}_srcID".format(d)
                        nTriggerPktkey = "dep{}_nTriggerPkt".format(d)
                        dct[srcIDkey] = target.Dep[d].srcId
                        dct[nTriggerPktkey] = target.Dep[d].nTriggerPkt
                        # also search for SOURCE dependant
                        if target.Dep[d].srcId==DEF_SOURCE_ID:
                            srcFound = True
                            srcPayload.append(target.Dep[d].nTriggerPkt)
                    cfg.append(dct)
                    # and put the payload to the current word in the dict
                if srcFound:
                    self.srcTarget.append(nodes.Id)
                    # self.srcTarget[nodes.Id] = srcPayload --> ini yang lama sebelum aku REVISI
                dag.append(cfg)

            self.dag = dag
            #self.dag = experiment_dag0020()


            # for debugging:
            #print "SpiNNaker usage  :", self.TGmap
            if SHOW_PARSING_RESULT:
                print "TG configuration :", self.dag
            #print len(self.dag)
            print "Source Target    :", self.srcTarget

            # then load the TGmap configuration file
            tgmapConfigFile = QtGui.QFileDialog.getOpenFileName(self, "Open TGmap file", "./", "*.tgmap")
            if not tgmapConfigFile:
                print "Cancelled!"
                self.dag = None
                self.srcTarget = list()
                return

            tgmap, ok = self.readTGmap(tgmapConfigFile, self.chipList, len(self.dag))
            if tgmap is None:
                print "Failed to get correct TGmap configuration!"
                # then cancel the operation and reset
                self.dag = None
                self.srcTarget = list()
                return
            else:
                if ok:
                    #print tgmap
                    print "Loaded tgmap from:", tgmapConfigFile
                    self.TGmap = tgmap
                else:
                    print "Missing node is detected! Maybe dead chip?"
                    # then cancel the operation and reset
                    self.dag = None
                    self.srcTarget = list()
            """
            # Then ask for the appropriate map
            cbItem = tg2spinMap.keys();
            # simTick, ok = QtGui.QInputDialog.getInt(self, "Simulation Tick", "Enter Simulation Tick in microsecond", self.simTick, DEF_MIN_TIMER_TICK, 10000000, 1)

            mapItem, ok = QtGui.QInputDialog.getItem(self, "Select Map", "Which map will be used?", cbItem, 0, False)
            if ok is True:
                print "Will use",mapItem,':',tg2spinMap[str(mapItem)]
                # self.initMap(mapItem)
                self.TGmap = tg2spinMap[str(mapItem)]
            else:
                print "Cancelled!"
                return
            """


            # continue with send and init?
            contSendInit = QtGui.QMessageBox.question(self, "Continue", "Continue with Send and Init?",
                                                      QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if contSendInit==QtGui.QMessageBox.Ok:
                self.sendAndInit()
            else:
                QtGui.QMessageBox.information(self, "Done",
                                              "Loading XML and TGmap is done! You can continue with Send and Init!")


    @QtCore.pyqtSlot()
    def testSpin1(self):
        """
        send a request to dump tgsdp configuration data
        sendSDP(self, flags, tag, dp, dc, dax, day, cmd, seq, arg1, arg2, arg3, bArray):
        """
        f = NO_REPLY
        t = DEF_SEND_IPTAG
        p = DEF_SDP_CONF_PORT
        c = DEF_SDP_CORE
        m = TGPKT_HOST_ASK_REPORT

        for item in self.TGmap:
            if item != -1 and item != DEF_SOURCE_ID:
                x, y = getChipXYfromID(self.TGmap, item, self.chipList)
                #print "Sending a request to <{},{}:{}>".format(x,y,c)
                self.sdp.sendSDP(f,t,p,c,x,y,m,0,0,0,0,None)
                time.sleep(DEF_SDP_TIMEOUT)

    @QtCore.pyqtSlot()
    def sendAndInit(self):
        """
        will send aplx to corresponding chip and initialize/configure the chip
        Assuming that the board has been booted?
        """

        if self.dag==None:
            QtGui.QMessageBox.information(self, "Information", "No valid network structure yet!")
            return

        # First, need to translate from node-ID to chip position <x,y>, including the SOURCE and SINK node
        # use self.TGmap
        print "Doing translation from node to chip..."
        self.xSrc, self.ySrc = getChipXYfromID(self.TGmap, DEF_SOURCE_ID, self.chipList)
        appCores = dict()
        for item in self.TGmap:
            if item != -1 and item != DEF_SOURCE_ID:
                x, y = getChipXYfromID(self.TGmap, item, self.chipList)
                appCores[(x,y)] = [DEF_APP_CORE]

        if SHOW_PARSING_RESULT:
            print "Application cores :", appCores
        allChips = dict()
        for item in self.chipList:
            allChips[(item[0],item[1])] = [DEF_MON_CORE]
        if SHOW_PARSING_RESULT:
            print "Monitor cores :", allChips
        # Second, send the aplx (tgsdp.aplx and srcsink.aplx) to the corresponding chip
        # example: mc.load_application("bla_bla_bla.aplx", {(0,0):[1,2,10,17]}, app_id=16)
        # so, the chip is a tupple and cores is in a list!!!
        # Do you want something nice? Use QFileDialog


        if ENABLE_IPTAG:
            print "Send iptag..."
            self.mc.iptag_set(DEF_TUBO_IPTAG,self.myPC,DEF_TUBO_PORT,0,0) # prepare iptag for myTub, because boot in rig doesn't provide this
            self.mc.iptag_set(DEF_REPORT_IPTAG, self.myPC, DEF_REPORT_PORT,0,0)

        print "Send the aplxs to the corresponding chips...",
        srcsinkaplx = "/local/new_home/indi/Projects/P/Graceful_TG_SDP_virtualenv/src/aplx/srcsink.aplx"
        tgsdpaplx = "/local/new_home/indi/Projects/P/Graceful_TG_SDP_virtualenv/src/aplx/tgsdp.aplx"
        monaplx = "/local/new_home/indi/Projects/P/Graceful_TG_SDP_virtualenv/src/aplx/monitor.aplx"
        self.mc.load_application(srcsinkaplx, {(self.xSrc, self.ySrc):[DEF_APP_CORE]}, app_id=APPID_SRCSINK)
        self.mc.load_application(tgsdpaplx, appCores, app_id=APPID_TGSDP)
        self.mc.load_application(monaplx, allChips, app_id=APPID_MONITOR)
        time.sleep(5)
        self.mc.send_signal('sync0',app_id=APPID_SRCSINK)
        self.mc.send_signal('sync0',app_id=APPID_TGSDP)
        self.mc.send_signal('sync0',app_id=APPID_MONITOR)
        print "done!"

        # Debugging: why some chips generate WDOG?
        self.sdp.sendPing(self.TGmap)

        # Third, send the configuration to the corresponding node
        print "Sending the configuration data to the corresponding chip...",
        for node in self.dag: # self.dag should be a list of a list of a dict
            #print "Node =",node
            time.sleep(DEF_SDP_TIMEOUT)     # WEIRD!!!! If I remove this, then node-0 will be corrupted!!!
            self.sdp.sendConfig(self.TGmap, node)
        print "done!"

        print "Sending special configuration to SOURCE/SINK node...",
        # TODO: send the source target list!!!
        self.sdp.sendSourceTarget(self.TGmap, self.srcTarget)   # butuh TGmap karena butuh xSrc dan ySrc
        print "done! ---------- WAIT, Abaikan nilai payload-nya!!!! ------------"
        # NOTE: di bagian sdp.sendSourceTarget() tidak aku ubah untuk akomodasi hal tersebut!!!!!!!!!
        #       Jadi, sangat tergantung srcsink.c untuk betulin-nya!!!!

        print "Sending network map...",
        self.sdp.sendChipMap(self.TGmap)
        print "done! SpiNNaker is ready for TGSDP simulation (set tick if necessary)!"
        QtGui.QMessageBox.information(self, "Done",
                                      "SpiNNaker is ready for TGSDP simulation (set tick if necessary)!")

        # TODO: 1. Baca P2P table
        #       2. Petakan dan kirim ke tgsdpvis.py. Nanti tgsdpvis.py akan memberi warna
        apasihini = self.mc.get_system_info()
        p2p_tables = {(x, y): self.mc.get_p2p_routing_table(x, y) for x, y in self.mc.get_system_info()}
        #for c in apasihini.chips():
        #    print c

    @QtCore.pyqtSlot()
    def getSimulationTick(self):
        simTick, ok = QtGui.QInputDialog.getInt(self, "Simulation Tick", "Enter Simulation Tick in microsecond",
                                                self.simTick, DEF_MIN_TIMER_TICK, 1000, 1)
        if ok is True:
            print "Sending tick {} microseconds".format(simTick)
            self.simTick = simTick
            self.sdp.sendSimTick(self.xSrc, self.ySrc, simTick)

    @QtCore.pyqtSlot()
    def startSim(self):
        # First ask, for how long
        msLong, ok = QtGui.QInputDialog.getInt(self, "Running Time", "Enter simulation running time (in ms)",
                                               60000, DEF_MIN_RUNNING_TIME, DEF_MAX_RUNNING_TIME, 1)
        if ok:
            self.runningTime = msLong

        self.actionStop.setEnabled(True)
        self.actionStart.setEnabled(False)
        self.sdp.sendStartCmd(self.xSrc, self.ySrc)
        print "Starting simulation..."
        # untuk ambil data, buat timer:
        if self.runningTime > 0:
            print "Set interval to",self.runningTime,"ms"
            self.timer.setInterval(self.runningTime)
            self.timer.start()


    @QtCore.pyqtSlot()
    def stopSim(self):
        if self.timer.isActive():
            self.timer.stop()
        self.actionStop.setEnabled(False)
        self.actionStart.setEnabled(True)
        # self.sdp.sendStopCmd(self.xSrc, self.ySrc) #-> only to SOURCE/SINK node
        self.sdp.sendStopCmd(self.xSrc, self.ySrc, self.TGmap)  #-> to all nodes
        print "Experimen selesai. Sekarang lihat iobuf core-1 di chip<0,0> (srcsink node)"
        QtGui.QMessageBox.information(self, "Experiment Done!",
                                      "Look the result at iobuf core-1 in chip<0,0> (srcsink node)!")
