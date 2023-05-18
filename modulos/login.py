from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from modulos.principal import telaprincipal
from template.login import Ui_login
from db.query import sqlite_db

class login(QDialog):
  
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/about.jpg'))
        self.ui.pushButton.clicked.connect(self.login)
        #self.ui.pushButton_2.clicked.connect(self.login)
        


    def login(self):
        db = sqlite_db("manager.db")

        user = self.ui.lineEdit.text()
        passwd =self.ui.lineEdit_2.text()
        if user ==" " or  passwd==" ":
            QMessageBox.warning(QMessageBox(),"Alerta!", "Preencha todos os campos!!")
        else:
            dados = db.pega_dados("SELECT acesso FROM user WHERE username = '{}' and password ='{}'" .format(user,passwd))
            if dados: 
                QMessageBox.information(QMessageBox(),"login realizado!", "ENTROU COM SUCESSO!")
                self.logado = user
                self.window = telaprincipal(self,self.logado)
                self.window.show()
                self.hide()
            else:
                QMessageBox.warning(QMessageBox(),"login errado!", "NÃO ENTROU COM SUCESSO!")
        


