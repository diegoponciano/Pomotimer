#!/usr/bin/python

import os
import sys
import unittest

path = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(path, os.pardir)
os.chdir(src_dir)

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import mainwidget_test
import todolist_test

from pomolib import config
config.tomatoes_dir = os.path.join(path, "data")
config.tomatoes_data = os.path.join(config.tomatoes_dir, "data.fs")

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(mainwidget_test.MainWidgetTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(todolist_test.TodoListTest))
    unittest.TextTestRunner(verbosity=1).run(suite)
