#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Notify', '0.7')
from gi.repository import Notify

__author__ = "Alex Kalinkin"


class AppMenu(Gtk.Menu):
    wm = None
    translations = None

    def __init__(self, window_manager, translations):
        self.wm = window_manager
        self.translations = translations

    def build(self):
        menu = Gtk.Menu()

        menu_item_projects = Gtk.MenuItem(self.translations.MENU_ITEM_PROJECTS)
        menu_item_projects.set_submenu(self._build_projects_menu())
        menu.append(menu_item_projects)

        menu_separator = Gtk.SeparatorMenuItem()
        menu.append(menu_separator)

        menu_item_about = Gtk.MenuItem(self.translations.MENU_ITEM_ABOUT)
        menu_item_about.connect('activate', self.menu_item_about_handler)
        menu.append(menu_item_about)

        menu_item_quit = Gtk.MenuItem(self.translations.MENU_ITEM_QUIT)
        menu_item_quit.connect('activate', self.menu_item_quit_handler)
        menu.append(menu_item_quit)

        menu.show_all()

        return menu

    @staticmethod
    def menu_item_quit_handler(_):
        Notify.uninit()
        Gtk.main_quit()

    def _build_projects_menu(self):
        # projects = ['Project1', 'Project 2', 'Project 3']

        menu = Gtk.Menu()

        menu_item_projects_create = Gtk.MenuItem(self.translations.MENU_ITEM_PROJECTS_CREATE)
        menu_item_projects_create.connect('activate', self.menu_item_projects_create_handler)
        menu.append(menu_item_projects_create)

        menu_separator = Gtk.SeparatorMenuItem()
        menu.append(menu_separator)

        # TODO: Build projects menu

        return menu

    def menu_item_projects_create_handler(self, _):
        Notify.Notification.new('<b>{0} clicked</b>'.format(self.translations.MENU_ITEM_PROJECTS_CREATE),
                                'Create some logic to build your project', None).show()

    def menu_item_about_handler(self, _):
        self.wm.AboutWindow().show()
