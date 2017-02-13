from PIL import Image, ImageQt
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPen, QPainter
import sys
from dpx import upload
from util import getday

points = dict(
    R05L_N1 = (290, 290),
    R05L_N2 = (370, 290),
    R05L_N4 = (1030, 290),
    R05L_N5 = (990, 290),
    R05L_N6 = (1360, 290),
    R05L_N7 = (1210, 290),
    R05L_N8 = (1450, 290),
    R05L_N9 = (1650, 290),
    R05L_L1 = (1465, 290),
    R05L_N10 = (1990, 290),
    R05L_N11 = (2080, 290),
    R05L_L2 = (2080, 290),

    N1_R05L=(290, 290),
    N2_R05L=(370, 290),
    N4_R05L=(1030, 290),
    N5_R05L=(990, 290),
    N6_R05L=(1360, 290),
    N7_R05L=(1210, 290),
    N8_R05L=(1450, 290),
    N9_R05L=(1650, 290),
    L1_R05L=(1465, 290),
    N10_R05L=(1990, 290),
    N11_R05L=(2080, 290),
    L2_R05L=(2080, 290),

    NC_N1 = (290, 390),
    NC_N2 = (370, 390),
    NC_WC = (844, 390),
    NC_N4 = (844, 390),
    NC_NN = (1040, 390),
    NC_N6 = (1175, 390),
    NC_N7 = (1400, 390),
    NC_EC = (1630, 390),
    NC_N8 = (1630, 390),
    NC_N9 = (1820, 390),
    NC_N10 = (1990, 390),
    NC_N11 = (2080, 390),

    N1_NC = (290, 390),
    N2_NC = (370, 390),
    WC_NC = (844, 390),
    N4_NC = (844, 390),
    NN_NC = (1040, 390),
    N6_NC = (1175, 390),
    N7_NC = (1400, 390),
    EC_NC = (1630, 390),
    N8_NC = (1630, 390),
    N9_NC = (1820, 390),
    N10_NC = (1990, 390),
    N11_NC = (2080, 390),

    NP_N1 = (290, 445),
    NP_N2 = (370, 445),
    NP_WC = (844, 445),
    NP_N4 = (844, 445),
    NP_NN = (1040, 445),
    NP_N6 = (1175, 445),
    NP_N7 = (1400, 445),
    NP_EC = (1630, 445),

    N1_NP = (290, 445),
    N2_NP = (370, 445),
    WC_NP = (844, 445),
    N4_NP = (844, 445),
    NN_NP = (1040, 445),
    N6_NP = (1175, 445),
    N7_NP = (1400, 445),
    EC_NP = (1630, 445),

    L_L1 = (1920, 120),
    L_L2 = (2070, 120),

    L1_L = (1920, 120),
    L2_L = (2070, 120),

    R05R_S1 = (140, 1030),
    R05R_S2 = (200, 1030),
    R05R_S3 = (250, 1030),
    R05R_S4 = (680, 1030),
    R05R_S5 = (1025, 1030),
    R05R_S6 = (980, 1030),
    R05R_S7 = (1300, 1030),
    R05R_S8 = (1630, 1030),
    R05R_S9 = (1820, 1030),
    R05R_S10 = (1990, 1030),

    S1_R05R = (140, 1030),
    S2_R05R = (200, 1030),
    S3_R05R = (250, 1030),
    S4_R05R = (680, 1030),
    S5_R05R = (1025, 1030),
    S6_R05R = (980, 1030),
    S7_R05R = (1300, 1030),
    S8_R05R = (1630, 1030),
    S9_R05R = (1820, 1030),
    S10_R05R = (1990, 1030),

    S_S1 = (140, 925),
    S_R1 = (140, 925),
    S_S2 = (200, 925),
    S_R2 = (200, 925),
    S_S3 = (250, 925),
    S_R3 = (250, 925),
    S_S4 = (500, 925),
    S_R4 = (500, 925),
    S_S5 = (840, 925),
    S_Q1 = (840, 925),
    S_S6 = (1180, 925),
    S_Q2 = (1180, 925),
    S_S7 = (1500, 925),
    S_Q3 = (1490, 925),
    S_S8 = (1630, 925),
    S_Q4 = (1630, 925),
    S_S9 = (1820, 925),
    S_S10 = (1990, 925),

    S1_S = (140, 925),
    R1_S = (140, 925),
    S2_S = (200, 925),
    R2_S = (200, 925),
    S3_S = (250, 925),
    R3_S = (250, 925),
    S4_S = (500, 925),
    R4_S = (500, 925),
    S5_S = (840, 925),
    Q1_S = (840, 925),
    S6_S = (1180, 925),
    Q2_S = (1180, 925),
    S7_S = (1500, 925),
    Q3_S = (1490, 925),
    S8_S = (1630, 925),
    Q4_S = (1630, 925),
    S9_S = (1820, 925),
    S10_S = (1990, 925),

    R_R1 = (200, 875),
    R_R2 = (200, 875),
    R_R3 = (250, 875),
    R_R4 = (500, 875),
    R_Q1 = (840, 875),

    R1_R = (200, 875),
    R2_R = (200, 875),
    R3_R = (250, 875),
    R4_R = (500, 875),
    Q1_R = (840, 875),

    Q_Q1 = (845, 820),
    Q_WC = (845, 820),
    Q_Q2 = (1180, 820),
    Q_Q3 = (1490, 820),
    Q_Q4 = (1630, 820),
    Q_EC = (1630, 820),

    Q1_Q = (845, 820),
    WC_Q = (845, 820),
    Q2_Q = (1180, 820),
    Q3_Q = (1490, 820),
    Q4_Q = (1630, 820),
    EC_Q = (1630, 820),

    bA1 = (1570, 445),
    bA2 = (1540, 445),
    bA3 = (1500, 445),
    bA4 = (1480, 445),
    bA5 = (1435, 445),
    bA6 = (1390, 445),
    bA7 = (1345, 445),
    bA8 = (1300, 445),
    bA9 = (1260, 445),

    bD1 = (1230, 445),
    bD2 = (1190, 445),
    bD3 = (1160, 445),
    bD4 = (1120, 445),
    bD5 = (1080, 445),
    bD6 = (1040, 445),
    bD7 = (1000, 445),
    bD8 = (960, 445),
    bD9 = (920, 445),
    bD10 = (890, 445),

    bB1 = (1570, 820),
    bB2 = (1540, 820),
    bB3 = (1500, 820),
    bB4 = (1480, 820),
    bB5 = (1435, 820),
    bB6 = (1390, 820),
    bB7 = (1350, 820),
    bB8 = (1310, 820),
    bB9 = (1270, 820),

    bC1 = (1230, 820),
    bC2 = (1190, 820),
    bC3 = (1160, 820),
    bC4 = (1120, 820),
    bC5 = (1080, 820),
    bC6 = (1040, 820),
    bC7 = (1003, 820),
    bC8 = (967, 820),
    bC9 = (930, 820),
    bC10 = (890, 820),

    b501 = (2210, 390),
    b502 = (2170, 390),
    b503 = (2130, 390),
    b504 = (2090, 390),
    b505 = (2050, 390),
    b506 = (2020, 390),
    b507 = (1980, 390),
    b508 = (1950, 390),
    b509 = (1910, 390),
    b510 = (1880, 390),
    b511 = (1840, 390),
    b512 = (1810, 390),
    b513 = (1760, 390),
    b514 = (1710, 390),
    b515 = (1670, 390),

    b516 = (1820, 120),
    b517 = (1860, 120),
    b518 = (1900, 120),
    b519 = (1950, 120),
    b520 = (2000, 120),
    b521 = (2050, 120),
    b522 = (2100, 120),
    b523 = (2150, 120),
    b524 = (2200, 120),
    b525 = (2245, 120),

    b601 = (1580, 925),
    b602 = (1540, 925),
    b603 = (1430, 925),
    b604 = (1395, 925),
    b605 = (1350, 925),
    b606 = (1310, 925),
    b607 = (1270, 925),
    b608 = (1230, 925),
    b609 = (1140, 925),
    b610 = (1110, 925),
    b611 = (1070, 925),
    b612 = (1030, 925),
    b613 = (985, 925),
    b614 = (950, 925),
    b615 = (910, 925),

    b801 = (795, 875),
    b802 = (760, 875),
    b803 = (725, 875),
    b804 = (690, 875),
    b805 = (655, 875),
    b806 = (620, 875),
    b807 = (580, 875),
    b808 = (540, 875),
)

