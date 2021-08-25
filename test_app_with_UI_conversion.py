# -*- coding: utf-8 -*-

# Qt Python bindings
from PySide2.QtWidgets import QMainWindow
# UI file
from UI_file import Ui_MainWindow


class TestWindow(QMainWindow):

    def __init__(self):
        super(TestWindow, self).__init__()
        # Load the UI file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Show the UI
        self.show()


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    _ = TestWindow()
    sys.exit(app.exec_())