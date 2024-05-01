
# Copyright (c) 2024 Jelmer de Vries
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation in its latest version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import Qt, pyqtSignal, QThread, pyqtSlot
import numpy as np
from dataHandling.Constants import Constants, OptionConstrType
from dataHandling.DataStructures import DetailObject
from .VisualizationWindow import VisualizationWindow
import pandas as pd


def floatFromString(str_flt, default=0.0):
    try:
        return float(str_flt)
    except ValueError:
        return default


class OptionVisualization(VisualizationWindow):

    option_type = Constants.CALL
    order_type = Constants.BUY
    constr_type = OptionConstrType.single
    
    first_price = False
    stock_fetch_initiated = False
    
    current_selection = None

    last_price = None
    _underlying_price = None

    req_all_strikes = pyqtSignal(list, float, float, int, int)
    stock_selection_signal = pyqtSignal(DetailObject)

    req_by_strike_execute = pyqtSignal(float)
    req_by_exp = pyqtSignal(str, bool)
    req_by_exp_execute = pyqtSignal(str)

    constr_change_signal = pyqtSignal(str, str, str, list, list)


    def __init__(self, option_data_manager, symbol_manager):
        super().__init__()

        self.option_data_manager = option_data_manager
        self.symbol_manager = symbol_manager
        
        self.connectManagerAndPlots(option_data_manager)
    
        self.symbol_manager.api_updater.connect(self.contractUpdate, Qt.QueuedConnection)

        self.connectSignals()
        self.resetInputBoxes(self.constr_type)
        

    def connectManagerAndPlots(self, option_data_manager):
        option_data_manager.api_updater.connect(self.apiUpdate, Qt.QueuedConnection)
        option_data_manager.latest_price_signal.connect(self.underlyingPriceUpdate, Qt.QueuedConnection)
    
        self.strike_comp_frame = self.option_data_manager.getStrikeFrame()
        self.exp_comp_frame = option_data_manager.getExpirationFrame()
        self.all_option_frame = option_data_manager.getBufferedFrame()
        
        self.min_all_strike.connect(self.all_option_frame.setMinimumStrike, Qt.QueuedConnection)
        self.max_all_strike.connect(self.all_option_frame.setMaximumStrike, Qt.QueuedConnection)
        self.min_all_expiration.connect(self.all_option_frame.setMinimumExpiration, Qt.QueuedConnection)
        self.max_all_expiration.connect(self.all_option_frame.setMaximumExpiration, Qt.QueuedConnection)

        self.strike_plot.setDataObject(self.strike_comp_frame)
        self.expiration_plot.setDataObject(self.exp_comp_frame)
        self.strike_grouped_plot.setDataObject(self.all_option_frame)
        self.exp_grouped_plot.setDataObject(self.all_option_frame)
        self.price_est_plot.setDataObject(self.all_option_frame)


    def connectSignals(self):
        self.stock_selection_signal.connect(self.option_data_manager.makeStockSelection, type=Qt.QueuedConnection)
        self.req_all_strikes.connect(self.option_data_manager.requestForAllStrikesAndExpirations, type=Qt.QueuedConnection)
        self.req_by_strike_execute.connect(self.option_data_manager.requestOptionDataForStrike, type=Qt.QueuedConnection)

        self.req_by_exp.connect(self.option_data_manager.requestOptionDataForExpiration, type=Qt.QueuedConnection)
        self.req_by_exp_execute.connect(self.option_data_manager.requestOptionDataForExpiration, type=Qt.QueuedConnection)

        self.flush_button.clicked.connect(self.option_data_manager.flushData, type=Qt.QueuedConnection)
        self.reset_button.clicked.connect(self.option_data_manager.resetWholeChain, type=Qt.QueuedConnection)

        self.constr_change_signal.connect(self.option_data_manager.structureSelectionChanged, type=Qt.QueuedConnection)
        

    def structureSelectionChanged(self, value):
        self.constr_type = OptionConstrType(value)
        self.resetInputBoxes(self.constr_type)
        self.constructionPropsChange()


    def resetInputBoxes(self, constr_type):        
        self.setOffsetDefaults(constr_type)
        self.setRatioDefaults(constr_type)
        

    def getCurrentOffsets(self):
        upper_offset = floatFromString(self.upper_offset_box.currentText(), default=0.0)
        lower_offset = floatFromString(self.upper_offset_box.currentText(), default=0.0)
        return [upper_offset, lower_offset]


    def getCurrentRatios(self):
        base_ratio = self.base_ratio_box.value()
        upper_ratio = self.upper_ratio_box.value()
        lower_ratio = self.lower_ratio_box.value()
        return [base_ratio, upper_ratio, lower_ratio]


    def findPrefferedOffset(self, strike_diffs, preferred_values):
        for value in preferred_values:
            index = np.where(strike_diffs == value)
            if len(index[0]) > 0:
                return (index[0][0], value)
        return None


    def getStrikeDifferences(self):
        active_strikes = self.all_option_frame.getAvailableStrikes().values
        strike_diffs = (active_strikes[:, None] - active_strikes).ravel()
        strike_diffs = np.unique(np.abs(strike_diffs))
        strike_diffs = strike_diffs[strike_diffs > 0]
        strike_diffs_str = [str(val) for val in strike_diffs]
        return strike_diffs, strike_diffs_str


    def setOffsetDefaults(self, constr_type):
        self.upper_offset_box.blockSignals(True)
        self.lower_offset_box.blockSignals(True)
    
        self.upper_offset_box.clear()
        self.upper_offset_box.setEnabled(False)
        self.lower_offset_box.setEnabled(False)
        if constr_type != OptionConstrType.single:
            strike_diffs, strike_diffs_str = self.getStrikeDifferences()
            self.upper_offset_box.addItems(strike_diffs_str)
            self.upper_offset_box.setEnabled(True)
            
            pref_pair = None
            if constr_type == OptionConstrType.vertical_spread or constr_type == OptionConstrType.iron_condor:
                preffered_diffs = Constants.PREFFERED_DIFFS_SMALL
                pref_pair = self.findPrefferedOffset(strike_diffs, preffered_diffs)
            elif constr_type == OptionConstrType.butterfly:
                preffered_diffs = Constants.PREFFERED_DIFFS_LARGE
                pref_pair = self.findPrefferedOffset(strike_diffs, preffered_diffs)

            if pref_pair is not None:
                self.upper_offset_box.setCurrentIndex(pref_pair[0])    
            
            if (constr_type == OptionConstrType.iron_condor) or (constr_type == OptionConstrType.split_butterfly):
                self.lower_offset_box.setEnabled(True)
                self.lower_offset_box.addItems(strike_diffs_str)
                if pref_pair is not None:
                    self.lower_offset_box.setCurrentIndex(pref_pair[0])

        self.upper_offset_box.blockSignals(False)
        self.lower_offset_box.blockSignals(False)
        


    def setRatioDefaults(self, constr_type):
        
        self.upper_ratio_box.blockSignals(True)
        self.base_ratio_box.blockSignals(True)
        self.lower_ratio_box.blockSignals(True)
        

        if constr_type == OptionConstrType.butterfly:
            ratios = [1,2,1]
        else:
            ratios = [1,1,1]

        self.upper_ratio_box.setEnabled(False)
        self.lower_ratio_box.setEnabled(False)
        if constr_type != OptionConstrType.single:
            self.upper_ratio_box.setEnabled(True)
            self.lower_ratio_box.setEnabled(True)
        
        self.upper_ratio_box.setValue(ratios[0])
        self.base_ratio_box.setValue(ratios[1])
        self.lower_ratio_box.setValue(ratios[2])
        self.upper_ratio_box.blockSignals(False)
        self.base_ratio_box.blockSignals(False)
        self.lower_ratio_box.blockSignals(False)
        


    def radioAllSelection(self, value):
        if self.premium_a_radio.isChecked():
            self.all_option_frame.setPriceType('premium')
        elif self.price_a_radio.isChecked():
            self.all_option_frame.setPriceType('price')
        elif self.rel_premium_a_radio.isChecked():
            self.all_option_frame.setPriceType('relative premium')
                                
        
    def radioStrikeSelection(self, value):
        if self.premium_s_radio.isChecked():
            self.strike_comp_frame.setPremium(True)
        elif self.price_s_radio.isChecked():
            self.strike_comp_frame.setPremium(False)


    def snapshotChange(self, value):
        self.option_data_manager.snapshot = value


    def selectedContract(self, contractDetails):
        self.symbol_label.setText(contractDetails.long_name + ' (' + contractDetails.exchange + ')')
        self.current_selection = contractDetails
            

        #this is the callback from the symbol textbox selection
    def returnSelection(self):
        if self.current_selection is not None:
            self.stock_selection_signal.emit(self.current_selection)
            self.stock_fetch_initiated = True
            self.first_price = True
            self.updateOptionGUI([],[])
            self.current_selection = None


    @pyqtSlot(str, dict)
    def apiUpdate(self, signal, sub_signal):
        if signal == Constants.OPTION_INFO_LOADED:
            self.updateOptionGUI(sub_signal['expirations'], sub_signal['strikes'])
            self.fetch_all_button.setEnabled(sub_signal['is_verified'])
            
                #if we just fetched for the first time, we want to fetch basic price infs
            if self.stock_fetch_initiated:
                self.expiration_box.setCurrentIndex(1)
                self.strike_box.setCurrentIndex(int(len(sub_signal['strikes'])/2))
        
        elif signal == Constants.OPTIONS_LOADED:
            self.fetch_all_button.setEnabled(True)
            self.setGUIValues(self.all_option_frame.getBoundaries())
        elif signal == Constants.PROGRESS_UPDATE:
            if sub_signal['open_requests'] == 0:
                self.statusbar.showMessage(f"All {sub_signal['request_type']} requests completed")
            else:
                self.statusbar.showMessage(f"{sub_signal['open_requests']} of {sub_signal['total_requests']} {sub_signal['request_type']} requests left")


    @pyqtSlot(float, str)
    def underlyingPriceUpdate(self, price, tick_type):
        if self.first_price:
            self.strike_plot.addPriceLine()
            self.first_price = False
        self.updatePrice(price)
    
        
    def requestLiveUpdates(self, current_selection):
        dates_by_days = {item[0]: item[2] for item in self.expiration_pairs}
        if current_selection['plot_type'] == 'expiration_grouped':
            self.req_by_exp_execute.emit(dates_by_days[current_selection['key']])
            self.tab_plot_widget.setCurrentIndex(0)
        elif current_selection['plot_type'] == 'strike_grouped':
            self.req_by_strike_execute.emit(current_selection['key'])
            self.tab_plot_widget.setCurrentIndex(1)
        

    def requestPL(self, current_selection):
        self.tab_plot_widget.setCurrentIndex(4)
        self.all_option_frame.setSelectedStrike(current_selection['x_value'], current_selection['key'], current_selection['y_value'])
    

    def updatePrice(self, price):
        self._underlying_price = price
        if self.last_price is not None:
            if self.last_price > price:
                self.price_label.setText('<font color="red">' + str(price) + '</font>')
            else:
                self.price_label.setText('<font color="green">' + str(price) + '</font>')
        else:
            self.price_label.setText(str(price))

        self.last_price = price
        self.updatePlotPrice(price)


    def expirationSelectionChange(self, index_value):
        expirations = [item[2] for item in self.expiration_pairs]
        self.req_by_exp_execute.emit(expirations[index_value])


    def strikeSelectionChange(self, index_value):
        strike_values = [item[0] for item in self.strike_pairs]
        self.req_by_strike_execute.emit(strike_values[index_value])


    def constructionPropsChange(self):
        self.constr_change_signal.emit(self.option_type, self.order_type, self.constr_type.value, self.getCurrentOffsets(), self.getCurrentRatios())
            

    def fetchAllStrikes(self):
        self.fetch_all_button.setEnabled(False)
        option_types = []
        if self.call_selection.isChecked():
            option_types.append(Constants.CALL)
        if self.put_selection.isChecked():
            option_types.append(Constants.PUT)

        min_strike, max_strike, min_exp, max_exp = self.getDownloadRanges()
        self.req_all_strikes.emit(option_types, min_strike, max_strike, min_exp, max_exp)


    def getDownloadRanges(self):
        min_strike = self.strike_pairs[self.min_strike_box.currentIndex()][0]
        max_strike = self.strike_pairs[self.max_strike_box.currentIndex()][0]
        min_exp = self.expiration_pairs[self.min_exp_box.currentIndex()][0]
        max_exp = self.expiration_pairs[self.max_exp_box.currentIndex()][0]
        return min_strike, max_strike, min_exp, max_exp


    def callPutAction(self, value):
        if value == self.put_radio: new_type = Constants.PUT
        if value == self.call_radio: new_type = Constants.CALL
        if new_type != self.option_type:
            self.option_type = new_type
            self.constructionPropsChange()
            
    
    def buySellAction(self, value):
        if value == self.buy_radio:
            self.order_type = Constants.BUY
            self.constructionPropsChange()
        elif value == self.sell_radio:
            self.order_type = Constants.SELL
            self.constructionPropsChange()


        #TODO this should be in super
    def accepts(self, value):
        return False
        