intersection = dict(
    NC_N1 = ["R05L_N1", "NC_N2", "NP_N1"],
    NC_N2 = ["R05L_N2", "NC_WC", "NP_N2", "NC_N1"],
    NC_WC = ["R05L_N4", "NC_NN", "NP_WC", "NC_N2"],
    NC_NN = ["NC_N6", "NP_NN", "NC_WC"],
    NC_N6 = ["R05L_N6", "NC_N7", "NP_N6", "NC_NN"],
    NC_N7 = ["NC_EC", "NP_N7", "NC_N6", "R05L_N7"],
    NC_EC = ["NC_N9", "NP_EC", "NC_N7", "R05L_N8"],
    NC_N8 = ["NC_N9", "NP_EC", "NC_N7", "R05L_N8"],
    NC_N9 = ["NC_N10", "NC_EC", "R05L_N9"],
    NC_N10 = ["R05L_N10", "NC_N11", "NC_N9"],
    NC_N11 = ["R05L_N11", "b501", "NC_N10"],

    NP_N1 = ["NC_N1", "NP_N2"],
    NP_N2 = ["NC_N2", "NP_WC", "NP_N1"],
    NP_WC = ["NC_WC", "NP_NN", "Q_WC", "NP_N2"],
    NP_NN = ["NC_NN", "NP_N6", "NP_WC"],
    NP_N6 = ["NC_N6", "NP_N7", "NP_NN"],
    NP_N7 = ["NC_N7", "NP_EC", "NP_N6"],
    NP_EC = ["NC_EC", "Q_EC", "NP_N7"],

    Q_WC = ["NP_WC", "Q_Q2", "R_Q1"],
    Q_EC = ["NP_EC", "S_Q4", "Q_Q3"],

    R_R2 = ["R_R3", "S_R2", "S_R1"],
    R_R3 = ["R_R4", "S_R3", "R_R2"],
    R_R4 = ["R_Q1", "S_R4", "R_R3"],
    R_Q1 = ["Q_Q1", "S_Q1", "R_R4"],

    S_S1 = ["R_R1", "S_R2", "R05R_S1"],
    S_S2 = ["R_R2", "S_R3", "R05R_S2", "S_S1"],
    S_S3 = ["R_R3", "S_R4", "R05R_S3", "S_S2"],
    S_S4 = ["R_R4", "S_Q1", "R05R_S4", "S_S3"],
    S_S5 = ["R_Q1", "S_Q2", "R05R_S5", "S_S4"],
    S_S6 = ["Q_Q2", "S_S7", "R05R_S6", "S_S5"],
    S_S7 = ["Q_Q3", "S_S8", "R05R_S7", "S_S6"],
    S_S8 = ["Q_Q4", "S_S9", "R05R_S8", "S_S7"],
    S_S9 = ["S_S10", "R05R_S9", "S_S8"],
    S_S10 = ["R05R_S10", "S_S9"],

    S_Q1 = ["R_Q1", "S_Q2", "R05R_S5", "S_S4"],
    S_Q2 = ["Q_Q2", "S_S7", "R05R_S6", "S_S5"],
    S_Q3 = ["Q_Q3", "S_S8", "R05R_S7", "S_S6"],

    R05L_N1 = ["R05L_N11"],
    R05R_S1 = ["R05R_S10"],
)

