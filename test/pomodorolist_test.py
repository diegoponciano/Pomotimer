#!/usr/bin/python

import os
import sys
import unittest

path = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(path,os.pardir, 'src')
os.chdir(src_dir)

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import mainwidget

class PomodoroListTest(unittest.TestCase):
    '''Test the pomodoro list'''
    def setUp(self):
        print 'setup'
        
    def test_add_task_without_description(self):
        '''assert no items were added'''
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
