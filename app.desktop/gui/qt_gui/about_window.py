#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

__author__ = "Alex Kalinkin"


class AboutWindow(QWidget):
    def __init__(self, translation, parent=None):
        super(AboutWindow, self).__init__(parent)

        self.resize(320, 240)
        self.move(300, 300)
        self.setWindowTitle(translation.WINDOW_ABOUT_TITLE + ' QT')

        self.lbl_about_text = QLabel()
        self.lbl_about_text.setText(translation.WINDOW_ABOUT_TEXT)

        self.btn_close = QPushButton(translation.APP_BUTTONS_CLOSE_TEXT)
        self.btn_close.clicked.connect(self.close)

        self.h_box = QHBoxLayout()
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.btn_close)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.lbl_about_text)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)
        self.center()

    def center(self):
        frame_gm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_gm.moveCenter(center_point)
        self.move(frame_gm.topLeft())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
