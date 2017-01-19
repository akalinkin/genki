#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

__author__ = "Alex Kalinkin"


class MainWindow(Gtk.Window):
    def __init__(self, T):
        Gtk.Window.__init__(self, title='Main')
        self.set_default_size(320, 240)
        self.set_position(Gtk.WindowPosition.CENTER)

    def show(self):
        print("MainWindow.show()")
        self.show_all()
