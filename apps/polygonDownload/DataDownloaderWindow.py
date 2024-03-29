# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QStyledItemDelegate
from uiComps.qtGeneration.DataDetails_UI import Ui_MainWindow as DataDetails_UI
from dataHandling.Constants import Constants
from dataHandling.UserDataManagement import getStockListNames

from uiComps.customWidgets.PlotWidgets.CandlePlotWidget import CandlePlotWidget
from uiComps.customWidgets.CheckableComboBox import CheckableComboBox

class RightAlignedDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignRight


        

class DataDownloaderWindow(QMainWindow, DataDetails_UI):

    column_for_name = {'Price': 1, 'Day': 2, 'Week': 3, '2 Weeks': 4, 'Month': 5, "2 Months": 6, "6 Months": 7 , "1 Year": 8}
    period_options = ["Day", "Week", "2 Weeks", "Month", "2 Months", "3 Months", "6 Months", "1 Year"]
    corr_period_options = ["2 hours", "4 hours", "Today", "24 hours", "1 week", "2 week", "Month", "2 Months", "3 Months", "6 Months", "max"]
    

    def __init__(self, bar_types):
        QMainWindow.__init__(self)
        DataDetails_UI.__init__(self)

        self.bar_types = bar_types
        self.bar_selection = dict()
        for bar_type in self.bar_types:
            self.bar_selection[bar_type] = (bar_type == Constants.FIFTEEN_MIN_BAR)

        self.setupUi(self)
        self.addAdditionalComponents()
        self.populateBoxes()
        self.setupActions()


    def addAdditionalComponents(self):

        self.trade_plot = CandlePlotWidget(self.setLevels)
        self.graph_layout.addWidget(self.trade_plot, 1, 0, 1, 1)

        self.download_bar_selector = CheckableComboBox()
        self.download_bar_layout.insertWidget(1, self.download_bar_selector)

        self.download_list_checker = CheckableComboBox()
        self.download_list_checker.setEnabled(False)
        self.download_control_layout.addWidget(self.download_list_checker, 2, 2, 1, 1)


    def setLevels(self):
        pass


    def setupActions(self):
        self.list_selector.currentIndexChanged.connect(self.listSelection)
        self.ticker_selector.currentIndexChanged.connect(self.tickerSelection)
        self.bar_selector_point.currentIndexChanged.connect(self.timeFramePointSel)
        self.bar_selector_graph.currentIndexChanged.connect(self.timeFrameGraphSel)
        self.download_bar_selector.activated.connect(self.barChecksChanged)
        self.download_type_group.buttonClicked.connect(self.radioSelection)
        self.download_button.clicked.connect(self.downloadData)
        

    def populateBoxes(self):
        self.stock_lists = getStockListNames()
        for file_name, list_name in self.stock_lists:
            self.list_selector.addItem(list_name)
    
        self.bar_selector_graph.addItems(self.bar_types)
        self.bar_selector_point.addItems(self.bar_types)

        self.populateCheckableBars()
        self.populateCheckableLists()


    def populateCheckableBars(self):
        
        self.download_bar_selector.blockSignals(True)

        for index, bar_type in enumerate(self.bar_types):
            self.download_bar_selector.addItem(bar_type)

            item = self.download_bar_selector.model().item(index, 0)
            if self.bar_selection[bar_type]: item.setCheckState(QtCore.Qt.Checked)
            else: item.setCheckState(QtCore.Qt.Unchecked)

        self.download_bar_selector.blockSignals(False)            


    def populateCheckableLists(self):
        
        stock_lists = getStockListNames()
        check_list = {k: False for k in range(len(stock_lists))}

        self.download_list_checker.blockSignals(True)

        file_list = dict()

        for index, (file_name, list_name) in enumerate(stock_lists):

            file_list[index] = file_name
            self.download_list_checker.key_list = file_list
            self.download_list_checker.addItem(list_name)

            item = self.download_list_checker.model().item(index, 0)
            if check_list[index]: item.setCheckState(QtCore.Qt.Checked)
            else: item.setCheckState(QtCore.Qt.Unchecked)

        self.download_list_checker.key_list = file_list
        self.download_list_checker.blockSignals(False)            




    def onTabChange(self, value):
        pass
        # self.period_selector.setEnabled(value==0)


    def setTableProperties(self):
        # Get the horizontal header
        header = self.data_ranges_table.horizontalHeader()

        # Set the first column width to be resized to its contents
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # Set the second and third column to take up the rest of the space
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)


        self.data_ranges_table.setSortingEnabled(True)
        self.data_count_table.setSortingEnabled(True)
        self.data_point_table.setSortingEnabled(True)
        # for column_index in range(2,9):
        #     self.low_table.horizontalHeader().setSectionResizeMode(column_index, QtWidgets.QHeaderView.Stretch)
        #     self.high_table.horizontalHeader().setSectionResizeMode(column_index, QtWidgets.QHeaderView.Stretch)

        # for column_index in self.step_mapping.keys():
        #     self.step_up_table.horizontalHeader().setSectionResizeMode(column_index, QtWidgets.QHeaderView.ResizeToContents)
        #     self.step_down_table.horizontalHeader().setSectionResizeMode(column_index, QtWidgets.QHeaderView.ResizeToContents)

        #self.step_up_table.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)

        # create delegate
        delegate = RightAlignedDelegate()

        # set delegate for second and third columns
        self.data_ranges_table.setItemDelegateForColumn(1, delegate)
        self.data_ranges_table.setItemDelegateForColumn(2, delegate)


    def setupAlignment(self):
        #TODO: Why is this still here?
        pass
        # alignDelegate = AlignDelegate(self.overview_table)
        # percAlignDelegate = PercAlignDelegate(self.overview_table)
        # bigNumAlignDelegate = BigNumberAlignDelegate(self.overview_table)
        # self.overview_table.setItemDelegateForColumn(1, alignDelegate)
        # self.overview_table.setItemDelegateForColumn(2, alignDelegate)
        # self.overview_table.setItemDelegateForColumn(3, percAlignDelegate)
        # self.overview_table.setItemDelegateForColumn(4, alignDelegate)
        # self.overview_table.setItemDelegateForColumn(5, percAlignDelegate)
        # self.overview_table.setItemDelegateForColumn(6, percAlignDelegate)
        # self.overview_table.setItemDelegateForColumn(7, bigNumAlignDelegate)


 

        
