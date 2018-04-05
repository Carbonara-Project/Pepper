import idc
import idaapi

import guanciale

from PyQt5 import QtGui, QtWidgets, QtCore

class Context(object):
	def __init__(self):
		self.updated = False
		self.bi = None
		self.descriptions = {}
