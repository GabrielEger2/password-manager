# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mai3nlTDIna.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLineEdit, QCheckBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider, QHBoxLayout,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 215)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 215))
        MainWindow.setMaximumSize(QSize(700, 230))
        MainWindow.setStyleSheet(u"QTabBar::tab \n"
"{\n"
"    background: #48555E;\n"
"    color: white;   \n"
"    border-color: #48555E;\n"
"}\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: #1D2A32;\n"
"    border-color: #40494E;\n"
"    color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #C1D8E8, stop: 1 #F0F5F8); \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    font-size: 13pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #2D5BD4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(14, 12, 14, 12)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_website = QLabel(self.centralwidget)
        self.lb_website.setObjectName(u"lb_website")

        self.horizontalLayout_5.addWidget(self.lb_website)

        self.et_website = QLineEdit(self.centralwidget)
        self.et_website.setObjectName(u"et_website")

        self.horizontalLayout_5.addWidget(self.et_website)

        self.bt_sp = QPushButton(self.centralwidget)
        self.bt_sp.setObjectName(u"bt_sp")

        self.horizontalLayout_5.addWidget(self.bt_sp)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_email = QLabel(self.centralwidget)
        self.lb_email.setObjectName(u"lb_email")

        self.horizontalLayout_2.addWidget(self.lb_email)

        self.et_email = QLineEdit(self.centralwidget)
        self.et_email.setObjectName(u"et_email")
        self.et_email.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(31)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.et_email.sizePolicy().hasHeightForWidth())
        self.et_email.setSizePolicy(sizePolicy1)
        self.et_email.setMinimumSize(QSize(32, 0))
        self.et_email.setMaximumSize(QSize(16777215, 16777215))
        self.et_email.setSizeIncrement(QSize(1, 0))

        self.horizontalLayout_2.addWidget(self.et_email)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_password = QLabel(self.centralwidget)
        self.lb_password.setObjectName(u"lb_password")

        self.horizontalLayout.addWidget(self.lb_password)

        self.et_password = QLineEdit(self.centralwidget)
        self.et_password.setObjectName(u"et_password")

        self.horizontalLayout.addWidget(self.et_password)

        self.bt_password = QPushButton(self.centralwidget)
        self.bt_password.setObjectName(u"bt_password")

        self.horizontalLayout.addWidget(self.bt_password)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.keep_check = QCheckBox(self.centralwidget)
        self.keep_check.setObjectName(u"keep_check")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(14)
        sizePolicy2.setVerticalStretch(14)
        sizePolicy2.setHeightForWidth(self.keep_check.sizePolicy().hasHeightForWidth())
        self.keep_check.setSizePolicy(sizePolicy2)
        self.keep_check.setMinimumSize(QSize(14, 14))

        self.horizontalLayout_3.addWidget(self.keep_check)

        self.email_lb = QLabel(self.centralwidget)
        self.email_lb.setObjectName(u"email_lb")

        self.horizontalLayout_3.addWidget(self.email_lb)

        self.bt_add = QPushButton(self.centralwidget)
        self.bt_add.setObjectName(u"bt_add")

        self.horizontalLayout_3.addWidget(self.bt_add)

        self.space = QLabel(self.centralwidget)
        self.space.setObjectName(u"space")

        self.horizontalLayout_3.addWidget(self.space)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Manager", None))
        self.lb_website.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">               Website:</span></p></body></html>", None))
        self.bt_sp.setText(QCoreApplication.translate("MainWindow", u"  Search Password  ", None))
        self.lb_email.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> E-mail/Username:</span></p></body></html>", None))
        self.lb_password.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">             Password:</span></p></body></html>", None))
        self.bt_password.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.keep_check.setText("")
        self.email_lb.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#dcffdf;\">Keep E-mail</span></p></body></html>", None))
        self.bt_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.space.setText("")
    # retranslateUi

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        if not PasswordGenerator.objectName():
            PasswordGenerator.setObjectName(u"PasswordGenerator")
        PasswordGenerator.resize(450, 200)
        PasswordGenerator.setMinimumSize(QSize(450, 200))
        PasswordGenerator.setMaximumSize(QSize(450, 200))
        PasswordGenerator.setStyleSheet(u"QTabBar::tab \n"
"{\n"
"    background: #48555E;\n"
"    color: white;   \n"
"    border-color: #48555E;\n"
"}\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: #1D2A32;\n"
"    border-color: #40494E;\n"
"    color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #C1D8E8, stop: 1 #F0F5F8); \n"
"}")
        self.centralwidget = QWidget(PasswordGenerator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    font-size: 13pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #2D5BD4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_password = QLineEdit(self.centralwidget)
        self.line_password.setObjectName(u"line_password")

        self.horizontalLayout.addWidget(self.line_password)

        self.btn_select = QPushButton(self.centralwidget)
        self.btn_select.setObjectName(u"btn_select")
        self.btn_select.setStyleSheet(u"")
        icon = QIcon()
        iconThemeName = u"accessories-dictionary"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../PasswordGenerator", QSize(), QIcon.Normal, QIcon.Off)

        self.btn_select.setIcon(icon)
        self.btn_select.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_select)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slider_lenght = QSlider(self.centralwidget)
        self.slider_lenght.setObjectName(u"slider_lenght")
        self.slider_lenght.setMaximum(25)
        self.slider_lenght.setValue(0)
        self.slider_lenght.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.slider_lenght)

        self.spin_lenght = QSpinBox(self.centralwidget)
        self.spin_lenght.setObjectName(u"spin_lenght")
        self.spin_lenght.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spin_lenght.setMaximum(25)
        self.spin_lenght.setValue(0)

        self.horizontalLayout_2.addWidget(self.spin_lenght)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_az = QPushButton(self.centralwidget)
        self.btn_az.setObjectName(u"btn_az")
        self.btn_az.setStyleSheet(u"")
        self.btn_az.setCheckable(True)
        self.btn_az.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_az)

        self.btn_AZ = QPushButton(self.centralwidget)
        self.btn_AZ.setObjectName(u"btn_AZ")
        self.btn_AZ.setStyleSheet(u"")
        self.btn_AZ.setCheckable(True)
        self.btn_AZ.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_AZ)

        self.btn_09 = QPushButton(self.centralwidget)
        self.btn_09.setObjectName(u"btn_09")
        self.btn_09.setStyleSheet(u"")
        self.btn_09.setCheckable(True)
        self.btn_09.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_09)

        self.btn_symbols = QPushButton(self.centralwidget)
        self.btn_symbols.setObjectName(u"btn_symbols")
        self.btn_symbols.setStyleSheet(u"")
        self.btn_symbols.setCheckable(True)
        self.btn_symbols.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_symbols)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        PasswordGenerator.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordGenerator)

        QMetaObject.connectSlotsByName(PasswordGenerator)
    # setupUi

    def retranslateUi(self, PasswordGenerator):
        PasswordGenerator.setWindowTitle(QCoreApplication.translate("PasswordGenerator", u"Password Generator", None))
        self.btn_select.setText(QCoreApplication.translate("PasswordGenerator", u"Copy", None))
        self.btn_az.setText(QCoreApplication.translate("PasswordGenerator", u"a-z", None))
        self.btn_AZ.setText(QCoreApplication.translate("PasswordGenerator", u"A-Z", None))
        self.btn_09.setText(QCoreApplication.translate("PasswordGenerator", u"0-9", None))
        self.btn_symbols.setText(QCoreApplication.translate("PasswordGenerator", u"#$%", None))
    # retranslateUi

