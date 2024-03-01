# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIComps/QTGeneration/AlertWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.main = QtWidgets.QWidget(MainWindow)
        self.main.setObjectName("main")
        self.gridLayout = QtWidgets.QGridLayout(self.main)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.main)
        self.tabWidget.setObjectName("tabWidget")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stock_count_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stock_count_label.sizePolicy().hasHeightForWidth())
        self.stock_count_label.setSizePolicy(sizePolicy)
        self.stock_count_label.setObjectName("stock_count_label")
        self.gridLayout_2.addWidget(self.stock_count_label, 4, 3, 1, 1)
        self.list_selection_button = QtWidgets.QPushButton(self.centralwidget)
        self.list_selection_button.setObjectName("list_selection_button")
        self.gridLayout_2.addWidget(self.list_selection_button, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 4, 2, 1, 1)
        self.rotation_button = QtWidgets.QPushButton(self.centralwidget)
        self.rotation_button.setObjectName("rotation_button")
        self.gridLayout_2.addWidget(self.rotation_button, 3, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.data_listen_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.data_listen_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.data_listen_checkbox.setObjectName("data_listen_checkbox")
        self.verticalLayout.addWidget(self.data_listen_checkbox)
        self.alert_box_rsi = QtWidgets.QCheckBox(self.centralwidget)
        self.alert_box_rsi.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.alert_box_rsi.setChecked(True)
        self.alert_box_rsi.setObjectName("alert_box_rsi")
        self.verticalLayout.addWidget(self.alert_box_rsi)
        self.alert_box_steps = QtWidgets.QCheckBox(self.centralwidget)
        self.alert_box_steps.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.alert_box_steps.setChecked(True)
        self.alert_box_steps.setObjectName("alert_box_steps")
        self.verticalLayout.addWidget(self.alert_box_steps)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.centralwidget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.cross_box_15m = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_15m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_15m.setChecked(True)
        self.cross_box_15m.setObjectName("cross_box_15m")
        self.gridLayout_3.addWidget(self.cross_box_15m, 5, 2, 1, 1)
        self.reversal_box_1m = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_1m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_1m.setChecked(True)
        self.reversal_box_1m.setObjectName("reversal_box_1m")
        self.gridLayout_3.addWidget(self.reversal_box_1m, 1, 6, 1, 1)
        self.higher_spin_3m = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_3m.setMaximum(100)
        self.higher_spin_3m.setProperty("value", 80)
        self.higher_spin_3m.setObjectName("higher_spin_3m")
        self.gridLayout_3.addWidget(self.higher_spin_3m, 3, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.cross_box_2m = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_2m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_2m.setChecked(True)
        self.cross_box_2m.setObjectName("cross_box_2m")
        self.gridLayout_3.addWidget(self.cross_box_2m, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)
        self.lower_spin_4h = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_4h.setMaximum(100)
        self.lower_spin_4h.setProperty("value", 20)
        self.lower_spin_4h.setObjectName("lower_spin_4h")
        self.gridLayout_3.addWidget(self.lower_spin_4h, 7, 3, 1, 1)
        self.higher_spin_1h = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_1h.setMaximum(100)
        self.higher_spin_1h.setProperty("value", 80)
        self.higher_spin_1h.setObjectName("higher_spin_1h")
        self.gridLayout_3.addWidget(self.higher_spin_1h, 6, 4, 1, 1)
        self.lower_spin_all = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_all.setMaximum(100)
        self.lower_spin_all.setProperty("value", 20)
        self.lower_spin_all.setObjectName("lower_spin_all")
        self.gridLayout_3.addWidget(self.lower_spin_all, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 6, 0, 1, 1)
        self.lower_spin_1h = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_1h.setMaximum(100)
        self.lower_spin_1h.setProperty("value", 20)
        self.lower_spin_1h.setObjectName("lower_spin_1h")
        self.gridLayout_3.addWidget(self.lower_spin_1h, 6, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.higher_spin_15m = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_15m.setMaximum(100)
        self.higher_spin_15m.setProperty("value", 80)
        self.higher_spin_15m.setObjectName("higher_spin_15m")
        self.gridLayout_3.addWidget(self.higher_spin_15m, 5, 4, 1, 1)
        self.cross_box_4h = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_4h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_4h.setChecked(True)
        self.cross_box_4h.setObjectName("cross_box_4h")
        self.gridLayout_3.addWidget(self.cross_box_4h, 7, 2, 1, 1)
        self.lower_spin_3m = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_3m.setMaximum(100)
        self.lower_spin_3m.setProperty("value", 20)
        self.lower_spin_3m.setObjectName("lower_spin_3m")
        self.gridLayout_3.addWidget(self.lower_spin_3m, 3, 3, 1, 1)
        self.reversal_box_2m = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_2m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_2m.setChecked(True)
        self.reversal_box_2m.setObjectName("reversal_box_2m")
        self.gridLayout_3.addWidget(self.reversal_box_2m, 2, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)
        self.reversal_box_all = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_all.setChecked(True)
        self.reversal_box_all.setObjectName("reversal_box_all")
        self.gridLayout_3.addWidget(self.reversal_box_all, 0, 6, 1, 1)
        self.higher_spin_2m = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_2m.setMaximum(100)
        self.higher_spin_2m.setProperty("value", 80)
        self.higher_spin_2m.setObjectName("higher_spin_2m")
        self.gridLayout_3.addWidget(self.higher_spin_2m, 2, 4, 1, 1)
        self.lower_spin_5m = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_5m.setMaximum(100)
        self.lower_spin_5m.setProperty("value", 20)
        self.lower_spin_5m.setObjectName("lower_spin_5m")
        self.gridLayout_3.addWidget(self.lower_spin_5m, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.cross_box_3m = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_3m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_3m.setChecked(True)
        self.cross_box_3m.setObjectName("cross_box_3m")
        self.gridLayout_3.addWidget(self.cross_box_3m, 3, 2, 1, 1)
        self.cross_box_1h = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_1h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_1h.setChecked(True)
        self.cross_box_1h.setObjectName("cross_box_1h")
        self.gridLayout_3.addWidget(self.cross_box_1h, 6, 2, 1, 1)
        self.cross_box_all = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_all.setChecked(True)
        self.cross_box_all.setObjectName("cross_box_all")
        self.gridLayout_3.addWidget(self.cross_box_all, 0, 2, 1, 1)
        self.higher_spin_all = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_all.setMaximum(100)
        self.higher_spin_all.setProperty("value", 80)
        self.higher_spin_all.setObjectName("higher_spin_all")
        self.gridLayout_3.addWidget(self.higher_spin_all, 0, 4, 1, 1)
        self.cross_box_5m = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_5m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_5m.setChecked(True)
        self.cross_box_5m.setObjectName("cross_box_5m")
        self.gridLayout_3.addWidget(self.cross_box_5m, 4, 2, 1, 1)
        self.higher_spin_1m = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_1m.setMaximum(100)
        self.higher_spin_1m.setProperty("value", 80)
        self.higher_spin_1m.setObjectName("higher_spin_1m")
        self.gridLayout_3.addWidget(self.higher_spin_1m, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 5, 1, 1)
        self.reversal_box_3m = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_3m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_3m.setChecked(True)
        self.reversal_box_3m.setObjectName("reversal_box_3m")
        self.gridLayout_3.addWidget(self.reversal_box_3m, 3, 6, 1, 1)
        self.reversal_box_4h = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_4h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_4h.setChecked(True)
        self.reversal_box_4h.setObjectName("reversal_box_4h")
        self.gridLayout_3.addWidget(self.reversal_box_4h, 7, 6, 1, 1)
        self.higher_spin_4h = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_4h.setMaximum(100)
        self.higher_spin_4h.setProperty("value", 80)
        self.higher_spin_4h.setObjectName("higher_spin_4h")
        self.gridLayout_3.addWidget(self.higher_spin_4h, 7, 4, 1, 1)
        self.cross_box_1m = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_1m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cross_box_1m.setChecked(True)
        self.cross_box_1m.setObjectName("cross_box_1m")
        self.gridLayout_3.addWidget(self.cross_box_1m, 1, 2, 1, 1)
        self.lower_spin_2m = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_2m.setMaximum(100)
        self.lower_spin_2m.setProperty("value", 20)
        self.lower_spin_2m.setObjectName("lower_spin_2m")
        self.gridLayout_3.addWidget(self.lower_spin_2m, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 7, 1, 1)
        self.reversal_box_5m = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_5m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_5m.setChecked(True)
        self.reversal_box_5m.setObjectName("reversal_box_5m")
        self.gridLayout_3.addWidget(self.reversal_box_5m, 4, 6, 1, 1)
        self.higher_spin_5m = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_5m.setMaximum(100)
        self.higher_spin_5m.setProperty("value", 80)
        self.higher_spin_5m.setObjectName("higher_spin_5m")
        self.gridLayout_3.addWidget(self.higher_spin_5m, 4, 4, 1, 1)
        self.reversal_box_15m = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_15m.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_15m.setChecked(True)
        self.reversal_box_15m.setObjectName("reversal_box_15m")
        self.gridLayout_3.addWidget(self.reversal_box_15m, 5, 6, 1, 1)
        self.lower_spin_15m = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_15m.setMaximum(100)
        self.lower_spin_15m.setProperty("value", 20)
        self.lower_spin_15m.setObjectName("lower_spin_15m")
        self.gridLayout_3.addWidget(self.lower_spin_15m, 5, 3, 1, 1)
        self.reversal_box_1h = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_1h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reversal_box_1h.setChecked(True)
        self.reversal_box_1h.setObjectName("reversal_box_1h")
        self.gridLayout_3.addWidget(self.reversal_box_1h, 6, 6, 1, 1)
        self.lower_spin_1m = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_1m.setMaximum(100)
        self.lower_spin_1m.setProperty("value", 20)
        self.lower_spin_1m.setObjectName("lower_spin_1m")
        self.gridLayout_3.addWidget(self.lower_spin_1m, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 8, 0, 1, 1)
        self.cross_box_1d = QtWidgets.QCheckBox(self.tab_2)
        self.cross_box_1d.setChecked(True)
        self.cross_box_1d.setObjectName("cross_box_1d")
        self.gridLayout_3.addWidget(self.cross_box_1d, 8, 2, 1, 1)
        self.lower_spin_1d = QtWidgets.QSpinBox(self.tab_2)
        self.lower_spin_1d.setProperty("value", 20)
        self.lower_spin_1d.setObjectName("lower_spin_1d")
        self.gridLayout_3.addWidget(self.lower_spin_1d, 8, 3, 1, 1)
        self.higher_spin_1d = QtWidgets.QSpinBox(self.tab_2)
        self.higher_spin_1d.setProperty("value", 80)
        self.higher_spin_1d.setObjectName("higher_spin_1d")
        self.gridLayout_3.addWidget(self.higher_spin_1d, 8, 4, 1, 1)
        self.reversal_box_1d = QtWidgets.QCheckBox(self.tab_2)
        self.reversal_box_1d.setChecked(True)
        self.reversal_box_1d.setObjectName("reversal_box_1d")
        self.gridLayout_3.addWidget(self.reversal_box_1d, 8, 6, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.up_spin_5m = QtWidgets.QSpinBox(self.tab)
        self.up_spin_5m.setMaximum(40)
        self.up_spin_5m.setProperty("value", 10)
        self.up_spin_5m.setObjectName("up_spin_5m")
        self.gridLayout_6.addWidget(self.up_spin_5m, 5, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 4, 0, 1, 1)
        self.down_check_2m = QtWidgets.QCheckBox(self.tab)
        self.down_check_2m.setChecked(True)
        self.down_check_2m.setObjectName("down_check_2m")
        self.gridLayout_6.addWidget(self.down_check_2m, 3, 5, 1, 1)
        self.up_check_1m = QtWidgets.QCheckBox(self.tab)
        self.up_check_1m.setChecked(True)
        self.up_check_1m.setObjectName("up_check_1m")
        self.gridLayout_6.addWidget(self.up_check_1m, 2, 2, 1, 1)
        self.down_check_1m = QtWidgets.QCheckBox(self.tab)
        self.down_check_1m.setChecked(True)
        self.down_check_1m.setObjectName("down_check_1m")
        self.gridLayout_6.addWidget(self.down_check_1m, 2, 5, 1, 1)
        self.down_spin_1m = QtWidgets.QSpinBox(self.tab)
        self.down_spin_1m.setMinimum(2)
        self.down_spin_1m.setMaximum(40)
        self.down_spin_1m.setProperty("value", 10)
        self.down_spin_1m.setObjectName("down_spin_1m")
        self.gridLayout_6.addWidget(self.down_spin_1m, 2, 6, 1, 1)
        self.down_check_1h = QtWidgets.QCheckBox(self.tab)
        self.down_check_1h.setChecked(True)
        self.down_check_1h.setObjectName("down_check_1h")
        self.gridLayout_6.addWidget(self.down_check_1h, 7, 5, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 3, 0, 1, 1)
        self.up_check_5m = QtWidgets.QCheckBox(self.tab)
        self.up_check_5m.setChecked(True)
        self.up_check_5m.setObjectName("up_check_5m")
        self.gridLayout_6.addWidget(self.up_check_5m, 5, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setObjectName("label_27")
        self.gridLayout_6.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 7, 0, 1, 1)
        self.down_check_4h = QtWidgets.QCheckBox(self.tab)
        self.down_check_4h.setChecked(True)
        self.down_check_4h.setObjectName("down_check_4h")
        self.gridLayout_6.addWidget(self.down_check_4h, 8, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 7, 1, 1)
        self.up_spin_15m = QtWidgets.QSpinBox(self.tab)
        self.up_spin_15m.setMaximum(40)
        self.up_spin_15m.setProperty("value", 10)
        self.up_spin_15m.setObjectName("up_spin_15m")
        self.gridLayout_6.addWidget(self.up_spin_15m, 6, 3, 1, 1)
        self.up_spin_3m = QtWidgets.QSpinBox(self.tab)
        self.up_spin_3m.setMaximum(40)
        self.up_spin_3m.setProperty("value", 10)
        self.up_spin_3m.setObjectName("up_spin_3m")
        self.gridLayout_6.addWidget(self.up_spin_3m, 4, 3, 1, 1)
        self.up_spin_all = QtWidgets.QSpinBox(self.tab)
        self.up_spin_all.setMaximum(100)
        self.up_spin_all.setProperty("value", 10)
        self.up_spin_all.setObjectName("up_spin_all")
        self.gridLayout_6.addWidget(self.up_spin_all, 0, 3, 1, 1)
        self.up_check_2m = QtWidgets.QCheckBox(self.tab)
        self.up_check_2m.setChecked(True)
        self.up_check_2m.setObjectName("up_check_2m")
        self.gridLayout_6.addWidget(self.up_check_2m, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 1, 1, 1)
        self.down_spin_3m = QtWidgets.QSpinBox(self.tab)
        self.down_spin_3m.setMinimum(2)
        self.down_spin_3m.setMaximum(40)
        self.down_spin_3m.setProperty("value", 10)
        self.down_spin_3m.setObjectName("down_spin_3m")
        self.gridLayout_6.addWidget(self.down_spin_3m, 4, 6, 1, 1)
        self.up_check_4h = QtWidgets.QCheckBox(self.tab)
        self.up_check_4h.setChecked(True)
        self.up_check_4h.setObjectName("up_check_4h")
        self.gridLayout_6.addWidget(self.up_check_4h, 8, 2, 1, 1)
        self.up_check_3m = QtWidgets.QCheckBox(self.tab)
        self.up_check_3m.setChecked(True)
        self.up_check_3m.setObjectName("up_check_3m")
        self.gridLayout_6.addWidget(self.up_check_3m, 4, 2, 1, 1)
        self.down_check_15m = QtWidgets.QCheckBox(self.tab)
        self.down_check_15m.setChecked(True)
        self.down_check_15m.setObjectName("down_check_15m")
        self.gridLayout_6.addWidget(self.down_check_15m, 6, 5, 1, 1)
        self.up_spin_1m = QtWidgets.QSpinBox(self.tab)
        self.up_spin_1m.setMaximum(100)
        self.up_spin_1m.setProperty("value", 10)
        self.up_spin_1m.setObjectName("up_spin_1m")
        self.gridLayout_6.addWidget(self.up_spin_1m, 2, 3, 1, 1)
        self.up_check_all = QtWidgets.QCheckBox(self.tab)
        self.up_check_all.setChecked(True)
        self.up_check_all.setObjectName("up_check_all")
        self.gridLayout_6.addWidget(self.up_check_all, 0, 2, 1, 1)
        self.up_spin_4h = QtWidgets.QSpinBox(self.tab)
        self.up_spin_4h.setMaximum(40)
        self.up_spin_4h.setProperty("value", 10)
        self.up_spin_4h.setObjectName("up_spin_4h")
        self.gridLayout_6.addWidget(self.up_spin_4h, 8, 3, 1, 1)
        self.down_spin_2m = QtWidgets.QSpinBox(self.tab)
        self.down_spin_2m.setMinimum(2)
        self.down_spin_2m.setMaximum(40)
        self.down_spin_2m.setProperty("value", 10)
        self.down_spin_2m.setObjectName("down_spin_2m")
        self.gridLayout_6.addWidget(self.down_spin_2m, 3, 6, 1, 1)
        self.down_spin_all = QtWidgets.QSpinBox(self.tab)
        self.down_spin_all.setMinimum(2)
        self.down_spin_all.setMaximum(40)
        self.down_spin_all.setProperty("value", 10)
        self.down_spin_all.setObjectName("down_spin_all")
        self.gridLayout_6.addWidget(self.down_spin_all, 0, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 0, 4, 1, 1)
        self.down_check_3m = QtWidgets.QCheckBox(self.tab)
        self.down_check_3m.setChecked(True)
        self.down_check_3m.setObjectName("down_check_3m")
        self.gridLayout_6.addWidget(self.down_check_3m, 4, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 5, 0, 1, 1)
        self.down_spin_1h = QtWidgets.QSpinBox(self.tab)
        self.down_spin_1h.setMinimum(2)
        self.down_spin_1h.setMaximum(40)
        self.down_spin_1h.setProperty("value", 10)
        self.down_spin_1h.setObjectName("down_spin_1h")
        self.gridLayout_6.addWidget(self.down_spin_1h, 7, 6, 1, 1)
        self.up_check_1h = QtWidgets.QCheckBox(self.tab)
        self.up_check_1h.setChecked(True)
        self.up_check_1h.setObjectName("up_check_1h")
        self.gridLayout_6.addWidget(self.up_check_1h, 7, 2, 1, 1)
        self.up_spin_2m = QtWidgets.QSpinBox(self.tab)
        self.up_spin_2m.setMaximum(40)
        self.up_spin_2m.setProperty("value", 10)
        self.up_spin_2m.setObjectName("up_spin_2m")
        self.gridLayout_6.addWidget(self.up_spin_2m, 3, 3, 1, 1)
        self.down_spin_4h = QtWidgets.QSpinBox(self.tab)
        self.down_spin_4h.setMinimum(2)
        self.down_spin_4h.setMaximum(40)
        self.down_spin_4h.setProperty("value", 10)
        self.down_spin_4h.setObjectName("down_spin_4h")
        self.gridLayout_6.addWidget(self.down_spin_4h, 8, 6, 1, 1)
        self.up_check_15m = QtWidgets.QCheckBox(self.tab)
        self.up_check_15m.setChecked(True)
        self.up_check_15m.setObjectName("up_check_15m")
        self.gridLayout_6.addWidget(self.up_check_15m, 6, 2, 1, 1)
        self.down_spin_5m = QtWidgets.QSpinBox(self.tab)
        self.down_spin_5m.setMinimum(2)
        self.down_spin_5m.setMaximum(40)
        self.down_spin_5m.setProperty("value", 10)
        self.down_spin_5m.setObjectName("down_spin_5m")
        self.gridLayout_6.addWidget(self.down_spin_5m, 5, 6, 1, 1)
        self.down_check_5m = QtWidgets.QCheckBox(self.tab)
        self.down_check_5m.setChecked(True)
        self.down_check_5m.setObjectName("down_check_5m")
        self.gridLayout_6.addWidget(self.down_check_5m, 5, 5, 1, 1)
        self.down_spin_15m = QtWidgets.QSpinBox(self.tab)
        self.down_spin_15m.setMinimum(2)
        self.down_spin_15m.setMaximum(40)
        self.down_spin_15m.setProperty("value", 10)
        self.down_spin_15m.setObjectName("down_spin_15m")
        self.gridLayout_6.addWidget(self.down_spin_15m, 6, 6, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 6, 0, 1, 1)
        self.up_spin_1h = QtWidgets.QSpinBox(self.tab)
        self.up_spin_1h.setMaximum(40)
        self.up_spin_1h.setProperty("value", 10)
        self.up_spin_1h.setObjectName("up_spin_1h")
        self.gridLayout_6.addWidget(self.up_spin_1h, 7, 3, 1, 1)
        self.down_check_all = QtWidgets.QCheckBox(self.tab)
        self.down_check_all.setChecked(True)
        self.down_check_all.setObjectName("down_check_all")
        self.gridLayout_6.addWidget(self.down_check_all, 0, 5, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 8, 0, 1, 1)
        self.up_check_1d = QtWidgets.QCheckBox(self.tab)
        self.up_check_1d.setChecked(True)
        self.up_check_1d.setObjectName("up_check_1d")
        self.gridLayout_6.addWidget(self.up_check_1d, 9, 2, 1, 1)
        self.down_check_1d = QtWidgets.QCheckBox(self.tab)
        self.down_check_1d.setChecked(True)
        self.down_check_1d.setObjectName("down_check_1d")
        self.gridLayout_6.addWidget(self.down_check_1d, 9, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 9, 0, 1, 1)
        self.up_spin_1d = QtWidgets.QSpinBox(self.tab)
        self.up_spin_1d.setProperty("value", 10)
        self.up_spin_1d.setObjectName("up_spin_1d")
        self.gridLayout_6.addWidget(self.up_spin_1d, 9, 3, 1, 1)
        self.down_spin_1d = QtWidgets.QSpinBox(self.tab)
        self.down_spin_1d.setProperty("value", 10)
        self.down_spin_1d.setObjectName("down_spin_1d")
        self.gridLayout_6.addWidget(self.down_spin_1d, 9, 6, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.main)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alerts"))
        self.stock_count_label.setText(_translate("MainWindow", "0"))
        self.list_selection_button.setText(_translate("MainWindow", "All On"))
        self.label_13.setText(_translate("MainWindow", "Stock count:"))
        self.rotation_button.setText(_translate("MainWindow", "Continuous Updates"))
        self.data_listen_checkbox.setText(_translate("MainWindow", "Alerting On"))
        self.alert_box_rsi.setText(_translate("MainWindow", "RSIs"))
        self.alert_box_steps.setText(_translate("MainWindow", "Steps"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.centralwidget), _translate("MainWindow", "Main"))
        self.label_12.setText(_translate("MainWindow", "All:"))
        self.cross_box_15m.setText(_translate("MainWindow", "Cross"))
        self.reversal_box_1m.setText(_translate("MainWindow", "Reversal"))
        self.label_7.setText(_translate("MainWindow", "5m"))
        self.cross_box_2m.setText(_translate("MainWindow", "Cross"))
        self.label_8.setText(_translate("MainWindow", "15m"))
        self.label_9.setText(_translate("MainWindow", "1h"))
        self.label_11.setText(_translate("MainWindow", "1m"))
        self.cross_box_4h.setText(_translate("MainWindow", "Cross"))
        self.reversal_box_2m.setText(_translate("MainWindow", "Reversal"))
        self.label_10.setText(_translate("MainWindow", "4h"))
        self.reversal_box_all.setText(_translate("MainWindow", "Reversal"))
        self.cross_box_3m.setText(_translate("MainWindow", "Cross"))
        self.cross_box_1h.setText(_translate("MainWindow", "Cross"))
        self.cross_box_all.setText(_translate("MainWindow", "Cross"))
        self.cross_box_5m.setText(_translate("MainWindow", "Cross"))
        self.reversal_box_3m.setText(_translate("MainWindow", "Reversal"))
        self.reversal_box_4h.setText(_translate("MainWindow", "Reversal"))
        self.cross_box_1m.setText(_translate("MainWindow", "Cross"))
        self.label_5.setText(_translate("MainWindow", "2m"))
        self.reversal_box_5m.setText(_translate("MainWindow", "Reversal"))
        self.reversal_box_15m.setText(_translate("MainWindow", "Reversal"))
        self.reversal_box_1h.setText(_translate("MainWindow", "Reversal"))
        self.label_6.setText(_translate("MainWindow", "3m"))
        self.label.setText(_translate("MainWindow", "1 d"))
        self.cross_box_1d.setText(_translate("MainWindow", "Cross"))
        self.reversal_box_1d.setText(_translate("MainWindow", "Reversal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "RSIs"))
        self.label_28.setText(_translate("MainWindow", "3m"))
        self.down_check_2m.setText(_translate("MainWindow", "Down"))
        self.up_check_1m.setText(_translate("MainWindow", "Up"))
        self.down_check_1m.setText(_translate("MainWindow", "Down"))
        self.down_check_1h.setText(_translate("MainWindow", "Down"))
        self.label_26.setText(_translate("MainWindow", "2m"))
        self.up_check_5m.setText(_translate("MainWindow", "Up"))
        self.label_27.setText(_translate("MainWindow", "1m"))
        self.label_25.setText(_translate("MainWindow", "1h"))
        self.down_check_4h.setText(_translate("MainWindow", "Down"))
        self.up_check_2m.setText(_translate("MainWindow", "Up"))
        self.up_check_4h.setText(_translate("MainWindow", "Up"))
        self.up_check_3m.setText(_translate("MainWindow", "Up"))
        self.down_check_15m.setText(_translate("MainWindow", "Down"))
        self.up_check_all.setText(_translate("MainWindow", "Up"))
        self.down_check_3m.setText(_translate("MainWindow", "Down"))
        self.label_29.setText(_translate("MainWindow", "5m"))
        self.up_check_1h.setText(_translate("MainWindow", "Up"))
        self.up_check_15m.setText(_translate("MainWindow", "Up"))
        self.down_check_5m.setText(_translate("MainWindow", "Down"))
        self.label_32.setText(_translate("MainWindow", "All:"))
        self.label_30.setText(_translate("MainWindow", "15m"))
        self.down_check_all.setText(_translate("MainWindow", "Down"))
        self.label_31.setText(_translate("MainWindow", "4h"))
        self.up_check_1d.setText(_translate("MainWindow", "Up"))
        self.down_check_1d.setText(_translate("MainWindow", "Down"))
        self.label_2.setText(_translate("MainWindow", "1d"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Steps"))
