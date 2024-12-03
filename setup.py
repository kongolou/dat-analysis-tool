# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupgdGNmZ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QComboBox,
    QDialogButtonBox,
    QLabel,
    QSpinBox,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        icon = QIcon()
        icon.addFile("dat-logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(40, 110, 91, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(40, 60, 91, 31))
        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setGeometry(QRect(140, 110, 141, 31))
        self.spinBox.setMinimum(1)
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(140, 60, 141, 31))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.comboBox.addItems(["K-Means"])  # my code

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Cluster Setup", None)
        )
        self.label.setText(
            QCoreApplication.translate("Dialog", "Cluster Number:", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("Dialog", "Cluster Method:", None)
        )
        self.comboBox.setCurrentText("")

    # retranslateUi
