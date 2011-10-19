#!/usr/bin/python

import sys

from PySide import QtCore
from PySide import QtUiTools
from PySide import QtGui
from PySide import QtDeclarative
from pprint import pprint
import os
import mainwidget

# Comment the line below if you don't want to use OpenGL for QML rendering or if it is not supported
from PySide import QtOpenGL

def main():

    app = QtGui.QApplication(sys.argv)

    window = mainwidget.MainWindow()
    window.show()
    window.center()

    #widgetWindow = mainwidget.MainWidget()
    #widgetWindow.show()
    #widgetWindow.resize(QtCore.QSize(QtCore.QRect(0,0,661,487).size()))

    return app.exec_()

if __name__ == "__main__":
    main()
