from PySide import QtCore

normal_style = """
 QLabel {
   color: black;
   font-size: 120pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

warning_style = """
 QLabel {
   color: red;
   font-size: 120pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

negative_style = """
 QLabel {
   color: black;
   background-color: red;
   font-size: 120pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

standby_style = """
 QLabel {
   color: green;
   background-color: black;
   font-size: 80pt;
   font-family: "PT Sans";
   font-weight: bold;
}"""

class PomodoroTimer(object):
  def __init__(self, label, totalTime, callback):
        self.label = label
        self.totalTime = totalTime
        self.callback = callback 
        self.remainingTime = totalTime
        self.current_state = self.standingby
        self.current_state()
        self.timer = QtCore.QTimer(interval=1000) # miliseconds
        self.timer.timeout.connect(self.on_every_second)

    # Event methods:
  def on_every_second(self):
        self.remainingTime -= 1
        self.current_state()

    # Methods:
  def start(self):
        if self.current_state not in [self.standingby, self.stopped]:
            return
        self.remainingTime = self.totalTime
        self.current_state = self.countdown
        self.current_state()
        self.timer.start()

  def stop(self):
        if self.current_state in [self.standingby, self.stopped]:
            return
        self.timer.stop()
        self.current_state = self.stopped
        self.current_state()
        self.callback()

  def standby(self):
        self.timer.stop()
        self.current_state = self.standingby
        self.current_state()


    # States:
  def standingby(self):
        self.label.setStyleSheet(standby_style)
        self.label.setText("TEDxSkopje")

  def stopped(self):
        self.label.setStyleSheet(normal_style)
        self.label.setText("00:00")

  def countdown(self):
        if self.remainingTime < 0:
            self.label.setStyleSheet(negative_style)
            self.label.setText("%02d:%02d" % divmod(abs(self.remainingTime), 60))
        elif self.remainingTime < 60:
            self.label.setStyleSheet(warning_style)
            self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60))
        else:
            self.label.setStyleSheet(normal_style)
            self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60))


