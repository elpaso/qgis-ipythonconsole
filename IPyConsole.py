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
from qgis.core import *

from propertize import propertize
import resources

class IPyConsole:

    # Store status
    status = None

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = iface.mapCanvas()

    def initGui(self):
        # Create action that will start plugin
        self.action = QAction(QIcon(":/plugins/IPyConsole/icons/icon.png"), \
            QCoreApplication.translate("IPyConsole", "&IPython QGIS Console"), self.iface.mainWindow())
        self.docked_action = QAction(QIcon(":/plugins/IPyConsole/icons/icon.png"), \
            QCoreApplication.translate("IPyConsole", "&Docked"), self.iface.mainWindow())
        self.windowed_action = QAction(QIcon(":/plugins/IPyConsole/icons/icon.png"), \
            QCoreApplication.translate("IPyConsole", "&Windowed"), self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.docked_action, SIGNAL("activated()"), self.docked)
        QObject.connect(self.windowed_action, SIGNAL("activated()"), self.windowed)
        QObject.connect(self.action, SIGNAL("activated()"), self.default)

        # Add toolbar button
        self.iface.addToolBarIcon(self.action)

        # Build menu
        self.menu = QMenu(QCoreApplication.translate("IPyConsole", "&IPython QGIS Console"))
        self.menu.setIcon(QIcon(":/plugins/IPyConsole/icons/icon.png"))
        self.menu.addActions([self.docked_action, self.windowed_action])
        self.iface.pluginMenu().addMenu( self.menu )


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("IPyConsole", self.docked_action)
        self.iface.removePluginMenu("IPyConsole", self.windowed_action)
        self.iface.removeToolBarIcon(self.action)


    def default(self):
        """TODO: read config setting for default window type"""
        self.run(dock=False)

    def windowed(self):
        self.run(dock=False)

    def docked(self):
        self.run(dock=True)

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
            kernel.shell.ex('propertize(core)')
            kernel.shell.ex('propertize(gui)')

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

            class myWidget(IPythonWidget):
                def closeEvent(self, event):
                    stop()
                    event.accept()

            class myDock(QDockWidget):
                def closeEvent(self, event):
                    stop()
                    event.accept()

            #control = RichIPythonWidget()
            # Poor version
            # IPythonWidget.gui_completion : ‘plain’|’droplist’|’ncurses’
            # IPythonWidget.height : Integer
            # IPythonWidget.width : Integer
            # TODO: configurable
            myWidget.gui_completion = 'plain'
            myWidget.paging = 'none'
            self.control = myWidget()

            # Font size regulation
            # TODO: configurable
            #self.control.change_font_size(-1)
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
                self.control._append_html('<small>%s</small>' % default_gui_banner.replace('\n', '<br>').strip())
                self.control._append_html( QCoreApplication.translate("IPyConsole", """<br><h3>Welcome to QGIS <a href="https://ipython.org/">IPython</a> Console</h3>
                You have access to <code>canvas</code>, <code>iface</code>, <code>app</code> (QGIS application) objects and to <code>core</code> and <code>gui</code> QGIS modules. All returning-something and no-args <code>core.Qgs*</code> and <code>gui.Qgs*</code> class members have a <code>p_*</code> equivalent property to ease class introspection with <strong>TAB</strong> completion.<br>
                <em>Enjoy IPyConsole!</em><br><small> Another hack by <a href="http://www.itopen.it">ItOpen</a></small><br>
                """))

            QTimer.singleShot(0, shout)



        except ImportError:
            QMessageBox.information(self.iface.mainWindow(),  QCoreApplication.translate("IPyConsole", u'Error'), QCoreApplication.translate("IPyConsole", u'You need to install <b>IPython</b> (and then restart QGIS) before running this plugin.<br>IPython can be installed with <code>pip install IPython</code>.'))


if __name__ == "__main__":
    pass
