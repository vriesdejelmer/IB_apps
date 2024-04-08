# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIComps/QTGeneration/VisualizationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 649)
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
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.base_ratio_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.base_ratio_box.sizePolicy().hasHeightForWidth())
        self.base_ratio_box.setSizePolicy(sizePolicy)
        self.base_ratio_box.setMinimum(1)
        self.base_ratio_box.setObjectName("base_ratio_box")
        self.horizontalLayout_7.addWidget(self.base_ratio_box)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.call_radio = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.call_radio.sizePolicy().hasHeightForWidth())
        self.call_radio.setSizePolicy(sizePolicy)
        self.call_radio.setObjectName("call_radio")
        self.call_put_group = QtWidgets.QButtonGroup(MainWindow)
        self.call_put_group.setObjectName("call_put_group")
        self.call_put_group.addButton(self.call_radio)
        self.horizontalLayout_8.addWidget(self.call_radio)
        self.put_radio = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.put_radio.sizePolicy().hasHeightForWidth())
        self.put_radio.setSizePolicy(sizePolicy)
        self.put_radio.setObjectName("put_radio")
        self.call_put_group.addButton(self.put_radio)
        self.horizontalLayout_8.addWidget(self.put_radio)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 3, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.lower_ratio_box = QtWidgets.QSpinBox(self.centralwidget)
        self.lower_ratio_box.setMinimum(1)
        self.lower_ratio_box.setObjectName("lower_ratio_box")
        self.horizontalLayout_9.addWidget(self.lower_ratio_box)
        self.lower_offset_box = QtWidgets.QComboBox(self.centralwidget)
        self.lower_offset_box.setObjectName("lower_offset_box")
        self.horizontalLayout_9.addWidget(self.lower_offset_box)
        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 3, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.structure_type = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.structure_type.sizePolicy().hasHeightForWidth())
        self.structure_type.setSizePolicy(sizePolicy)
        self.structure_type.setObjectName("structure_type")
        self.horizontalLayout_5.addWidget(self.structure_type)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.search_field = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_field.sizePolicy().hasHeightForWidth())
        self.search_field.setSizePolicy(sizePolicy)
        self.search_field.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.search_field.setClearButtonEnabled(True)
        self.search_field.setObjectName("search_field")
        self.horizontalLayout_4.addWidget(self.search_field)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.symbol_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symbol_label.sizePolicy().hasHeightForWidth())
        self.symbol_label.setSizePolicy(sizePolicy)
        self.symbol_label.setObjectName("symbol_label")
        self.gridLayout.addWidget(self.symbol_label, 4, 0, 1, 1)
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_label.sizePolicy().hasHeightForWidth())
        self.price_label.setSizePolicy(sizePolicy)
        self.price_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price_label.setObjectName("price_label")
        self.gridLayout.addWidget(self.price_label, 4, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.upper_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upper_label.sizePolicy().hasHeightForWidth())
        self.upper_label.setSizePolicy(sizePolicy)
        self.upper_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.upper_label.setObjectName("upper_label")
        self.horizontalLayout_2.addWidget(self.upper_label)
        self.upper_ratio_box = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upper_ratio_box.sizePolicy().hasHeightForWidth())
        self.upper_ratio_box.setSizePolicy(sizePolicy)
        self.upper_ratio_box.setMinimum(1)
        self.upper_ratio_box.setObjectName("upper_ratio_box")
        self.horizontalLayout_2.addWidget(self.upper_ratio_box)
        self.upper_offset_box = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upper_offset_box.sizePolicy().hasHeightForWidth())
        self.upper_offset_box.setSizePolicy(sizePolicy)
        self.upper_offset_box.setObjectName("upper_offset_box")
        self.horizontalLayout_2.addWidget(self.upper_offset_box)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.buy_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.buy_radio.setChecked(True)
        self.buy_radio.setObjectName("buy_radio")
        self.buy_sell_group = QtWidgets.QButtonGroup(MainWindow)
        self.buy_sell_group.setObjectName("buy_sell_group")
        self.buy_sell_group.addButton(self.buy_radio)
        self.horizontalLayout_12.addWidget(self.buy_radio)
        self.sell_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.sell_radio.setObjectName("sell_radio")
        self.buy_sell_group.addButton(self.sell_radio)
        self.horizontalLayout_12.addWidget(self.sell_radio)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_12.addWidget(self.line)
        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.plot_widget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy)
        self.plot_widget.setObjectName("plot_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.exp_grouped_plot_layout = QtWidgets.QVBoxLayout()
        self.exp_grouped_plot_layout.setObjectName("exp_grouped_plot_layout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.premium_a_radio = QtWidgets.QRadioButton(self.tab)
        self.premium_a_radio.setObjectName("premium_a_radio")
        self.premium_price_all_group = QtWidgets.QButtonGroup(MainWindow)
        self.premium_price_all_group.setObjectName("premium_price_all_group")
        self.premium_price_all_group.addButton(self.premium_a_radio)
        self.horizontalLayout_6.addWidget(self.premium_a_radio)
        self.price_a_radio = QtWidgets.QRadioButton(self.tab)
        self.price_a_radio.setChecked(True)
        self.price_a_radio.setObjectName("price_a_radio")
        self.premium_price_all_group.addButton(self.price_a_radio)
        self.horizontalLayout_6.addWidget(self.price_a_radio)
        self.rel_premium_a_radio = QtWidgets.QRadioButton(self.tab)
        self.rel_premium_a_radio.setObjectName("rel_premium_a_radio")
        self.premium_price_all_group.addButton(self.rel_premium_a_radio)
        self.horizontalLayout_6.addWidget(self.rel_premium_a_radio)
        self.rel_price_a_radio = QtWidgets.QRadioButton(self.tab)
        self.rel_price_a_radio.setObjectName("rel_price_a_radio")
        self.premium_price_all_group.addButton(self.rel_price_a_radio)
        self.horizontalLayout_6.addWidget(self.rel_price_a_radio)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.min_exp_plt_box = QtWidgets.QComboBox(self.tab)
        self.min_exp_plt_box.setObjectName("min_exp_plt_box")
        self.horizontalLayout_6.addWidget(self.min_exp_plt_box)
        self.max_exp_plt_box = QtWidgets.QComboBox(self.tab)
        self.max_exp_plt_box.setObjectName("max_exp_plt_box")
        self.horizontalLayout_6.addWidget(self.max_exp_plt_box)
        self.exp_grouped_plot_layout.addLayout(self.horizontalLayout_6)
        self.gridLayout_5.addLayout(self.exp_grouped_plot_layout, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.reset_button = QtWidgets.QPushButton(self.tab)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout_10.addWidget(self.reset_button)
        self.flush_button = QtWidgets.QPushButton(self.tab)
        self.flush_button.setObjectName("flush_button")
        self.horizontalLayout_10.addWidget(self.flush_button)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.min_strike_box = QtWidgets.QComboBox(self.tab)
        self.min_strike_box.setObjectName("min_strike_box")
        self.horizontalLayout_10.addWidget(self.min_strike_box)
        self.max_strike_box = QtWidgets.QComboBox(self.tab)
        self.max_strike_box.setObjectName("max_strike_box")
        self.horizontalLayout_10.addWidget(self.max_strike_box)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.min_exp_box = QtWidgets.QComboBox(self.tab)
        self.min_exp_box.setObjectName("min_exp_box")
        self.horizontalLayout_10.addWidget(self.min_exp_box)
        self.max_exp_box = QtWidgets.QComboBox(self.tab)
        self.max_exp_box.setObjectName("max_exp_box")
        self.horizontalLayout_10.addWidget(self.max_exp_box)
        self.call_selection = QtWidgets.QCheckBox(self.tab)
        self.call_selection.setChecked(True)
        self.call_selection.setObjectName("call_selection")
        self.horizontalLayout_10.addWidget(self.call_selection)
        self.put_selection = QtWidgets.QCheckBox(self.tab)
        self.put_selection.setChecked(True)
        self.put_selection.setObjectName("put_selection")
        self.horizontalLayout_10.addWidget(self.put_selection)
        self.fetch_all_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetch_all_button.sizePolicy().hasHeightForWidth())
        self.fetch_all_button.setSizePolicy(sizePolicy)
        self.fetch_all_button.setObjectName("fetch_all_button")
        self.horizontalLayout_10.addWidget(self.fetch_all_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.plot_widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.strike_grouped_plot_layout = QtWidgets.QVBoxLayout()
        self.strike_grouped_plot_layout.setObjectName("strike_grouped_plot_layout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.min_strike_plt_box = QtWidgets.QComboBox(self.tab_2)
        self.min_strike_plt_box.setObjectName("min_strike_plt_box")
        self.horizontalLayout_11.addWidget(self.min_strike_plt_box)
        self.max_strike_plt_box = QtWidgets.QComboBox(self.tab_2)
        self.max_strike_plt_box.setObjectName("max_strike_plt_box")
        self.horizontalLayout_11.addWidget(self.max_strike_plt_box)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.strike_grouped_plot_layout.addLayout(self.horizontalLayout_11)
        self.gridLayout_6.addLayout(self.strike_grouped_plot_layout, 0, 0, 1, 1)
        self.plot_widget.addTab(self.tab_2, "")
        self.strike_plot_tab = QtWidgets.QWidget()
        self.strike_plot_tab.setObjectName("strike_plot_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.strike_plot_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.strike_plot_layout = QtWidgets.QVBoxLayout()
        self.strike_plot_layout.setObjectName("strike_plot_layout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.premium_s_radio = QtWidgets.QRadioButton(self.strike_plot_tab)
        self.premium_s_radio.setChecked(True)
        self.premium_s_radio.setObjectName("premium_s_radio")
        self.premium_price_strike_group = QtWidgets.QButtonGroup(MainWindow)
        self.premium_price_strike_group.setObjectName("premium_price_strike_group")
        self.premium_price_strike_group.addButton(self.premium_s_radio)
        self.horizontalLayout_3.addWidget(self.premium_s_radio)
        self.price_s_radio = QtWidgets.QRadioButton(self.strike_plot_tab)
        self.price_s_radio.setChecked(False)
        self.price_s_radio.setObjectName("price_s_radio")
        self.premium_price_strike_group.addButton(self.price_s_radio)
        self.horizontalLayout_3.addWidget(self.price_s_radio)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.expiration_label = QtWidgets.QLabel(self.strike_plot_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expiration_label.sizePolicy().hasHeightForWidth())
        self.expiration_label.setSizePolicy(sizePolicy)
        self.expiration_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.expiration_label.setObjectName("expiration_label")
        self.horizontalLayout_3.addWidget(self.expiration_label)
        self.expiration_box = QtWidgets.QComboBox(self.strike_plot_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expiration_box.sizePolicy().hasHeightForWidth())
        self.expiration_box.setSizePolicy(sizePolicy)
        self.expiration_box.setObjectName("expiration_box")
        self.horizontalLayout_3.addWidget(self.expiration_box)
        self.checkBox = QtWidgets.QCheckBox(self.strike_plot_tab)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.strike_plot_layout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.strike_plot_layout, 0, 0, 1, 1)
        self.plot_widget.addTab(self.strike_plot_tab, "")
        self.exp_plot_tab = QtWidgets.QWidget()
        self.exp_plot_tab.setObjectName("exp_plot_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.exp_plot_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.exp_plot_layout = QtWidgets.QVBoxLayout()
        self.exp_plot_layout.setObjectName("exp_plot_layout")
        self.gridLayout_4.addLayout(self.exp_plot_layout, 0, 0, 1, 1)
        self.plot_widget.addTab(self.exp_plot_tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pl_layout = QtWidgets.QVBoxLayout()
        self.pl_layout.setObjectName("pl_layout")
        self.gridLayout_7.addLayout(self.pl_layout, 0, 0, 1, 1)
        self.plot_widget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.plot_widget)
        self.verticalLayout.setStretch(1, 5)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.plot_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "B"))
        self.call_radio.setText(_translate("MainWindow", "Call"))
        self.put_radio.setText(_translate("MainWindow", "Put"))
        self.label_4.setText(_translate("MainWindow", "L"))
        self.label_3.setText(_translate("MainWindow", "Structure:"))
        self.label_2.setText(_translate("MainWindow", "Symbol:"))
        self.symbol_label.setText(_translate("MainWindow", "SYMBOL"))
        self.price_label.setText(_translate("MainWindow", "PRICE"))
        self.upper_label.setText(_translate("MainWindow", "U"))
        self.buy_radio.setText(_translate("MainWindow", "Buy"))
        self.sell_radio.setText(_translate("MainWindow", "Sell"))
        self.premium_a_radio.setText(_translate("MainWindow", "Premium"))
        self.price_a_radio.setText(_translate("MainWindow", "Price"))
        self.rel_premium_a_radio.setText(_translate("MainWindow", "Relative Premium"))
        self.rel_price_a_radio.setText(_translate("MainWindow", "Relative Price"))
        self.label_9.setText(_translate("MainWindow", "Plot range:"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.flush_button.setText(_translate("MainWindow", "Flush"))
        self.label_5.setText(_translate("MainWindow", "Strikes"))
        self.label_6.setText(_translate("MainWindow", "Exps"))
        self.call_selection.setText(_translate("MainWindow", "C"))
        self.put_selection.setText(_translate("MainWindow", "P"))
        self.fetch_all_button.setText(_translate("MainWindow", "Fetch"))
        self.plot_widget.setTabText(self.plot_widget.indexOf(self.tab), _translate("MainWindow", "Exps Grouped"))
        self.label_7.setText(_translate("MainWindow", "Strikes plot range:"))
        self.plot_widget.setTabText(self.plot_widget.indexOf(self.tab_2), _translate("MainWindow", "Strike Grouped"))
        self.premium_s_radio.setText(_translate("MainWindow", "Premium"))
        self.price_s_radio.setText(_translate("MainWindow", "Price"))
        self.expiration_label.setText(_translate("MainWindow", "Expiration"))
        self.checkBox.setText(_translate("MainWindow", "Live Stream"))
        self.plot_widget.setTabText(self.plot_widget.indexOf(self.strike_plot_tab), _translate("MainWindow", "Live by Strike"))
        self.plot_widget.setTabText(self.plot_widget.indexOf(self.exp_plot_tab), _translate("MainWindow", "Live by Exp"))
        self.plot_widget.setTabText(self.plot_widget.indexOf(self.tab_3), _translate("MainWindow", "PL Graph"))
