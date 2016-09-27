# -*- coding: utf-8 -*-

"""
***************************************************************************
    SettingsDlg.py        IPyConsole settings dialog
    ---------------------
    Date                 : April 2015
    Copyright            : (C) 2015 by Alessandro Pasotti (ItOpen)
    Email                : apasotti at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
__author__ = 'Alessandro Pasotti'
__date__ = 'April 2015'
__copyright__ = '(C) 2015, Alessandro Pasotti'


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .Ui_SettingsDialog import Ui_SettingsDialog

# create the dialog for Settings
class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
