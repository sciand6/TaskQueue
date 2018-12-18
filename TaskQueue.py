# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Malcolm\Desktop\TaskQueue\TaskQueue\TaskQueue.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Task Queue")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 751, 461))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 231, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 10, 541, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuTask_Queue = QtWidgets.QMenu(self.menubar)
        self.menuTask_Queue.setObjectName("menuTask_Queue")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTask_Queue.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Buttons
        self.pushButton.clicked.connect(self.addItem)
        self.pushButton_2.clicked.connect(self.deleteItem)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Type a task description and click here to add the task to the task queue.</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Add Task"))
        self.label.setText(_translate("MainWindow", "Task Description:"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Task"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select a task to delete it from the queue.</p></body></html>"))
        self.menuTask_Queue.setTitle(_translate("MainWindow", "Task Queue"))

    def deleteItem(self):
        item = self.listWidget.takeItem(self.listWidget.currentRow())
        item = None

    def addItem(self):
        val = self.lineEdit.text()
        self.lineEdit.clear()
        self.listWidget.addItem(val)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

