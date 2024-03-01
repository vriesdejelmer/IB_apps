# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
#import pyqtgraph as pg
from dataHandling.Constants import Constants, OptionConstrType
from uiComps.qtGeneration.Visualization_UI import Ui_MainWindow as Visualization_UI
import sys
from datetime import datetime
from pytz import timezone

from generalFunctionality.SymbolFinderImpl import SymbolFinderImplementation

from uiComps.QHelper import Validator
from uiComps.customWidgets.PlotWidgets.StrikeLineObject import StrikeLineObject
from uiComps.customWidgets.PlotWidgets.OptionPlotWidget import PremiumPlotWidget, OptionPlotWidget
from uiComps.customWidgets.PlotWidgets.OptionAllPlotWidget import OptionAllPlotWidget


class VisualizationWindow(QMainWindow, Visualization_UI, SymbolFinderImplementation):

    # no_strike_set = True
    # selected_strike = None
    # data_exp_mid = None
    # data_strike_mid = None
    # price = None
    constr_types = [OptionConstrType.single, OptionConstrType.vertical_spread, OptionConstrType.butterfly, OptionConstrType.split_butterfly, OptionConstrType.iron_condor, OptionConstrType.topped_ratio_spread]

    min_exp = None
    max_exp = None
    min_strike = None
    max_strike = None
        

    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Visualization_UI.__init__(self)
        SymbolFinderImplementation.__init__(self)

        self.setupUi(self)

        self.connectSearchField()
        self.connectActions()
        self.populateBoxes()
        self.setupGraphs()
        self.disableInterface() 


        
    def populateBoxes(self):
        for item in self.constr_types:
            self.structure_type.addItem(item.value)


    # def setDefaults(self, option_type):
    #     if option_type == Constants.CALL:
    #         self.call_button.setChecked(True)
    #     elif option_type == Constants.PUT:
    #         self.put_button.setChecked(True)


    def connectActions(self):
        self.expiration_box.currentIndexChanged.connect(self.expirationSelectionChange)
        self.structure_type.currentTextChanged.connect(self.structureSelectionChanged)
        self.call_put_group.buttonClicked.connect(self.callPutAction)
        self.buy_sell_group.buttonClicked.connect(self.buySellAction)
        self.upper_offset_box.currentTextChanged.connect(self.constructionPropsChange)
        self.premium_price_strike_group.buttonClicked.connect(self.radioStrikeSelection)
        self.premium_price_all_group.buttonClicked.connect(self.radioAllSelection)
        self.fetch_all_button.clicked.connect(self.fetchAllStrikes)
        self.base_ratio_box.valueChanged.connect(self.constructionPropsChange)
        self.upper_ratio_box.valueChanged.connect(self.constructionPropsChange)
        self.lower_ratio_box.valueChanged.connect(self.constructionPropsChange)
        self.min_strike_box.currentIndexChanged.connect(self.minStrikeChange)
        self.max_strike_box.currentIndexChanged.connect(self.maxStrikeChange)
        self.min_exp_box.currentIndexChanged.connect(self.minExpChange)
        self.max_exp_box.currentIndexChanged.connect(self.maxExpChange)

        self.min_strike_plt_box.currentIndexChanged.connect(self.minStrikePlotChange)
        self.max_strike_plt_box.currentIndexChanged.connect(self.maxStrikePlotChange)
        self.min_exp_plt_box.currentIndexChanged.connect(self.minExpPlotChange)
        self.max_exp_plt_box.currentIndexChanged.connect(self.maxExpPlotChange)


    def setupGraphs(self):     

        self.strike_plot = PremiumPlotWidget(self, labels=['Premium', 'Change'])
        self.strike_plot_layout.addWidget(self.strike_plot)

        self.expiration_plot = OptionPlotWidget(self, inverted=True)
        self.exp_plot_layout.addWidget(self.expiration_plot)

        self.exp_grouped_plot = OptionAllPlotWidget(self, 'expiration_grouped', 'Strike Price ($)', legend_alignment='right')
        self.exp_grouped_plot_layout.addWidget(self.exp_grouped_plot)
                # Remove x-axis of the top plot
        # self.exp_grouped_plot.hideAxis('bottom')

        # self.exp_grouped_rel_plot = OptionAllPlotWidget('expiration_grouped', 'Strike Price', legend_alignment='right', difference_plot=True)
        # self.exp_grouped_plot_layout.addWidget(self.exp_grouped_rel_plot)        
        # self.exp_grouped_plot.setXLink(self.exp_grouped_rel_plot)

        # self.exp_diff_grouped_rel_plot = OptionAllPlotWidget('expiration_diffs', 'Strike Price', legend_alignment='right', difference_plot=True)
        # self.exp_diff_grouped_layout.addWidget(self.exp_diff_grouped_rel_plot)
        # self.exp_diff_grouped_plot.setXLink(self.exp_diff_grouped_rel_plot)

        
        self.strike_grouped_plot = OptionAllPlotWidget(self, 'strike_grouped', 'Days Till Expiriation', legend_alignment='left')
        self.strike_grouped_plot_layout.addWidget(self.strike_grouped_plot)
        
        # self.verticalLayout_2.setStretch(0, 1)
        # self.verticalLayout_2.setStretch(1, 6)
        # self.verticalLayout_2.setStretch(2, 1)
        # self.verticalLayout_2.setStretch(3, 6)

        self.price_est_plot = OptionAllPlotWidget(self, 'price_est', 'Price Movement ($)', legend_alignment='right')
        self.pl_layout.addWidget(self.price_est_plot)

        
    
    def updatePlotPrice(self, price):
        pass
        #self.strike_plot.updatePrice(price)


    def disableInterface(self):
        self.toggleInterface(False)


    def enableInterface(self):
        self.toggleInterface(True)


    def toggleInterface(self, enabled):
        self.resetInputBoxes(self.constr_type)
        self.expiration_box.setEnabled(enabled)


    def updateOptionGUI(self, expirations, strikes):
        print("Visualization_UI.updateOptionGUI")
        print("How often do we come here?")
        self.applySignalBlock(True)
        self.clearOptionGUI()
        self.populateExpirationBoxes(expirations)
        self.populateStrikeBoxes(strikes)
        self.enableInterface()
        self.applySignalBlock(False)


    def applySignalBlock(self, value):
        self.expiration_box.blockSignals(value)
        

        self.min_exp_plt_box.blockSignals(value)
        self.max_exp_plt_box.blockSignals(value)
        self.min_strike_plt_box.blockSignals(value)
        self.max_strike_plt_box.blockSignals(value)
        
        
        # self.min_exp_box.blockSignals(value)
        # self.max_exp_box.blockSignals(value)
        # self.min_strike_box.blockSignals(value)
        # self.max_strike_box.blockSignals(value)


    def setGUIValues(self, boundaries):
        min_exp, max_exp, min_strike, max_strike = boundaries
        print('Visualization_UI.setGUIValue')

        self.min_exp = min_exp
        self.max_exp = max_exp
        self.min_strike = min_strike
        self.max_strike = max_strike



    def clearOptionGUI(self):
        self.expiration_box.clear()

        self.min_exp_box.clear()
        self.max_exp_box.clear()        
        self.min_strike_box.clear()
        self.max_strike_box.clear()

        self.min_strike_plt_box.clear()
        self.max_strike_plt_box.clear()
        self.min_exp_plt_box.clear()
        self.max_exp_plt_box.clear()

        
        

    @pyqtSlot(int)
    def minStrikeChange(self, value):
        self.min_strike_signal.emit(self.strike_pairs[value][0])
    
    @pyqtSlot(int)
    def maxStrikeChange(self, value):
        self.max_strike_signal.emit(self.strike_pairs[value][0])
    
    @pyqtSlot(int)
    def minExpChange(self, value):
        self.min_expiration_signal.emit(self.expiration_pairs[value][0])
    
    @pyqtSlot(int)
    def maxExpChange(self, value):
        self.max_expiration_signal.emit(self.expiration_pairs[value][0])


    @pyqtSlot(int)
    def minStrikePlotChange(self, value):
        self.strike_grouped_plot.setMinimumKey(self.strike_pairs[value][0])
    

    @pyqtSlot(int)
    def maxStrikePlotChange(self, value):
        self.strike_grouped_plot.setMaximumKey(self.strike_pairs[value][0])
    

    @pyqtSlot(int)
    def minExpPlotChange(self, value):
        self.exp_grouped_plot.setMinimumKey(self.expiration_pairs[value][0])
    

    @pyqtSlot(int)
    def maxExpPlotChange(self, value):
        self.exp_grouped_plot.setMaximumKey(self.expiration_pairs[value][0])


    def populateStrikeBoxes(self, strikes):
        strike_strings = list(map(str, strikes))
        self.strike_pairs = list(sorted(zip(strikes, strike_strings)))
        sorted_strike_strings = [item[1] for item in self.strike_pairs]
        sorted_strikes = [item[0] for item in self.strike_pairs]

        self.min_strike_box.addItems(sorted_strike_strings)
        self.max_strike_box.addItems(sorted_strike_strings)

        if self.max_strike is not None:
            max_strike_index = sorted_strikes.index(self.max_strike)
            self.max_strike_box.setCurrentText(sorted_strike_strings[max_strike_index])
        else:
            self.max_strike_box.setCurrentIndex(len(sorted_strike_strings)-1)

        if self.min_strike is not None:
            min_strike_index = sorted_strikes.index(self.min_strike)
            self.min_strike_box.setCurrentText(sorted_strike_strings[min_strike_index])

        self.min_strike_plt_box.addItems(sorted_strike_strings)
        self.max_strike_plt_box.addItems(sorted_strike_strings)
        self.max_strike_plt_box.setCurrentIndex(len(sorted_strike_strings)-1)
    
        
    def getExpirationString(self, expiration_date):
        datetime_obj = datetime.strptime(expiration_date, '%Y%m%d')
        return datetime_obj.date().strftime("%d %B %Y")


    def populateExpirationBoxes(self, expirations):
        days_till_exp = [self.getDaysTillExpiration(exp) for exp in expirations]
        expiration_pp_str = [self.getExpirationString(exp) for exp in expirations]
        
        self.expiration_pairs = list(sorted(zip(days_till_exp, expiration_pp_str, expirations)))
        sorted_expiration_strings = [item[1] for item in self.expiration_pairs]
        sorted_expirations = [item[0] for item in self.expiration_pairs]

        
        self.expiration_box.addItems(sorted_expiration_strings)
        self.min_exp_box.addItems(sorted_expiration_strings)
        self.max_exp_box.addItems(sorted_expiration_strings)
        self.max_exp_box.setCurrentIndex(len(sorted_expiration_strings)-1)

        if self.max_exp is not None:
            max_exp_index = sorted_expirations.index(self.max_exp)
            self.max_exp_box.setCurrentText(sorted_expiration_strings[max_exp_index])
        else:
            self.max_exp_box.setCurrentIndex(len(sorted_expiration_strings)-1)

        if self.min_exp is not None:
            min_exp_index = sorted_expirations.index(self.min_exp)
            self.min_exp_box.setCurrentText(sorted_expiration_strings[min_exp_index])


        self.min_exp_plt_box.addItems(sorted_expiration_strings)
        self.max_exp_plt_box.addItems(sorted_expiration_strings)
        self.max_exp_plt_box.setCurrentIndex(len(sorted_expiration_strings)-1)


    def getDaysTillExpiration(self, expiration_date):
        #TODO This one is called an aweful lot
        datetime_obj = datetime.strptime(expiration_date, '%Y%m%d').date()
        today = datetime.now(timezone(Constants.NYC_TIMEZONE)).date()
        return (datetime_obj - today).days

