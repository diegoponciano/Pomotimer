#!/usr/bin/python

import os
import sys
import unittest

import todolist

class TodoListTest(unittest.TestCase):
    '''Test the pomodoro list'''
    def setUp(self):
        self.todolist = todolist.TodoList()

    def test_add_task_with_description(self):
        '''assert items were added'''
        tasks_size = len(self.todolist.tasks)
        new_task = self.todolist.addItem("make tomato")
        tasks_new_size = len(self.todolist.tasks)

        self.assertTrue(tasks_new_size > tasks_size)
        self.assertNotEqual(new_task.id, 0)

if __name__ == "__main__":
    unittest.main()
