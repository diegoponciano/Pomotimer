#!/usr/bin/python

import sys

from PySide import QtGui

import mainwidget

def main():

    app = QtGui.QApplication(sys.argv)

    window = mainwidget.MainWindow()
    window.show()
    window.center()

    icon = QtGui.QIcon('Tomato.png')
    window.setWindowIcon(icon)
    window.setWindowIconText('Pomotimer')
    window.setWindowTitle('Pomotimer')

    return app.exec_()

if __name__ == "__main__":
    main()
