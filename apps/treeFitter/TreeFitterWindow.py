# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import numpy as np
from uiComps.qtGeneration.TreeFittingWindow_UI import Ui_MainWindow as TreeFittingWindow_UI
import sys
from dataHandling.Constants import Constants
from dataHandling.TradeManagement.UserDataManagement import getStockListNames

from uiComps.customWidgets.CheckableComboBox import CheckableComboBox


class TreeFitterWindow(QMainWindow, TreeFittingWindow_UI):

	bar_types = ['1 min', '2 mins', '3 mins', '5 mins', '15 mins']
	current_selection = None

	def __init__(self):
		QMainWindow.__init__(self)
		TreeFittingWindow_UI.__init__(self)
		#SymbolFinderImplementation.__init__(self)
		self.setupUi(self)
		self.addCheckableTickerBox()

		self.connectActions()
		self.populateBoxes()
		self.stock_list = dict()


	def addCheckableTickerBox(self):
		self.checkable_ticker_box = CheckableComboBox()
		self.gridLayout_2.addWidget(self.checkable_ticker_box, 0, 3, 1, 1)


	def connectActions(self):
		self.generate_frame_button.clicked.connect(self.generateFrames)
		self.add_feature_button.clicked.connect(self.addFeatures)
		self.save_frame_button.clicked.connect(self.saveFrames)
		self.load_frame_button.clicked.connect(self.loadFrames)
		self.data_training_button.clicked.connect(self.trainData)
		self.checkable_ticker_box.activated.connect(self.tickerListClicked)
		self.sel_all_button.clicked.connect(self.tickerSelectionToggle)
		self.save_trees_button.clicked.connect(self.saveTrainedTrees)
		self.bar_selector.currentTextChanged.connect(self.selectBarType)
		self.list_selector.currentIndexChanged.connect(self.loadNewStockList)

		self.rsirev_check.stateChanged.connect(self.rsirevCheck)
		self.stairstep_check.stateChanged.connect(self.stairCheck)
		self.insidebar_check.stateChanged.connect(self.insideCheck)

		self.stock_rsi_check.stateChanged.connect(self.stockRSICheck)
		self.sector_rsi_check.stateChanged.connect(self.sectorRSICheck)
		self.volatility_check.stateChanged.connect(self.volatilityCheck)
		self.stock_move_check.stateChanged.connect(self.moveCheck)

		
	def populateBoxes(self):
		self.populateListBox()
		self.populateBarBox()


	def populateBarBox(self):
		self.bar_selector.blockSignals(True)
		self.bar_selector.addItems(self.bar_types)
		self.bar_selector.blockSignals(False)


	def populateListBox(self):
		self.stock_lists = getStockListNames()
		self.list_selector.blockSignals(True)
		for _, list_name in self.stock_lists:
			self.list_selector.addItem(list_name)
		self.list_selector.blockSignals(False)


	@pyqtSlot(str, dict)
	def apiUpdate(self, signal, sub_signal):
		for key, model in self.regression_models:
			pickle.dump(model, open(Constants.ANAYLIS_RESULTS_FOLDER + 'models/xgbregressor' + key + '.pkl', 'wb'))
		

	def loadModels(self):
		for strategy_type, checked in self.strategy_types:
			if checked:
				try:
					self.model[strategy] = pd.read_pickle(Constants.ANAYLIS_RESULTS_FOLDER + 'models/xgbregressor' + key + '.pkl')
				except:
					print(f"Failed loading model for strategy: {strategy_type}")
	