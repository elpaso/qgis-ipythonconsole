# -*- coding: utf-8 -*-

"""
***************************************************************************
    IPyConsole.py
    ---------------------
    Begin                : April 2015
    Date                 : June 2020
    Copyright            : (C) 2015-2020 by Alessandro Pasotti (ItOpen)
    Email                : apasotti at gmail dot com
    Email                : brookforestscitech at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

import os
import inspect

__authors__ = ['Alessandro Pasotti', 'Sean Barnett']
__date__ = 'June 2020'
__copyright__ = '(C) 2015-2020, Alessandro Pasotti'


# Import the PyQt and QGIS libraries
from qgis.core import Qgis
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt import uic
os.environ['QT_API'] = 'pyqt5'


from qgis.core import *
from .propertize import propertize

PLUGIN_DOMAIN = "IPyConsole"

# Defaults for settings
DEFAULT_WINDOW_MODE = 'docked'
DEFAULT_FONT_SIZE = 10
DEFAULT_PROPERTIZE = 1
DEFAULT_AUTO_OPEN = 0
DEFAULT_SHOW_HELP = 1
DEFAULT_THEME = 'light'


class SettingsDialog(QDialog):
    """Dumb dialog for settings"""

    def __init__(self, console_font):
        super(SettingsDialog, self).__init__()
        self.console_font = console_font
        uic.loadUi(os.path.join(os.path.dirname(
            __file__), 'Ui_SettingsDialog.ui'), self)
        QMetaObject.connectSlotsByName(self)
        self.update_label()
        self.btn_fontEdit.clicked.connect(self.on_fontEdit_clicked)

    def update_label(self):
        self.lbl_font.setFont(self.console_font)
        self.lbl_font.setText(_tr("Current console font (%s [%s])" % (
            self.console_font.family(), self.console_font.pointSize())))

    def on_fontEdit_clicked(self):
        fd = QFontDialog()
        (font, ok) = fd.getFont(self.console_font)
        if ok:
            self.console_font = font
            self.update_label()


def _tr(s):
    """Translate, save some typing"""
    return QCoreApplication.translate(PLUGIN_DOMAIN, s)


class IPyConsole:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.status = None
        self.control = None
        self.console_font = None
        self.settingsDlg = None
        self.dock = None
        self.settings = QSettings('ItOpen', PLUGIN_DOMAIN)
        # If auto_open: connect
        if int(self.get_settings('auto_open', DEFAULT_AUTO_OPEN)):
            if self.get_settings('default_window_mode', DEFAULT_WINDOW_MODE) == 'windowed':
                self.iface.mapCanvas().renderStarting.connect(self.default)
            else:
                self.default()

    def initGui(self):
        # Create action that will start plugin
        current_directory = os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.default_action = QAction(QIcon(os.path.join(current_directory, "icons", "icon.png")),
                                      _tr("&IPython QGIS Console"), self.iface.mainWindow())
        self.docked_action = QAction(QIcon(os.path.join(current_directory, "icons", "icon.png")),
                                     _tr("&Docked"), self.iface.mainWindow())
        self.windowed_action = QAction(QIcon(os.path.join(current_directory, "icons", "icon.png")),
                                       _tr("&Windowed"), self.iface.mainWindow())
        self.settings_action = QAction(QIcon(os.path.join(current_directory, "icons", "settings.svg")),
                                       _tr("&Settings"), self.iface.mainWindow())

        # connect the actions to the methods
        self.docked_action.triggered.connect(self.docked)
        self.windowed_action.triggered.connect(self.windowed)
        self.default_action.triggered.connect(self.default)
        self.settings_action.triggered.connect(self.show_settings)

        # Add toolbar button
        self.iface.addToolBarIcon(self.default_action)

        # Build menu
        self.menu = QMenu(_tr("&IPython QGIS Console"))
        self.menu.setIcon(
            QIcon(os.path.join(current_directory, "icons", "icon.png")))
        self.menu.addActions(
            [self.docked_action, self.windowed_action, self.settings_action])
        self.iface.pluginMenu().addMenu(self.menu)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("IPyConsole", self.docked_action)
        self.iface.removePluginMenu("IPyConsole", self.windowed_action)
        self.iface.removePluginMenu("IPyConsole", self.settings_action)
        self.iface.removeToolBarIcon(self.default_action)
        if hasattr(self, 'dock') and self.dock is not None:
            self.dock.close()
        if hasattr(self, 'control') and self.control is not None:
            self.control.close()

    def default(self):
        """TODO: read settings setting for default window type"""
        try:
            # Disconnect the signal if it was connected to allow auto_open
            self.iface.mapCanvas().renderStarting.disconnect(self.default)
        except TypeError:
            pass

        is_docked = self.get_settings(
            'default_window_mode', DEFAULT_WINDOW_MODE) == 'docked'
        selected_theme = self.get_settings('theme_setting', DEFAULT_THEME)
        self.run(dock=is_docked, theme=selected_theme)

    def windowed(self):
        selected_theme = self.get_settings('theme_setting', DEFAULT_THEME)
        self.run(dock=False, theme=selected_theme)

    def docked(self):
        selected_theme = self.get_settings('theme_setting', DEFAULT_THEME)
        self.run(dock=True, theme=selected_theme)

    def set_font(self):
        """Read font from settings"""
        font_family = self.get_settings('font_family', QFont().family())
        font_size = int(self.get_settings('font_size', DEFAULT_FONT_SIZE))
        font = QFont(font_family, font_size)
        self.console_font = font

    def show_settings(self):
        if self.settingsDlg is None:
            self.read_settings()
            self.set_font()
            self.settingsDlg = SettingsDialog(self.console_font)

            # Set values - window mode
            winmode = self.get_settings(
                'default_window_mode', DEFAULT_WINDOW_MODE)
            if winmode == 'docked':
                self.settingsDlg.windowModeDocked.setChecked(True)
            else:
                self.settingsDlg.windowModeFloating.setChecked(True)

            # Set values - theme
            theme = self.get_settings('theme_setting', DEFAULT_THEME)
            if theme == 'light':
                self.settingsDlg.lightTheme.setChecked(True)
            elif theme == 'dark':
                self.settingsDlg.darkTheme.setChecked(True)
            else:
                self.settingsDlg.bwTheme.setChecked(True)

            propertize_setting = self.get_settings(
                'propertize', DEFAULT_PROPERTIZE)
            self.settingsDlg.propertize.setChecked(int(propertize_setting))
            auto_open = self.get_settings('auto_open', DEFAULT_AUTO_OPEN)
            self.settingsDlg.auto_open.setChecked(int(auto_open))
            show_help = self.get_settings('show_help', DEFAULT_SHOW_HELP)
            self.settingsDlg.show_help.setChecked(int(show_help))

        self.settingsDlg.show()
        self.settingsDlg.adjustSize()
        result = self.settingsDlg.exec_()
        if result:
            self.set_settings(
                'font_family', self.settingsDlg.console_font.family())
            self.set_settings(
                'font_size', self.settingsDlg.console_font.pointSize())
            self.set_font()

            if self.control is not None:
                self.control._set_font(self.console_font)
            if self.settingsDlg.windowModeFloating.isChecked():
                winmode = 'windowed'
            elif self.settingsDlg.windowModeDocked.isChecked():
                winmode = 'docked'

            if self.settingsDlg.lightTheme.isChecked():
                theme = 'light'
            elif self.settingsDlg.darkTheme.isChecked():
                theme = 'dark'
            else:
                theme = 'black and white'

            self.set_settings('default_window_mode', winmode)
            self.set_settings('theme_setting', theme)
            self.set_settings('propertize', int(
                self.settingsDlg.propertize.isChecked()))
            self.set_settings('auto_open', int(
                self.settingsDlg.auto_open.isChecked()))
            self.set_settings('show_help', int(
                self.settingsDlg.show_help.isChecked()))
            self.store_settings()

    # return a settings parameter
    def get_settings(self, key, default=''):
        return self.settings.value(key, default)

   # set a settings parameter
    def set_settings(self, key, value):
        return self.settings.setValue(key, value)

    # read settings from file
    def read_settings(self):
        if not self.settings.isWritable():
            infoString = unicode(_tr(
                "<strong>IPyConsole plugin</strong> cannot read settings file (%s).<br>Please check your settings and file permissions.")) % unicode(self.settings.fileName())
            QMessageBox.information(self.iface.mainWindow(), _tr(
                "IPyConsole settings"), infoString)

    # save to a file the settings array
    def store_settings(self):
        if not self.settings.isWritable():
            infoString = unicode(_tr(
                "<strong>IPyConsole plugin</strong> cannot write settings file (%s).<br>Please check your settings and file permissions.")) % unicode(self.settings.fileName())
            QMessageBox.information(self.iface.mainWindow(), _tr(
                "IPyConsole settings"), infoString)
            return
        self.settings.sync()

    # run
    def run(self, dock=False, theme='light'):
        # Checks if a console is open
        if self.status is not None:
            if (dock and self.status == 'docked') or (not dock and self.status == 'windowed'):
                if self.status == 'windowed':
                    self.control.raise_()
                    self.control.activateWindow()
                return
            elif self.status == 'docked':
                # Close current
                if self.dock is not None:
                    self.dock.close()
            else:
                # Close current
                self.control.close()
        try:
            from qtconsole.rich_jupyter_widget import RichJupyterWidget
        except ImportError as e:
            error_message = _tr('You need to install <b>Jupyter 1.0.0</b> (and then restart QGIS) before running this <b>IPyConsole</b> plugin.<br>IPython can be installed with <code>pip install jupyter==1.0.0</code>. More informations about IPython installation on <a href="https://ipython.org/install.html">https://ipython.org/install.html</a>. Windows users might need to run the commands as admin in the OSGEO Command Shell.<br>The exception message is: %s') % e
            QMessageBox.information(
                self.iface.mainWindow(), _tr(u'Error'), error_message)

        import io
        import sys
        sys.stdout = sys.stderr = io.StringIO()
        from qtconsole.inprocess import QtInProcessKernelManager

        from qgis import core, gui

       # Create an in-process kernel
        kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel = kernel_manager.kernel
        kernel.gui = 'qt'
        kernel.shell.push({
            'iface': self.iface,
            'canvas': self.canvas,
            'core': core,
            'gui': gui,
            'propertize': propertize,
            'plugin_instance': self,
            #'app': app,
        })

        if int(self.get_settings('propertize', DEFAULT_PROPERTIZE)):
            kernel.shell.ex('propertize(core)')
            kernel.shell.ex('propertize(gui)')
        # Import in the current namespace
        kernel.shell.ex('from qgis.PyQt.QtCore import *')
        kernel.shell.ex('from qgis.PyQt.QtGui import *')
        kernel.shell.ex('from qgis.core import *')
        kernel.shell.ex('from qgis.gui import *')

        kernel_client = kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            # No: this exits QGIS!
            # app.exit()
            self.status = None
            self.control = None
            self.dock = None

         # or RichJupyterWidget
        class myWidget(RichJupyterWidget):
            def closeEvent(self, event):
                stop()
                event.accept()

            def resizeEvent(self, event):
                super(myWidget, self).resizeEvent(event)
                self.console_resize()
                event.accept()

            def get_columns(self):
                try:
                    font_width = QFontMetrics(self.font).width(' ')
                except TypeError:
                    font_width = 10
                return int(self.size().width() / font_width)

            def console_resize(self):
                self.width = self.get_columns()

            def set_theme(self):
                if theme == 'light':
                    self.set_default_style(colors='lightbg')
                elif theme == 'dark':
                    self.set_default_style(colors='linux')
                else:
                    self.set_default_style(colors='nocolor')

        class myDock(QDockWidget):
            def closeEvent(self, event):
                stop()
                event.accept()

        # TODO: settings
        # myWidget.width = 160
        myWidget.gui_completion = 'plain'
        myWidget.paging = 'none'
        self.control = myWidget()

        self.control.kernel_manager = kernel_manager
        self.control.kernel_client = kernel_client
        self.control.exit_requested.connect(stop)

        if not dock:
            self.status = 'windowed'
            self.control.show()
            self.control.set_theme()
        else:
            self.status = 'docked'
            self.dock = myDock()
            self.control.set_theme()
            self.dock.setWidget(self.control)
            self.iface.addDockWidget(Qt.BottomDockWidgetArea, self.dock)

        # Font size regulation
        self.set_font()
        self.control._set_font(self.console_font)

        def shout():
            from IPython.core import usage
            self.control._control.clear()
            self.control._reading = False
            self.control._highlighter.highlighting_on = False
            try:
                self.control._append_before_prompt_pos = self.control._get_cursor().position()
            except Exception as ex:
                # Can't set attribute .... on mac/win
                pass
            if int(self.get_settings('show_help', DEFAULT_SHOW_HELP)):
                try:
                    banner = usage.default_banner
                except:
                    try:
                        banner = ' '.join(usage.default_banner_parts)
                    except:
                        banner = ''
                self.control._append_html(
                    '<small>%s</small>' % banner.replace('\n', '<br>').strip())
                if int(self.get_settings('propertize', DEFAULT_PROPERTIZE)):
                    propertize_text = (
                        """All returning-something and no-args <code>core</code> and <code>gui</code> <code>Qgs*</code> class members have a <code>p_*</code> equivalent property to ease class introspection with <strong>TAB</strong> completion.""")
                else:
                    propertize_text = _tr(
                        """Propertize has been disabled, you can re-activate it in the pugin's settings.""")
                self.control._append_html(_tr("""<br><h3>Welcome to QGIS <a href="https://ipython.org/">IPython</a> Console</h3>
                You have access to <code>canvas</code>, <code>iface</code>, <code>app</code> (QGIS application) objects and to all <code>qgis</code> and <code>PyQt</code> <code>core</code> and <code>gui</code> modules directly from the shell. %s Don't forget that you have access to all your underlying shell commands too!<br>
                <em>Enjoy IPyConsole! Another hack by <a href="http://www.itopen.it">ItOpen</a></em></br>
                """) % propertize_text)

        def monkey_patch_columnize(control):
            """As the name suggests... dynamic column number: stock
            qtconsole doesn't resize its column number on window
            resize but sticks to 80"""
            from qtconsole.util import columnize

            old_columnize = columnize

            def new_columnize(control):
                items = [sug["text"] for sug in control.get_suggestions()]
                displaywidth = control.get_columns()
                separator = "  "
                return old_columnize(items, separator, displaywidth)

            columnize = new_columnize

        monkey_patch_columnize(self.control)
        QTimer.singleShot(0, shout)


if __name__ == "__main__":
    pass
