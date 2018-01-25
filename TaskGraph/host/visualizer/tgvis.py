from PyQt4 import Qt, QtGui, QtCore
from PyQt4 import QtSvg

# copy from constDef:
DEF_DEAD_CHIP_COLOR = Qt.Qt.red
DEF_ACTIVE_CHIP_COLOR = Qt.Qt.blue
DEF_INACTIVE_CHIP_COLOR = Qt.Qt.white
DEF_OK_CHIP_TEXT = Qt.Qt.black
DEF_DEAD_CHIP_TEXT = Qt.Qt.red

class chipBox(QtGui.QGraphicsRectItem):
    def __init__(self, id, parent=None):
        QtGui.QGraphicsRectItem.__init__(self, parent)
        self.on = True
        self.id = id

    def mousePressEvent(self, event):
        print "chip ID =", self.id, "is clicked!"


class visWidget(QtGui.QGraphicsView):
    def __init__(self, mw, mh, okChipList, knownDeadChipList, okToClose=False, parent=None):
        """
        :param mw: machine width
        :param mh: machine height
        :param chipList: list of tuples of chip X,Y coordinates
        :param knownDeadChips: list of tuples of dead chip X,Y coordinates
        :param parent: QWidget
        """
        self.okChipList = okChipList
        self.deadChipList = knownDeadChipList
        self.nOKChips = len(okChipList)
        self.nDeadChips = len(knownDeadChipList)

        #print self.chipList

        QtGui.QGraphicsView.__init__(self, parent)
        self.scene = QtGui.QGraphicsScene()
        #self.scene.addText("Test")

        self.drawLayout()
        #self.drawLayout(mode=1)    # it will produce messy connection!!!
        #self.scene.addRect(0,0,100,100)

        self.setScene(self.scene)
        #self.view = QtGui.QGraphicsView(self.scene, self)
        #self.view.show()

        self.sceneTimer = QtCore.QTimer(self)
        # self.cbChips.currentIndexChanged.connect(self.chipChanged)
        self.sceneTimer.timeout.connect(self.sceneTimerTimeout)
        #self.sceneTimer.start(1000) # will fire every 1000ms (every 1 sec)
        self.on = False
        self.okToClose = okToClose
        self.saveToSVG()

    def closeEvent(self, e):
        if self.okToClose:
            print "closing..."
            e.accept()

    @QtCore.pyqtSlot()
    def sceneTimerTimeout(self):
        """
        Update the content of the scene
        """
        for i in range(self.nOKChips):
            self.okChips[i].setBrush(DEF_INACTIVE_CHIP_COLOR)
        """
        self.on = not self.on
        if self.on is True:
            for i in range(48):
                self.chips[i].setBrush(Qt.Qt.red)
        else:
            for i in range(48):
                self.chips[i].setBrush(Qt.Qt.white)
        """

    def saveToSVG(self):
        """
        save into a file in svg format
        """
        self.svgGen = QtSvg.QSvgGenerator()
        self.svgGen.setFileName("/local/new_home/indi/coba.svg")
        szF = self.scene.itemsBoundingRect()
        sz = Qt.QSize(int(szF.width()), int(szF.height()))
        self.svgGen.setSize(sz)
        bx = Qt.QRect(0,0,sz.width(),sz.height())
        self.svgGen.setViewBox(bx)
        self.svgGen.setTitle("Coba untuk tgsdp")
        self.svgGen.setDescription("By Indar Sugiarto")
        painter = Qt.QPainter(self.svgGen)
        self.scene.render(painter)

    def drawLayout(self):
        # Draw Spin5 chip layout
        w = 85  # width of the box displaying a chip
        h = 85  # height of the box displaying a chip
        xoffset = 125
        yoffset = -125
        hspace = xoffset-85

        # draw as logical layout
        self.okChipIDTxt = [QtGui.QGraphicsTextItem() for _ in range(self.nOKChips)]
        self.deadChipIDTxt = [QtGui.QGraphicsTextItem() for _ in range(self.nDeadChips)]
        fnt = Qt.QFont()
        fnt.setPointSize(14)
        fnt.setWeight(Qt.QFont.Bold)
        for ctxt in self.okChipIDTxt:
            ctxt.setDefaultTextColor(Qt.QColor(DEF_OK_CHIP_TEXT))
            ctxt.setFont(fnt)
        for ctxt in self.deadChipIDTxt:
            ctxt.setDefaultTextColor(Qt.QColor(DEF_DEAD_CHIP_TEXT))

        self.edges = [[QtGui.QGraphicsLineItem() for _ in range(6)] for _ in range(self.nOKChips + self.nDeadChips)]
        #self.chips = [QtGui.QGraphicsRectItem() for _ in range(self.nChips)]

        # instantiate box for chip visualization
        allOKIdx = list()
        for i in range(self.nOKChips):
            allOKIdx.append(self.getIdxFromXY(self.okChipList[i]))
        self.okChips = [chipBox(id) for id in allOKIdx]
        # for dead chips, the ID won't be reported by getIdxFromXY because
        # getIdxFromXY is based on reported working chips by rig
        additionalID = self.nOKChips
        allDeadIdx = list()
        for i in range(self.nDeadChips):
            allDeadIdx.append(additionalID)
            additionalID += 1
        self.deadChips = [chipBox(id) for id in allDeadIdx]


        pen = QtGui.QPen()
        pen.setWidth(2)
        # for available chips
        for i in range(self.nOKChips):
            edgeIdx = i
            x = self.okChipList[i][0]
            y = self.okChipList[i][1]
            self.okChips[i].setRect(x*xoffset,y*yoffset,w,h)
            self.okChips[i].setPen(pen)
            self.okChips[i].setBrush(DEF_INACTIVE_CHIP_COLOR)
            self.scene.addItem(self.okChips[i])
            #self.scene.addRect(x*xoffset,y*yoffset,w,h,pen)
            self.okChipIDTxt[i].setPos(x*xoffset+25,y*yoffset+25)
            txt = "%d,%d" % (self.okChipList[i][0], self.okChipList[i][1])
            #print txt
            self.okChipIDTxt[i].setPlainText(txt)
            # put edge-0
            x1 = x*xoffset+w
            y1 = y*yoffset+h/2
            x2 = x1+hspace/2
            y2 = y1
            self.edges[edgeIdx][0].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][0])
            # put edge-1
            x1 = x*xoffset+w
            y1 = y*yoffset
            x2 = x1+hspace/2
            y2 = y1-hspace/2
            self.edges[edgeIdx][1].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][1])
            # put edge-2
            x1 = x*xoffset+w/2
            y1 = y*yoffset
            x2 = x1
            y2 = y1-hspace/2
            self.edges[edgeIdx][2].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][2])
            # put edge-3
            x1 = x*xoffset
            y1 = y*yoffset+h/2
            x2 = x1-hspace/2
            y2 = y1
            self.edges[edgeIdx][3].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][3])
            # put edge-4
            x1 = x*xoffset
            y1 = y*yoffset+h
            x2 = x1-hspace/2
            y2 = y1+hspace/2
            self.edges[edgeIdx][4].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][4])
            # put edge-5
            x1 = x*xoffset+w/2
            y1 = y*yoffset+h
            x2 = x1
            y2 = y1+hspace/2
            self.edges[edgeIdx][5].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][5])
            for j in range(6):
                self.edges[edgeIdx][j].setPen(pen)
            self.scene.addItem(self.okChipIDTxt[i])

        # for dead chips
        for i in range(self.nDeadChips):
            edgeIdx = self.nOKChips + i
            x = self.deadChipList[i][0]
            y = self.deadChipList[i][1]
            self.deadChips[i].setRect(x*xoffset,y*yoffset,w,h)
            self.deadChips[i].setPen(pen)
            self.deadChips[i].setBrush(DEF_DEAD_CHIP_COLOR)
            self.scene.addItem(self.deadChips[i])
            #self.scene.addRect(x*xoffset,y*yoffset,w,h,pen)
            self.deadChipIDTxt[i].setPos(x*xoffset+25,y*yoffset+25)
            txt = "%d,%d" % (self.deadChipList[i][0], self.deadChipList[i][1])
            #print txt
            self.deadChipIDTxt[i].setPlainText(txt)
            # put edge-0
            x1 = x*xoffset+w
            y1 = y*yoffset+h/2
            x2 = x1+hspace/2
            y2 = y1
            self.edges[edgeIdx][0].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][0])
            # put edge-1
            x1 = x*xoffset+w
            y1 = y*yoffset
            x2 = x1+hspace/2
            y2 = y1-hspace/2
            self.edges[edgeIdx][1].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][1])
            # put edge-2
            x1 = x*xoffset+w/2
            y1 = y*yoffset
            x2 = x1
            y2 = y1-hspace/2
            self.edges[edgeIdx][2].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][2])
            # put edge-3
            x1 = x*xoffset
            y1 = y*yoffset+h/2
            x2 = x1-hspace/2
            y2 = y1
            self.edges[edgeIdx][3].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][3])
            # put edge-4
            x1 = x*xoffset
            y1 = y*yoffset+h
            x2 = x1-hspace/2
            y2 = y1+hspace/2
            self.edges[edgeIdx][4].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][4])
            # put edge-5
            x1 = x*xoffset+w/2
            y1 = y*yoffset+h
            x2 = x1
            y2 = y1+hspace/2
            self.edges[edgeIdx][5].setLine(x1,y1,x2,y2)
            self.scene.addItem(self.edges[edgeIdx][5])
            for j in range(6):
                self.edges[edgeIdx][j].setPen(pen)
            self.scene.addItem(self.deadChipIDTxt[i])

    #self.scene.addLine(0,0,70,70)

    @QtCore.pyqtSlot(list)
    def updateHist(self, xy, clr=DEF_ACTIVE_CHIP_COLOR):
        """
        This Slot should be connected to sdp.histUpdate
        """
        cId = self.getIdxFromXY(xy)
        #print "xy={}, cId={}".format(xy, cId)
        #cId might be None if the chip xy is dead
        if cId is not None:
            self.chips[cId].setBrush(clr)

    def updateLink(self):
        """
        Got new information regarding paths taken for sending sdp within spinnaker machine?
        :return:
        """

    def getIdxFromXY(self, xy):   # xy is a chip coordinate as a tuple
        for i in range(self.nOKChips):
            if self.okChipList[i]==xy:
                return i


