#!/usr/bin/python3
import os
import signal
import locale
import gettext
from gui.window_manager import WindowManager

__author__ = "Alex Kalinkin"


APP_INDICATOR_ID = 'genki.app.desktop'
APP_ICON = 'assets/app_icon.svg'
APP_WINDOW_MANAGER = 'Gtk3'  # ['Qt5','Gtk3']
AVAILABLE_L10NS = ['ru_RU', 'en_US']
DEFAULT_L10N = 'en_US'


def main():
    init()


def init():
    set_work_directory()
    translation = init_l10n()
    window_manager = WindowManager(APP_WINDOW_MANAGER, translation)
    print('Application started with AppId: "{0}"'.format(APP_INDICATOR_ID))
    window_manager.start(APP_INDICATOR_ID, APP_ICON)


def init_l10n():
    print('Available translations: {0}'.format(AVAILABLE_L10NS))

    current_locale = locale.getdefaultlocale()
    print('Current l10n: {0}'.format(current_locale))

    if current_locale[0] in AVAILABLE_L10NS:
        locale_code = current_locale[0]
    else:
        locale_code = DEFAULT_L10N

    lang = gettext.translation('app', localedir='l10n', languages=[locale_code])
    lang.install()

    from l10n.app_strings import Translations
    t = Translations

    return t


def set_work_directory():
    abspath = os.path.abspath(__file__)
    dir_name = os.path.dirname(abspath)
    os.chdir(dir_name)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
