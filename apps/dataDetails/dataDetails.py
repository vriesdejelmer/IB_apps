
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot

import pandas as pd
import numpy as np
from dataHandling.Constants import Constants, TableType, MAIN_BAR_TYPES
from .DataDetailsWindow import DataDetailsWindow
from .polygonDownloader import PolygonDownloader

from dataHandling.HistoryManagement.BufferedManager import BufferedDataManager
import sys #, threading, math

from ibapi.contract import Contract
from uiComps.TableModels import PandasDataModel
from uiComps.customWidgets.TaskProgressWindow import TaskProgressWindow

from dataHandling.TradeManagement.UserDataManagement import readStockList

from generalFunctionality.GenFunctions import dateToReadableString
from datetime import datetime
from dateutil.relativedelta import relativedelta


class DataDetails(DataDetailsWindow):

    timer = None
    download_selection = "Whole List"
    data_processor = None
    buffered_manager = None
    status_window = None

    def __init__(self, history_manager):
        super().__init__(MAIN_BAR_TYPES)

        file_name, _ = self.stock_lists[0]
        self.stock_list = readStockList(file_name)

        self.buffered_manager = BufferedDataManager(history_manager, self.stock_list, name="MoversBuffer")
        self.buffered_manager.api_updater.connect(self.apiUpdate)
        self.selected_key = list(self.stock_list.keys())[0]
        self.selected_bar_type = self.bar_types[0]
        
        
        self.history_manager = history_manager
        self.history_manager.most_recent_first = True
        self.history_manager.queue_cap = 10

        self.polygonDownloader = PolygonDownloader()
        self.polygonDownloader.api_updater.connect(self.apiUpdate)
        self.polygonDownloader.start()

        self.generateColumnNames() #TODO: this is a bit ugly
        self.resetTickerList()
        self.resetDataFrames()
        self.initDataModels()
        self.trade_plot.clearPlot()
        self.trade_plot.setHistoricalData(self.data_frame_points.copy())
        self.ticker_description_label.setText(self.stock_list[self.selected_key]['long_name'])
        self.setTableProperties()

        #self.history_manager.fetchEarliestDates(self.stock_list)

    def getCurrentKey(self):
        return (self.selected_key, self.selected_bar_type)


    def hasDataForCurrentKey(self):
        return self.getCurrentKey() in self.buffered_manager.existing_buffers


    def resetDataFrames(self):
        if self.hasDataForCurrentKey():
            self.resetCounts()
            self.resetDataPoints()
            self.resetRanges()
        else:
            self.data_count_frame = pd.DataFrame(columns=self.count_columns)
            self.data_frame_ranges = pd.DataFrame(columns=self.range_columns)
            self.data_frame_points = pd.DataFrame(columns=self.point_columns)


    def resetCounts(self):
        # Initialize an empty dataframe to store results
        self.data_count_frame = pd.DataFrame()

        for key, df in self.buffered_manager.existing_buffers.items():
            if key[0] == self.selected_key:

                counts = df.between_time('09:30', '16:00').resample('D').count().iloc[:, 0]
                # The counts Series will have as index the dates and the counts as values
                # Convert it to DataFrame and rename the column with the name of the current dataframe
                counts.replace(0, np.nan, inplace=True)

                counts = counts.to_frame(name=str(key[1]))
                # If data_count_frame is empty, assign directly
                if self.data_count_frame.empty:
                    self.data_count_frame = counts
                # If not, join with existing dataframe
                else:
                    self.data_count_frame = self.data_count_frame.join(counts, how='outer')

        print(self.data_count_frame)
        self.data_count_frame = self.data_count_frame.reindex(columns=self.count_columns)
        self.data_count_frame.dropna(how='all', inplace=True)

    # def resetCounts(self):
    #     # Initialize an empty dataframe to store results
    #     self.data_count_frame = pd.DataFrame(columns=self.count_columns)

    #     for key, df in self.buffered_manager.existing_buffers.items():
    #         if key[0] == self.selected_key:

    #             counts = df.between_time('09:30', '16:00').resample('D').count().iloc[:, 0]
    #             # The counts Series will have as index the dates and the counts as values
    #             # Convert it to DataFrame and rename the column with the name of the current dataframe
    #             counts.replace(0, np.nan, inplace=True)

    #             counts = counts.to_frame(name=str(key[1]))
    #             # Finally, we join this dataframe to our result dataframe
    #             self.data_count_frame = pd.concat([self.data_count_frame, counts], axis=1)

    #     self.data_count_frame.dropna(how='all', inplace=True)


    def resetDataPoints(self):
        key_tuple = (self.selected_key, self.selected_bar_type)
        self.data_frame_points = self.buffered_manager.existing_buffers[key_tuple]
        

    def resetRanges(self):

        self.data_frame_ranges = pd.DataFrame(columns=self.range_columns)

        for key, df in self.buffered_manager.existing_buffers.items():
            if key[0] == self.selected_key:
                curr_ranges = df.attrs['ranges']
                ranges_df = pd.DataFrame(curr_ranges, columns=['Start', 'End'])
                ranges_df['Time frame'] = key[1]
                self.data_frame_ranges = pd.concat([self.data_frame_ranges, ranges_df], axis=0)


    def resetTickerList(self):
        self.ticker_selector.blockSignals(True)
        self.ticker_selector.clear()
        for uid, stock_inf in self.stock_list.items():
            self.ticker_selector.addItem(stock_inf[Constants.SYMBOL])
        self.ticker_selector.blockSignals(False)


    def updateTables(self):
        self.data_count_model.setDataFrame(self.data_count_frame)
        self.data_point_model.setDataFrame(self.data_frame_points)
        self.data_ranges_model.setDataFrame(self.data_frame_ranges)
        self.trade_plot.clearPlot()
        self.trade_plot.setHistoricalData(self.data_frame_points.copy())

        self.data_ranges_model.layoutChanged.emit()
        self.data_point_model.layoutChanged.emit()
        self.data_count_model.layoutChanged.emit()
        

    def generateColumnNames(self):
        self.count_columns = self.bar_types
        self.point_columns = [Constants.OPEN, Constants.CLOSE, Constants.LOW, Constants.HIGH, Constants.VOLUME]
        self.range_columns = ['Time frame', 'Start', 'End']

        
    def initDataModels(self):

        # Print the DataFrame

        mapping = {0: '__INDEX__'}
        for index, bar_type in enumerate(self.bar_types):
            mapping[index+1] = bar_type
        header_labels = ['Date', '5 min', '15 min', '1 hour', '4 hour', '1 day']
        self.data_count_model = PandasDataModel(self.data_count_frame, mapping, header_labels=header_labels)
        self.data_count_table.setModel(self.data_count_model)
        self.data_count_model.api_updater.connect(self.processingUpdate)


        mapping = {0: '__INDEX__', 1: Constants.OPEN, 2: Constants.CLOSE, 3: Constants.LOW, 4: Constants.HIGH, 5: Constants.VOLUME}
        header_labels = ['Time', 'Open', 'Close', 'Low', 'High', 'Volume']
        self.data_point_model = PandasDataModel(self.data_frame_points, mapping, header_labels=header_labels)
        self.data_point_table.setModel(self.data_point_model)
        self.data_point_model.api_updater.connect(self.processingUpdate)


        mapping = {0: 'Time frame', 1: 'Start', 2: 'End'}
        self.data_ranges_model = PandasDataModel(self.data_frame_ranges, mapping)
        self.data_ranges_table.setModel(self.data_ranges_model)
        self.data_ranges_model.api_updater.connect(self.processingUpdate)

        # self.models = [self.overview_model, self.low_model, self.high_model, self.step_up_model, self.step_down_model, self.rsi_model, self.rel_rsi_model, self.index_corr_model]
        # for model in self.models: model.greyout_stale = self.use_stale_box.isChecked()

