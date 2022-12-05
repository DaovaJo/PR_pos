# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwind.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(1350, 537)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setStyleSheet(u"QFrame{\n"
"	background-color: #fff;\n"
"	border: 0.5px solid #52B7D8;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding-left: 15px;\n"
"	background: #D0E4EB;\n"
"	border-radius: 15px;\n"
"\n"
"	font-family: 'Inter';\n"
"	font-style: normal;\n"
"	font-size: 16px;\n"
"	line-height: 27px;\n"
"}\n"
"\n"
"QLabel{\n"
"	border: solid 1px #73C8F0;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background: #52B7D8;\n"
"	border-radius: 25px;\n"
"\n"
"	font-family: 'Inter';\n"
"	font-style: normal;\n"
"	font-weight: 700;\n"
"	font-size: 22px;\n"
"	line-height: 27px;\n"
"	/* identical to box height */\n"
"\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: rgb(24,90,112);\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(-10, -10, 1934, 1091))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.group = QFrame(self.widget1)
        self.group.setObjectName(u"group")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group.sizePolicy().hasHeightForWidth())
        self.group.setSizePolicy(sizePolicy)
        self.group.setMinimumSize(QSize(1370, 540))
        self.group.setMaximumSize(QSize(1370, 540))
        self.group.setStyleSheet(u"")
        self.group.setFrameShape(QFrame.StyledPanel)
        self.group.setFrameShadow(QFrame.Raised)
        self.widget2 = QWidget(self.group)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(553, 10, 791, 271))
        self.gridLayout_2 = QGridLayout(self.widget2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(35, 32))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u"object/\u0434\u043e\u043f \u043f\u0430\u0440.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(32, 35))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)

        self.gridLayout_2.addWidget(self.pushButton_6, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.widget2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setMinimumSize(QSize(0, 0))
        self.pushButton_5.setMaximumSize(QSize(500, 22))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"background: #fff;\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 18px;\n"
"line-height: 22px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #014E1F;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #12D460;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_23 = QLabel(self.widget2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(72, 25))

        self.verticalLayout_7.addWidget(self.label_23)

        self.label_20 = QLabel(self.widget2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(72, 25))

        self.verticalLayout_7.addWidget(self.label_20)

        self.label_24 = QLabel(self.widget2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(72, 25))

        self.verticalLayout_7.addWidget(self.label_24)


        self.gridLayout_2.addLayout(self.verticalLayout_7, 3, 3, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_21 = QLabel(self.widget2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)
        self.label_21.setMinimumSize(QSize(72, 25))
        self.label_21.setMaximumSize(QSize(72, 25))
        self.label_21.setStyleSheet(u"background-color:#E16032;")

        self.verticalLayout_6.addWidget(self.label_21)

        self.label_19 = QLabel(self.widget2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(72, 25))
        self.label_19.setMaximumSize(QSize(72, 25))
        self.label_19.setStyleSheet(u"background-color:#52B7D8;")

        self.verticalLayout_6.addWidget(self.label_19)

        self.label_22 = QLabel(self.widget2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(72, 25))
        self.label_22.setMaximumSize(QSize(72, 25))
        self.label_22.setStyleSheet(u"background-color: #F6AF39;")

        self.verticalLayout_6.addWidget(self.label_22)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 3, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_16 = QLabel(self.widget2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 22px;\n"
"line-height: 27px;\n"
"\n"
"\n"
"\n"
"color: #005774;")
        self.label_16.setFrameShape(QFrame.NoFrame)
        self.label_16.setFrameShadow(QFrame.Plain)
        self.label_16.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_5.addWidget(self.label_16)

        self.label_18 = QLabel(self.widget2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"color: rgba(0, 0, 0, 0.6);")
        self.label_18.setFrameShape(QFrame.NoFrame)
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_18.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_5.addWidget(self.label_18)

        self.label_17 = QLabel(self.widget2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"\n"
"")
        self.label_17.setFrameShape(QFrame.NoFrame)
        self.label_17.setFrameShadow(QFrame.Plain)
        self.label_17.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_5.addWidget(self.label_17)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 3, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.gridLayout_2.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.widget3 = QWidget(self.group)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(30, 20, 521, 511))
        self.verticalLayout = QVBoxLayout(self.widget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_gr = QLineEdit(self.widget3)
        self.search_gr.setObjectName(u"search_gr")
        self.search_gr.setMinimumSize(QSize(0, 34))

        self.verticalLayout.addWidget(self.search_gr)

        self.label_15 = QLabel(self.widget3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setPixmap(QPixmap(u"object/\u043a\u0440\u0443\u0433\u043e\u0432\u043e\u0439 \u0438\u043d\u0434\u0435\u043a\u0430\u0442\u043e\u0440.png"))

        self.verticalLayout.addWidget(self.label_15)

        self.widget4 = QWidget(self.group)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(890, 310, 456, 161))
        self.verticalLayout_9 = QVBoxLayout(self.widget4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(454, 72))

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_25 = QLabel(self.widget4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setLayoutDirection(Qt.LeftToRight)
        self.label_25.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"\n"
"")
        self.label_25.setFrameShape(QFrame.NoFrame)
        self.label_25.setFrameShadow(QFrame.Plain)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_25.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout.addWidget(self.label_25)

        self.pushButton_7 = QPushButton(self.widget4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 0))
        self.pushButton_7.setMaximumSize(QSize(84, 43))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"border-radius: 20px;\n"
"background-color: #12D460;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #027731;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout)


        self.verticalLayout_11.addWidget(self.group)

        self.potok = QFrame(self.widget1)
        self.potok.setObjectName(u"potok")
        self.potok.setMinimumSize(QSize(1370, 540))
        self.potok.setStyleSheet(u"")
        self.potok.setFrameShape(QFrame.StyledPanel)
        self.potok.setFrameShadow(QFrame.Raised)
        self.widget5 = QWidget(self.potok)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(0, 10, 1345, 476))
        self.gridLayout = QGridLayout(self.widget5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_4 = QRadioButton(self.widget5)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 27px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #000000;")

        self.verticalLayout_2.addWidget(self.radioButton_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 7, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.widget5)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 27px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #000000;")

        self.gridLayout.addWidget(self.radioButton_3, 1, 2, 1, 1)

        self.label_27 = QLabel(self.widget5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 22px;\n"
"line-height: 27px;\n"
"\n"
"\n"
"\n"
"color: #005774;")
        self.label_27.setFrameShape(QFrame.NoFrame)
        self.label_27.setFrameShadow(QFrame.Plain)
        self.label_27.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.label_27, 0, 2, 1, 1)

        self.label_26 = QLabel(self.widget5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u"object/\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u043a\u0443\u0440\u0441\u044b.png"))

        self.gridLayout.addWidget(self.label_26, 8, 0, 3, 3)


        self.verticalLayout_11.addWidget(self.potok)


        self.horizontalLayout_2.addLayout(self.verticalLayout_11)

        self.student = QFrame(self.widget1)
        self.student.setObjectName(u"student")
        sizePolicy2.setHeightForWidth(self.student.sizePolicy().hasHeightForWidth())
        self.student.setSizePolicy(sizePolicy2)
        self.student.setMinimumSize(QSize(0, 0))
        self.student.setMaximumSize(QSize(8000, 8000))
        self.student.setStyleSheet(u"")
        self.student.setFrameShape(QFrame.StyledPanel)
        self.student.setFrameShadow(QFrame.Raised)
        self.widget6 = QWidget(self.student)
        self.widget6.setObjectName(u"widget6")
        self.widget6.setGeometry(QRect(20, 20, 521, 941))
        self.verticalLayout_4 = QVBoxLayout(self.widget6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_std = QLineEdit(self.widget6)
        self.search_std.setObjectName(u"search_std")
        self.search_std.setMinimumSize(QSize(509, 34))
        self.search_std.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout_4.addWidget(self.search_std)

        self.pushButton_2 = QPushButton(self.widget6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(35, 32))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(32, 35))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"\n"