entire = dict(
    N1 = ['R05R_N1', 'NP_N1'],
    N2 = ['R05R_N2', 'NP_N2'],
    N3 = ['R05R_N3', 'NP_N3'],
    N4 = ['R05R_N4', 'NP_N4'],
    N5 = ['R05R_N5', 'NP_N5'],
    N6 = ['R05R_N6', 'NP_N6'],
    N7 = ['R05R_N7', 'NP_N7'],
    N8 = ['R05R_N8', 'NP_N8'],
    N9 = ['R05R_N9', 'NP_N9'],
    N10 = ['R05R_N10', 'NP_N10'],
    N11 = ['R05R_N11', 'NP_N11'],

    S1 = ['R05R_S1', 'S_S1'],
    S2 = ['R05R_S2', 'S_S2'],
    S3 = ['R05R_S3', 'S_S3'],
    S4 = ['R05R_S4', 'S_S4'],
    S5 = ['R05R_S5', 'S_S5'],
    S6 = ['R05R_S6', 'S_S6'],
    S7 = ['R05R_S7', 'S_S7'],
    S8 = ['R05R_S8', 'S_S8'],
    S9 = ['R05R_S9', 'S_S9'],
    S10 = ['R05R_S10', 'S_S10'],

    R1 = ['R_R1', 'S_S1'],
    R2 = ['R_R2', 'S_S2'],
    R3 = ['R_R3', 'S_S3'],
    R4 = ['R_R4', 'S_S4'],

)

