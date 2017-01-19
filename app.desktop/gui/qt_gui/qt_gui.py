#!/usr/bin/python3

import os
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
import PyQt5.QtGui as QtGui
from .app_menu import AppMenu

__author__ = "Alex Kalinkin"


class QtWindowManager:
    app = None
    translations = None

    def __init__(self, translations):
        import sys

        self.translations = translations
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

    def start(self, indicator_id, icon):
        icon = QSystemTrayIcon(QtGui.QIcon(os.path.abspath(icon)), self.app)
        icon.setContextMenu(self.AppMenu().build())
        icon.show()

        self.app.exec_()

    def AppMenu(self):
        if hasattr(self, 'appMenu'):
            return self.appMenu
        else:
            self.appMenu = AppMenu(self, self.translations)
            return self.appMenu

    def MainWindow(self):
        if hasattr(self, 'mainWindow'):
            return self.mainWindow
        else:
            from .main_window import MainWindow
            self.mainWindow = MainWindow(self.translations)
            return self.mainWindow

    def AboutWindow(self):
        if hasattr(self, 'aboutWindow'):
            return self.aboutWindow
        else:
            from .about_window import AboutWindow
            self.aboutWindow = AboutWindow(self.translations)
            return self.aboutWindow

    def MainTaskOfTheDayWindow(self):
        if hasattr(self, 'mainTaskOfTheDayWindow'):
            return self.mainTaskOfTheDayWindow
        else:
            from .main_task_of_the_day_window import MainTaskOfTheDayWindow
            self.mainTaskOfTheDayWindow = MainTaskOfTheDayWindow(self.translations)
            return self.mainTaskOfTheDayWindow