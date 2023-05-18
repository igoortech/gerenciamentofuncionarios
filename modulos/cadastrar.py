from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.cadastrar import Ui_cadastrar

from db.query import sqlite_db

class cadastrar(QDialog):
    def __init__(self,carregados,*args,**argvs):
        super(cadastrar,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar()
        self.ui.setupUi(self)
        self.ui.btnadd.clicked.connect(self.add)
        self.ui.btnc.clicked.connect(self.can)
        self.ui.btnl.clicked.connect(self.LimparCampos)
        self.carregainfo = carregados

        quit = QtWidgets.QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)

    def closeEvent(self,event):
        self.carregainfo()

    def LimparCampos(self):
            nome = ""
            documento = ""
            endereco = ""
            self.ui.inputnome.setText(nome)
            self.ui.inputdoc.setText(documento)
            self.ui.inputend.setText(endereco)



    def add(self):
        db = sqlite_db("manager.db")

        name = self.ui.inputnome.text()
        docu = self.ui.inputdoc.text()
        end = self.ui.inputend.text()
        adm = 1
        if name == "" or docu ==""  or end =="":
             QMessageBox.information(QMessageBox(),"OPA PA", "Preencha todos os campos!")
        else:
            db.inserir_apaga_atualiza("INSERT INTO funcionarios (nome, documento,endereco,admin) VALUES ('{}', '{}', '{}', '{}')".format(name,docu,end,adm))
            QMessageBox.information(QMessageBox(),"OPA PA", "DADOS GRAVADOS COM SUCESSO!")
            self.LimparCampos()
            


    
    def can(self):
        self.close()
  
