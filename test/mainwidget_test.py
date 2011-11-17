#!/usr/bin/python

import os
import sys
import unittest
from PySide.QtGui import QApplication
from PySide.QtTest import QTest
from PySide.QtCore import Qt
from PySide.QtCore import QCoreApplication

from pomolib import mainwidget

class MainWidgetTest(unittest.TestCase):
    '''Test the pomodoro GUI'''
    @classmethod
    def setUpClass(cls):
        if not QCoreApplication.instance():
            cls.app = QApplication(sys.argv)
        else:
            cls.app = QCoreApplication.instance()

        cls.window = mainwidget.MainWindow()
        cls.form = cls.window.ui

    @classmethod
    def tearDownClass(cls):
        cls.window.dispose()

    #def setFormToZero(self):
        #'''Set all ingredients to zero in preparation for setting just one
        #to a nonzero value.
        #'''
        #self.form.tequilaScrollBar.setValue(0)
        #self.form.tripleSecSpinBox.setValue(0)
        #self.form.limeJuiceLineEdit.setText("0.0")
        #self.form.iceHorizontalSlider.setValue(0)

    def test_defaults(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.form.AddTaskButton.text(), "+ add task")
        #self.assertEqual(self.form.tequilaScrollBar.value(), 8)
        #self.assertEqual(self.form.tripleSecSpinBox.value(), 4)
        #self.assertEqual(self.form.limeJuiceLineEdit.text(), "12.0")
        #self.assertEqual(self.form.iceHorizontalSlider.value(), 12)
        #self.assertEqual(self.form.speedButtonGroup.checkedButton().text(), "&Karate Chop")

        ## Class is in the default state even without pressing OK
        #self.assertEqual(self.form.getJiggers(), 36.0)
        #self.assertEqual(self.form.getSpeedName(), "&Karate Chop")
        
    def test_add_task_without_description(self):
        itemsBefore = self.form.listWidget.count()
        '''ensures AddTaskEdit is empty'''
        QTest.keyClicks(self.form.AddTaskEdit, "")
        addButton = self.form.AddTaskButton
        QTest.mouseClick(addButton, Qt.LeftButton)
        '''assert no items were added'''
        self.assertEqual(self.form.listWidget.count(), itemsBefore)

    def test_add_task_with_description(self):
        itemsBefore = self.form.listWidget.count()
        '''ensures AddTaskEdit contains text'''
        QTest.keyClicks(self.form.AddTaskEdit, "task one")
        addButton = self.form.AddTaskButton
        QTest.mouseClick(addButton, Qt.LeftButton)
        '''assert there is one more item'''
        self.assertEqual(self.form.listWidget.count(), itemsBefore+1)

    def test_add_two_tasks_correct_size(self):
        itemsBefore = self.form.listWidget.count()
        currentHeight = self.form.listWidget.parentWidget().size().height()
        '''ensures AddTaskEdit contains text'''
        QTest.keyClicks(self.form.AddTaskEdit, "task one")
        addButton = self.form.AddTaskButton
        QTest.mouseClick(addButton, Qt.LeftButton)
        QTest.mouseClick(addButton, Qt.LeftButton)
        '''assert there is two more items, and size grew'''
        self.assertEqual(self.form.listWidget.count(), itemsBefore+2)
        newHeight = self.form.listWidget.parentWidget().size().height()
        twoLines = 2*21
        twoSpaces = 2*2
        self.assertEqual(currentHeight+twoLines+twoSpaces, newHeight)

if __name__ == "__main__":
    unittest.main()
