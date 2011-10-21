#!/usr/bin/python

import os
import sys
import unittest

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
