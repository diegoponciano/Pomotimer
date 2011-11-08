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
  def __init__(self, window, listWidget):
    QtCore.QObject.__init__(self)
    self.window = window
    self.tasks = listWidget
    self.task_in_progress = False
    self.row = '' 
    self.item = None 
    self.pomotimer = None 
    self.start_event = self.on_start_clicked 

  def newItem(self, labelText):

    item = QtGui.QListWidgetItem()
    item.setSizeHint(QtCore.QSize(378,22))
    self.tasks.addItem(item)
    row = str(self.tasks.indexFromItem(item).row())

    new_frame = QtGui.QFrame()
    new_frame.setFrameShape(QtGui.QFrame.StyledPanel)
    new_frame.setFrameShadow(QtGui.QFrame.Raised)
    new_frame.setObjectName("frame_" + row)

    new_task = QtGui.QWidget(new_frame)
    new_task.setGeometry(QtCore.QRect(0, 0, 378, 22))
    new_task.setAutoFillBackground(False)
    new_task.setObjectName("task_" + row)

    new_taskLabel = QtGui.QLabel(new_task)
    new_taskLabel.setGeometry(QtCore.QRect(40, 3, 291, 17))
    new_taskLabel.setStyleSheet("")
    new_taskLabel.setText(labelText)
    new_taskLabel.setObjectName("taskLabel_" + row)

    #new_taskCompleteButton = QtGui.QToolButton(new_task)
    #new_taskCompleteButton.setGeometry(QtCore.QRect(310, -2, 24, 26))
    new_taskRemoveButton = QtGui.QToolButton(new_task)
    new_taskRemoveButton.setGeometry(QtCore.QRect(340, -2, 24, 26))
    new_taskStartButton = QtGui.QToolButton(new_task)
    new_taskStartButton.setGeometry(QtCore.QRect(5, -2, 24, 26))

    #icon = QtGui.QIcon()
    #icon.addPixmap(QtGui.QPixmap("check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    #new_taskCompleteButton.setIcon(icon)
    #new_taskCompleteButton.setObjectName("taskCompleteButton" + row)

    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    new_taskRemoveButton.setIcon(icon1)
    new_taskRemoveButton.setObjectName("taskRemoveButton_" + row)

    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    new_taskStartButton.setIcon(icon2)
    new_taskStartButton.setObjectName("taskStartButton_" + row)

    hoverOpacity = HoverOpacity(self)
    hoverOpacity.applyOpacity(new_task)
    new_task.installEventFilter(hoverOpacity)

    self.tasks.setItemWidget(item, new_frame)

    new_taskRemoveButton.clicked[bool].connect(lambda a: self.removeItem(a, item))
    new_taskStartButton.clicked[bool].connect(lambda a: self.start_event(a, item))

  def removeItem(self, pressed, item):
    row = self.tasks.indexFromItem(item).row()
    self.tasks.takeItem(row)

  def on_start_clicked(self, pressed, item):
    self.row = self.tasks.indexFromItem(item).row()
    self.item = self.tasks.itemWidget(item)

    self.disableItems()

    startBtn = self.item.findChild(QtGui.QToolButton, "taskStartButton_"+str(self.row))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    startBtn.setIcon(icon)
    self.start_event = self.on_stop_clicked 

    self.pomotimer = PomoTimer(self.window.TimerLabel, 25*60, self.tomatoFinished)
    self.pomotimer.start()
  
  def on_stop_clicked(self, pressed, item):
    reply = QtGui.QMessageBox.question(self.window, 'Smash?', "Do you want to smash this tomato?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
      startBtn = self.item.findChild(QtGui.QToolButton, "taskStartButton_"+str(self.row))
      icon = QtGui.QIcon()
      icon.addPixmap(QtGui.QPixmap("start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
      startBtn.setIcon(icon)
      self.enableItems()
      self.start_event = self.on_start_clicked 
      self.pomotimer.stop()
   
  def enableItems(self):
    for item in self.tasks.findItems('', QtCore.Qt.MatchRegExp):
      itemWidget = self.tasks.itemWidget(item)
      itemWidget.setEnabled(True)
    removeBtn = self.item.findChild(QtGui.QToolButton, "taskRemoveButton_"+str(self.row))
    removeBtn.setEnabled(True)
 
  def disableItems(self):
    for item in self.tasks.findItems('', QtCore.Qt.MatchRegExp):
      itemWidget = self.tasks.itemWidget(item)
      itemWidget.setEnabled(False)
    self.item.setEnabled(True)
    removeBtn = self.item.findChild(QtGui.QToolButton, "taskRemoveButton_"+str(self.row))
    removeBtn.setEnabled(False)

  def tomatoFinished(self):
    pass

normal_style = """
 QLabel {
   color: black;
   font-size: 120pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

warning_style = """
 QLabel {
   color: red;
   font-size: 120pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

negative_style = """
 QLabel {
   color: black;
   background-color: red;
   font-size: 120pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

standby_style = """
 QLabel {
   color: green;
   background-color: black;
   font-size: 80pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

class PomoTimer(object):
  def __init__(self, label, totalTime, callback):
        self.label = label
        self.totalTime = totalTime
        self.callback = callback 
        self.remainingTime = totalTime
        self.current_state = self.standingby
        self.current_state()
        self.timer = QtCore.QTimer(interval=1000) # miliseconds
        self.timer.timeout.connect(self.on_every_second)

    # Event methods:
  def on_every_second(self):
        self.remainingTime -= 1
        self.current_state()

    # Methods:
  def start(self):
        if self.current_state not in [self.standingby, self.stopped]:
            return
        self.remainingTime = self.totalTime
        self.current_state = self.countdown
        self.current_state()
        self.timer.start()

  def stop(self):
        if self.current_state in [self.standingby, self.stopped]:
            return
        self.timer.stop()
        self.current_state = self.stopped
        self.current_state()
        self.callback()

  def standby(self):
        self.timer.stop()
        self.current_state = self.standingby
        self.current_state()


    # States:
  def standingby(self):
        self.label.setStyleSheet(standby_style)
        self.label.setText("TEDxSkopje")

  def stopped(self):
        self.label.setStyleSheet(normal_style)
        self.label.setText("00:00")

  def countdown(self):
        if self.remainingTime < 0:
            self.label.setStyleSheet(negative_style)
            self.label.setText("%02d:%02d" % divmod(abs(self.remainingTime), 60))
        elif self.remainingTime < 60:
            self.label.setStyleSheet(warning_style)
            self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60))
        else:
            self.label.setStyleSheet(normal_style)
            self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60))


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

        self.ui.AddTaskButton.clicked[bool].connect(self.on_addTask_clicked)

        QtCore.QMetaObject.connectSlotsByName(self.ui.centralwidget)
        #self.create_menus()

        self.todoListWidget = TodoListWidget(self.ui, self.ui.listWidget)

    @QtCore.Slot()
    def on_StartButton_clicked(self):
      print 'oi'

    @QtCore.Slot(str)
    def on_statusbar_messageChanged(self, text):
        if text:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(255,170,0))
        else:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(222,222,222))

    def on_addTask_clicked(self):
      if self.ui.AddTaskEdit.text():
        self.todoListWidget.newItem(self.ui.AddTaskEdit.text())
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
