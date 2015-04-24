# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SettingsDialog.ui'
#
# Created: Fri Apr 24 15:55:59 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(1115, 710)
        self.gridLayout_2 = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setAccessibleName(_fromUtf8(""))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.windowModeFloating = QtGui.QRadioButton(self.groupBox)
        self.windowModeFloating.setObjectName(_fromUtf8("windowModeFloating"))
        self.verticalLayout_5.addWidget(self.windowModeFloating)
        self.windowModeDocked = QtGui.QRadioButton(self.groupBox)
        self.windowModeDocked.setObjectName(_fromUtf8("windowModeDocked"))
        self.verticalLayout_5.addWidget(self.windowModeDocked)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.fontSize = QtGui.QSpinBox(self.tab)
        self.fontSize.setMinimum(6)
        self.fontSize.setMaximum(40)
        self.fontSize.setProperty("value", 10)
        self.fontSize.setObjectName(_fromUtf8("fontSize"))
        self.gridLayout.addWidget(self.fontSize, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.auto_open = QtGui.QCheckBox(self.tab)
        self.auto_open.setObjectName(_fromUtf8("auto_open"))
        self.gridLayout_3.addWidget(self.auto_open, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.propertize = QtGui.QCheckBox(self.tab_3)
        self.propertize.setObjectName(_fromUtf8("propertize"))
        self.gridLayout_6.addWidget(self.propertize, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_7.addWidget(self.label_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings", None))
        self.groupBox.setTitle(_translate("SettingsDialog", "Default window mode", None))
        self.windowModeFloating.setText(_translate("SettingsDialog", "floating", None))
        self.windowModeDocked.setText(_translate("SettingsDialog", "docked", None))
        self.label_2.setText(_translate("SettingsDialog", "Console font size", None))
        self.auto_open.setText(_translate("SettingsDialog", "Launch automatically when QGIS starts", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "General", None))
        self.label_4.setText(_translate("SettingsDialog", "<h3>Python code configuration</h3>\n"
"<p><code>propertize</code> adds <code>p_</code> prefixed alias properties for all (0-arguments and returning-something) functions in <code>Qgs*</code> classes from <code>qgis.core</code> and  <code>qgis.gui</code> modules.</p>\n"
"<p>This is extremely useful when working with IPython\'s amazing <b>TAB</b> completion feature.</b>\n"
"<p>For example, you will be able to <b>TAB</b>-complete the following statement in IPython console:\n"
"<pre>\n"
"registry = core.QgsMapLayerRegistry.instance()\n"
"layer = registry.p_mapLayers.values()[0]\n"
"layer.p_crs.p_authid\n"
"</pre>\n"
"</p>", None))
        self.propertize.setText(_translate("SettingsDialog", "Enable propertize", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingsDialog", "Python", None))
        self.label.setText(_translate("SettingsDialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">IPython QGIS Console </span></p><p>An IPython interactive console with batteries included. </p><p><a href=\"http://www.itopen.it/qgis-and-ipython-the-definitive-interactive-console/\"><span style=\" text-decoration: underline; color:#0057ae;\">Plugin Home Page</span></a>  (feed-back is highly appreciated!)</p><p><a href=\"http://www.ipython.org\"><span style=\" text-decoration: underline; color:#0057ae;\">IPython Home Page</span></a></p><p><a href=\"https://github.com/elpaso/qgis-ipythonconsole\"><span style=\" text-decoration: underline; color:#0057ae;\">Source Code and Bug Tracker</span></a></p><p><b>Do you like IPyConsole? Make a <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XEXYSQAQQYZGS\"><span style=\" text-decoration: underline; color:#0057ae;\">small donation</span></a> to keep this project alive! <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XEXYSQAQQYZGS\"><img src=\":/plugins/IPyConsole/icons/paypal.png\"/></a></b></p>\n"
"<p><i>Enjoy IPyConsole!<br>Made in Italy by<a href=\"http://www.itopen.it\"><span style=\" text-decoration: underline; color:#0057ae;\"> Alessandro Pasotti (ItOpen)</a></i></p> </body></html>", None))
        self.label_3.setText(_translate("SettingsDialog", "<html><head/><body><p><img src=\":/plugins/IPyConsole/icons/icon.png\"/></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "About", None))

import resources_rc
