# -*- coding: utf-8 -*-

"""
***************************************************************************
    IPyConsole.py
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


import os

# Import the PyQt and QGIS libraries

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import loadUi

from qgis.core import *

from propertize import propertize
import resources_rc

PLUGIN_DOMAIN="IPyConsole"

# Defaults for settings
DEFAULT_WINDOW_MODE='windowed'
DEFAULT_FONT_SIZE=10
DEFAULT_PROPERTIZE=1
DEFAULT_AUTO_OPEN=0
DEFAULT_SHOW_HELP=1

# Loads GUI from .ui
DEBUG=False

if not DEBUG:
    from SettingsDialog import SettingsDialog
else:
    from PyQt4 import uic
    import os
    class SettingsDialog(QDialog):
        def __init__(self):
            super(SettingsDialog, self ).__init__()
            uic.loadUi(os.path.join(os.path.dirname(__file__), 'Ui_SettingsDialog.ui'), self)
            QMetaObject.connectSlotsByName(self)

def _tr(s):
    """Translate, save some typing"""
    return QCoreApplication.translate(PLUGIN_DOMAIN, s)


class IPyConsole:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.status = None
        self.settingsDlg = None
        self.settings =  QSettings('ItOpen', PLUGIN_DOMAIN)
        # If auto_open: connect
        if int(self.get_settings('auto_open', DEFAULT_AUTO_OPEN)):
            if self.get_settings('default_window_mode', DEFAULT_WINDOW_MODE) == 'windowed':
                self.iface.mapCanvas().renderStarting.connect(self.default)
            else:
                self.default()


    def initGui(self):
        # Create action that will start plugin
        self.default_action = QAction(QIcon(":/plugins/IPyConsole/icons/icon.png"), \
            _tr("&IPython QGIS Console"), self.iface.mainWindow())
        self.docked_action = QAction(QIcon(":/plugins/IPyConsole/icons/icon.png"), \
            _tr("&Docked"), self.iface.mainWindow())
        self.windowed_action = QAction(QIcon(":/plugins/IPyConsole/icons/icon.png"), \
            _tr("&Windowed"), self.iface.mainWindow())
        self.settings_action = QAction(QIcon(":/plugins/IPyConsole/icons/settings.svg"), \
            _tr("&Settings"), self.iface.mainWindow())

        # connect the actions to the methods
        self.docked_action.activated.connect(self.docked)
        self.windowed_action.activated.connect(self.windowed)
        self.default_action.activated.connect(self.default)
        self.settings_action.activated.connect(self.show_settings)

        # Add toolbar button
        self.iface.addToolBarIcon(self.default_action)

        # Build menu
        self.menu = QMenu(_tr("&IPython QGIS Console"))
        self.menu.setIcon(QIcon(":/plugins/IPyConsole/icons/icon.png"))
        self.menu.addActions([self.docked_action, self.windowed_action, self.settings_action])
        self.iface.pluginMenu().addMenu( self.menu )


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("IPyConsole", self.docked_action)
        self.iface.removePluginMenu("IPyConsole", self.windowed_action)
        self.iface.removePluginMenu("IPyConsole", self.settings_action)
        self.iface.removeToolBarIcon(self.default_action)


    def default(self):
        """TODO: read settings setting for default window type"""
        try:
            # Disconnect the signal if it was connected to allow
            # auto_open
            self.iface.mapCanvas().renderStarting.disconnect(self.default)
        except TypeError:
            pass
        self.run(dock=(self.get_settings('default_window_mode', DEFAULT_WINDOW_MODE) == 'docked'))

    def windowed(self):
        self.run(dock=False)

    def docked(self):
        self.run(dock=True)

    def show_settings(self):
        if self.settingsDlg is None:
            self.read_settings()
            self.settingsDlg = SettingsDialog()
            # Set values
            winmode = self.get_settings('default_window_mode', DEFAULT_WINDOW_MODE)
            if winmode == 'docked':
                self.settingsDlg.windowModeDocked.setChecked(True)
            else:
                self.settingsDlg.windowModeFloating.setChecked(True)
            font_size =  self.get_settings('font_size', DEFAULT_FONT_SIZE)
            self.settingsDlg.fontSize.setValue(int(font_size))
            propertize_setting = self.get_settings('propertize', DEFAULT_PROPERTIZE)
            self.settingsDlg.propertize.setChecked(int(propertize_setting))
            auto_open = self.get_settings('auto_open', DEFAULT_AUTO_OPEN)
            self.settingsDlg.auto_open.setChecked(int(auto_open))
            show_help = self.get_settings('show_help', DEFAULT_SHOW_HELP)
            self.settingsDlg.show_help.setChecked(int(show_help))

        self.settingsDlg.show()
        self.settingsDlg.adjustSize()
        result = self.settingsDlg.exec_()
        if result:
            #import pdb; pyqtRemoveInputHook(); pdb.set_trace()
            self.set_settings('font_size', self.settingsDlg.fontSize.value())
            winmode = 'windowed'
            if self.settingsDlg.windowModeFloating.isChecked():
                winmode = DEFAULT_WINDOW_MODE
            elif self.settingsDlg.windowModeDocked.isChecked():
                winmode = 'docked'
            self.set_settings('default_window_mode', winmode)
            self.set_settings('propertize', int(self.settingsDlg.propertize.isChecked()))
            self.set_settings('auto_open', int(self.settingsDlg.auto_open.isChecked()))
            self.set_settings('show_help', int(self.settingsDlg.show_help.isChecked()))
            self.store_settings()


    # return a settings parameter
    def get_settings(self, key, default=''):
        return self.settings.value(key, default);


   # set a settings parameter
    def set_settings(self, key, value):
        return self.settings.setValue(key, value);

    #read settings from file
    def read_settings(self):
        if not self.settings.isWritable():
            infoString = unicode(_tr( "<strong>IPyConsole plugin</strong> cannot read settings file (%s).<br>Please check your settings and file permissions.")) %  unicode(self.settings.fileName())
            QMessageBox.information(self.iface.mainWindow(), _tr("IPyConsole settings"), infoString)


    # save to a file the settings array
    def store_settings(self):
        if not self.settings.isWritable():
            infoString = unicode(_tr( "<strong>IPyConsole plugin</strong> cannot write settings file (%s).<br>Please check your settings and file permissions.")) %  unicode(self.settings.fileName())
            QMessageBox.information(self.iface.mainWindow(), _tr("IPyConsole settings") ,infoString)
            return
        self.settings.sync()
        qDebug('IPyConsole settings written on ' + self.settings.fileName())

    # run
    def run(self, dock=False):
        # Checks if a console is open
        if self.status is not None:
            if (dock and self.status == 'docked') or (not dock and self.status == 'windowed'):
                return
            elif self.status == 'docked':
                # Close current
                self.dock.close()
            else:
                # Close current
                self.control.close()
        try:
            import IPython
            if IPython.version_info[:2] < (3, 1):
                raise ImportError
            from IPython.qt.console.rich_ipython_widget import RichIPythonWidget, IPythonWidget
            from IPython.qt.inprocess import QtInProcessKernelManager
            from IPython.lib import guisupport
            from qgis import core, gui

            app = guisupport.get_app_qt4()

            # Create an in-process kernel
            kernel_manager = QtInProcessKernelManager()
            kernel_manager.start_kernel()
            kernel = kernel_manager.kernel
            kernel.gui = 'qt4'
            #import pdb; pyqtRemoveInputHook(); pdb.set_trace()
            kernel.shell.push({
                'iface': self.iface,
                'canvas': self.canvas,
                'core' : core,
                'gui' : gui,
                'propertize': propertize,
                'plugin_instance' : self,
                'app': app,
            })
            if int(self.get_settings('propertize', DEFAULT_PROPERTIZE)):
                kernel.shell.ex('propertize(core)')
                kernel.shell.ex('propertize(gui)')
            # Import in the current namespace
            kernel.shell.ex('from PyQt4.QtCore import *')
            kernel.shell.ex('from PyQt4.QtGui import *')
            kernel.shell.ex('from qgis.core import *')
            kernel.shell.ex('from qgis.gui import *')


            kernel_client = kernel_manager.client()
            kernel_client.start_channels()

            def stop():
                kernel_client.stop_channels()
                kernel_manager.shutdown_kernel()
                # No: this exits QGIS!
                #app.exit()
                self.status = None
                self.control = None
                self.dock = None

             # or RichIPythonWidget
            class myWidget(IPythonWidget):
                def closeEvent(self, event):
                    stop()
                    event.accept()

                def resizeEvent(self, event):
                    super(myWidget, self).resizeEvent(event)
                    self.console_resize()
                    event.accept()

                def get_columns(self):
                    font_width = QFontMetrics(self.font).width(' ')
                    return self.size().width() / font_width

                def console_resize(self):
                    self.width = self.get_columns()

            class myDock(QDockWidget):
                def closeEvent(self, event):
                    stop()
                    event.accept()


            # IPythonWidget.gui_completion : ‘plain’|’droplist’|’ncurses’
            # IPythonWidget.height : Integer
            # IPythonWidget.width : Integer
            # TODO: settings
            # myWidget.width = 160
            myWidget.gui_completion = 'plain'
            myWidget.paging = 'none'
            self.control = myWidget()

            # Font size regulation
            #self.control.change_font_size(-1)
            font = self.control.font
            font.setPointSize(int(self.get_settings('font_size', DEFAULT_FONT_SIZE)))
            self.control._set_font(font)
            self.control.kernel_manager = kernel_manager
            self.control.kernel_client = kernel_client
            self.control.exit_requested.connect(stop)
            #import pdb; pyqtRemoveInputHook(); pdb.set_trace()

            if not dock:
                self.status = 'windowed'
                self.control.show()
            else:
                self.status = 'docked'
                self.dock = myDock()
                self.dock.setWidget(self.control)
                self.iface.addDockWidget(Qt.BottomDockWidgetArea, self.dock)

            #import pdb; pyqtRemoveInputHook(); pdb.set_trace()
            def shout():
                from IPython.core.usage import default_gui_banner
                self.control._control.clear()
                self.control._reading = False
                self.control._highlighter.highlighting_on = False
                self.control._append_before_prompt_pos = self.control._get_cursor().position()
                if int(self.get_settings('show_help', DEFAULT_SHOW_HELP)):
                    self.control._append_html('<small>%s</small>' % default_gui_banner.replace('\n', '<br>').strip())
                    if int(self.get_settings('propertize', DEFAULT_PROPERTIZE)):
                        propertize_text = ("""All returning-something and no-args <code>core</code> and <code>gui</code> <code>Qgs*</code> class members have a <code>p_*</code> equivalent property to ease class introspection with <strong>TAB</strong> completion.""")
                    else:
                        propertize_text = _tr("""Propertize has been disabled, you can re-activate it in the pugin's settings.""")
                    self.control._append_html( _tr("""<br><h3>Welcome to QGIS <a href="https://ipython.org/">IPython</a> Console</h3>
                    You have access to <code>canvas</code>, <code>iface</code>, <code>app</code> (QGIS application) objects and to all <code>qgis</code> and <code>PyQt4</code> <code>core</code> and <code>gui</code> modules directly from the shell. %s Don't forget that you have access to all your underlying shell commands too!<br>
                    <em>Enjoy IPyConsole! Another hack by <a href="http://www.itopen.it">ItOpen</a></em></br>
                    """) % propertize_text)

            def monkey_patch_columnize(control):
                """As the name suggests... dynamic column number: stock
                qtconsole doesn't resize its column number on window
                resize but sticks to 80"""
                from IPython.qt.console.completion_plain import text
                old_columnize = text.columnize
                def new_columnize(items, separator='  ', displaywidth=80):
                    displaywidth = control.get_columns()
                    return old_columnize(items, separator, displaywidth)
                text.columnize = new_columnize

            monkey_patch_columnize(self.control)
            QTimer.singleShot(0, shout)

        except ImportError, e:
            QMessageBox.information(self.iface.mainWindow(), _tr(u'Error'), _tr(u'You need to install <b>IPython >= 3.1</b> (and then restart QGIS) before running this <b>IPyConsole</b> plugin.<br>IPython can be installed with <code>pip install "ipython[all]"</code>. More informations about IPython installation on <a href="https://ipython.org/install.html">https://ipython.org/install.html</a><br>The exception message is: %s') % e)


if __name__ == "__main__":
    pass
