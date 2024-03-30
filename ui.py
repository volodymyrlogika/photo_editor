# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 745)
        MainWindow.setStyleSheet("background: #1e0038;\n"
"color: white;\n"
"font-size: 20px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_list = QtWidgets.QListWidget(self.centralwidget)
        self.image_list.setGeometry(QtCore.QRect(20, 90, 191, 571))
        self.image_list.setObjectName("image_list")
        self.folder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.folder_btn.setGeometry(QtCore.QRect(20, 20, 191, 51))
        self.folder_btn.setStyleSheet("background: #ac51fc;\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.folder_btn.setObjectName("folder_btn")
        self.right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn.setGeometry(QtCore.QRect(230, 20, 121, 51))
        self.right_btn.setStyleSheet("border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.right_btn.setObjectName("right_btn")
        self.left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn.setGeometry(QtCore.QRect(370, 20, 121, 51))
        self.left_btn.setStyleSheet("border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.left_btn.setObjectName("left_btn")
        self.blur_btn = QtWidgets.QPushButton(self.centralwidget)
        self.blur_btn.setGeometry(QtCore.QRect(500, 20, 111, 51))
        self.blur_btn.setStyleSheet("border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.blur_btn.setObjectName("blur_btn")
        self.bw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.bw_btn.setGeometry(QtCore.QRect(630, 20, 141, 51))
        self.bw_btn.setStyleSheet("border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.bw_btn.setObjectName("bw_btn")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(230, 90, 861, 551))
        self.image_label.setObjectName("image_label")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(960, 20, 141, 51))
        self.save_btn.setStyleSheet("background: #ac51fc;\n"
"border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.save_btn.setObjectName("save_btn")
        self.mirror_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mirror_btn.setGeometry(QtCore.QRect(780, 20, 141, 51))
        self.mirror_btn.setStyleSheet("border: 3px solid white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.mirror_btn.setObjectName("mirror_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1138, 34))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Editor"))
        self.folder_btn.setText(_translate("MainWindow", "Відкрити папку"))
        self.right_btn.setText(_translate("MainWindow", "Вправо"))
        self.left_btn.setText(_translate("MainWindow", "Влів"))
        self.blur_btn.setText(_translate("MainWindow", "Розмиття"))
        self.bw_btn.setText(_translate("MainWindow", "Чорно-білий"))
        self.image_label.setText(_translate("MainWindow", "Зображення"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.mirror_btn.setText(_translate("MainWindow", "Дзеркало"))
        self.menu.setTitle(_translate("MainWindow", "Редагувати"))
        self.action.setText(_translate("MainWindow", "Відкрити папку"))
        self.action_2.setText(_translate("MainWindow", "Зберегти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
