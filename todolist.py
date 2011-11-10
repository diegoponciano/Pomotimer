#!/usr/bin/python

import os
import anydbm
import transaction

from ZODB import FileStorage, DB
from ZODB.PersistentList import PersistentList
from persistent import Persistent
from BTrees.OOBTree import OOBTree

import config

class TodoItem(Persistent):
  pass

class TodoList():
  def __init__(self):
      if not os.path.exists(config.tomatoes_dir):
          os.path.os.mkdir(config.tomatoes_dir)

      self.store = FileStorage.FileStorage(config.tomatoes_data)
      self.db = DB(self.store)
      self.conn = self.db.open()
      self.dbroot = self.conn.root()

      if not self.dbroot.has_key('tasks'):
          self.dbroot['tasks'] = OOBTree()
      self.tasks = self.dbroot['tasks']
  
  def close(self):
      try:
          self.conn.close()
          self.db.close()
          self.store.close()
          return True
      except:
          return False

  def addItem(self, task):
      if (len(self.tasks) > 0):
          last_id = self.tasks.maxKey()
          new_id = last_id+1 
      else:
        new_id = 1

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
