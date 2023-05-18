from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.atualiza_tela import Ui_Atualizar
from db.query import sqlite_db

class Objeto_Atualizar(QDialog):
  
    def __init__(self, *args, **argvs):
        super(Objeto_Atualizar,self).__init__(*args,**argvs)
        self.ui = Ui_Atualizar()
        self.ui.setupUi(self)
        self.ui.tableWidget.itemSelectionChanged.connect(self.PreencherCampos_Automaticamente)
        self.ui.pushButton_3.clicked.connect(self.Apagar_Cadastro)
        self.ui.pushButton.clicked.connect(self.Atualizar_Cadastro)
        self.ui.pushButton_2.clicked.connect(self.LimparCampos)
        self.ui.Search.clicked.connect(self.Pesquisar)
        self.Carregadados()

    def LimparCampos(self):
        nome = ""
        documento = ""
        endereco = ""
        self.ui.lineEdit.setText(nome)
        self.ui.lineEdit_2.setText(documento)
        self.ui.lineEdit_3.setText(endereco)

    def Atualizar_Cadastro(self):
        try:
            db = sqlite_db("manager.db")
            Id = self.PegaSelecaoDaTabela()
            Nome = self.ui.lineEdit.text()
            Documento = self.ui.lineEdit_2.text()
            Endereco = self.ui.lineEdit_3.text()
            db.inserir_apaga_atualiza(f"UPDATE funcionarios SET nome='{Nome}', documento='{Documento}', endereco='{Endereco}' WHERE id={Id}")
            QMessageBox.warning(QMessageBox(), "Deu bom!", "Cadastro atualizado!")
            self.Carregadados()
            self.LimparCampos()
        except:
            QMessageBox.warning(
                QMessageBox(), "Algo deu ruim!", "Não foi possivel!")



    def PreencherCampos_Automaticamente(self):
        IdLinhaSelecionada = self.PegaSelecaoDoBanco()

        if self.ui.tableWidget.item(IdLinhaSelecionada, 1) != None:
            nome = self.ui.tableWidget.item(IdLinhaSelecionada, 1).text()
            self.ui.lineEdit.setText(nome)
        
        if self.ui.tableWidget.item(IdLinhaSelecionada, 2) != None:
            documento = self.ui.tableWidget.item(IdLinhaSelecionada, 2).text()
            self.ui.lineEdit_2.setText(documento)
        
        if self.ui.tableWidget.item(IdLinhaSelecionada, 3) != None:
            endereco = self.ui.tableWidget.item(IdLinhaSelecionada, 3).text()
            self.ui.lineEdit_3.setText(endereco)

        

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.tableWidget.currentRow() 
        
    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
         valor = self.ui.tableWidget.item(self.PegaSelecaoDoBanco(), 0)
         return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def Apagar_Cadastro(self):
        try:
            db = sqlite_db("manager.db")
            Id = self.PegaSelecaoDaTabela()
            print(Id)
            db.inserir_apaga_atualiza("DELETE FROM funcionarios WHERE id='{}'".format(Id))
            QMessageBox.information(QMessageBox(), "Já era!","Passado varal!!")
            self.Carregadados()
        except:
            QMessageBox.warning(QMessageBox(), "Algo deu ruim!","Não foi possivel apagar!")    


    def Carregadados(self):
        db = sqlite_db("manager.db")
        lista = db.pega_dados("SELECT * FROM funcionarios")
        
        self.ui.tableWidget.setRowCount(0)
        #primeiro for trás
        for idxLinha, linha in enumerate(lista):
            self.ui.tableWidget.insertRow(idxLinha)
            for idxColuna, coluna in enumerate(linha):
                self.ui.tableWidget.setItem(idxLinha, idxColuna, QTableWidgetItem(str(coluna)))

    def Pesquisar(self):
        db = sqlite_db("manager.db")
        valor_consulta = ""
        valor_consulta = self.ui.inserirconsultar.text()

        lista = db.pega_dados(
            f"SELECT * FROM funcionarios where nome like '%{valor_consulta}%' or documento like'%{valor_consulta}%'")
        lista = list(lista)
        if not lista:
            return QMessageBox.warning(QMessageBox(), "Atenção!!", "Usuario não tem cadastro!!")

        else:
            self.ui.tableWidget.setRowCount(0)
            #primeiro for trás
            for idxLinha, linha in enumerate(lista):
                self.ui.tableWidget.insertRow(idxLinha)
                for idxColuna, coluna in enumerate(linha):
                    self.ui.tableWidget.setItem(
                        idxLinha, idxColuna, QTableWidgetItem(str(coluna)))

    
  
