from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.tela import Ui_MainWindow
from modulos.cadastrar import cadastrar
from modulos.Atualizar import Objeto_Atualizar
from modulos.Consultar import Pesquisar_Objeto
from db.query import sqlite_db


class telaprincipal(QMainWindow):
    def __init__(self,telalogin,logado,*args,**argvs):
        super(telaprincipal,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.telalogin = telalogin
        self.ui.actionCadastrar.triggered.connect(self.add)
        self.ui.actionRefresh.triggered.connect(self.carregadados)
        self.ui.actionAtualizar.triggered.connect(self.Atualizar)
        self.ui.actionProcurar.triggered.connect(self.Pesquisar)
        self.ui.actionApagar.triggered.connect(self.Apagar_registro)
        self.carregadados()
        self.userlogado =logado
        self.ui.logado.setText(self.userlogado)

        #fecha a janela atual e reexiba a janela desejada.

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Alerta!',
                                     "Tem certeza que deseja sair?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.telalogin.show()
            self.clearMask()
            self.destroy()
        else:
            event.ignore()

    def Apagar_registro(self):
        try:
            db = sqlite_db("manager.db")
            Id = self.PegaSelecaoDaTabela()
            db.inserir_apaga_atualiza("DELETE FROM funcionarios WHERE id='{}'".format(Id))
            QMessageBox.information(QMessageBox(), "Já era!", "Passado varal!!")
            self.carregadados()
        except:
            QMessageBox.warning(QMessageBox(), "Algo deu ruim!", "Não foi possivel!")



    def carregadados(self):
        db = sqlite_db("manager.db")
        lista = db.pega_dados("SELECT * FROM funcionarios")
        lista = lista[-10:]
        lista.reverse()

        self.ui.tableWidget.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha,coluna_n,QTableWidgetItem(str(dados)))
                a = 1

    def PegaSelecaoDaTabela(self):  # pega id seleção da tabela
        valor = self.ui.tableWidget.item(self.PegaSelecaoDoBanco(), 0) 
        return valor.text() if not valor is None else valor  #deve retornar valor str não memoria

    def PegaSelecaoDoBanco(self):  # pega id seleção do banco
        return self.ui.tableWidget.currentRow() 




    def Atualizar(self):
        Atualizar = Objeto_Atualizar()
        Atualizar.exec_()
        
    def Pesquisar(self):
        Pesquisar = Pesquisar_Objeto()
        Pesquisar.exec_()

    def add(self):
        add = cadastrar(self.carregadados)
        add.exec_()
