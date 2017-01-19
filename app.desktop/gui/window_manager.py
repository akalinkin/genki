#!/usr/bin/python3

__author__ = "Alex Kalinkin"


class WindowManager:
    manager = None

    def __init__(self, gui_type, translations):
        if gui_type == 'Gtk3':
            from gui.gtk_gui import gtk_gui
            self.manager = gtk_gui.Gtk3WindowManager(translations)
        elif gui_type == 'Qt5':
            from gui.qt_gui import qt_gui
            self.manager = qt_gui.QtWindowManager(translations)
        else:
            print('Wrong gui_type parameter. Only [Gtk3,Qt5] allowed')

    def start(self, indicator_id, icon):
        self.manager.Start(indicator_id, icon)

    def AppMenu(self):
        return self.manager.AppMenu(self)

    def AboutWindow(self):
        return self.manager.AboutWindow()

    def MainTaskOfTheDayWindow(self):
        return self.manager.MainTaskOfTheDayWindow()
