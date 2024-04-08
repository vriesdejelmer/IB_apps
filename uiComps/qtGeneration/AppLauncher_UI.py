# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIComps/QTGeneration/AppLauncher.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 649)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 20, 20, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.open_list_manager = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_list_manager.sizePolicy().hasHeightForWidth())
        self.open_list_manager.setSizePolicy(sizePolicy)
        self.open_list_manager.setObjectName("open_list_manager")
        self.ib_group = QtWidgets.QButtonGroup(MainWindow)
        self.ib_group.setObjectName("ib_group")
        self.ib_group.addButton(self.open_list_manager)
        self.gridLayout_6.addWidget(self.open_list_manager, 0, 1, 1, 1)
        self.open_stocks = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_stocks.sizePolicy().hasHeightForWidth())
        self.open_stocks.setSizePolicy(sizePolicy)
        self.open_stocks.setObjectName("open_stocks")
        self.ib_group.addButton(self.open_stocks)
        self.gridLayout_6.addWidget(self.open_stocks, 0, 0, 1, 1)
        self.open_man_trader = QtWidgets.QPushButton(self.centralwidget)
        self.open_man_trader.setObjectName("open_man_trader")
        self.ib_group.addButton(self.open_man_trader)
        self.gridLayout_6.addWidget(self.open_man_trader, 1, 1, 1, 1)
        self.open_option_pos = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_option_pos.sizePolicy().hasHeightForWidth())
        self.open_option_pos.setSizePolicy(sizePolicy)
        self.open_option_pos.setObjectName("open_option_pos")
        self.ib_group.addButton(self.open_option_pos)
        self.gridLayout_6.addWidget(self.open_option_pos, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_6)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.open_movers = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_movers.sizePolicy().hasHeightForWidth())
        self.open_movers.setSizePolicy(sizePolicy)
        self.open_movers.setObjectName("open_movers")
        self.general_history_group = QtWidgets.QButtonGroup(MainWindow)
        self.general_history_group.setObjectName("general_history_group")
        self.general_history_group.addButton(self.open_movers)
        self.gridLayout_7.addWidget(self.open_movers, 0, 0, 1, 1)
        self.open_comparisons = QtWidgets.QPushButton(self.centralwidget)
        self.open_comparisons.setObjectName("open_comparisons")
        self.general_history_group.addButton(self.open_comparisons)
        self.gridLayout_7.addWidget(self.open_comparisons, 1, 0, 1, 1)
        self.open_alert_system = QtWidgets.QPushButton(self.centralwidget)
        self.open_alert_system.setObjectName("open_alert_system")
        self.general_history_group.addButton(self.open_alert_system)
        self.gridLayout_7.addWidget(self.open_alert_system, 0, 1, 1, 1)
        self.open_poly_downloader = QtWidgets.QPushButton(self.centralwidget)
        self.open_poly_downloader.setObjectName("open_poly_downloader")
        self.gridLayout_7.addWidget(self.open_poly_downloader, 2, 1, 1, 1)
        self.open_option_viz = QtWidgets.QPushButton(self.centralwidget)
        self.open_option_viz.setObjectName("open_option_viz")
        self.ib_group.addButton(self.open_option_viz)
        self.gridLayout_7.addWidget(self.open_option_viz, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(137, 137, 137, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_2.setPalette(palette)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.real_ibg_button = QtWidgets.QRadioButton(self.centralwidget)
        self.real_ibg_button.setObjectName("real_ibg_button")
        self.trading_type_group = QtWidgets.QButtonGroup(MainWindow)
        self.trading_type_group.setObjectName("trading_type_group")
        self.trading_type_group.addButton(self.real_ibg_button)
        self.horizontalLayout_2.addWidget(self.real_ibg_button)
        self.paper_ibg_button = QtWidgets.QRadioButton(self.centralwidget)
        self.paper_ibg_button.setObjectName("paper_ibg_button")
        self.trading_type_group.addButton(self.paper_ibg_button)
        self.horizontalLayout_2.addWidget(self.paper_ibg_button)
        self.custom_button = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_button.sizePolicy().hasHeightForWidth())
        self.custom_button.setSizePolicy(sizePolicy)
        self.custom_button.setObjectName("custom_button")
        self.trading_type_group.addButton(self.custom_button)
        self.horizontalLayout_2.addWidget(self.custom_button)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.socket_label = QtWidgets.QLabel(self.centralwidget)
        self.socket_label.setObjectName("socket_label")
        self.gridLayout_4.addWidget(self.socket_label, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ib_data_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.ib_data_radio.setChecked(True)
        self.ib_data_radio.setObjectName("ib_data_radio")
        self.data_group = QtWidgets.QButtonGroup(MainWindow)
        self.data_group.setObjectName("data_group")
        self.data_group.addButton(self.ib_data_radio)
        self.horizontalLayout_3.addWidget(self.ib_data_radio)
        self.finazon_data_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.finazon_data_radio.setObjectName("finazon_data_radio")
        self.data_group.addButton(self.finazon_data_radio)
        self.horizontalLayout_3.addWidget(self.finazon_data_radio)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.real_tws_button = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.real_tws_button.sizePolicy().hasHeightForWidth())
        self.real_tws_button.setSizePolicy(sizePolicy)
        self.real_tws_button.setObjectName("real_tws_button")
        self.trading_type_group.addButton(self.real_tws_button)
        self.horizontalLayout.addWidget(self.real_tws_button)
        self.paper_tws_button = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paper_tws_button.sizePolicy().hasHeightForWidth())
        self.paper_tws_button.setSizePolicy(sizePolicy)
        self.paper_tws_button.setObjectName("paper_tws_button")
        self.trading_type_group.addButton(self.paper_tws_button)
        self.horizontalLayout.addWidget(self.paper_tws_button)
        self.gridLayout_4.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.address_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address_line.sizePolicy().hasHeightForWidth())
        self.address_line.setSizePolicy(sizePolicy)
        self.address_line.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.address_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address_line.setClearButtonEnabled(True)
        self.address_line.setObjectName("address_line")
        self.gridLayout_4.addWidget(self.address_line, 1, 1, 1, 1)
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setObjectName("address_label")
        self.gridLayout_4.addWidget(self.address_label, 1, 0, 1, 1)
        self.socket_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.socket_line.sizePolicy().hasHeightForWidth())
        self.socket_line.setSizePolicy(sizePolicy)
        self.socket_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.socket_line.setObjectName("socket_line")
        self.gridLayout_4.addWidget(self.socket_line, 2, 1, 1, 1)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_button.sizePolicy().hasHeightForWidth())
        self.connect_button.setSizePolicy(sizePolicy)
        self.connect_button.setObjectName("connect_button")
        self.gridLayout_4.addWidget(self.connect_button, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.telegram_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.telegram_checkbox.setObjectName("telegram_checkbox")
        self.horizontalLayout_4.addWidget(self.telegram_checkbox)
        self.fetch_rates = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_rates.sizePolicy().hasHeightForWidth())
        self.fetch_rates.setSizePolicy(sizePolicy)
        self.fetch_rates.setObjectName("fetch_rates")
        self.horizontalLayout_4.addWidget(self.fetch_rates)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.log_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log_window.setObjectName("log_window")
        self.verticalLayout.addWidget(self.log_window)
        self.verticalLayout.setStretch(2, 2)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Launch Manager"))
        self.label.setText(_translate("MainWindow", "Apps:"))
        self.label_4.setText(_translate("MainWindow", "IB Trade Management"))
        self.open_list_manager.setText(_translate("MainWindow", "List Manager"))
        self.open_stocks.setText(_translate("MainWindow", "Stock Positions"))
        self.open_man_trader.setText(_translate("MainWindow", "Manual Trader"))
        self.open_option_pos.setText(_translate("MainWindow", "Option Positions"))
        self.label_5.setText(_translate("MainWindow", "Data Tools"))
        self.open_movers.setText(_translate("MainWindow", "Movers"))
        self.open_comparisons.setText(_translate("MainWindow", "Comparisons"))
        self.open_alert_system.setText(_translate("MainWindow", "Updating/Alerting"))
        self.open_poly_downloader.setText(_translate("MainWindow", "Polygon Download"))
        self.open_option_viz.setText(_translate("MainWindow", "Option Visuallizer"))
        self.label_2.setText(_translate("MainWindow", "Connection:"))
        self.label_3.setText(_translate("MainWindow", "Data Source:"))
        self.real_ibg_button.setText(_translate("MainWindow", "IB Real"))
        self.paper_ibg_button.setText(_translate("MainWindow", "IB Paper"))
        self.custom_button.setText(_translate("MainWindow", "Custom"))
        self.socket_label.setText(_translate("MainWindow", "Socket"))
        self.ib_data_radio.setText(_translate("MainWindow", "IB"))
        self.finazon_data_radio.setText(_translate("MainWindow", "Finazon"))
        self.real_tws_button.setText(_translate("MainWindow", "TWS Real"))
        self.paper_tws_button.setText(_translate("MainWindow", "TWS Paper"))
        self.address_label.setText(_translate("MainWindow", "Local Address"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.telegram_checkbox.setText(_translate("MainWindow", "Telegram Bot"))
        self.fetch_rates.setText(_translate("MainWindow", "Fetch Short Rates"))
        self.label_6.setText(_translate("MainWindow", "TWS Messages:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
