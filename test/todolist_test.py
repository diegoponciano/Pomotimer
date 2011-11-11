#!/usr/bin/python

import os
import sys
import unittest

from pomolib import todolist

class TodoListTest(unittest.TestCase):
    '''Test the pomodoro list'''
    @classmethod
    def setUpClass(cls):
        cls.todolist = todolist.TodoList()

    def test_add_task_with_description(self):
        '''assert items were added'''
        tasks_size = len(self.todolist.tasks)
        new_task = self.todolist.addItem("make tomato")
        tasks_new_size = len(self.todolist.tasks)

        self.assertEqual(tasks_new_size, tasks_size+1)
        self.assertNotEqual(new_task.id, 0)
        self.assertEqual(new_task.description, 'make tomato')

    def test_remove_task(self):
        '''assert item was removed'''
        self.todolist.addItem("make tomato")
        another_item = self.todolist.addItem("make another tomato")

        tasks_size = len(self.todolist.tasks)
        item_id = self.todolist.tasks.minKey()
        self.todolist.removeItem(item_id)
        tasks_new_size = len(self.todolist.tasks)

        self.assertEqual(tasks_new_size, tasks_size-1)

    def test_remove_two_tasks(self):
        '''assert two items were removed'''
        self.todolist.addItem("make tomato")
        another_item = self.todolist.addItem("make another tomato")

        tasks_size = len(self.todolist.tasks)
        item_id = self.todolist.tasks.minKey()
        self.todolist.removeItem(item_id)
        self.todolist.removeItem(another_item.id)
        tasks_new_size = len(self.todolist.tasks)

        self.assertEqual(tasks_new_size, tasks_size-2)

if __name__ == "__main__":
    unittest.main()
