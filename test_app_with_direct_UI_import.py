# -*- coding: utf-8 -*-

# Qt Python bindings
from PySide2.QtWidgets import QMainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
# Custom widgets
from custom_label import CustomLabel
from custom_button import CustomButton


class TestWindow(QMainWindow):

    def __init__(self, path_to_ui_file):
        super(TestWindow, self).__init__()
        # Load the UI file
        self.loadUIFile(path_to_ui_file)
        self.ui.show()

    def loadUIFile(self, path_to_UI_file):
        loader = QUiLoader()
        loader.registerCustomWidget(CustomLabel)
        loader.registerCustomWidget(CustomButton)
        ui_file = QFile(path_to_UI_file)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    _ = TestWindow('UI_file.ui')
    sys.exit(app.exec_())