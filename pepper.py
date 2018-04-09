import idc
import idaapi

import guanciale
import requests
import appdirs
import os

from PyQt5 import QtGui, QtWidgets, QtCore
from ui import *

dirs = appdirs.AppDirs("carbonara_cli")
token_path = os.path.join(os.path.dirname(dirs.user_config_dir), "carbonara_cli.token")

CARBONARA_URL = "https://carbonaraproject.com"
#CARBONARA_URL = "http://localhost:8000"
CLIENT_ID="2MBBuSf2kKNhHyDMjKi80jJPeJqzhYdzsOxzHM3z"

class LoginDialog(QtWidgets.QDialog):
    
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
    
    @staticmethod
    def get_credentials():
        dialog = LoginDialog()
        r = dialog.exec_()
        if r == QtWidgets.QDialog.Accepted:
            user = dialog.ui.mailEdit.toPlainText()
            passw = dialog.ui.passEdit.toPlainText()
            return (user, passw)
        return None

class Context(object):
	def __init__(self):
		self.token = None
		self.updated = False
		self.bi = None
		self.descriptions = {}

	def get_token(self):    
		request_token = False
		try:
		    token_file = open(token_path)
		    token = token_file.read()
		    token_file.close()
		except:
		    request_token = True

		#verify token
		if request_token == False:
		    done = False
		    headers = {"Authorization": "Bearer " + token}
		    try:
		        r = requests.head(CARBONARA_URL + "/api/program/", headers=headers)
		        done = True
		        #print r
		    except:
		        request_token = True
		    
		    if done:
		        if r.status_code == 401 or r.status_code == 403: #token expired
		            request_token = True
		        elif r.status_code != 400 and r.status_code != 200 and r.status_code != 204:
		            return "cannot verify auth token"
		            request_token = True
		
		if request_token:
		    login = LoginDialog.get_credentials()
		    if login == None:
		    	return
		    username, password = login
		    auth_body = {
		        "client_id": CLIENT_ID,
		        "grant_type": "password",
		        "username": username,
		        "password": password
		    }
		    try:
		        r = requests.post(CARBONARA_URL + "/users/o/token/", data=auth_body)
		    except:
		        return "cannot get auth token"
		    
		    if r.status_code != 200:
		        return "cannot get auth token"
		    self.token = r.json()["access_token"]
		
		if self.token == None:
		    return "wrong authentication"
		
		try:
		    token_file = open(token_path, "w")
		    token_file.write(self.token)
		    token_file.close()
		except:
		    #printwarn("cannot save auth token")
		    pass
		return self.token


context = None

def init():
	global context
	filename = idaapi.get_input_file_path()
	context = Context()
	context.bi = guanciale.BinaryInfo(filename)
	

def uploadAll():
	pass





