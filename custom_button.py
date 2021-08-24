# -*- coding: utf-8 -*-

# Qt Python bindings
from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Signal


class CustomButton(QPushButton):

    buttonPressed = Signal(list)
    # You can change the signature here and in the Designer to test.
    # Signal() works with no types in the Designer and no arguments in the slot
    # Signal(bool) works with bool type in the Designer independently of the slot
    # Signal(int) works
    # Signal(float) does not
    # Signal(list) does not with list in the Designer and the slot
    # Signal(tuple) neither

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText('Press Me!')  # Not displayed for some reason

    def mousePressEvent(self, event):
        print("The button was pressed FYI.")
        self.buttonPressed.emit([0, 1])
