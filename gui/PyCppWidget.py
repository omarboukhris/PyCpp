# Form implementation generated from reading ui file 'pycpp_template.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_pyCppGui(object):
    def setupUi(self, pyCppGui):
        pyCppGui.setObjectName("pyCppGui")
        pyCppGui.resize(601, 551)
        self.gridLayout_2 = QtWidgets.QGridLayout(pyCppGui)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(pyCppGui)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cgw_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.cgw_checkBox.setObjectName("cgw_checkBox")
        self.gridLayout_3.addWidget(self.cgw_checkBox, 0, 0, 1, 1)
        self.pygw_checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.pygw_checkBox.setEnabled(False)
        self.pygw_checkBox.setObjectName("pygw_checkBox")
        self.gridLayout_3.addWidget(self.pygw_checkBox, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 3, 1, 3)
        self.gencode_pushButton = QtWidgets.QPushButton(pyCppGui)
        self.gencode_pushButton.setObjectName("gencode_pushButton")
        self.gridLayout_2.addWidget(self.gencode_pushButton, 5, 2, 1, 3)
        self.progressBar = QtWidgets.QProgressBar(pyCppGui)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 6, 0, 1, 6)
        self.groupBox = QtWidgets.QGroupBox(pyCppGui)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.x_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.x_radioButton.setObjectName("x_radioButton")
        self.gridLayout.addWidget(self.x_radioButton, 3, 0, 1, 1)
        self.so_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.so_radioButton.setChecked(False)
        self.so_radioButton.setObjectName("so_radioButton")
        self.gridLayout.addWidget(self.so_radioButton, 1, 0, 1, 1)
        self.static_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.static_radioButton.setChecked(True)
        self.static_radioButton.setObjectName("static_radioButton")
        self.gridLayout.addWidget(self.static_radioButton, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 3)
        self.getfolder_pushButton = QtWidgets.QPushButton(pyCppGui)
        self.getfolder_pushButton.setObjectName("getfolder_pushButton")
        self.gridLayout_2.addWidget(self.getfolder_pushButton, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(pyCppGui)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.globex_lineEdit = QtWidgets.QLineEdit(pyCppGui)
        self.globex_lineEdit.setObjectName("globex_lineEdit")
        self.gridLayout_2.addWidget(self.globex_lineEdit, 2, 1, 1, 5)
        self.close_pushButton = QtWidgets.QPushButton(pyCppGui)
        self.close_pushButton.setObjectName("close_pushButton")
        self.gridLayout_2.addWidget(self.close_pushButton, 5, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(pyCppGui)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.rootfolder_lineEdit = QtWidgets.QLineEdit(pyCppGui)
        self.rootfolder_lineEdit.setEnabled(True)
        self.rootfolder_lineEdit.setObjectName("rootfolder_lineEdit")
        self.gridLayout_2.addWidget(self.rootfolder_lineEdit, 1, 1, 1, 5)
        self.groupBox_3 = QtWidgets.QGroupBox(pyCppGui)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.cppver_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.cppver_comboBox.setObjectName("cppver_comboBox")
        self.cppver_comboBox.addItem("")
        self.cppver_comboBox.addItem("")
        self.cppver_comboBox.addItem("")
        self.cppver_comboBox.addItem("")
        self.gridLayout_4.addWidget(self.cppver_comboBox, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.cmkver_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.cmkver_lineEdit.setObjectName("cmkver_lineEdit")
        self.gridLayout_4.addWidget(self.cmkver_lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.buildtype_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.buildtype_comboBox.setObjectName("buildtype_comboBox")
        self.buildtype_comboBox.addItem("")
        self.buildtype_comboBox.addItem("")
        self.gridLayout_4.addWidget(self.buildtype_comboBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.relflg_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.relflg_lineEdit.setObjectName("relflg_lineEdit")
        self.gridLayout_4.addWidget(self.relflg_lineEdit, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)
        self.dbgflg_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.dbgflg_lineEdit.setObjectName("dbgflg_lineEdit")
        self.gridLayout_4.addWidget(self.dbgflg_lineEdit, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 5, 0, 1, 1)
        self.libs_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.libs_lineEdit.setObjectName("libs_lineEdit")
        self.gridLayout_4.addWidget(self.libs_lineEdit, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 4, 0, 1, 6)
        self.projectname_lineEdit = QtWidgets.QLineEdit(pyCppGui)
        self.projectname_lineEdit.setObjectName("projectname_lineEdit")
        self.gridLayout_2.addWidget(self.projectname_lineEdit, 0, 1, 1, 5)
        self.label_9 = QtWidgets.QLabel(pyCppGui)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.status_label = QtWidgets.QLabel(pyCppGui)
        self.status_label.setObjectName("status_label")
        self.gridLayout_2.addWidget(self.status_label, 7, 0, 1, 6)

        self.retranslateUi(pyCppGui)
        self.cgw_checkBox.clicked['bool'].connect(self.pygw_checkBox.setEnabled)
        self.so_radioButton.clicked['bool'].connect(self.groupBox_2.setEnabled)
        self.static_radioButton.clicked['bool'].connect(self.groupBox_2.setDisabled)
        self.x_radioButton.clicked['bool'].connect(self.groupBox_2.setDisabled)
        self.close_pushButton.clicked.connect(pyCppGui.close)
        QtCore.QMetaObject.connectSlotsByName(pyCppGui)
        pyCppGui.setTabOrder(self.projectname_lineEdit, self.rootfolder_lineEdit)
        pyCppGui.setTabOrder(self.rootfolder_lineEdit, self.globex_lineEdit)
        pyCppGui.setTabOrder(self.globex_lineEdit, self.static_radioButton)
        pyCppGui.setTabOrder(self.static_radioButton, self.so_radioButton)
        pyCppGui.setTabOrder(self.so_radioButton, self.x_radioButton)
        pyCppGui.setTabOrder(self.x_radioButton, self.cgw_checkBox)
        pyCppGui.setTabOrder(self.cgw_checkBox, self.pygw_checkBox)
        pyCppGui.setTabOrder(self.pygw_checkBox, self.cppver_comboBox)
        pyCppGui.setTabOrder(self.cppver_comboBox, self.cmkver_lineEdit)
        pyCppGui.setTabOrder(self.cmkver_lineEdit, self.buildtype_comboBox)
        pyCppGui.setTabOrder(self.buildtype_comboBox, self.relflg_lineEdit)
        pyCppGui.setTabOrder(self.relflg_lineEdit, self.dbgflg_lineEdit)
        pyCppGui.setTabOrder(self.dbgflg_lineEdit, self.libs_lineEdit)
        pyCppGui.setTabOrder(self.libs_lineEdit, self.getfolder_pushButton)
        pyCppGui.setTabOrder(self.getfolder_pushButton, self.gencode_pushButton)
        pyCppGui.setTabOrder(self.gencode_pushButton, self.close_pushButton)

    def retranslateUi(self, pyCppGui):
        _translate = QtCore.QCoreApplication.translate
        pyCppGui.setWindowTitle(_translate("pyCppGui", "PyCpp GUI"))
        self.groupBox_2.setTitle(_translate("pyCppGui", "Gateway options"))
        self.cgw_checkBox.setText(_translate("pyCppGui", "C gateway"))
        self.pygw_checkBox.setText(_translate("pyCppGui", "Py gateway"))
        self.gencode_pushButton.setText(_translate("pyCppGui", "Generate Code"))
        self.groupBox.setTitle(_translate("pyCppGui", "Project type"))
        self.x_radioButton.setText(_translate("pyCppGui", "Executable"))
        self.so_radioButton.setText(_translate("pyCppGui", "Shared Object"))
        self.static_radioButton.setText(_translate("pyCppGui", "Static Library"))
        self.getfolder_pushButton.setText(_translate("pyCppGui", "Select Folder"))
        self.label.setText(_translate("pyCppGui", "Root folder"))
        self.globex_lineEdit.setText(_translate("pyCppGui", "*.cxx"))
        self.close_pushButton.setText(_translate("pyCppGui", "Close"))
        self.label_2.setText(_translate("pyCppGui", "Glob regex"))
        self.groupBox_3.setTitle(_translate("pyCppGui", "CMake param"))
        self.label_7.setText(_translate("pyCppGui", "C++ version"))
        self.cppver_comboBox.setCurrentText(_translate("pyCppGui", "11"))
        self.cppver_comboBox.setItemText(0, _translate("pyCppGui", "11"))
        self.cppver_comboBox.setItemText(1, _translate("pyCppGui", "14"))
        self.cppver_comboBox.setItemText(2, _translate("pyCppGui", "17"))
        self.cppver_comboBox.setItemText(3, _translate("pyCppGui", "20"))
        self.label_6.setText(_translate("pyCppGui", "CMake min version"))
        self.cmkver_lineEdit.setText(_translate("pyCppGui", "3.5"))
        self.label_3.setText(_translate("pyCppGui", "Build type"))
        self.buildtype_comboBox.setItemText(0, _translate("pyCppGui", "Release"))
        self.buildtype_comboBox.setItemText(1, _translate("pyCppGui", "Debug"))
        self.label_4.setText(_translate("pyCppGui", "Release flags"))
        self.relflg_lineEdit.setText(_translate("pyCppGui", "-O2"))
        self.label_5.setText(_translate("pyCppGui", "Debug flags"))
        self.dbgflg_lineEdit.setText(_translate("pyCppGui", "-g"))
        self.label_8.setText(_translate("pyCppGui", "Libraries"))
        self.label_9.setText(_translate("pyCppGui", "Project name"))
        self.status_label.setText(_translate("pyCppGui", "status: idle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pyCppGui = QtWidgets.QWidget()
    ui = Ui_pyCppGui()
    ui.setupUi(pyCppGui)
    pyCppGui.show()
    sys.exit(app.exec())