class Ui_SearchPassword(object):
    def setupUi(self, SearchPassword):
        if not SearchPassword.objectName():
            SearchPassword.setObjectName(u"SearchPassword")
        SearchPassword.resize(400, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchPassword.sizePolicy().hasHeightForWidth())
        SearchPassword.setSizePolicy(sizePolicy)
        SearchPassword.setMinimumSize(QSize(400, 120))
        SearchPassword.setMaximumSize(QSize(400, 120))
        SearchPassword.setStyleSheet(u"QTabBar::tab \n"
"{\n"
"    background: #48555E;\n"
"    color: black;   \n"
"    border-color: #48555E;\n"
"}\n"
"\n"
"QTabBar::tab:selected, \n"
"QTabBar::tab:hover \n"
"{\n"
"    border-top-color: #1D2A32;\n"
"    border-color: #40494E;\n"
"    color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #C1D8E8, stop: 1 #F0F5F8); \n"
"}")
        self.centralwidget = QWidget(SearchPassword)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    font-size: 13pt;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_web = QLabel(self.centralwidget)
        self.lb_web.setObjectName(u"lb_web")

        self.horizontalLayout.addWidget(self.lb_web)

        self.in_web = QLabel(self.centralwidget)
        self.in_web.setObjectName(u"in_web")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.in_web.sizePolicy().hasHeightForWidth())
        self.in_web.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.in_web)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_ema = QLabel(self.centralwidget)
        self.lb_ema.setObjectName(u"lb_ema")

        self.horizontalLayout_2.addWidget(self.lb_ema)

        self.in_ema = QLabel(self.centralwidget)
        self.in_ema.setObjectName(u"in_ema")
        sizePolicy1.setHeightForWidth(self.in_ema.sizePolicy().hasHeightForWidth())
        self.in_ema.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.in_ema)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_pass = QLabel(self.centralwidget)
        self.lb_pass.setObjectName(u"lb_pass")

        self.horizontalLayout_3.addWidget(self.lb_pass)

        self.in_pass = QLabel(self.centralwidget)
        self.in_pass.setObjectName(u"in_pass")
        sizePolicy1.setHeightForWidth(self.in_pass.sizePolicy().hasHeightForWidth())
        self.in_pass.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.in_pass)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        SearchPassword.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchPassword)

        QMetaObject.connectSlotsByName(SearchPassword)
    # setupUi

    def retranslateUi(self, SearchPassword):
        SearchPassword.setWindowTitle(QCoreApplication.translate("SearchPassword", u"Password Results", None))
