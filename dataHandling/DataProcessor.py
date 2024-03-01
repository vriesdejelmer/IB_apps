from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot, Qt
from dataHandling.Constants import Constants
from datetime import datetime, timedelta
import pandas as pd
from pytz import timezone
import itertools
from dataHandling.HistoryManagement.BufferedManager import BufferedDataManager


class DataProcessor(QObject):

    stock_df = None
    previous_df = None
    _index_list = None
    stale_delay_min = 15

    initial_fetch = False

    def __init__(self, history_manager, stock_list=None, index_list=None):
        super().__init__()
        print("DataProcessor.init")
        self.buffered_manager = BufferedDataManager(history_manager, name="MoversBuffer")
        self.data_buffers = self.buffered_manager.data_buffers
        self.data_buffers.buffer_updater.connect(self.bufferUpdate, Qt.QueuedConnection)
        self.initial_stock_list = stock_list
        self.initial_index_list = index_list


    def moveToThread(self, thread):
        self.buffered_manager.moveToThread(thread)
        super().moveToThread(thread)
    

    @pyqtSlot()
    def run(self):
        print(f"Dataprocessor is running on {int(QThread.currentThreadId())}")
        if self.initial_index_list is not None:
            self._index_list = self.initial_index_list

        self.setStockList(self.initial_stock_list)

    def stop(self):
        print("THIS SHOULD BE MADE DEPENDENT ON WHETHER THE OWNER IS SINGULAR")
        self.buffered_manager.reset_signal.emit()


############## DATA PROCESSING


    @pyqtSlot()
    def fetchLatestStockData(self):
        # print(f"This should be the data_processor THREAD: {int(QThread.currentThreadId())}")
        self.updated_uids = []
        self.buffered_manager.fetchLatestStockData()


    @pyqtSlot(str, bool)
    def requestUpdatesSlot(self, base_bar_type, keep_up_to_date=False):
        self.buffered_manager.requestUpdates(keep_up_to_date=keep_up_to_date)


    @pyqtSlot(dict)
    def setStockList(self, stock_list):
        self._stock_list = stock_list

        if self._index_list is not None:
            merged_dict = {**stock_list, **self._index_list}
            self.buffered_manager.setStockList(merged_dict)
        else:
            self.buffered_manager.setStockList(stock_list)


    def determineStale(self):
        keys = self._stock_list.keys()
        delay_dif = timedelta(minutes=self.stale_delay_min)
        now_time = pd.to_datetime(datetime.now(timezone(Constants.NYC_TIMEZONE)))
        
        for uid in keys:
            self.stock_df.loc[uid, Constants.STALE] = True      #We assume data is stale

            if self.data_buffers.bufferExists(uid, Constants.FIVE_MIN_BAR):
                last_five_min_mark = self.data_buffers.getIndicesFor(uid, Constants.FIVE_MIN_BAR).max()
                        
                time_del = (now_time - last_five_min_mark)
                if time_del < delay_dif:
                    self.stock_df.loc[uid, Constants.STALE] = False   
            

    def getBarData(self, uid, bar_type):
        if self.data_buffers.bufferExists(uid, bar_type):
            return self.data_buffers.getBufferFor(uid, bar_type)
        return None




