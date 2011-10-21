# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Oct 21 13:04:54 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(661, 487)
        MainWindow.setStyleSheet("#ShortBreakButton,#LongBreakButton,#PomodoroButton {\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #FBFBFB, stop: 1 #E0E0E0);\n"
"    min-width: 80px;\n"
"}\n"
"#ShortBreakButton:hover,#LongBreakButton:hover,#PomodoroButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #CCC);\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #EDF4F8, stop: 1 #C2D1DE);*/\n"
"}\n"
"#PomodoroButton {\n"
"    border-top-left-radius: 6px;\n"
"    border-bottom-left-radius: 6px;\n"
"}\n"
"#ShortBreakButton {\n"
"    border-left: 0px;\n"
"}\n"
"#LongBreakButton {\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    border-left: 0px;\n"
"}\n"
"#StartButton {\n"
"    border: 1px solid #8f8f91;\n"
"    border-radius:5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #4FE455, stop: 1 #12A719);\n"
"    color:white;\n"
"    min-width: 180px;\n"
"    height:60px;\n"
"    font-size:17px/20px;\n"
"}\n"
"#StartButton:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #3FF047, stop: 1 #15B91D);\n"
"}\n"
"#AddTaskEdit {\n"
"    height:20px;\n"
"    margin:0;\n"
"    padding:0;\n"
"    outline:none;\n"
"}\n"
"#AddTaskEdit:hover {\n"
"        /*box-shadow: 0 0 5px rgba(81, 203, 238, 1);*/\n"
"}\n"
"#AddTaskButton {\n"
"    color:#FFF;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #4FE455, stop: 1 #12A719);\n"
"    /*border-left: 0px;*/\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    min-width: 80px;\n"
"    height:20px;\n"
"}\n"
"QPushButton {\n"
"    height:25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
" }\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}\n"
"#SummaryWidget {\n"
"    background-color:#F6F6F6;\n"
"    border-top:1px solid #CCC;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 291, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ButtonsGrid = QtGui.QGridLayout(self.gridLayoutWidget)
        self.ButtonsGrid.setSpacing(0)
        self.ButtonsGrid.setContentsMargins(0, 0, 0, 0)
        self.ButtonsGrid.setObjectName("ButtonsGrid")
        self.PomodoroButton = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        self.PomodoroButton.setFont(font)
        self.PomodoroButton.setStyleSheet("")
        self.PomodoroButton.setObjectName("PomodoroButton")
        self.ButtonsGrid.addWidget(self.PomodoroButton, 0, 0, 1, 1)
        self.ShortBreakButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.ShortBreakButton.setObjectName("ShortBreakButton")
        self.ButtonsGrid.addWidget(self.ShortBreakButton, 0, 1, 1, 1)
        self.LongBreakButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.LongBreakButton.setObjectName("LongBreakButton")
        self.ButtonsGrid.addWidget(self.LongBreakButton, 0, 2, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 661, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.StartGrid = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.StartGrid.setContentsMargins(0, 0, 0, 0)
        self.StartGrid.setObjectName("StartGrid")
        self.StartButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.StartButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setIconSize(QtCore.QSize(16, 16))
        self.StartButton.setObjectName("StartButton")
        self.StartGrid.addWidget(self.StartButton, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.StartGrid.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.StartGrid.addItem(spacerItem1, 0, 2, 1, 1)
        self.SummaryWidget = QtGui.QWidget(self.centralwidget)
        self.SummaryWidget.setGeometry(QtCore.QRect(0, 170, 661, 301))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(14)
        self.SummaryWidget.setFont(font)
        self.SummaryWidget.setStyleSheet("")
        self.SummaryWidget.setObjectName("SummaryWidget")
        self.SummaryTabs = QtGui.QTabWidget(self.SummaryWidget)
        self.SummaryTabs.setGeometry(QtCore.QRect(0, 10, 661, 291))
        self.SummaryTabs.setAutoFillBackground(False)
        self.SummaryTabs.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"     /*border-top: 2px solid #C2C7CB;*/\n"
"    /*background-color:#F6F6F6;*/\n"
"    border:0;\n"
"     position: absolute;\n"
"     top: -0.5em;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"     alignment: center;\n"
" }\n"
"  QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     /*border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     /*border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;*/\n"
"    background-color:#F6F6F6;\n"
"     min-width: 12ex;\n"
"     /*padding: 2px;*/\n"
"    padding:0;\n"
"    color: #AAA;\n"
"    font-size: 16px;\n"
"    font-family: \'PT Sans\';\n"
"    /*font-weight:bold;*/\n"
" }\n"
"QTabBar::tab:selected {\n"
"    color: #111;\n"
"    font-size: 16px;\n"
"    font-family: \'PT Sans\';\n"
"    font-weight: bold;\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     /*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);*/\n"
" }\n"
"QTabBar::tab:hover {\n"
"    color:#111;\n"
"}\n"
" QTabBar::tab:selected {\n"
"     /*border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }")
        self.SummaryTabs.setObjectName("SummaryTabs")
        self.TodoTab = QtGui.QWidget()
        self.TodoTab.setObjectName("TodoTab")
        self.horizontalLayoutWidget = QtGui.QWidget(self.TodoTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 10, 371, 46))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddTaskEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.AddTaskEdit.setObjectName("AddTaskEdit")
        self.horizontalLayout.addWidget(self.AddTaskEdit)
        self.AddTaskButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.AddTaskButton.setAutoFillBackground(False)
        self.AddTaskButton.setObjectName("AddTaskButton")
        self.horizontalLayout.addWidget(self.AddTaskButton)
        self.verticalLayoutWidget = QtGui.QWidget(self.TodoTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 54, 371, 16))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.TasksVertical = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.TasksVertical.setSpacing(2)
        self.TasksVertical.setContentsMargins(0, 0, 0, 0)
        self.TasksVertical.setObjectName("TasksVertical")
        self.SummaryTabs.addTab(self.TodoTab, "")
        self.HistoryTab = QtGui.QWidget()
        self.HistoryTab.setObjectName("HistoryTab")
        self.SummaryTabs.addTab(self.HistoryTab, "")
        self.StatsTab = QtGui.QWidget()
        self.StatsTab.setObjectName("StatsTab")
        self.SummaryTabs.addTab(self.StatsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.SummaryTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.PomodoroButton.setText(QtGui.QApplication.translate("MainWindow", "pomodoro", None, QtGui.QApplication.UnicodeUTF8))
        self.ShortBreakButton.setText(QtGui.QApplication.translate("MainWindow", "short break", None, QtGui.QApplication.UnicodeUTF8))
        self.LongBreakButton.setText(QtGui.QApplication.translate("MainWindow", "long break", None, QtGui.QApplication.UnicodeUTF8))
        self.StartButton.setText(QtGui.QApplication.translate("MainWindow", "start pomodoro", None, QtGui.QApplication.UnicodeUTF8))
        self.AddTaskButton.setText(QtGui.QApplication.translate("MainWindow", "+ add task", None, QtGui.QApplication.UnicodeUTF8))
        self.SummaryTabs.setTabText(self.SummaryTabs.indexOf(self.TodoTab), QtGui.QApplication.translate("MainWindow", "To-Do Today", None, QtGui.QApplication.UnicodeUTF8))
        self.SummaryTabs.setTabText(self.SummaryTabs.indexOf(self.HistoryTab), QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.SummaryTabs.setTabText(self.SummaryTabs.indexOf(self.StatsTab), QtGui.QApplication.translate("MainWindow", "Stats", None, QtGui.QApplication.UnicodeUTF8))

