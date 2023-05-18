from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from db.query import sqlite_db
from template.pesquisar_tela import Ui_Pesquisar

class Pesquisar_Objeto(QDialog):
  
    def __init__(self,*args,**argvs):
        super(Pesquisar_Objeto,self).__init__(*args,**argvs)
        self.ui = Ui_Pesquisar()
        self.ui.setupUi(self)
        self.ui.BTNConsultar.clicked.connect(self.Pesquisar)

    def Pesquisar(self):
        db = sqlite_db("manager.db")
        valor_consulta =""
        valor_consulta = self.ui.entradaconsulta.text()

        lista = db.pega_dados(f"SELECT * FROM funcionarios where nome like '%{valor_consulta}%' or documento like'%{valor_consulta}%'")
        lista = list(lista)
        if not lista:
            return  QMessageBox.warning(QMessageBox(),"Atenção!!", "Usuario não tem cadastro!!")
            
        else:   
            self.ui.tableWidget.setRowCount(0)
            #primeiro for trás
            for idxLinha, linha in enumerate(lista):
                self.ui.tableWidget.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.ui.tableWidget.setItem(idxLinha, idxColuna, QTableWidgetItem(str(coluna)))


 
