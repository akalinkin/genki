#!/usr/bin/python3

__author__ = "Alex Kalinkin"

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator

from .app_menu import AppMenu
from .about import AboutWindow


class Gtk3WindowManager:
    translations = None

    def __init__(self, translations):
        self.translations = translations

    def start(self, indicator_id, icon):
        indicator = appindicator.Indicator.new(indicator_id, os.path.abspath(icon), appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        indicator.set_menu(self.AppMenu().build())
        gtk.main()

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
            from .main import MainWindow
            self.mainWindow = MainWindow(self.translations)
            return self.mainWindow

    def AboutWindow(self):
        if hasattr(self, 'aboutWindow'):
            return self.aboutWindow
        else:
            from .about import AboutWindow
            self.aboutWindow = AboutWindow(self.translations)
            return self.aboutWindow
