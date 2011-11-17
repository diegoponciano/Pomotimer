#!/usr/bin/python

import sys

from PySide import QtCore
from PySide import QtUiTools
from PySide import QtGui
from timer import PomodoroTimer
import os
import todolist
import config
import ui_mainwindow

def changeActiveColor(obj, color):
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(color)
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
    obj.setAutoFillBackground(True)
    obj.setPalette(palette)

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
    self.todolist = todolist.TodoList()
    self.loadItems()

  def dispose(self):
    self.todolist.close()
  
  def loadItems(self):
    for item in list(self.todolist.tasks.values()):
      self.appendItem(item.description, item.id)

  def newTask(self, description):
    new_task = self.todolist.addItem(description)
    self.appendItem(description, new_task.id)

  def appendItem(self, labelText, task_id):
    item = QtGui.QListWidgetItem()
    item.id = task_id
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

    new_taskRemoveButton = QtGui.QToolButton(new_task)
    new_taskRemoveButton.setGeometry(QtCore.QRect(340, -2, 24, 26))
    new_taskStartButton = QtGui.QToolButton(new_task)
    new_taskStartButton.setGeometry(QtCore.QRect(5, -2, 24, 26))

    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(os.path.join(config.assets_dir, 'delete.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    new_taskRemoveButton.setIcon(icon1)
    new_taskRemoveButton.setObjectName("taskRemoveButton_" + row)

    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(os.path.join(config.assets_dir, 'start.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    new_taskStartButton.setIcon(icon2)
    new_taskStartButton.setObjectName("taskStartButton_" + row)

    hoverOpacity = HoverOpacity(self)
    hoverOpacity.applyOpacity(new_task)
    new_task.installEventFilter(hoverOpacity)

    self.tasks.setItemWidget(item, new_frame)

    new_taskRemoveButton.clicked[bool].connect(lambda a: self.removeItem(a, item))
    new_taskStartButton.clicked[bool].connect(lambda a: self.start_event(a, item))

    return item

  def removeItem(self, pressed, item):
    row = self.tasks.indexFromItem(item).row()
    self.tasks.takeItem(row)
    self.todolist.removeItem(item.id)

  def on_start_clicked(self, pressed, item):
    self.row = self.tasks.indexFromItem(item).row()
    self.item = self.tasks.itemWidget(item)

    self.disableItems()

    startBtn = self.item.findChild(QtGui.QToolButton, "taskStartButton_"+str(self.row))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(os.path.join(config.assets_dir, 'stop.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    startBtn.setIcon(icon)
    self.start_event = self.on_stop_clicked 

    self.pomotimer = PomodoroTimer(self.window.ui.TimerLabel, 25*60, self.tomatoFinished)
    self.pomotimer.start()
  
  def on_stop_clicked(self, pressed, item):
    reply = QtGui.QMessageBox.question(self.window, 'Smash?', "Do you want to smash this tomato?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    if reply == QtGui.QMessageBox.Yes:
      startBtn = self.item.findChild(QtGui.QToolButton, "taskStartButton_"+str(self.row))
      icon = QtGui.QIcon()
      icon.addPixmap(QtGui.QPixmap(os.path.join(config.assets_dir, 'start.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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


class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent=parent)

        QtGui.QFontDatabase.addApplicationFont(os.path.join(config.assets_dir, 'PTS55F.ttf'))

        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(670, 480)
        self.setCentralWidget(self.ui.centralwidget)

        self.ui.AddTaskButton.clicked[bool].connect(self.on_addTask_clicked)
        self.ui.statusbar.messageChanged.connect(self.on_statusbar_messageChanged)

        QtCore.QMetaObject.connectSlotsByName(self.ui.centralwidget)
        #self.create_menus()

        self.todoListWidget = TodoListWidget(self, self.ui.listWidget)
        #changeActiveColor(self.ui.SummaryTabs, QtGui.QColor(246,246,246))

    def dispose(self):
      self.todoListWidget.dispose()

    def on_statusbar_messageChanged(self, text):
        if text:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(255,170,0))
        else:
            changeActiveColor(self.ui.statusbar, QtGui.QColor(222,222,222))

    def on_addTask_clicked(self):
      if self.ui.AddTaskEdit.text():
        self.todoListWidget.newTask(self.ui.AddTaskEdit.text())
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
