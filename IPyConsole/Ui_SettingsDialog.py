# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

try:
    from PyQt5 import QtCore, QtGui, QtWidgets
except:
    from PyQt4 import QtCore, QtGui as QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(300, 200)
        self.gridLayout_2 = QtWidgets.QGridLayout(SettingsDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleName("")
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.auto_open = QtWidgets.QCheckBox(self.groupBox_2)
        self.auto_open.setObjectName("auto_open")
        self.gridLayout_8.addWidget(self.auto_open, 1, 0, 1, 1)
        self.show_help = QtWidgets.QCheckBox(self.groupBox_2)
        self.show_help.setObjectName("show_help")
        self.gridLayout_8.addWidget(self.show_help, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 964, 2))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.windowModeFloating = QtWidgets.QRadioButton(self.groupBox)
        self.windowModeFloating.setObjectName("windowModeFloating")
        self.verticalLayout_5.addWidget(self.windowModeFloating)
        self.windowModeDocked = QtWidgets.QRadioButton(self.groupBox)
        self.windowModeDocked.setObjectName("windowModeDocked")
        self.verticalLayout_5.addWidget(self.windowModeDocked)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.fontSize = QtWidgets.QSpinBox(self.tab)
        self.fontSize.setMinimum(6)
        self.fontSize.setMaximum(40)
        self.fontSize.setProperty("value", 10)
        self.fontSize.setObjectName("fontSize")
        self.gridLayout.addWidget(self.fontSize, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 7, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.propertize = QtWidgets.QCheckBox(self.tab_3)
        self.propertize.setObjectName("propertize")
        self.gridLayout_6.addWidget(self.propertize, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Startup options"))
        self.auto_open.setText(_translate("SettingsDialog", "Launch automatically when QGIS starts"))
        self.show_help.setText(_translate("SettingsDialog", "Show help message when IPyConsole starts"))
        self.groupBox.setTitle(_translate("SettingsDialog", "Default window mode"))
        self.windowModeFloating.setText(_translate("SettingsDialog", "floating"))
        self.windowModeDocked.setText(_translate("SettingsDialog", "docked"))
        self.label_2.setText(_translate("SettingsDialog", "Console font size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "General"))
        self.label_4.setText(_translate("SettingsDialog", "<p><code><b>propertize</b></code> adds <code><b>p_</b></code> prefixed alias properties for all (0-arguments and returning-something) functions in <code><b>Qgs*</b></code> classes from <code><b>qgis.core</b></code> and  <code><b>qgis.gui</b></code> modules.</p>\n"
"<p>This is extremely useful when working with IPython\'s amazing <b>TAB</b> completion feature.</b>\n"
"<p>For example, you will be able to <b>TAB</b>-complete the following statement in IPython console:\n"
"<pre><b>\n"
"registry = core.QgsMapLayerRegistry.instance()\n"
"layer = registry.p_mapLayers.values()[0]\n"
"layer.p_crs.p_authid\n"
"</b></pre>\n"
"</p>"))
        self.propertize.setText(_translate("SettingsDialog", "Enable propertize"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingsDialog", "Python"))
        self.label.setText(_translate("SettingsDialog", "<html><head/><body><p><span style=\" font-size:xx-large; font-weight:600;\">IPython QGIS Console </span></p><p>An IPython interactive console with batteries included. </p><p><a href=\"http://www.itopen.it/qgis-and-ipython-the-definitive-interactive-console/\"><span style=\" text-decoration: underline; color:#0057ae;\">Plugin Home Page</span></a>  (feed-back is highly appreciated!)</p><p><a href=\"http://www.ipython.org\"><span style=\" text-decoration: underline; color:#0057ae;\">IPython Home Page</span></a></p><p><a href=\"https://github.com/elpaso/qgis-ipythonconsole\"><span style=\" text-decoration: underline; color:#0057ae;\">Source Code and Bug Tracker</span></a></p><p><b>Do you like IPyConsole? Make a <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XEXYSQAQQYZGS\"><span style=\" text-decoration: underline; color:#0057ae;\">small donation</span></a> to keep this project alive! <a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=XEXYSQAQQYZGS\"><img src=\":/plugins/IPyConsole/icons/paypal.png\"/></a></b></p>\n"
"<p><i>Enjoy IPyConsole!<br>Made in Italy by<a href=\"http://www.itopen.it\"><span style=\" text-decoration: underline; color:#0057ae;\"> Alessandro Pasotti (ItOpen)</a></i></p> </body></html>"))
        self.label_3.setText(_translate("SettingsDialog", "<html><head/><body><p><img src=\":/plugins/IPyConsole/icons/icon.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "About"))

from . import resources_rc
