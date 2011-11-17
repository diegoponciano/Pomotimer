from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="pomotimer",
      scripts=['pomotimer'],
      packages=['pomolib'],
      version='0.1.0',
      maintainer="Diego Ponciano",
      maintainer_email="diego@diegoponciano.com",
      description="A simple Pomodoro timer",
      long_description=read('pomotimer.longdesc'),
      data_files=[('share/applications',['pomotimer.desktop']),
                  ('share/pixmaps', ['pomotimer.png']),
                  ('share/pomotimer/assets', glob.glob(os.path.join('assets', '*')))]
      )
