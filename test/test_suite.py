#!/usr/bin/python

import os
import sys
import unittest
import pprint

path = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(path,os.pardir, 'src')
os.chdir(src_dir)

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import mainwidget_test
import pomodorolist_test

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(mainwidget_test.MainWidgetTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(pomodorolist_test.PomodoroListTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
