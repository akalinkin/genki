#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget

__author__ = "Alex Kalinkin"


class MainWindow(QWidget):
    def __init__(self, translation, parent=None):
        super(MainWindow, self).__init__(parent)

        self.resize(320, 240)
        self.move(300, 300)
        self.setWindowTitle('Application title')
