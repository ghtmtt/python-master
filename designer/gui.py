from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

import os
import sys

ui_path = os.path.join(
    os.path.dirname(__file__),
    'interface.ui'
)

FORM_CLASS, _ = uic.loadUiType(ui_path)


class myUi(QDialog, FORM_CLASS):

    def __init__(self):

        QDialog.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = myUi()
    form.show()
    app.exec_()


