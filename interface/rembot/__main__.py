#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
License is available in LICENSE
@brief Rembot main program execution
@author eeshiken
@since 2017-DEC-28
"""

from PyQt5.QtWidgets import QApplication
from main_ui import MainUI


if __name__ == '__main__':
    import sys
    APP = QApplication(sys.argv)
    MAIN = MainUI()
    sys.exit(APP.exec_())
