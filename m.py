# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(429, 224)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setBaseSize(QtCore.QSize(0, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.cb_record_name = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_record_name.sizePolicy().hasHeightForWidth())
        self.cb_record_name.setSizePolicy(sizePolicy)
        self.cb_record_name.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_record_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cb_record_name.setBaseSize(QtCore.QSize(0, 25))
        self.cb_record_name.setEditable(True)
        self.cb_record_name.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.cb_record_name.setObjectName(_fromUtf8("cb_record_name"))
        self.horizontalLayout.addWidget(self.cb_record_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setBaseSize(QtCore.QSize(0, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cb_record_state = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_record_state.sizePolicy().hasHeightForWidth())
        self.cb_record_state.setSizePolicy(sizePolicy)
        self.cb_record_state.setMinimumSize(QtCore.QSize(200, 0))
        self.cb_record_state.setMaximumSize(QtCore.QSize(16777215, 25))
        self.cb_record_state.setBaseSize(QtCore.QSize(0, 25))
        self.cb_record_state.setEditable(True)
        self.cb_record_state.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.cb_record_state.setObjectName(_fromUtf8("cb_record_state"))
        self.horizontalLayout_2.addWidget(self.cb_record_state)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.btnRecordToday = QtGui.QPushButton(Dialog)
        self.btnRecordToday.setObjectName(_fromUtf8("btnRecordToday"))
        self.horizontalLayout_3.addWidget(self.btnRecordToday)
        self.de_record_date = QtGui.QDateEdit(Dialog)
        self.de_record_date.setMinimumSize(QtCore.QSize(200, 0))
        self.de_record_date.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.de_record_date.setCalendarPopup(True)
        self.de_record_date.setObjectName(_fromUtf8("de_record_date"))
        self.horizontalLayout_3.addWidget(self.de_record_date)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.cb_record_name, self.cb_record_state)
        Dialog.setTabOrder(self.cb_record_state, self.de_record_date)
        Dialog.setTabOrder(self.de_record_date, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "项目进度记录", None))
        self.label_4.setText(_translate("Dialog", "外委项目进度记录小工具", None))
        self.label_2.setText(_translate("Dialog", "项目名称：", None))
        self.label_3.setText(_translate("Dialog", "项目进度：", None))
        self.label.setText(_translate("Dialog", "进度完成时间：", None))
        self.btnRecordToday.setText(_translate("Dialog", "今天", None))
        self.de_record_date.setDisplayFormat(_translate("Dialog", "yyyy-M-d", None))

