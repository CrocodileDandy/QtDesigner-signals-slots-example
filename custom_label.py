# -*- coding: utf-8 -*-

# Qt Python bindings
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Slot


class CustomLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @Slot(list)
    def setCustomText(self, value):
        self.setText(f"The button was pressed! {value}")
