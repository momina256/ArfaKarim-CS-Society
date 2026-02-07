# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.genConfig.clicked.connect(self.genConfig)

    def genConfig(self):
        global config
        config = ""
        if self.ui.fileTypeDetection.isChecked() == True:
            config = config + "filetype on\n"
        if self.ui.fileTypeIndent.isChecked() == True:
            config = config + "filetype indent on\n"
        if self.ui.lineNumbers.isChecked() == True:
            config = config + "set number\n"
        if self.ui.noBackupFiles.isChecked() == True:
            config = config + "set nobackup\n"
        if self.ui.syntaxHighlight.isChecked() == True:
            config = config + "syntax on\n"
        if self.ui.wildmenu.isChecked() == True:
            config = config + "set wildmenu\n"
        colorscheme = self.ui.comboBox.currentText()
        config = config + colorscheme
        config_file = QFileDialog.getSaveFileName(self, "Save config", "~/.vimrc")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
