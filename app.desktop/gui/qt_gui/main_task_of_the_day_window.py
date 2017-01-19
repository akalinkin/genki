#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QTextEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from model.task import Task

__author__ = "Alex Kalinkin"


class MainTaskOfTheDayWindow(QWidget):
    def __init__(self, T, parent=None):
        super(MainTaskOfTheDayWindow, self).__init__(parent)

        self.model = MainTaskOfTheDayViewModel()

        self.resize(320, 240)
        self.move(300, 300)
        self.setWindowTitle(T.WINDOW_MAIN_TASK_OF_THE_DAY_TITLE)

        self.lbl_main_task_description = QLabel()
        self.lbl_main_task_description.setText(T.WINDOW_MAIN_TASK_OF_THE_DAY_DESCRIPTION)

        self.text_edit_main_task = QTextEdit()
        self.text_edit_main_task.textChanged.connect(self.on_main_task_changed)

        self.btn_ok = QPushButton(T.APP_BUTTONS_OK_TEXT)
        self.btn_ok.clicked.connect(self.btn_ok_handler)

        self.btn_close = QPushButton(T.APP_BUTTONS_CLOSE_TEXT)
        self.btn_close.clicked.connect(self.btn_close_handler)

        self.h_box = QHBoxLayout()
        self.h_box.addStretch(1)
        self.h_box.addWidget(self.btn_ok)
        self.h_box.addWidget(self.btn_close)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.lbl_main_task_description)
        self.v_box.addWidget(self.text_edit_main_task)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def btn_ok_handler(self):
        print("btn_ok_handler()")
        self.model.save()
        self.close()

    def btn_close_handler(self):
        print("btn_close_handler()")
        self.close()

    def on_main_task_changed(self):
        value = self.text_edit_main_task.toPlainText()
        print("on_main_task_changed({})".format(value))
        self.model.main_task.name = value


class MainTaskOfTheDayViewModel:
    def __init__(self):
        self.main_task = Task()

    def load(self):
        # TODO: using task_repository try to find Task with current date and create new if not found
        pass

    def save(self):
        # save data TODO: Move code to task_repository class
        from sqlalchemy.orm import sessionmaker
        from model import model
        engine = model.db_connect()
        session_maker = sessionmaker(bind=engine)
        session = session_maker()
        session.add(self.main_task)
        session.commit()
