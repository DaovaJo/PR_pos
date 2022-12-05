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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 990)
        Form.setMinimumSize(QSize(1920, 990))
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
"	position: absolute;\n"
"	width: 454px;\n"
"	height: 72px;\n"
"	left: 1422px;\n"
"	top: 956px;\n"
"\n"
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
        self.widget.setGeometry(QRect(0, -10, 1932, 1089))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.group = QFrame(self.widget)
        self.group.setObjectName(u"group")
        self.group.setMinimumSize(QSize(1370, 540))
        self.group.setMaximumSize(QSize(1370, 540))
        self.group.setStyleSheet(u"")
        self.group.setFrameShape(QFrame.StyledPanel)
        self.group.setFrameShadow(QFrame.Raised)
        self.search_gr = QLineEdit(self.group)
        self.search_gr.setObjectName(u"search_gr")
        self.search_gr.setGeometry(QRect(20, 20, 509, 34))
        self.search_gr.setMinimumSize(QSize(509, 34))
        self.label_15 = QLabel(self.group)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 80, 451, 421))
        self.label_15.setMinimumSize(QSize(451, 375))
        self.label_15.setPixmap(QPixmap(u"object/\u043a\u0440\u0443\u0433\u043e\u0432\u043e\u0439 \u0438\u043d\u0434\u0435\u043a\u0430\u0442\u043e\u0440.png"))
        self.label_18 = QLabel(self.group)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(550, 160, 171, 31))
        self.label_18.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"color: rgba(0, 0, 0, 0.6);")
        self.label_18.setFrameShape(QFrame.NoFrame)
        self.label_18.setFrameShadow(QFrame.Plain)
        self.label_18.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_16 = QLabel(self.group)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(550, 120, 211, 31))
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
        self.label_17 = QLabel(self.group)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(550, 190, 211, 31))
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
        self.label_24 = QLabel(self.group)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(930, 200, 321, 25))
        self.label_24.setMinimumSize(QSize(72, 25))
        self.label_20 = QLabel(self.group)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(930, 160, 321, 25))
        self.label_20.setMinimumSize(QSize(72, 25))
        self.label_23 = QLabel(self.group)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(930, 120, 321, 25))
        self.label_23.setMinimumSize(QSize(72, 25))
        self.label_21 = QLabel(self.group)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(830, 120, 72, 25))
        self.label_21.setMinimumSize(QSize(72, 25))
        self.label_21.setStyleSheet(u"background-color:#E16032;")
        self.label_19 = QLabel(self.group)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(830, 160, 72, 25))
        self.label_19.setMinimumSize(QSize(72, 25))
        self.label_19.setStyleSheet(u"background-color:#52B7D8;")
        self.label_22 = QLabel(self.group)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(830, 200, 72, 25))
        self.label_22.setMinimumSize(QSize(72, 25))
        self.label_22.setStyleSheet(u"background-color: #F6AF39;")
        self.pushButton_4 = QPushButton(self.group)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(830, 280, 454, 72))
        self.pushButton_4.setMinimumSize(QSize(454, 72))
        self.pushButton_5 = QPushButton(self.group)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(590, 30, 355, 22))
        self.pushButton_5.setMinimumSize(QSize(339, 22))
        self.pushButton_5.setMaximumSize(QSize(355, 22))
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
        self.pushButton_6 = QPushButton(self.group)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1250, 20, 35, 32))
        self.pushButton_6.setMinimumSize(QSize(35, 32))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        icon = QIcon()
        icon.addFile(u"object/\u0434\u043e\u043f \u043f\u0430\u0440.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(32, 35))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)
        self.pushButton_7 = QPushButton(self.group)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1190, 400, 84, 43))
        self.pushButton_7.setMinimumSize(QSize(84, 43))
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
        self.label_25 = QLabel(self.group)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(920, 410, 251, 31))
        self.label_25.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"\n"
"")
        self.label_25.setFrameShape(QFrame.NoFrame)
        self.label_25.setFrameShadow(QFrame.Plain)
        self.label_25.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.group, 0, 0, 1, 1)

        self.student = QFrame(self.widget)
        self.student.setObjectName(u"student")
        self.student.setMinimumSize(QSize(553, 990))
        self.student.setMaximumSize(QSize(543, 1080))
        self.student.setStyleSheet(u"")
        self.student.setFrameShape(QFrame.StyledPanel)
        self.student.setFrameShadow(QFrame.Raised)
        self.search_std = QLineEdit(self.student)
        self.search_std.setObjectName(u"search_std")
        self.search_std.setGeometry(QRect(20, 20, 509, 34))
        self.search_std.setMinimumSize(QSize(509, 34))
        self.search_std.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label = QLabel(self.student)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 80, 481, 31))
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
        self.label_2 = QLabel(self.student)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 130, 481, 31))
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
        self.label_3 = QLabel(self.student)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 180, 481, 31))
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
        self.label_4 = QLabel(self.student)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 220, 481, 31))
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
        self.label_5 = QLabel(self.student)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 260, 481, 31))
        self.label_5.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 16px;\n"