#if QT_CONFIG(tooltip)
        self.centralwidget.setToolTip(QCoreApplication.translate("SearchPassword", u"<html><head/><body><pre style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New';\"><br/></pre></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lb_web.setText(QCoreApplication.translate("SearchPassword", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">              Website:</span></p></body></html>", None))
        self.in_web.setText(QCoreApplication.translate("SearchPassword", u"<html><head/><body><p><span style=\" color:#ffffff;\">in_web</span></p></body></html>", None))
        self.lb_ema.setText(QCoreApplication.translate("SearchPassword", u"<html><head/><body><p><span style=\" color:#ffffff;\">E-mail/Username:</span></p></body></html>", None))
        self.in_ema.setText(QCoreApplication.translate("SearchPassword", u"<html><head/><body><p><span style=\" color:#ffffff;\">in_email</span></p></body></html>", None))
        self.lb_pass.setText(QCoreApplication.translate("SearchPassword", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">            Password:</span></p></body></html>", None))
        self.in_pass.setText(QCoreApplication.translate("SearchPassword", u"<html><head/><body><p><span style=\" color:#ffffff;\">in_password</span></p></body></html>", None))
    # retranslateUi

class Ui_ErrorMassage(object):
    def setupUi(self, ErrorMassage):
        if not ErrorMassage.objectName():
            ErrorMassage.setObjectName(u"ErrorMassage")
        ErrorMassage.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorMassage.sizePolicy().hasHeightForWidth())
        ErrorMassage.setSizePolicy(sizePolicy)
        ErrorMassage.setMinimumSize(QSize(400, 150))
        ErrorMassage.setMaximumSize(QSize(400, 150))
        font = QFont()
        font.setBold(False)
        ErrorMassage.setFont(font)
        self.centralwidget = QWidget(ErrorMassage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e1e;\n"
"    font-size: 13pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px;\n"
"    background-color: #2a2a2a;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"    background-color: #2d5bd4;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #2D5BD4;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    color: #d8d8d8;\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    background-color: #404040;\n"
"    padding: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.lb_ERROR = QLabel(self.centralwidget)
        self.lb_ERROR.setObjectName(u"lb_ERROR")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.lb_ERROR.setFont(font1)

        self.verticalLayout.addWidget(self.lb_ERROR)

        self.lb_em = QLabel(self.centralwidget)
        self.lb_em.setObjectName(u"lb_em")

        self.verticalLayout.addWidget(self.lb_em)

        ErrorMassage.setCentralWidget(self.centralwidget)

        self.retranslateUi(ErrorMassage)

        QMetaObject.connectSlotsByName(ErrorMassage)
    # setupUi

    def retranslateUi(self, ErrorMassage):
        ErrorMassage.setWindowTitle(QCoreApplication.translate("ErrorMassage", u"Error Massage", None))
        self.lb_ERROR.setText(QCoreApplication.translate("ErrorMassage", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">ERROR</span></p></body></html>", None))
        self.lb_em.setText(QCoreApplication.translate("ErrorMassage", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Error Massage</span></p></body></html>", None))
    # retranslateUi




