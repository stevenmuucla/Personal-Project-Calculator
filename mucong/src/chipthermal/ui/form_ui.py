# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QPalette)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QFormLayout,
                               QFrame, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(945, 789)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 439, 727))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_40 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_40)

        self.label = QLabel(self.scrollAreaWidgetContents_4)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lineEdit_Q = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Q.setObjectName(u"lineEdit_Q")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Q)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_Qt = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Qt.setObjectName(u"lineEdit_Qt")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_Qt)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_29)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_T0 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_T0.setObjectName(u"lineEdit_T0")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_T0)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_v0 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_v0.setObjectName(u"lineEdit_v0")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lineEdit_v0)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_26)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_a = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_a.setObjectName(u"lineEdit_a")

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.lineEdit_a)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_b = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_b.setObjectName(u"lineEdit_b")

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.lineEdit_b)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_h = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_h.setObjectName(u"lineEdit_h")

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.lineEdit_h)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_Tjmax = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Tjmax.setObjectName(u"lineEdit_Tjmax")

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.lineEdit_Tjmax)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_Rjc = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Rjc.setObjectName(u"lineEdit_Rjc")

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.lineEdit_Rjc)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_17)

        self.lineEdit_Rjb = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Rjb.setObjectName(u"lineEdit_Rjb")

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.lineEdit_Rjb)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.label_30)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_lambda = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_lambda.setObjectName(u"lineEdit_lambda")

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.lineEdit_lambda)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.label_15)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.label_28)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(19, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_A0 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_A0.setObjectName(u"lineEdit_A0")

        self.formLayout_2.setWidget(19, QFormLayout.FieldRole, self.lineEdit_A0)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_2.setWidget(20, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_lambda_b = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_lambda_b.setObjectName(u"lineEdit_lambda_b")

        self.formLayout_2.setWidget(20, QFormLayout.FieldRole, self.lineEdit_lambda_b)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_2.setWidget(21, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_hb = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_hb.setObjectName(u"lineEdit_hb")

        self.formLayout_2.setWidget(21, QFormLayout.FieldRole, self.lineEdit_hb)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_Ab = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Ab.setObjectName(u"lineEdit_Ab")

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.lineEdit_Ab)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(23, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_S = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_S.setObjectName(u"lineEdit_S")

        self.formLayout_2.setWidget(23, QFormLayout.FieldRole, self.lineEdit_S)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setEnabled(True)
        self.label_35.setLineWidth(1)

        self.verticalLayout_3.addWidget(self.label_35)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox2 = QCheckBox(self.frame_3)
        self.checkBox2.setObjectName(u"checkBox2")

        self.horizontalLayout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox(self.frame_3)
        self.checkBox3.setObjectName(u"checkBox3")

        self.horizontalLayout.addWidget(self.checkBox3)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 421, 509))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_44 = QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_44)

        self.lineEdit_h1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_h1.setObjectName(u"lineEdit_h1")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit_h1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_45)

        self.lineEdit_A1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_A1.setObjectName(u"lineEdit_A1")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_A1)

        self.label_46 = QLabel(self.scrollAreaWidgetContents)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_46)

        self.lineEdit_lambda1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_lambda1.setObjectName(u"lineEdit_lambda1")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.lineEdit_lambda1)

        self.label_47 = QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_47)

        self.lineEdit_hTIM1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_hTIM1.setObjectName(u"lineEdit_hTIM1")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEdit_hTIM1)

        self.label_48 = QLabel(self.scrollAreaWidgetContents)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_48)

        self.lineEdit_ATIM1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_ATIM1.setObjectName(u"lineEdit_ATIM1")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.lineEdit_ATIM1)

        self.label_49 = QLabel(self.scrollAreaWidgetContents)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_49)

        self.lineEdit_lambdaTIM1 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_lambdaTIM1.setObjectName(u"lineEdit_lambdaTIM1")

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.lineEdit_lambdaTIM1)

        self.label_50 = QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_5.setWidget(7, QFormLayout.LabelRole, self.label_50)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_5.setWidget(7, QFormLayout.FieldRole, self.lineEdit_11)

        self.label_51 = QLabel(self.scrollAreaWidgetContents)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_5.setWidget(8, QFormLayout.LabelRole, self.label_51)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_5.setWidget(8, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_52 = QLabel(self.scrollAreaWidgetContents)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_5.setWidget(9, QFormLayout.LabelRole, self.label_52)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_5.setWidget(9, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_53 = QLabel(self.scrollAreaWidgetContents)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_5.setWidget(10, QFormLayout.LabelRole, self.label_53)

        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_5.setWidget(10, QFormLayout.FieldRole, self.lineEdit_14)

        self.label_54 = QLabel(self.scrollAreaWidgetContents)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_5.setWidget(11, QFormLayout.LabelRole, self.label_54)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.formLayout_5.setWidget(11, QFormLayout.FieldRole, self.lineEdit_15)

        self.label_55 = QLabel(self.scrollAreaWidgetContents)
        self.label_55.setObjectName(u"label_55")

        self.formLayout_5.setWidget(12, QFormLayout.LabelRole, self.label_55)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.formLayout_5.setWidget(12, QFormLayout.FieldRole, self.lineEdit_16)

        self.label_56 = QLabel(self.scrollAreaWidgetContents)
        self.label_56.setObjectName(u"label_56")

        self.formLayout_5.setWidget(13, QFormLayout.LabelRole, self.label_56)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.formLayout_5.setWidget(13, QFormLayout.FieldRole, self.lineEdit_17)

        self.label_57 = QLabel(self.scrollAreaWidgetContents)
        self.label_57.setObjectName(u"label_57")

        self.formLayout_5.setWidget(14, QFormLayout.LabelRole, self.label_57)

        self.lineEdit_18 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.formLayout_5.setWidget(14, QFormLayout.FieldRole, self.lineEdit_18)

        self.label_58 = QLabel(self.scrollAreaWidgetContents)
        self.label_58.setObjectName(u"label_58")

        self.formLayout_5.setWidget(15, QFormLayout.LabelRole, self.label_58)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.formLayout_5.setWidget(15, QFormLayout.FieldRole, self.lineEdit_19)

        self.label_59 = QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_5.setWidget(16, QFormLayout.LabelRole, self.label_59)

        self.lineEdit_20 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.formLayout_5.setWidget(16, QFormLayout.FieldRole, self.lineEdit_20)

        self.label_60 = QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName(u"label_60")

        self.formLayout_5.setWidget(17, QFormLayout.LabelRole, self.label_60)

        self.lineEdit_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.formLayout_5.setWidget(17, QFormLayout.FieldRole, self.lineEdit_21)

        self.label_61 = QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName(u"label_61")

        self.formLayout_5.setWidget(18, QFormLayout.LabelRole, self.label_61)

        self.lineEdit_22 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.formLayout_5.setWidget(18, QFormLayout.FieldRole, self.lineEdit_22)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.comboBox)


        self.verticalLayout_4.addLayout(self.formLayout_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        palette = QPalette()
        brush = QBrush(QColor(190, 190, 190, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit.setPalette(palette)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_2.setPalette(palette1)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_22)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_3.setPalette(palette2)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_24)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_4.setPalette(palette3)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_5.setPalette(palette4)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_25)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_6.setPalette(palette5)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_31)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_7.setPalette(palette6)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lineEdit_7)

        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_32)

        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_8.setPalette(palette7)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_33)

        self.lineEdit_9 = QLineEdit(self.frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_9.setPalette(palette8)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_34 = QLabel(self.frame)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_34)

        self.lineEdit_10 = QLineEdit(self.frame)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.lineEdit_10.setPalette(palette9)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.lineEdit_10)


        self.verticalLayout_2.addLayout(self.formLayout_3)


        self.horizontalLayout_3.addWidget(self.frame)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"\u53d1\u70ed\u91cf\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u82af\u7247\u53d1\u70ed\u91cfQ(W)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5355\u5c42\u57fa\u677f\u4e0a\u6240\u6709\u82af\u7247\u7684\u603b\u53d1\u70ed\u91cfQ\u209c\uff08W\uff09", None))
        self.label_10.setText("")
        self.label_29.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u6761\u4ef6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u7a7a\u6c14\u6e29\u5ea6T\u2080\uff08\u2103\uff09", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7a7a\u6c14\u6765\u6d41\u901f\u5ea6v\u2080\uff08m/s\uff09", None))
        self.label_14.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7684\u8f93\u5165\u53c2\u6570\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u957fa\uff08mm\uff09", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u5bbdb\uff08mm\uff09", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u9ad8h\uff08mm\uff09", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7ed3\u8282\u7684\u6700\u9ad8\u8bb8\u7528\u6e29\u5ea6Tjmax\uff08\u2103\uff09", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7684\u7ed3\u8282-\u4e0a\u76d6\u70ed\u963bR\u2c7cc\uff08\u2103/W\uff09", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7684\u7ed3\u8282-\u57fa\u677f\u70ed\u963bR\u2c7cb\uff08\u2103/W\uff09", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"\u672a\u63d0\u4f9b2\u70ed\u963b\u7684\u60c5\u51b5\u4e0b\u9700\u63d0\u4f9b\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u6750\u6599\u70ed\u5bfc\u7387\u03bb\uff08W/m\u00b7\u2103\uff09", None))
        self.label_15.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u57fa\u677f\u7684\u8f93\u5165\u53c2\u6570\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u4e0e\u73af\u5883\u7a7a\u6c14\u63a5\u89e6\u7684\u8868\u9762\u79efA\u2080\uff08mm\u00b2\uff09", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u6750\u6599\u7684\u70ed\u5bfc\u7387\u03bbb\uff08W/m\u00b7K\uff09", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u7684\u539a\u5ea6hb\uff08mm\uff09", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u63a5\u89e6\u7a7a\u6c14\u7684\u8868\u9762\u79efAb\uff08mm\u00b2\uff09", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u8868\u9762\u79efS(mm\u00b2)", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checkBox2.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6750\u65992\u53ca\u754c\u9762\u6750\u65992", None))
        self.checkBox3.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6750\u65993\u53ca\u754c\u9762\u6750\u65993", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u7684\u539a\u5ea6h\u2081\uff08mm\uff09", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u7684\u5bfc\u70ed\u622a\u9762\u79efA\u2081\uff08mm\u00b2\uff09", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u7684\u70ed\u5bfc\u7387\u03bb\u2081\uff08W/m\u00b7K\uff09", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c421\u7684\u539a\u5ea6htim\u2081\uff08mm\uff09", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c421\u5185\u4fa7\u7684\u63a5\u89e6\u9762\u79efAtim\u2081\uff08mm\u00b2\uff09", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65991\u7684\u70ed\u5bfc\u7387\u03bbtim\u2081\uff08W/m\u00b7K\uff09", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u7684\u539a\u5ea6h\u2082\uff08mm\uff09", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u7684\u5bfc\u70ed\u622a\u9762\u79efA\u2082\uff08mm\u00b2\uff09", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u7684\u70ed\u5bfc\u7387\u03bb\u2082\uff08W/m\u00b7K\uff09", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c422\u7684\u539a\u5ea6htim\u2082\uff08mm\uff09", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c422\u5185\u4fa7\u7684\u63a5\u89e6\u9762\u79efAtim\u2082\uff08mm\u00b2\uff09", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65992\u7684\u70ed\u5bfc\u7387\u03bbtim\u2082\uff08W/m\u00b7K\uff09", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u7684\u539a\u5ea6h\u2083\uff08mm\uff09", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u7684\u5bfc\u70ed\u622a\u9762\u79efA\u2083\uff08mm\u00b2\uff09", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u7684\u70ed\u5bfc\u7387\u03bb\u2083\uff08W/m\u00b7K\uff09", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c423\u7684\u539a\u5ea6htim\u2083\uff08mm\uff09", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c423\u5185\u4fa7\u7684\u63a5\u89e6\u9762\u79efAtim\u2083\uff08mm\u00b2\uff09", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65993\u7684\u70ed\u5bfc\u7387\u03bbtim\u2083\uff08W/m\u00b7K\uff09", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u9ed8\u8ba4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6750\u65991", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u6750\u65992", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))

        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5c06\u5386\u53f2\u7ed3\u679c\u5bfc\u51fa\u4e3aexcel\u6587\u4ef6", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u63a5\u89e6\u73af\u5883\u7a7a\u6c14\u7684\u6750\u65991\u8868\u9762\u6e29\u5ea6T\u2081\u208b\u2080 \uff08\u2103\uff09", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u4e0e\u754c\u9762\u6750\u65991\u63a5\u89e6\u9762\u6e29\u5ea6Ttim\u2081\u208b\u2081 \uff08\u2103\uff09", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u4e0e\u754c\u9762\u6750\u65991\u63a5\u89e6\u9762\u6e29\u5ea6T\u2082\u208btim\u2081\uff08\u2103\uff09", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65992\u4e0e\u6750\u65992\u63a5\u89e6\u9762\u6e29\u5ea6Ttim\u2082\u208b\u2082 \uff08\u2103\uff09", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u4e0e\u754c\u9762\u6750\u65992\u63a5\u89e6\u9762\u6e29\u5ea6T\u2083\u208btim\u2082\uff08\u2103\uff09", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65993\u4e0e\u6750\u65993\u63a5\u89e6\u9762\u6e29\u5ea6Ttim\u2083\u208b\u2083\uff08\u2103\uff09", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u58f3\u4f53\u4e0a\u8868\u9762\u6e29\u5ea6Tc\uff08\u2103\uff09", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7ed3\u8282\u6e29\u5ea6\u8ba1\u7b97\u503cT\u2c7c\uff08\u2103\uff09", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u4e0e\u82af\u7247\u63a5\u89e6\u9762\u7684\u6e29\u5ea6T\u2c7c\u208bb\uff08\u2103\uff09", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u63a5\u89e6\u7a7a\u6c14\u7684\u4e0b\u8868\u9762\u6e29\u5ea6Tb\u208b\u2080\uff08\u2103\uff09", None))
    # retranslateUi