############## DATA PROCESSING


    @pyqtSlot(str, dict)
    def apiUpdate(self, signal, sub_signal):
        print(f"DataDetails.apiUpdate {signal}")
        if signal == Constants.DATES_RETRIEVED:
            self.earliest_date_by_uid = self.history_manager.earliest_date_by_uid
            self.earliest_date_label.setText(dateToReadableString(self.earliest_date_by_uid[self.selected_key]))
        elif signal == Constants.QUEUED_NEW_TASKS:
            self.createStatusWindow()
        elif signal == Constants.HISTORICAL_REQUEST_COMPLETED:
            if self.status_window is not None:
                self.status_window.updateTaskStatus(sub_signal['req_id'], "1: Completed")
            self.resetDataFrames()
            self.updateTables()
        elif signal == Constants.HISTORICAL_REQUEST_SUBMITTED:
            if self.status_window is not None:
                self.status_window.updateTaskStatus(sub_signal['req_id'], "0: Submitted")
        elif signal == Constants.POLYGON_REQUEST_COMPLETED:
            print("We receive polygon data!")
            uid_list = list(self.stock_list.keys())
            symbol_list = [stock_info[Constants.SYMBOL] for stock_info in self.stock_list.values()]
            for (symbol, polygon_bar_type), df in sub_signal.items():
                index = symbol_list.index(symbol)
                bar_type = self.getBarFromPolygonType(polygon_bar_type)
                self.buffered_manager.existing_buffers[uid_list[index], bar_type] = df
                print(f"We save for {polygon_bar_type}")
                self.buffered_manager.saveBuffers(for_uids=[uid_list[index]], for_bars=[bar_type], clear=True, polygon=True)


    def getBarFromPolygonType(self, polygon_bar):
        split_polygon_bar = polygon_bar.split()
        count = int(split_polygon_bar[0])
        unit = split_polygon_bar[1]

        if unit == 'minute':
            unit = 'min'
        elif unit == 'hour':
            unit = 'hour'

        if count > 1:
            unit += 's'
        return f"{count} {unit}"


    def listSelection(self, value):
        file_name, _ = self.stock_lists[value]
        self.stock_list = readStockList(file_name)
        self.selected_key = list(self.stock_list.keys())[0]
        self.buffered_manager.setStockList(self.stock_list)
        self.buffered_manager.history_manager.cancelActiveRequests(self)
        ordered_keys = list(self.buffered_manager.existing_buffers.keys())
        #self.history_manager.fetchEarliestDates(self.stock_list)
        self.resetTickerList()
        

    def frameChecksChanged(self, value):
        print(f"Does this help sufficiently? {value}")
        print(self.download_frame_selector.itemState(value))
        self.bar_selection[self.bar_types[value]] = self.download_frame_selector.itemState(value)

    def createStatusWindow(self):
        requests = self.history_manager.request_buffer
        data = {
            "Req ID": [req.req_id for req in requests],
            "Ticker ID": [req.contract.symbol for req in requests],
            "Bars": [f"{req.bar_type}" for req in requests],
            "Duration": [f"{req.period_string}" for req in requests],
            "End Date": [f"{dateToReadableString(req.end_date)}" for req in requests],
            "Status": ["-1: Pending"] * len(requests)
        }

        task_frame = pd.DataFrame(data)

        self.status_window = TaskProgressWindow(task_frame)
        self.status_window.setMinimumSize(600, 400)
        self.status_window.show()
        