app = QtGui.QApplication(sys.argv, False)
im = Image.open("RCTP.png")
qt_im = ImageQt.ImageQt(im)

def portionCLSD(start=None, end=None, baystart=None, bayend=None, linestyle="solid", note=""):
    if baystart != None:
        print "% " + baystart,
        x, y = points["b"+baystart]
        blk = (x - 20, y, x + 20, y)
        print blk
        drawLine(blk, fill="red", width=8, style=linestyle)
        drawLabel(points["b"+baystart], points["b"+baystart], note)

        if bayend != None:
            print "% " + bayend,
            x, y = points["b" + bayend]
            blk = (x - 20, y, x + 20, y)
            print blk
            drawLine(blk, fill="red", width=8, style=linestyle)

            print "$ " + baystart + " " + bayend,
            print points["b" + baystart],
            print points["b" + bayend]
            drawLine(points["b" + baystart] + points["b" + bayend], fill="red", width=8, style=linestyle)
            drawLabel(points["b" + baystart], points["b" + bayend], note)

        return

    print "# " + start, end,
    print points[start],
    print points[end]
    drawLine(points[start] + points[end], fill="red", width=8, style=linestyle)
    drawLabel(points[start], points[end], note)

def intersectionCLSD(cross, linestyle="solid"):
    lines = intersection[cross]
    for end in lines:
        print "* " + cross + " " +end,
        print points[cross],
        print points[end]
        drawLine(points[cross] + points[end], fill="red", width=8, style=linestyle)

def rwyCLSD(RWY, linestyle, note=""):
    if RWY == "05L":
        start = "R05L_N1"
        end = "R05L_N11"
    elif RWY == "05R":
        start = "R05R_S1"
        end = "R05R_S10"
    else:
        return False

    drawLine(points[start] + points[end], fill="red", width=10, style=linestyle)
    drawLabel(points[start], points[end], note)

def twyCLSD(TWY, linestyle, note=""):
    (start, end) = entire[TWY]

    drawLine(points[start] + points[end], fill="red", width=8, style=linestyle)

    return

def setDay(day, xy=(100, 100)):
    drawDay(xy, day)

def savePNG(day):
    setDay(day)
    fname = "TPEclsd_" + day + ".png"
    qt_im.save(fname, "png")
    upload()

def drawLine(xy, fill="black", width=1, style="solid"):
    if style == "dash":
        penstyle = QtCore.Qt.DashLine
        print "draw - - "
    else:
        penstyle = QtCore.Qt.SolidLine

    if fill == "red":
        pencolor = QtCore.Qt.red
    else:
        pencolor = QtCore.Qt.black

    painter = QPainter()
    painter.begin(qt_im)
    painter.setPen(QPen(pencolor, width, penstyle))
    x0, y0, x1, y1 = xy
    painter.drawLine(x0, y0, x1, y1)
    painter.end()

def drawDay(xy, txt):
    painter = QPainter()

    painter.begin(qt_im)
    painter.setFont(QtGui.QFont('Helvetica', 50))
    painter.setPen(QPen(QtCore.Qt.gray))
    x0, y0 = xy
    painter.drawText(x0, y0, txt)
    painter.end()

def drawLabel(start, end, txt):
    painter = QPainter()

    painter.begin(qt_im)
    painter.setFont(QtGui.QFont('Helvetica', 30))
    painter.setPen(QPen(QtCore.Qt.blue))
    x0, y0 = start
    x1, y1 = end
    painter.drawText((x0 + x1)/2, y0 - 20, txt)
    painter.end()

if __name__ == "__main__":
    # INTclsd("NC_N1")
    intersectionCLSD("R05R_S1")
    savePNG(getday)
