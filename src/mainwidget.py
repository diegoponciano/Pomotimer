#!/usr/bin/python

import sys
import pprint

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

class MousePressTask(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if not "border:2px solid black" in obj.parent().styleSheet():
                #obj.parent().setStyleSheet("QWidget { background-color: #758899;border:2px solid black; } QLabel { border:none; } QToolButton { background-color: none;border:none; }")
                obj.parent().setStyleSheet("QWidget { background-color: #fff;border:2px solid black; } QLabel { border:none; } QToolButton { background-color: none;border:none; }")
            else:
                obj.parent().setStyleSheet("QWidget { background-color: #fff;border:none; } QLabel { border:none; } QToolButton { background-color: none;border:none; }")
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

        self.ui.TasksVertical.parent().setGeometry(QtCore.QRect(0, 0, 370, 0))
        self.ui.TaskListWidget.setMinimumSize(300, 0)
        QtCore.QMetaObject.connectSlotsByName(self)

class TodoListWidget(QtCore.QObject):
  def __init__(self):
    QtCore.QObject.__init__(self)

  def doAddTask(self, pressed, listWidget, labelText):

    item = QtGui.QListWidgetItem()
    item.setSizeHint(QtCore.QSize(368,22))
    listWidget.addItem(item)
    row = str(listWidget.indexFromItem(item).row())

    new_frame = QtGui.QFrame()
    new_frame.setStyleSheet("QWidget { background-color: #fff;border:none; } QLabel { border:none; } QToolButton { background-color: none;border:none; }")
    new_frame.setFrameShape(QtGui.QFrame.StyledPanel)
    new_frame.setFrameShadow(QtGui.QFrame.Raised)
    new_frame.setObjectName("frame_" + row)

    new_task = QtGui.QWidget(new_frame)
    new_task.setGeometry(QtCore.QRect(0, 0, 368, 22))
    new_task.setAutoFillBackground(False)
    new_task.setObjectName("task_" + row)

    new_taskLabel = QtGui.QLabel(new_task)
    new_taskLabel.setGeometry(QtCore.QRect(10, 3, 291, 17))
    new_taskLabel.setStyleSheet("")
    new_taskLabel.setText(labelText)
    new_taskLabel.setObjectName("taskLabel" + row)

    new_taskCompleteButton = QtGui.QToolButton(new_task)
    new_taskCompleteButton.setGeometry(QtCore.QRect(310, -2, 24, 26))
    new_taskRemoveButton = QtGui.QToolButton(new_task)
    new_taskRemoveButton.setGeometry(QtCore.QRect(340, -2, 24, 26))

    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    new_taskCompleteButton.setIcon(icon)
    new_taskCompleteButton.setObjectName("taskCompleteButton" + row)

    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    new_taskRemoveButton.setIcon(icon1)
    new_taskRemoveButton.setObjectName("taskRemoveButton" + row)

    hoverOpacity = HoverOpacity(self)
    hoverOpacity.applyOpacity(new_task)
    new_task.installEventFilter(hoverOpacity)
    #mousePress = MousePressTask(self)
    #new_task.installEventFilter(mousePress)

    listWidget.setItemWidget(item, new_frame)

    new_taskRemoveButton.clicked[bool].connect(lambda a: self.doRemove(a, listWidget, item))

  def doRemove(self, pressed, listWidget, item):
    row = listWidget.indexFromItem(item).row()
    listWidget.takeItem(row)

class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent=parent)

        QtGui.QFontDatabase.addApplicationFont("./PTS55F.ttf")

        loader = QtUiTools.QUiLoader()
        uifile = QtCore.QFile("./mainwindow.ui")
        self.ui = loader.load(uifile)
        self.resize(670, 480)
        #self.setCentralWidget(self.ui.centralwidget)
        self.setCentralWidget(self.ui)

        self.ui.AddTaskButton.clicked[bool].connect(self.addTask)

        QtCore.QMetaObject.connectSlotsByName(self.ui)
        #self.create_menus()

    @QtCore.Slot()
    def on_AddTaskButton_clicked(self):
      print 'oi'

    @QtCore.Slot(str)
    def on_statusbar_messageChanged(self, text):
        if text:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(255,170,0))
        else:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(222,222,222))

    def addTask(self):
      if self.ui.AddTaskEdit.text():
        todoListWidget = TodoListWidget()
        todoListWidget.doAddTask(True, self.ui.listWidget, self.ui.AddTaskEdit.text())
      else:
        self.ui.statusbar.showMessage("You must add a description to your task.", 3500)

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
