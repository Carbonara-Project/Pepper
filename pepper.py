import idc
import idaapi

import guanciale

from PyQt5 import QtGui, QtWidgets, QtCore

class Context(object):
	def __init__(self):
		self.updated = False
		self.bi = None
		self.descriptions = {}

context = None

def load_binary():
	filename = idaapi.get_input_file_path()
	context = Context()
	context.bi = guanciale.BinaryInfo(filename)
	


