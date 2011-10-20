#!/usr/bin/python

import sys

from PySide import QtCore
from PySide import QtUiTools
from PySide import QtGui
from PySide import QtDeclarative
from pprint import pprint
import os

# Comment the line below if you don't want to use OpenGL for QML rendering or if it is not supported
from PySide import QtOpenGL

def changeActiveColor(obj, color):
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(color)
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
    obj.setPalette(palette)
    obj.setAutoFillBackground(True)

class HoverOpacity(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Enter:
            self.restoreOpacity(obj)
            return True
        elif event.type() == QtCore.QEvent.Leave:
            self.applyOpacity(obj)
            return True
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            print "Yay pressed"
            return True
        else:
            # standard event processing
            return QtCore.QObject.eventFilter(self, obj, event)

    def applyOpacity(self, obj):
        for element in obj.findChildren(QtGui.QToolButton, QtCore.QRegExp('')):
          effect = QtGui.QGraphicsOpacityEffect(obj)
          effect.setOpacity(0.3)
          element.setGraphicsEffect(effect)

    def restoreOpacity(self, obj):
        for element in obj.findChildren(QtGui.QToolButton, QtCore.QRegExp('')):
          effect = QtGui.QGraphicsOpacityEffect(obj)
          effect.setOpacity(0.8)
          element.setGraphicsEffect(effect)

class KeyPressEater(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            print "Ate key press", event.key()
            return True
        else:
            # standard event processing
            return QtCore.QObject.eventFilter(self, obj, event)

class MainWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)

        QtGui.QFontDatabase.addApplicationFont("./PTS55F.ttf")

        loader = QtUiTools.QUiLoader()
        uifile_loc = "./mainwindow.ui"
        uifile = QtCore.QFile(uifile_loc)
        ui = loader.load(uifile)
        ui.centralwidget
        
        self._layout = QtGui.QVBoxLayout()
        self._layout.addWidget(ui)
        self.setLayout(self._layout)

        self.ui = self.children()[1]

        hoverOpacity = HoverOpacity(self)
        self.ui.task1.installEventFilter(hoverOpacity)

        self.ui.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 55, 371, 0))
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.Slot()
    def on_StartButton_clicked(self):
        #self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))
        print "start"

    @QtCore.Slot()
    def on_AddTaskButton_clicked(self):
      if self.ui.AddTaskEdit.text():
        #self.ui.TaskLabel.setText(str(self.ui.AddTaskEdit.text()))



        containerHeight = self.ui.TasksVertical.parentWidget().size().height()
        self.ui.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 55, 371, containerHeight+23))

        self.ui.new_task = QtGui.QWidget(self.ui.verticalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        self.ui.new_task.setPalette(palette)
        self.ui.new_task.setAutoFillBackground(True)
        self.ui.new_task.setStyleSheet("QToolButton{background-color:none;border:none;}")

        self.ui.new_task.setObjectName("task1_5")
        self.ui.new_task.setGeometry(QtCore.QRect(1, 62, 369, 29))

        self.ui.new_taskLabel = QtGui.QLabel(self.ui.new_task)
        self.ui.new_taskLabel.setGeometry(QtCore.QRect(10, 3, 291, 17))
        self.ui.new_taskLabel.setStyleSheet("")
        self.ui.new_taskLabel.setObjectName("new_taskLabel")
        self.ui.new_taskCompleteButton = QtGui.QToolButton(self.ui.new_task)
        self.ui.new_taskCompleteButton.setGeometry(QtCore.QRect(310, -2, 24, 26))
        self.ui.new_taskCompleteButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.new_taskCompleteButton.setIcon(icon)
        self.ui.new_taskCompleteButton.setObjectName("new_taskCompleteButton")
        self.ui.new_taskRemoveButton = QtGui.QToolButton(self.ui.new_task)
        self.ui.new_taskRemoveButton.setGeometry(QtCore.QRect(340, -1, 24, 22))
        self.ui.new_taskRemoveButton.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.new_taskRemoveButton.setIcon(icon1)
        self.ui.new_taskRemoveButton.setObjectName("new_taskRemoveButton")

        self.ui.TasksVertical.addWidget(self.ui.new_task)

      else:
        self.ui.statusbar.showMessage("You must add a description to your task.", 3500)

    @QtCore.Slot(str)
    def on_statusbar_messageChanged(self, text):
        if text:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(255,170,0))
        else:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(222,222,222))

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent=parent)
        self.resize(670, 480)
        self.setCentralWidget(MainWidget())

        #self.centralWidget().button.clicked.connect(self.close)
        #print self.centralWidget().AddTaskButton
        #print self.centralWidget().button

        #print self.centralWidget().centralwidget
        #self.create_menus()

    def create_menus(self):

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction("&New")
        self.fileMenu.addAction("&Save")
        self.fileMenu.addSeparator()
        quitAction = self.fileMenu.addAction("&Quit")

        quitAction.triggered.connect(self.close)

    def center(self):
        '''Centers the window in the screen'''

        r = self.frameGeometry()
        r.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
        self.move(r.topLeft())
