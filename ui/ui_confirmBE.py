# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmBE.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(20)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.BEId = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BEId.sizePolicy().hasHeightForWidth())
        self.BEId.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(20)
        self.BEId.setFont(font)
        self.BEId.setStyleSheet("background-color: transparent;\n"
"border-color: none;\n"
"border: none;\n"
"border-bottom: none;\n"
"color: rgb(0, 0, 0);")
        self.BEId.setObjectName("BEId")
        self.verticalLayout_4.addWidget(self.BEId, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_8 = QtWidgets.QWidget(self.widget_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.widget_8)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_17.addWidget(self.label_3)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.widget_8)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Requester = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.Requester.setFont(font)
        self.Requester.setReadOnly(True)
        self.Requester.setObjectName("Requester")
        self.verticalLayout_18.addWidget(self.Requester)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_5.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.widget_3)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_15.addWidget(self.label_4)
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.widget_7)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.frame_8.setFont(font)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.creationDate = QtWidgets.QLineEdit(self.frame_8)
        self.creationDate.setReadOnly(True)
        self.creationDate.setObjectName("creationDate")
        self.verticalLayout_16.addWidget(self.creationDate)
        self.horizontalLayout_6.addWidget(self.frame_8)
        self.verticalLayout_5.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget_3)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_9 = QtWidgets.QFrame(self.widget_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_14.addWidget(self.label_5)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.widget_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.duedate = QtWidgets.QLineEdit(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.duedate.setFont(font)
        self.duedate.setReadOnly(True)
        self.duedate.setObjectName("duedate")
        self.verticalLayout_13.addWidget(self.duedate)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.widget_9 = QtWidgets.QWidget(self.widget_3)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_13 = QtWidgets.QFrame(self.widget_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_19.addWidget(self.label_7)
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.widget_9)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.staff = QtWidgets.QLineEdit(self.frame_14)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.staff.setFont(font)
        self.staff.setObjectName("staff")
        self.verticalLayout_20.addWidget(self.staff)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.verticalLayout_5.addWidget(self.widget_9)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_11 = QtWidgets.QWidget(self.widget_4)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ItemTable = QtWidgets.QTableWidget(self.widget_11)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(10)
        self.ItemTable.setFont(font)
        self.ItemTable.setObjectName("ItemTable")
        self.ItemTable.setColumnCount(4)
        self.ItemTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ItemTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ItemTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ItemTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ItemTable.setHorizontalHeaderItem(3, item)
        self.ItemTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_8.addWidget(self.ItemTable)
        self.verticalLayout_7.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.widget_12)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.widget_12)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.invoiceTotal = QtWidgets.QLineEdit(self.frame_4)
        self.invoiceTotal.setObjectName("invoiceTotal")
        self.verticalLayout_10.addWidget(self.invoiceTotal)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_7.addWidget(self.widget_12)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.confirmButton = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(11)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.verticalLayout_6.addWidget(self.confirmButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "| CONFRIM BUYING ENTRY #"))
        self.label_3.setText(_translate("MainWindow", "Requester"))
        self.label_4.setText(_translate("MainWindow", "Creation date"))
        self.label_5.setText(_translate("MainWindow", "Expected due date\""))
        self.label_7.setText(_translate("MainWindow", "Receiving Clerk"))
        item = self.ItemTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.ItemTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.ItemTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.ItemTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Real Amount"))
        self.label_2.setText(_translate("MainWindow", "Invoice total"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
