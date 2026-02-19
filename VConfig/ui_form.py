# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(254, 278)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        MainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 217, 238))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.colorscheme = QHBoxLayout()
        self.colorscheme.setObjectName(u"colorscheme")
        self.colorscheme_label = QLabel(self.layoutWidget)
        self.colorscheme_label.setObjectName(u"colorscheme_label")

        self.colorscheme.addWidget(self.colorscheme_label)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.colorscheme.addWidget(self.comboBox)


        self.gridLayout.addLayout(self.colorscheme, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineNumbers = QCheckBox(self.layoutWidget)
        self.lineNumbers.setObjectName(u"lineNumbers")

        self.verticalLayout.addWidget(self.lineNumbers)

        self.fileTypeDetection = QCheckBox(self.layoutWidget)
        self.fileTypeDetection.setObjectName(u"fileTypeDetection")

        self.verticalLayout.addWidget(self.fileTypeDetection)

        self.fileTypeIndent = QCheckBox(self.layoutWidget)
        self.fileTypeIndent.setObjectName(u"fileTypeIndent")

        self.verticalLayout.addWidget(self.fileTypeIndent)

        self.syntaxHighlight = QCheckBox(self.layoutWidget)
        self.syntaxHighlight.setObjectName(u"syntaxHighlight")

        self.verticalLayout.addWidget(self.syntaxHighlight)

        self.noBackupFiles = QCheckBox(self.layoutWidget)
        self.noBackupFiles.setObjectName(u"noBackupFiles")

        self.verticalLayout.addWidget(self.noBackupFiles)

        self.wildmenu = QCheckBox(self.layoutWidget)
        self.wildmenu.setObjectName(u"wildmenu")

        self.verticalLayout.addWidget(self.wildmenu)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.genConfig = QPushButton(self.layoutWidget)
        self.genConfig.setObjectName(u"genConfig")

        self.gridLayout.addWidget(self.genConfig, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VConfig", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.colorscheme_label.setText(QCoreApplication.translate("MainWindow", u"Colorscheme:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Dark Blue", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Default", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Delek", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Desert", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Elflord", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Evening", None))
        self.comboBox.setItemText(7, "")

        self.lineNumbers.setText(QCoreApplication.translate("MainWindow", u"Line numbers", None))
        self.fileTypeDetection.setText(QCoreApplication.translate("MainWindow", u"File type detection", None))
        self.fileTypeIndent.setText(QCoreApplication.translate("MainWindow", u"File type indendation", None))
        self.syntaxHighlight.setText(QCoreApplication.translate("MainWindow", u"Syntax highlighting", None))
        self.noBackupFiles.setText(QCoreApplication.translate("MainWindow", u"No backup files", None))
        self.wildmenu.setText(QCoreApplication.translate("MainWindow", u"Wildmenu (suggest file names)", None))
        self.genConfig.setText(QCoreApplication.translate("MainWindow", u"Generate Vim Config", None))
    # retranslateUi