"line-height: 27px;\n"
"color: rgba(0, 0, 0, 0.6);")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.label_6 = QLabel(self.student)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 300, 451, 421))
        self.label_6.setMinimumSize(QSize(451, 375))
        self.label_6.setPixmap(QPixmap(u"object/\u043a\u0440\u0443\u0433\u043e\u0432\u043e\u0439 \u0438\u043d\u0434\u0435\u043a\u0430\u0442\u043e\u0440.png"))
        self.label_7 = QLabel(self.student)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 750, 72, 25))
        self.label_7.setMinimumSize(QSize(72, 25))
        self.label_7.setStyleSheet(u"background-color:#E16032;")
        self.label_8 = QLabel(self.student)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 790, 72, 25))
        self.label_8.setMinimumSize(QSize(72, 25))
        self.label_8.setStyleSheet(u"background-color:#52B7D8;")
        self.label_9 = QLabel(self.student)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 830, 72, 25))
        self.label_9.setMinimumSize(QSize(72, 25))
        self.label_9.setStyleSheet(u"background-color: #F6AF39;")
        self.label_10 = QLabel(self.student)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 750, 321, 25))
        self.label_10.setMinimumSize(QSize(72, 25))
        self.label_11 = QLabel(self.student)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 790, 321, 25))
        self.label_11.setMinimumSize(QSize(72, 25))
        self.label_12 = QLabel(self.student)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(140, 830, 321, 25))
        self.label_12.setMinimumSize(QSize(72, 25))
        self.pushButton = QPushButton(self.student)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 900, 454, 72))
        self.pushButton.setMinimumSize(QSize(454, 72))
        self.pushButton_2 = QPushButton(self.student)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 70, 35, 32))
        self.pushButton_2.setMinimumSize(QSize(35, 32))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(32, 35))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)

        self.gridLayout.addWidget(self.student, 0, 1, 2, 1)

        self.potok = QFrame(self.widget)
        self.potok.setObjectName(u"potok")
        self.potok.setMinimumSize(QSize(1370, 540))
        self.potok.setStyleSheet(u"")
        self.potok.setFrameShape(QFrame.StyledPanel)
        self.potok.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.potok)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(160, 20, 1011, 431))
        self.label_26.setPixmap(QPixmap(u"object/\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 \u043a\u0443\u0440\u0441\u044b.png"))
        self.label_27 = QLabel(self.potok)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(930, 40, 361, 31))
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
        self.radioButton_3 = QRadioButton(self.potok)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(930, 110, 261, 20))
        self.radioButton_3.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 27px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #000000;")
        self.radioButton_4 = QRadioButton(self.potok)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(930, 150, 231, 20))
        self.radioButton_4.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
"line-height: 27px;\n"
"/* identical to box height */\n"
"\n"
"\n"
"color: #000000;")

        self.gridLayout.addWidget(self.potok, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_15.setText("")
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("Form", u"\u043a\u0443\u0440\u0441 3", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("Form", u"\u0418\u0414 23.2/\u04112-20", None))
#if QT_CONFIG(tooltip)
        self.label_17.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_17.setText(QCoreApplication.translate("Form", u"\u043e\u0447\u043d\u0430\u044f \u0444\u043e\u0440\u043c\u0430 ", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u043f\u043e \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"-- \u043f\u0440\u0438\u0441\u0442\u0443\u0441\u0442\u0432\u0438\u0435 \u043d\u0430 \u043f\u0430\u0440\u0435 ", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u0431\u0435\u0437 \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.label_21.setText("")
        self.label_19.setText("")
        self.label_22.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u044b\u0439 \u043e\u0442\u0447\u0435\u0442 ", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u044d\u043a\u0441\u043f\u043b\u0443\u0430\u0442\u0430\u0446\u0438\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b\u0435 \u0444\u0430\u0439\u043b\u044b -  ", None))
#if QT_CONFIG(whatsthis)
        self.student.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.search_std.setText("")
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
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u0431\u0435\u0437 \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"-- \u043f\u0440\u0438\u0441\u0442\u0443\u0441\u0442\u0432\u0438\u0435 \u043d\u0430 \u043f\u0430\u0440\u0435 ", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"-- \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0438\u0435 \u043f\u043e \u0443\u0432\u0430\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043f\u0440\u0438\u0447\u0438\u043d\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u044b\u0439 \u043e\u0442\u0447\u0435\u0442 ", None))
        self.pushButton_2.setText("")
        self.label_26.setText("")
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0446\u0435\u043d\u0442 \u043f\u043e\u0441\u0435\u0449\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043a\u0443\u0440\u0441\u043e\u0432  ", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u0432\u044b\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0434\u043d\u044f", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u043e\u0447\u043d\u0430\u044f", None))
    # retranslateUi