"color: rgba(0, 0, 0, 0.6);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.widget6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 22px;\n"
"line-height: 27px;\n"
"\n"
"\n"
"\n"
"color: #005774;")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"\n"
"")
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"\n"
"")
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"color: rgba(0, 0, 0, 0.6);")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_3.addWidget(self.label_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.label_6 = QLabel(self.widget6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(451, 375))
        self.label_6.setPixmap(QPixmap(u"object/\u043a\u0440\u0443\u0433\u043e\u0432\u043e\u0439 \u0438\u043d\u0434\u0435\u043a\u0430\u0442\u043e\u0440.png"))

        self.verticalLayout_4.addWidget(self.label_6)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(self.widget6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(72, 25))
        self.label_7.setStyleSheet(u"background-color:#E16032;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.label_10 = QLabel(self.widget6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(72, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_10)

        self.label_8 = QLabel(self.widget6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(72, 25))
        self.label_8.setStyleSheet(u"background-color:#52B7D8;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_11 = QLabel(self.widget6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(72, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_11)

        self.label_9 = QLabel(self.widget6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(72, 25))
        self.label_9.setStyleSheet(u"background-color: #F6AF39;")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.label_12 = QLabel(self.widget6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(72, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_12)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.pushButton = QPushButton(self.widget6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(454, 72))

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.student)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u044d\u043a\u0441\u043f\u043b\u0443\u0430\u0442\u0430\u0446\u0438\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u0431\u0435\u0437 \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"-- \u043f\u0440\u0438\u0441\u0442\u0443\u0441\u0442\u0432\u0438\u0435 \u043d\u0430 \u043f\u0430\u0440\u0435 ", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u043f\u043e \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.label_21.setText("")
        self.label_19.setText("")
        self.label_22.setText("")
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("Form", u"\u0418\u0414 23.2/\u04112-20", None))
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("Form", u"\u043a\u0443\u0440\u0441 3", None))
#if QT_CONFIG(tooltip)
        self.label_17.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("Form", u"\u043e\u0447\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430 ", None))
        self.label_15.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u044b\u0439 \u043e\u0442\u0447\u0435\u0442 ", None))
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0444\u0430\u0439\u043b\u044b -", None))
        self.pushButton_7.setText("")
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u043e\u0447\u043d\u0430\u044f", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0434\u043d\u044f", None))
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0446\u0435\u043d\u0442 \u043f\u043e\u0441\u0435\u0449\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043a\u0443\u0440\u0441\u043e\u0432  ", None))
        self.label_26.setText("")
#if QT_CONFIG(whatsthis)
        self.student.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.search_std.setText("")
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"ID 70870949", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043e\u0432\u0430 \u0414\u0436\u0430\u043c\u0438\u043b\u044f \u0417\u0443\u0440\u0430\u0431\u043e\u0432\u043d\u0430", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"\u043e\u0447\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430 ", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0433\u0440\u0443\u043f\u043f\u0430 \u0418\u0414 23.2/\u04112-20", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"\u043a\u0443\u0440\u0441 3", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u0431\u0435\u0437 \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.label_8.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"-- \u043f\u0440\u0438\u0441\u0442\u0443\u0441\u0442\u0432\u0438\u0435 \u043d\u0430 \u043f\u0430\u0440\u0435 ", None))
        self.label_9.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u043f\u043e \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u044b\u0439 \u043e\u0442\u0447\u0435\u0442 ", None))
    # retranslateUi

