# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""
import sys
import os
import site

site.addsitedir(os.path.abspath(os.path.dirname(__file__) + '/ext-libs'))

def classFactory(iface):
    from .IPyConsole import IPyConsole
    return IPyConsole(iface)
