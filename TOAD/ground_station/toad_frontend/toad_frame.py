# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toad_frame.ui'
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

class Ui_toad_frame(object):
    def setupUi(self, toad_frame):
        toad_frame.setObjectName(_fromUtf8("toad_frame"))
        toad_frame.resize(276, 581)
        toad_frame.setMinimumSize(QtCore.QSize(276, 0))
        toad_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        toad_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(toad_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_ranging = QtGui.QFormLayout()
        self.formLayout_ranging.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.formLayout_ranging.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_ranging.setObjectName(_fromUtf8("formLayout_ranging"))
        self.label_ranging_title = QtGui.QLabel(toad_frame)
        self.label_ranging_title.setMaximumSize(QtCore.QSize(640, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_ranging_title.setFont(font)
        self.label_ranging_title.setObjectName(_fromUtf8("label_ranging_title"))
        self.formLayout_ranging.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_ranging_title)
        self.label_timestamp = QtGui.QLabel(toad_frame)
        self.label_timestamp.setObjectName(_fromUtf8("label_timestamp"))
        self.formLayout_ranging.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_timestamp)
        self.lineEdit_timestamp = QtGui.QLineEdit(toad_frame)
        self.lineEdit_timestamp.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit_timestamp.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_timestamp.setReadOnly(True)
        self.lineEdit_timestamp.setObjectName(_fromUtf8("lineEdit_timestamp"))
        self.formLayout_ranging.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_timestamp)
        self.label_timestamp_itow = QtGui.QLabel(toad_frame)
        self.label_timestamp_itow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_timestamp_itow.setIndent(25)
        self.label_timestamp_itow.setObjectName(_fromUtf8("label_timestamp_itow"))
        self.formLayout_ranging.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_timestamp_itow)
        self.lineEdit_timestamp_itow = QtGui.QLineEdit(toad_frame)
        self.lineEdit_timestamp_itow.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit_timestamp_itow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_timestamp_itow.setReadOnly(True)
        self.lineEdit_timestamp_itow.setObjectName(_fromUtf8("lineEdit_timestamp_itow"))
        self.formLayout_ranging.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_timestamp_itow)
        self.label_timestamp_systicks = QtGui.QLabel(toad_frame)
        self.label_timestamp_systicks.setIndent(25)
        self.label_timestamp_systicks.setObjectName(_fromUtf8("label_timestamp_systicks"))
        self.formLayout_ranging.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_timestamp_systicks)
        self.lineEdit_timestamp_systicks = QtGui.QLineEdit(toad_frame)
        self.lineEdit_timestamp_systicks.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit_timestamp_systicks.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_timestamp_systicks.setReadOnly(True)
        self.lineEdit_timestamp_systicks.setObjectName(_fromUtf8("lineEdit_timestamp_systicks"))
        self.formLayout_ranging.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_timestamp_systicks)
        self.label_tof = QtGui.QLabel(toad_frame)
        self.label_tof.setWordWrap(True)
        self.label_tof.setObjectName(_fromUtf8("label_tof"))
        self.formLayout_ranging.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_tof)
        self.lineEdit_tof = QtGui.QLineEdit(toad_frame)
        self.lineEdit_tof.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit_tof.setReadOnly(True)
        self.lineEdit_tof.setObjectName(_fromUtf8("lineEdit_tof"))
        self.formLayout_ranging.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_tof)
        self.label_timerfreq = QtGui.QLabel(toad_frame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_timerfreq.setFont(font)
        self.label_timerfreq.setIndent(25)
        self.label_timerfreq.setObjectName(_fromUtf8("label_timerfreq"))
        self.formLayout_ranging.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_timerfreq)
        self.spinBox_timerfreq = QtGui.QSpinBox(toad_frame)
        self.spinBox_timerfreq.setMaximumSize(QtCore.QSize(500, 16777215))
        self.spinBox_timerfreq.setMaximum(99999999)
        self.spinBox_timerfreq.setSingleStep(1000)
        self.spinBox_timerfreq.setProperty("value", 84000000)
        self.spinBox_timerfreq.setObjectName(_fromUtf8("spinBox_timerfreq"))
        self.formLayout_ranging.setWidget(5, QtGui.QFormLayout.FieldRole, self.spinBox_timerfreq)
        self.label_distance = QtGui.QLabel(toad_frame)
        self.label_distance.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_distance.setIndent(25)
        self.label_distance.setObjectName(_fromUtf8("label_distance"))
        self.formLayout_ranging.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_distance)
        self.lineEdit_distance = QtGui.QLineEdit(toad_frame)
        self.lineEdit_distance.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEdit_distance.setReadOnly(True)
        self.lineEdit_distance.setObjectName(_fromUtf8("lineEdit_distance"))
        self.formLayout_ranging.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_distance)
        self.verticalLayout.addLayout(self.formLayout_ranging)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_pos = QtGui.QLabel(toad_frame)
        self.label_pos.setMaximumSize(QtCore.QSize(640, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_pos.setFont(font)
        self.label_pos.setObjectName(_fromUtf8("label_pos"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_pos)
        self.label_2 = QtGui.QLabel(toad_frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(toad_frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(toad_frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(toad_frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(toad_frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(toad_frame)
        QtCore.QMetaObject.connectSlotsByName(toad_frame)

    def retranslateUi(self, toad_frame):
        toad_frame.setWindowTitle(_translate("toad_frame", "toad_frame_window", None))
        self.label_ranging_title.setText(_translate("toad_frame", "Ranging", None))
        self.label_timestamp.setText(_translate("toad_frame", "Timestamp", None))
        self.label_timestamp_itow.setText(_translate("toad_frame", "(ITOW)", None))
        self.label_timestamp_systicks.setText(_translate("toad_frame", "(systicks)", None))
        self.label_tof.setText(_translate("toad_frame", "Time of flight (timer register)", None))
        self.label_timerfreq.setText(_translate("toad_frame", "Enter timer freq:", None))
        self.spinBox_timerfreq.setSuffix(_translate("toad_frame", "Hz", None))
        self.label_distance.setText(_translate("toad_frame", "Distance/m", None))
        self.label_pos.setText(_translate("toad_frame", "Position and Health", None))
        self.label_2.setText(_translate("toad_frame", "TextLabel", None))
        self.label_3.setText(_translate("toad_frame", "TextLabel", None))
        self.label_4.setText(_translate("toad_frame", "TextLabel", None))
        self.label_5.setText(_translate("toad_frame", "TextLabel", None))
        self.label_6.setText(_translate("toad_frame", "TextLabel", None))


class toad_frame(QtGui.QFrame, Ui_toad_frame):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QFrame.__init__(self, parent, f)

        self.setupUi(self)

