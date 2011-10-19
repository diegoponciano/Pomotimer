import os
import sys
import unittest
from PySide.QtGui import QApplication
from PySide.QtTest import QTest
from PySide.QtCore import Qt
from PySide.QtCore import QCoreApplication

path = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(path,os.pardir, 'src')

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import mainwidget

class MainWidgetTest(unittest.TestCase):
    '''Test the pomodoro GUI'''
    def setUp(self):
        '''Create the GUI'''
        if not QCoreApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QCoreApplication.instance()

        self.window = mainwidget.MainWindow()
        self.form = self.window.centralWidget()

    def setFormToZero(self):
        '''Set all ingredients to zero in preparation for setting just one
        to a nonzero value.
        '''
        #self.form.ui.tequilaScrollBar.setValue(0)
        #self.form.ui.tripleSecSpinBox.setValue(0)
        #self.form.ui.limeJuiceLineEdit.setText("0.0")
        #self.form.ui.iceHorizontalSlider.setValue(0)

    def test_defaults(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.form.ui.AddTaskButton.text(), "+ add task")
        #self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8)
        #self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
        #self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
        #self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
        #self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop")

        ## Class is in the default state even without pressing OK
        #self.assertEqual(self.form.getJiggers(), 36.0)
        #self.assertEqual(self.form.getSpeedName(), "&Karate Chop")
        
    def test_add_task_without_description(self):
        itemsBefore = self.form.ui.TasksVertical.count()
        '''ensures AddTaskEdit is empty'''
        QTest.keyClicks(self.form.ui.AddTaskEdit, "")
        addButton = self.form.ui.AddTaskButton
        QTest.mouseClick(addButton, Qt.LeftButton)
        '''assert no items were added'''
        self.assertEqual(self.form.ui.TasksVertical.count(), itemsBefore)

    def test_add_task_with_description(self):
        itemsBefore = self.form.ui.TasksVertical.count()
        '''ensures AddTaskEdit contains text'''
        QTest.keyClicks(self.form.ui.AddTaskEdit, "task one")
        addButton = self.form.ui.AddTaskButton
        QTest.mouseClick(addButton, Qt.LeftButton)
        '''assert there is one more item'''
        self.assertEqual(self.form.ui.TasksVertical.count(), itemsBefore+1)

    def test_add_two_tasks_correct_size(self):
        itemsBefore = self.form.ui.TasksVertical.count()
        currentHeight = self.form.ui.TasksVertical.parentWidget().size().height()
        '''ensures AddTaskEdit contains text'''
        QTest.keyClicks(self.form.ui.AddTaskEdit, "task one")
        addButton = self.form.ui.AddTaskButton
        QTest.mouseClick(addButton, Qt.LeftButton)
        QTest.mouseClick(addButton, Qt.LeftButton)
        '''assert there is two more items, and size grew'''
        self.assertEqual(self.form.ui.TasksVertical.count(), itemsBefore+2)
        newHeight = self.form.ui.TasksVertical.parentWidget().size().height()
        twoLines = 2*21
        twoSpaces = 2*2
        self.assertEqual(currentHeight+twoLines+twoSpaces, newHeight)

if __name__ == "__main__":
    unittest.main()
