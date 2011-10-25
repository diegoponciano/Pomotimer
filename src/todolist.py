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
      if (len(self.tasks) > 0):
          last_id = list(self.tasks)[-1]
          new_id = last_id+1 

      new_task = TodoItem()
      new_task.id = new_id
      new_task.description = task
      self.tasks[new_id] = new_task

      transaction.commit()
      return self.tasks[new_id]

  def removeItem(self, id):
      del self.tasks[id]

      transaction.commit()
      return
