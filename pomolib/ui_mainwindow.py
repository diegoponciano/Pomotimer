# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pomolib/mainwindow.ui'
#
# Created: Thu Nov 17 03:11:08 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.8
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(661, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Tomato.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#ShortBreakButton,#LongBreakButton,#PomodoroButton {\n"
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
"\n"
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
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 291, 37))
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 46, 661, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.StartGrid = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.StartGrid.setContentsMargins(0, 0, 0, 0)
        self.StartGrid.setObjectName("StartGrid")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.StartGrid.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.StartGrid.addItem(spacerItem1, 0, 2, 1, 1)
        self.TimerLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.TimerLabel.setStyleSheet("QLabel {\n"
"    color: black;\n"
"    font-size: 120pt;\n"
"    font-family: \"PT Sans\";\n"
"    font-weight: bold;\n"
"    padding:0;\n"
"}")
        self.TimerLabel.setObjectName("TimerLabel")
        self.StartGrid.addWidget(self.TimerLabel, 0, 1, 1, 1)
        self.SummaryFrame = QtGui.QFrame(self.centralwidget)
        self.SummaryFrame.setGeometry(QtCore.QRect(0, 204, 669, 267))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(14)
        self.SummaryFrame.setFont(font)
        self.SummaryFrame.setStyleSheet("#SummaryTabs {\n"
"    background-color:rgb(246, 246, 246);\n"
"    border-top: 3px solid #C2C7CB;\n"
"\n"
"}\n"
"QTabWidget {\n"
"    background-color:#F6F6F6;\n"
"\n"
"}\n"
"QTabWidget::pane { \n"
"    border:0;\n"
"    position: absolute;\n"
"    /*top: -0.5em;*/\n"
"    background-color:#F6F6F6;\n"
"}\n"
"QTabWidget::tab-bar { alignment: center; }\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    background-color:#F6F6F6;\n"
"    min-width: 12ex;\n"
"    padding:0;\n"
"    color: #AAA;\n"
"    font-size: 16px;\n"
"    font-family: \'PT Sans\';\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #111;\n"
"    font-size: 16px;\n"
"    font-family: \'PT Sans\';\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:hover { color:#111; }\n"
"QLabel { font-size: 16px; font-family: \'PT Sans\'; }")
        self.SummaryFrame.setObjectName("SummaryFrame")
        self.SummaryTabs = QtGui.QTabWidget(self.SummaryFrame)
        self.SummaryTabs.setGeometry(QtCore.QRect(0, 4, 671, 297))
        self.SummaryTabs.setAutoFillBackground(False)
        self.SummaryTabs.setStyleSheet("")
        self.SummaryTabs.setObjectName("SummaryTabs")
        self.TodoTab = QtGui.QWidget()
        self.TodoTab.setObjectName("TodoTab")
        self.horizontalLayoutWidget = QtGui.QWidget(self.TodoTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 8, 371, 31))
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
        self.listWidget = QtGui.QListWidget(self.TodoTab)
        self.listWidget.setGeometry(QtCore.QRect(130, 39, 390, 201))
        self.listWidget.setStyleSheet("QListView { background-color: #f6f6f6; }\n"
"QListView::item { background-color: #fff; border:none; }\n"
"QListView::item:selected { border: 1px solid #6a6ea9; }\n"
"QListView::item QWidget { border:none; } \n"
"QListView::item QLabel { border:none; } \n"
"QListView::item QToolButton { background-color: none;border:none; }\n"
"QScrollBar:vertical {\n"
"     border: 2px solid green;\n"
"     background: cyan;\n"
"     width: 10px;\n"
"     margin: 13px 0px 13px 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {\n"
"     background: gray;\n"
"     min-height: 16px;\n"
" }\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 2px solid green;\n"
"    background: #32CC99;\n"
"     height: 11px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 2px solid green;\n"
"     background: #32CC99;\n"
"     height: 11px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.listWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setSpacing(1)
        self.listWidget.setObjectName("listWidget")
        self.SummaryTabs.addTab(self.TodoTab, "")
        self.HistoryTab = QtGui.QWidget()
        self.HistoryTab.setObjectName("HistoryTab")
        self.label = QtGui.QLabel(self.HistoryTab)
        self.label.setGeometry(QtCore.QRect(188, 38, 185, 17))
        self.label.setObjectName("label")
        self.SummaryTabs.addTab(self.HistoryTab, "")
        self.StatsTab = QtGui.QWidget()
        self.StatsTab.setObjectName("StatsTab")
        self.label_2 = QtGui.QLabel(self.StatsTab)
        self.label_2.setGeometry(QtCore.QRect(188, 38, 185, 17))
        self.label_2.setObjectName("label_2")
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pomotimer", None, QtGui.QApplication.UnicodeUTF8))
        self.PomodoroButton.setText(QtGui.QApplication.translate("MainWindow", "pomodoro", None, QtGui.QApplication.UnicodeUTF8))
        self.ShortBreakButton.setText(QtGui.QApplication.translate("MainWindow", "short break", None, QtGui.QApplication.UnicodeUTF8))
        self.LongBreakButton.setText(QtGui.QApplication.translate("MainWindow", "long break", None, QtGui.QApplication.UnicodeUTF8))
        self.TimerLabel.setText(QtGui.QApplication.translate("MainWindow", "00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.AddTaskButton.setText(QtGui.QApplication.translate("MainWindow", "+ add task", None, QtGui.QApplication.UnicodeUTF8))
        self.SummaryTabs.setTabText(self.SummaryTabs.indexOf(self.TodoTab), QtGui.QApplication.translate("MainWindow", "To-Do Today", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Coming soon...", None, QtGui.QApplication.UnicodeUTF8))
        self.SummaryTabs.setTabText(self.SummaryTabs.indexOf(self.HistoryTab), QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Coming soon...", None, QtGui.QApplication.UnicodeUTF8))
        self.SummaryTabs.setTabText(self.SummaryTabs.indexOf(self.StatsTab), QtGui.QApplication.translate("MainWindow", "Stats", None, QtGui.QApplication.UnicodeUTF8))

