import os
import sys

from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QProgressBar, QVBoxLayout, QWidget)

from UI_Disign.mainwind import Ui_Form





class Root(QWidget):
    def __init__(self):
        super(Root, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()




if __name__ == "__main__":

    app = QApplication(sys.argv)
    root = Root()

    sys.exit(app.exec())