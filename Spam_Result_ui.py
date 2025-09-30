# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Spam_Result.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Result(object):
    def setupUi(self, Result):
        if not Result.objectName():
            Result.setObjectName(u"Result")
        Result.resize(627, 364)
        self.gridLayout = QGridLayout(Result)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Result)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Sans Serif Collection"])
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 0, 4);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.Confidence = QLabel(self.groupBox)
        self.Confidence.setObjectName(u"Confidence")
        font1 = QFont()
        font1.setPointSize(28)
        self.Confidence.setFont(font1)

        self.verticalLayout.addWidget(self.Confidence)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Result)

        QMetaObject.connectSlotsByName(Result)
    # setupUi

    def retranslateUi(self, Result):
        Result.setWindowTitle(QCoreApplication.translate("Result", u"Result", None))
        self.groupBox.setTitle(QCoreApplication.translate("Result", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("Result", u"This message is a spam ", None))
        self.Confidence.setText(QCoreApplication.translate("Result", u"Confidence Level:", None))
    # retranslateUi

