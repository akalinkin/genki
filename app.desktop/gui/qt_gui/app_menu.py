#!/usr/bin/python3

from PyQt5.QtWidgets import QMenu, QAction, qApp

__author__ = "Alex Kalinkin"


class AppMenu(QMenu):
    wm = None
    translations = None

    def __init__(self, window_manager, translations):
        super(AppMenu, self).__init__()

        self.wm = window_manager
        self.translations = translations

        self.main_task_of_the_day_action = QAction(self.translations.MENU_ITEM_MAIN_TASK_OF_THE_DAY, self, shortcut="Ctrl+M",
                statusTip="Set main task of your day", triggered=self.menu_item_main_task_of_the_day_handler)

        self.exit_action = QAction(self.translations.MENU_ITEM_QUIT, self, shortcut="Ctrl+Q",
                                   statusTip="Exit the application", triggered=self.menu_item_exit_handler)

        self.about_action = QAction(self.translations.MENU_ITEM_ABOUT, self,
                                    statusTip="Show the application's About box",
                                    triggered=self.menu_item_about_handler)

    def build(self):
        self.addAction(self.about_action)
        self.addAction(self.main_task_of_the_day_action)
        self.addSeparator()
        self.addAction(self.exit_action)

        return self

    @staticmethod
    def menu_item_exit_handler():
        print("menu_item_exit_handler()")
        qApp.quit()

    def menu_item_about_handler(self):
        print('menu_item_about_handler()')
        about_window = self.wm.AboutWindow()
        about_window.show()

    def menu_item_main_task_of_the_day_handler(self):
        print('menu_item_main_task_of_the_day_handler()')
        main_task_of_the_day_window = self.wm.MainTaskOfTheDayWindow()
        main_task_of_the_day_window.show()
