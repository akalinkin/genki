#!/usr/bin/python3
import os
import signal

__author__ = "Alex Kalinkin"


APP_INDICATOR_ID = 'genki.app.desktop'
APP_ICON = 'assets/app_icon.svg'
APP_WINDOW_MANAGER = 'Qt5'  # ['Qt5','Gtk3']
AVAILABLE_L10NS = ['ru_RU', 'en_US']
DEFAULT_L10N = 'en_US'


def main():
    init()


def init():
    set_work_directory()


def set_work_directory():
    abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(abspath)
    os.chdir(dir_name)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
