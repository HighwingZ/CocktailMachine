from PyQt4 import QtCore, QtGui
import RPi.GPIO as GPIO
import time
import sys
import os
import subprocess
from hx711 import HX711
from GUI_progressBar import Ui_MainWindow
#from matplotlib.pylab import *
from numpy import *
import numpy
#import pygame
GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

hx = HX711(29, 31)
hx.set_reading_format("LSB", "MSB")
hx.set_reference_unit(-1000)

volume = 0
tara = 0
a = 0.0

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):								
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
		
		F = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","r")
		global a
		a = F.read()
		self.lcdNumber.display(a)
		F.close()
		
		self.B_1.clicked.connect(self.captain)			# Captain Cola
		self.B_2.clicked.connect(self.monkey)			# Monkey Wrrench
		self.B_3.clicked.connect(self.pain)				# Painkiller
		self.B_4.clicked.connect(self.orange)			# Wodka-O
		self.B_5.clicked.connect(self.pool)				# Swimming Pool
		self.B_6.clicked.connect(self.sunrise)			# Wodka Sunrise
		self.B_7.clicked.connect(self.icetea)			# Long Island Icetea
		self.B_8.clicked.connect(self.chi)				# Chi-Chi
		self.B_9.clicked.connect(self.zombie)			# Zombie	
		
		self.B_100.clicked.connect(self.klein)
		self.B_200.clicked.connect(self.mittel)
		self.B_300.clicked.connect(self.gross)
		
		self.B_abbruch.clicked.connect(self.cleanAndExit)
		
		GPIO.setup(3,GPIO.IN)				#abschalten der GPIOS am Anfang
		GPIO.setup(5,GPIO.IN)
		GPIO.setup(11,GPIO.IN)
		GPIO.setup(13,GPIO.IN)
		GPIO.setup(18,GPIO.IN)
		GPIO.setup(12,GPIO.IN)
		GPIO.setup(16,GPIO.OUT)				#Licht an!
		
		# hx = HX711(29, 31)
		# hx.set_reading_format("LSB", "MSB")
		# hx.set_reference_unit(-1000)
		hx.reset()
		hx.tare()
		# self.checker()
		
		#pygame.init()
		#pygame.mixer.init()
		
	# def checker(self):
		# if self.B_100.isChecked():
			# volume = 100
			# #print(volume)
			# self.B_200.setChecked(False)
			# self.B_300.setChecked(False)
		# elif self.B_200.isChecked():
			# volume = 200
		# #	print(volume)
			# self.B_100.setChecked(False)
			# self.B_300.setChecked(False)
		# elif self.B_300.isChecked():
			# volume = 300
			# #print(volume)
			# self.B_100.setChecked(False)
			# self.B_200.setChecked(False)
			
	def allesaus(self):
		GPIO.setup(3,GPIO.IN)
		GPIO.setup(5,GPIO.IN)
		GPIO.setup(11,GPIO.IN)
		GPIO.setup(13,GPIO.IN)
		GPIO.setup(18,GPIO.IN)
			
	def klein(self):
		self.B_100.setChecked(True)
		self.B_200.setChecked(False)
		self.B_300.setChecked(False)
		GPIO.setup(12,GPIO.OUT)
		volume = 100
		
	def mittel(self):
		self.B_100.setChecked(False)
		self.B_200.setChecked(True)
		self.B_300.setChecked(False)
		GPIO.setup(12,GPIO.OUT)
		volume = 200
	
	def gross(self):
		self.B_100.setChecked(False)
		self.B_200.setChecked(False)
		self.B_300.setChecked(True)
		GPIO.setup(12,GPIO.OUT)
		volume = 300
		
	def uncheck(self):
		self.B_100.setChecked(False)
		self.B_200.setChecked(False)
		self.B_300.setChecked(False)
		self.B_1.setChecked(False)
		self.B_2.setChecked(False)
		self.B_3.setChecked(False)
		self.B_4.setChecked(False)
		self.B_5.setChecked(False)
		self.B_6.setChecked(False)
		self.B_7.setChecked(False)
		self.B_8.setChecked(False)
		self.B_9.setChecked(False)
	
	def enable_all(self):
		self.B_100.setDisabled(False)
		self.B_200.setDisabled(False)
		self.B_300.setDisabled(False)
		self.B_1.setDisabled(False)
		self.B_2.setDisabled(False)
		self.B_3.setDisabled(False)
		self.B_4.setDisabled(False)
		self.B_5.setDisabled(False)
		self.B_6.setDisabled(False)
		self.B_7.setDisabled(False)
		self.B_8.setDisabled(False)
		self.B_9.setDisabled(False)	
	
	def disable_all(self):
		self.B_100.setDisabled(True)
		self.B_200.setDisabled(True)
		self.B_300.setDisabled(True)
		self.B_1.setDisabled(True)
		self.B_2.setDisabled(True)
		self.B_3.setDisabled(True)
		self.B_4.setDisabled(True)
		self.B_5.setDisabled(True)
		self.B_6.setDisabled(True)
		self.B_7.setDisabled(True)
		self.B_8.setDisabled(True)
		self.B_9.setDisabled(True)

	def captain(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
			
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)			
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.2:
				#os.system("mpg321 gay.mp3")
				#subprocess.Popen(["mpg321","gay.mp3"])
				#music = os.popen('mpg321 gay.mp3', 'w')
				#music.close()
				GPIO.setup(5,GPIO.OUT)
			elif volume*0.2 < val - tara < volume:
				GPIO.setup(5,GPIO.IN)
				GPIO.setup(13,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(13,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
	
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)		
			
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
			
	def monkey(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
			
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.2:
				GPIO.setup(5,GPIO.OUT)
			elif volume*0.2 < val - tara < volume:
				GPIO.setup(5,GPIO.IN)
				GPIO.setup(18,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(18,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						
	
	def pain(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
			
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.2:
				GPIO.setup(5,GPIO.OUT)
			elif volume*0.2 < val - tara < volume*0.6:
				GPIO.setup(5,GPIO.IN)
				GPIO.setup(11,GPIO.OUT)
			elif volume*0.6 < val - tara < volume:
				GPIO.setup(11,GPIO.IN)
				GPIO.setup(18,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(18,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						
			
	def orange(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
			
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.2:
				GPIO.setup(3,GPIO.OUT)
			elif volume*0.2 < val - tara < volume:
				GPIO.setup(3,GPIO.IN)
				GPIO.setup(11,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(11,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						
			
	def pool(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
			
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.1428:
				GPIO.setup(5,GPIO.OUT)
			elif volume*0.1428 < val - tara < volume*0.2857:
				GPIO.setup(5,GPIO.IN)
				GPIO.setup(3,GPIO.OUT)
			elif volume*0.2857 < val - tara < volume:
				GPIO.setup(3,GPIO.IN)
				GPIO.setup(18,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(18,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						

	def sunrise(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
			
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.3333:
				GPIO.setup(3,GPIO.OUT)
			elif volume*0.3333 < val - tara < volume*0.6666:
				GPIO.setup(3,GPIO.IN)
				GPIO.setup(11,GPIO.OUT)
			elif volume*0.6666 < val - tara < volume:
				GPIO.setup(11,GPIO.IN)
				GPIO.setup(18,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(18,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						
	
	def icetea(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
				
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.1666:
				GPIO.setup(3,GPIO.OUT)
			elif volume*0.1666 < val - tara < volume*0.3333:
				GPIO.setup(3,GPIO.IN)
				GPIO.setup(5,GPIO.OUT)
			elif volume*0.3333 < val - tara < volume*0.6666:
				GPIO.setup(5,GPIO.IN)
				GPIO.setup(13,GPIO.OUT)
			elif volume*0.6666 < val - tara < volume:
				GPIO.setup(13,GPIO.IN)
				GPIO.setup(11,GPIO.OUT)					
			elif val - tara > volume:
				GPIO.setup(11,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						
	
	def chi(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
				
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			self.disable_all()
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.3333:
				GPIO.setup(3,GPIO.OUT)
			elif volume*0.3333 < val - tara < volume:
				GPIO.setup(3,GPIO.IN)
				GPIO.setup(18,GPIO.OUT)
			elif val - tara > volume:
				GPIO.setup(18,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						
				
	def zombie(self):
		tara = hx.get_weight(5)
		if self.B_100.isChecked():
			volume = 100
		elif self.B_200.isChecked():
			volume = 200
		elif self.B_300.isChecked():
			volume = 300
				
		while self.B_100.isChecked() or self.B_200.isChecked() or self.B_300.isChecked():
			self.disable_all()
			val = hx.get_weight(5)
			progress = 100*(val - tara)/(volume)
			self.progressBar.setProperty("value", progress)
			
			
			if val+5 <25:
				self.uncheck()
				self.allesaus()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break
			elif val < tara:
				self.uncheck()
				GPIO.cleanup()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				break			
			elif val - tara < volume*0.1666 :
				GPIO.setup(3,GPIO.OUT)
			elif volume*0.1666  < val - tara < volume*0.3333:
				GPIO.setup(3,GPIO.IN)
				GPIO.setup(5,GPIO.OUT)
			elif volume*0.3333 < val - tara < volume*0.6666:
				GPIO.setup(5,GPIO.IN)
				GPIO.setup(13,GPIO.OUT)
			elif volume*0.6666 < val - tara < volume*0.8333:
				GPIO.setup(13,GPIO.IN)
				GPIO.setup(11,GPIO.OUT)	
			elif volume*0.8333 < val - tara < volume:
				GPIO.setup(11,GPIO.IN)
				GPIO.setup(18,GPIO.OUT)						
			elif val - tara > volume:
				GPIO.setup(18,GPIO.IN)
				self.uncheck()
				self.progressBar.setProperty("value", 0)
				self.enable_all()
				GPIO.setup(12,GPIO.IN)
				
				b = volume*0.001
				global a
				print(b+float(a))
				a=b+float(a)
				self.lcdNumber.display(float(a))
				E = open("/home/pi/codes/GetrAtomat/Version_Oktober_17/data.txt","w")
				E.write(str(a))
				E.close()
				
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.IN)
				time.sleep(0.225)
				GPIO.setup(16,GPIO.OUT)
				
				break
			else:
				continue
			hx.power_down()
			hx.power_up()
			time.sleep(0.2)
		while not self.B_100.isChecked() or not self.B_200.isChecked() or not self.B_300.isChecked():
			self.uncheck()
			break
						

	def tarefunction():
		tara = hx.get_weight(5)					

	def cleanAndExit(self):
		print "Cleaning..."
		GPIO.cleanup()
		print "Bye!"
		sys.exit()
		
if __name__ == '__main__':                  
	app = QtGui.QApplication(sys.argv)    	
	s = MainWindow()                        
	s.show()                                
	sys.exit(app.exec_())	
