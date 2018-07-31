import sys,time,threading,struct
import PyQt5
try:
    import smbus
except:
    pass
from PyQt5.QtWidgets import *

import socket
try:
  import fcntl
except:
  pass
import mainwindow
"""
Motor 1: Blue Robotics 1
Motor 2: Blue Robotics 2
Motor 3: Maxon Sensorless

"""

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    return str(s.getsockname()[0])
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
 # access variables inside of the UI's file
 def __init__(self):
     super(self.__class__, self).__init__()
     self.setupUi(self) # gets defined in the UI file
     self.setCursor(PyQt5.QtCore.Qt.BlankCursor)


     self.active_motor="falcon_button"
     self.active_state="stop_button"
     self.motor_set_velocity=1000
     self.motor_get_velocity=0
     self.running = True
     self.statusBar.showMessage(get_ip_address('wlan0'))
     vel_loop = threading.Thread(target=self.motor_loop,args=[])
     vel_loop.start()

 def button_handler(self):
     print(self.sender().objectName())
     if self.sender().objectName() != self.active_motor:
         self.change_active_motor(self.sender().objectName())

 def change_active_motor(self,motor):
     if self.active_state == "stop_button":
         eval("self.%s.setStyleSheet(\"\")" % self.active_motor)
         eval("self.%s.setStyleSheet(\"QPushButton{color: blue}\")" % motor)
         if motor=="falcon_button" or motor == "savox_button":
          self.vel_up.setEnabled(True)
          self.vel_down.setEnabled(True)
          self.vel_up_10.setEnabled(True)
          self.vel_down_10.setEnabled(True)
          self.forward_button.setText("Forward")
          self.reverse_button.setText("Reverse")
         else:
          self.vel_up.setEnabled(False)
          self.vel_down.setEnabled(False)
          self.vel_up_10.setEnabled(False)
          self.vel_down_10.setEnabled(False)
          self.forward_button.setText("Expulsion")
          self.reverse_button.setText("Ingestion")
         self.motor_name.setText(str(motor.split("_")[0]).upper())
         self.active_motor=motor
 def get_motor_name(self):
     return str(self.active_motor)
 def up_velocity(self):
     self.motor_set_velocity=self.motor_set_velocity+100
     self.send_i2c_command(self.active_motor,"vel")
 def down_velocity(self):
     self.motor_set_velocity=self.motor_set_velocity-100
     self.send_i2c_command(self.active_motor,"vel")
 def up_velocity_10(self):
     self.motor_set_velocity=self.motor_set_velocity+10
     self.send_i2c_command(self.active_motor,"vel")
 def down_velocity_10(self):
     self.motor_set_velocity=self.motor_set_velocity-10
     self.send_i2c_command(self.active_motor,"vel")

 def set_motor_state(self):
     state=self.sender().objectName()
     if state != self.active_state:
         eval("self.%s.setStyleSheet(\"\")" % self.active_state)
         eval("self.%s.setStyleSheet(\"QPushButton{color:red;}\")" % state)
         self.send_i2c_command(self.active_motor,state.split("_")[0])
         self.active_state=state
 def get_motor_velocity(self):
     speed=self.send_i2c_command(self.active_motor,"getv")
     self.measured_velocity.setText(str(speed))
 def motor_loop(self):
     while (self.running):
         self.measured_velocity.setText(str(self.motor_get_velocity))
         if self.active_motor == "falcon_button" or self.active_motor=="savox_button":
          self.set_velocity_label.setText(str(self.motor_set_velocity))
          if self.active_motor=="savox_button" and (self.active_state=="forward_button" or self.active_state=="reverse_button"):
            if abs(self.motor_get_velocity) == abs(self.motor_set_velocity):
              eval("self.%s.setStyleSheet(\"\")" % self.active_state)
              eval("self.%s.setStyleSheet(\"QPushButton{color:red;}\")" % "stop_button")
              self.send_i2c_command(self.active_motor,"stop")
              self.active_state="stop_button"
         else:
          self.set_velocity_label.setText("--")
         self.get_motor_velocity()
         time.sleep(1)

 def send_i2c_command(self,dev,cmd):
     # name : [address,forward,reverse,off,set_vel]
     devices={"falcon_button":[0x12],
               "savox_button":[0x13],
               "br_button":[0x30],
               "br2_button":[0x32],
               "maxon_button":[0x31]}
     commands={"go":0x04,"vel":0x07,"get_vel":0x08}
     on_bit = 0x1
     #if dev != "falcon_button" :
     # commands["go"]=commands["go"]-1
     # commands["vel"]=commands["vel"]-1
     # commands["get_vel"]=commands["get_vel"]-1
     if dev == "savox_button" :
      self.label_3.setText("Measured Position")
      self.label_6.setText("Set Position")
      commands["go"]=0x4
      commands["vel"]=0x9
      commands["get_vel"]=0xA
      on_bit=0x2
      #set velocity for position control to 8000
      dir_bit=1
      if cmd=="reverse":
        dir_bit=-1
      reg=[0,0,0,0]
      reg[0] = ((dir_bit*8000) & 0xFF000000) >> 24;
      reg[1] = ((dir_bit*8000) & 0x00FF0000) >> 16;
      reg[2] = ((dir_bit*8000) & 0x0000FF00) >> 8;
      reg[3] = ((dir_bit*8000) & 0x000000FF) >> 0;
      print("I2C",devices[dev][0], 0x7, reg)
      try:
        bus.write_i2c_block_data(devices[dev][0], 0x07, reg)
      except OSError:
        pass
      #set accel for position control to 1000
      reg=[0,0,0,0]
      reg[0] = (1000 & 0xFF000000) >> 24;
      reg[1] = (1000 & 0x00FF0000) >> 16;
      reg[2] = (1000 & 0x0000FF00) >> 8;
      reg[3] = (1000 & 0x000000FF) >> 0;
      print("I2C",devices[dev][0], 0x5, reg)
      try:
        bus.write_i2c_block_data(devices[dev][0], 0x05, reg)
      except OSError:
        pass
      #set decel for position control to 1000
      reg=[0,0,0,0]
      reg[0] = (1000 & 0xFF000000) >> 24;
      reg[1] = (1000 & 0x00FF0000) >> 16;
      reg[2] = (1000 & 0x0000FF00) >> 8;
      reg[3] = (1000 & 0x000000FF) >> 0;
      print("I2C",devices[dev][0], 0x6, reg)
      try:
        bus.write_i2c_block_data(devices[dev][0], 0x06, reg)
      except OSError:
        pass
        
     else:
      self.label_3.setText("Measured Velocity")
      self.label_6.setText("Set Velocity")
     if cmd=="forward":
        #set negative vel
        reg=[0,0,0,0]
        self.motor_set_velocity = abs(self.motor_set_velocity)
        reg[0] = (self.motor_set_velocity & 0xFF000000) >> 24;
        reg[1] = (self.motor_set_velocity & 0x00FF0000) >> 16;
        reg[2] = (self.motor_set_velocity & 0x0000FF00) >> 8;
        reg[3] = (self.motor_set_velocity & 0x000000FF) >> 0;
        print("I2C",devices[dev][0], commands["vel"], reg)
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["vel"], reg)
        except OSError:
          pass
        #turn on
        
        reg=[0,0,0,0]
        reg[0] = (on_bit & 0xFF000000) >> 24
        reg[1] = (on_bit & 0x00FF0000) >> 16
        reg[2] = (on_bit & 0x0000FF00) >> 8
        reg[3] = (on_bit & 0x000000FF) >> 0
        print("I2C",devices[dev][0], commands["go"], reg)
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["go"], reg)
        except OSError:
          pass
     elif cmd=="reverse":
        #set negative vel
        reg=[0,0,0,0]
        self.motor_set_velocity = -1*abs(self.motor_set_velocity)
        reg[0] = (self.motor_set_velocity & 0xFF000000) >> 24;
        reg[1] = (self.motor_set_velocity & 0x00FF0000) >> 16;
        reg[2] = (self.motor_set_velocity & 0x0000FF00) >> 8;
        reg[3] = (self.motor_set_velocity & 0x000000FF) >> 0;
        print("I2C",devices[dev][0], commands["vel"], reg)
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["vel"], reg)
        except OSError:
          pass
        #turn on
        reg=[0,0,0,0]
        reg[0] = (on_bit & 0xFF000000) >> 24
        reg[1] = (on_bit & 0x00FF0000) >> 16
        reg[2] = (on_bit & 0x0000FF00) >> 8
        reg[3] = (on_bit & 0x000000FF) >> 0
        print("I2C",devices[dev][0], commands["go"], reg)
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["go"], reg)
        except OSError:
          pass
     elif cmd=="stop":
        reg=[0,0,0,0]
        reg[0] = (0x0 & 0xFF000000) >> 24
        reg[1] = (0x0 & 0x00FF0000) >> 16
        reg[2] = (0x0 & 0x0000FF00) >> 8
        reg[3] = (0x0 & 0x000000FF) >> 0
        print("I2C",devices[dev][0], commands["go"], reg)
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["go"], reg)
        except OSError:
          pass
     elif cmd == "getv":
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["get_vel"], [0])
          e=bus.read_i2c_block_data(devices[dev][0],commands["get_vel"],4)
          (spd,)=struct.unpack('>l',bytearray(e))
        except OSError:
          #Cannot read from device
          #self.statusBar.showMessage(self.active_motor.split("_")[0]+" is not connected",2000)
          return "Discon."
          
        #spd=(e[0] << 24) | (e[1] << 16) | (e[2] << 8) | (e[3] << 0)
        #print (e,"\n",spd)
        return spd
     else:
        #set velocity
        reg=[0,0,0,0]
        reg[0] = (self.motor_set_velocity & 0xFF000000) >> 24;
        reg[1] = (self.motor_set_velocity & 0x00FF0000) >> 16;
        reg[2] = (self.motor_set_velocity & 0x0000FF00) >> 8;
        reg[3] = (self.motor_set_velocity & 0x000000FF) >> 0;
        print("I2C",devices[dev][0], commands["vel"], reg)
        try:
          bus.write_i2c_block_data(devices[dev][0], commands["vel"], reg)
        except OSError:
          pass
def main():
 # a new app instance
 app = QApplication(sys.argv)
 form = MainWindow()
 form.showFullScreen()
 # without this, the script exits immediately.
 sys.exit(app.exec_())

try:
    bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
except:
    pass
main()