############## GUI SIGNALING

    def radioSelection(self, value):
        if self.rb_single_ticker.isChecked():
            self.download_selection = "Single Ticker"
            self.download_list_checker.setEnabled(False)
        elif self.rb_all_lists.isChecked():
            self.download_selection = "Multiple Lists"
            self.download_list_checker.setEnabled(True)
        elif self.rb_whole_list.isChecked():
            self.download_selection = "Whole List"
            self.download_list_checker.setEnabled(False)

    def tickerSelection(self, value):
        ordered_keys = list(self.stock_list.keys())
        self.selected_key = ordered_keys[value]
        self.resetDataFrames()
        self.updateTables()
        self.ticker_description_label.setText(self.stock_list[self.selected_key]['long_name'])


    def downloadData(self):
        selected_bar_types = [k for k, v in self.bar_selection.items() if v is True]
        if self.download_selection == "Single Ticker":
            self.buffered_manager.fetchHistStockData(bar_types=selected_bar_types, selected_uid=self.selected_key)
        elif self.download_selection == "Whole List":
            self.buffered_manager.fetchHistStockData(bar_types=selected_bar_types)
        elif self.download_selection == "Multiple Lists":
            pass
            # for list in 
            # self.buffered_manager.fetchHistStockData(bar_types=selected_bar_types)


    def downloadPolygonData(self):

        current_date = datetime.now()
        start_date = current_date - relativedelta(years=5)

        for bar_type, checked in self.selected_polygon_bars.items():
            if checked:
                if self.download_selection == "Single Ticker":
                    symbol = self.stock_list[self.selected_key][Constants.SYMBOL]
                    self.polygonDownloader.downloadForSymbol(symbol, bar_type, (start_date, current_date))
                elif self.download_selection == "Whole List":
                    symbol_list = [stock_info[Constants.SYMBOL] for stock_info in self.stock_list.values()]
                    self.polygonDownloader.downloadForSymbols(symbol_list, bar_type, (start_date, current_date))
                elif self.download_selection == "Multiple Lists":
                    pass
            # for list in 
            # self.buffered_manager.fetchHistStockData(bar_types=selected_bar_types)


    def polygonBarSelection(self, value):
        print(self.polygon_bar_types)
        print("-------")
        print(value)
        print("---0---")
        print(self.selected_polygon_bars)

        self.selected_polygon_bars[self.polygon_bar_types[value]] = self.polygon_bar_selector.itemState(value)

    def timeFramePointSel(self, value):
        self.selected_bar_type = self.bar_types[value]
        self.bar_selector_graph.setCurrentIndex(value)
        self.resetDataPoints()
        self.updateTables()


    def timeFrameGraphSel(self, value):
        self.selected_bar_type = self.bar_types[value]
        self.bar_selector_point.setCurrentIndex(value)
        self.resetDataPoints()
        self.updateTables()


    def processingUpdate(self, signal):
        print(f"DataDetails.processingUpdate {signal}")
        if signal == Constants.DATA_WILL_CHANGE:
            pass
        elif signal == Constants.DATA_DID_CHANGE:
            self.data_count_model.layoutChanged.emit()
            self.data_point_model.layoutChanged.emit()
            self.data_ranges_model.layoutChanged.emit()

    
    def signalCurrentTable(self):
        current_index = self.tab_widget.currentIndex()
        current_model = self.list_of_tables[current_index].model()
        current_model.layoutChanged.emit()
        current_model.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())


    def keepUpToDate(self, value):
        if value:
            self.buffered_manager.requestUpdates(keep_up_to_date=value)
    

