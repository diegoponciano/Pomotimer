#!/usr/bin/python

import os

tomatoes_dir = os.path.join(os.path.expanduser('~'), ".tomatoes")
tomatoes_data = os.path.join(tomatoes_dir, "data.fs")

import anydbm

from ZODB import FileStorage, DB
from ZODB.PersistentList import PersistentList
from persistent import Persistent
from BTrees.OOBTree import OOBTree
import transaction

class TodoItem(Persistent):
  pass

class TodoList():
  def __init__(self):
      if not os.path.exists(tomatoes_dir):
          os.path.os.mkdir(tomatoes_dir)

      storage = FileStorage.FileStorage(tomatoes_data)
      db = DB(storage)
      conn = db.open()
      self.dbroot = conn.root()
      if not self.dbroot.has_key('tasks'):
          self.dbroot['tasks'] = OOBTree()
      self.tasks = self.dbroot['tasks']

  def addItem(self, task):
      tasks_size = len(self.tasks)
      task_ident = tasks_size+1 

      new_task = TodoItem()
      new_task.id = task_ident
      new_task.description = task
      self.tasks[task_ident] = new_task

      transaction.commit()
      return self.tasks[task_ident]
