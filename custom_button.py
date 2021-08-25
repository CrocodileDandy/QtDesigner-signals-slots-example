# -*- coding: utf-8 -*-

# Qt Python bindings
from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Signal


class CustomButton(QPushButton):

    buttonPressed = Signal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        print("The button was pressed FYI.")
        self.buttonPressed.emit([0, 1])
