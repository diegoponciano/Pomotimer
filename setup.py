from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="pomotimer",
      scripts=['pomotimer'],
      version='0.1.0',
      maintainer="Diego",
      maintainer_email="email@example.com",
      description="A PySide example",
      long_description=read('pomotimer.longdesc'),
      data_files=[('share/applications',['pomotimer.desktop']),
                  ('share/pixmaps', ['pomotimer.png']),])
