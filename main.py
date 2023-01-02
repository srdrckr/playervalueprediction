import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from main_window_design import Ui_MainWindow

df = pd.read_csv("players.csv", usecols = ["name", "age", "position", "club", "nation", "value"])
name = df.name.to_list()
age = df.age.to_list()
position = df.position.to_list()
club = df.club.to_list()
nation = df.nation.to_list()
value = df.value.to_list()

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sayfa = Ui_MainWindow()
        self.sayfa.setupUi(self)
        self.tableshow()
        self.sayfa.lineEdit = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.sayfa.lineEdit.textChanged.connect(self.filter)

    def tableshow(self):
        self.sayfa.tableWidget.setSortingEnabled(True)
        self.sayfa.tableWidget.setColumnWidth(0, 180)
        self.sayfa.tableWidget.setColumnWidth(1, 100)
        self.sayfa.tableWidget.setColumnWidth(2, 50)
        self.sayfa.tableWidget.setColumnWidth(3, 200)
        self.sayfa.tableWidget.setColumnWidth(4, 200)
        self.sayfa.tableWidget.setColumnWidth(5, 80)
        self.sayfa.tableWidget.setRowCount(len(name))
        self.sayfa.tableWidget.setRowCount(len(age))
        self.sayfa.tableWidget.setRowCount(len(position))
        self.sayfa.tableWidget.setRowCount(len(club))
        self.sayfa.tableWidget.setRowCount(len(nation))
        self.sayfa.tableWidget.setRowCount(len(value))

        satir = 0
        for veri in name:
            self.sayfa.tableWidget.setItem(satir,0,QtWidgets.QTableWidgetItem(veri))
            satir +=1

        satir = 0
        for veri in position:
            self.sayfa.tableWidget.setItem(satir,1,QtWidgets.QTableWidgetItem(veri))
            satir +=1

        satir = 0
        for veri in age:
            self.sayfa.tableWidget.setItem(satir, 2, QtWidgets.QTableWidgetItem(str(veri)))
            satir += 1

        satir = 0
        for veri in club:
            self.sayfa.tableWidget.setItem(satir,3,QtWidgets.QTableWidgetItem(veri))
            satir +=1

        satir = 0
        for veri in nation:
            self.sayfa.tableWidget.setItem(satir,4,QtWidgets.QTableWidgetItem(veri))
            satir +=1

        satir = 0
        for veri in value:
            self.sayfa.tableWidget.setItem(satir, 5, QtWidgets.QTableWidgetItem(veri))
            satir += 1

    def filter(self, filter_text):
        for i in range(self.sayfa.tableWidget.rowCount()):
            for j in range(self.sayfa.tableWidget.columnCount()):
                item = self.sayfa.tableWidget.item(i, j)
                match = filter_text.lower() not in item.text().lower()
                self.sayfa.tableWidget.setRowHidden(i, match)
                if not match:
                    break

app = QApplication([])
pencere = main()
pencere.show()
app.exec_()

