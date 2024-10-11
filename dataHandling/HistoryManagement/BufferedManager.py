
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


from dataHandling.Constants import Constants, MAIN_BAR_TYPES, DT_BAR_TYPES, DOWNLOADABLE_BAR_TYPES
from dataHandling.DataStructures import DetailObject
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from pytz import utc
from generalFunctionality.GenFunctions import standardBeginDateFor
from generalFunctionality.DateTimeFunctions import getCurrentUtcTime

from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot, QThread, Qt, QEventLoop


class BufferedDataManager(QObject):

    api_updater = pyqtSignal(str, dict)

    alternate_list = None
    queue_update = False
    max_day_diff = 3
    stocks_to_fetch = dict()
    updated_through = dict()
    initial_fetch = True

    fetching_bars = None

    queued_update_requests = []

    reset_signal = pyqtSignal(int)
    create_request_signal = pyqtSignal(int, DetailObject, datetime, datetime, str, bool)
    request_update_signal = pyqtSignal(int, dict, dict, str, bool, bool)
    group_request_signal = pyqtSignal(str)
    execute_request_signal = pyqtSignal(int)


    def __init__(self, history_manager, name="BufferedManager"):
        super().__init__()
        self.name = name
        self.history_manager = history_manager
        self.hist_id = self.history_manager.registerOwner()
        self.data_buffers = history_manager.getDataBuffer()
        self.data_buffers.save_on = True
        self.history_manager.addNewListener(self, self.apiUpdate)
        

    def moveToThread(self, thread):
        super().moveToThread(thread)
        self.connectSignalsToSlots()


    def getDataBuffer(self):
        return self.data_buffers
        

    def connectSignalsToSlots(self):
        print(self.history_manager)
        self.reset_signal.connect(self.history_manager.cancelActiveRequests, Qt.QueuedConnection)
        self.create_request_signal.connect(self.history_manager.createRequestsForContract, Qt.QueuedConnection)
        self.request_update_signal.connect(self.history_manager.requestUpdates, Qt.QueuedConnection)
        self.group_request_signal.connect(self.history_manager.groupCurrentRequests, Qt.QueuedConnection)
        self.execute_request_signal.connect(self.history_manager.iterateHistoryRequests, Qt.QueuedConnection)
        
        # print("BufferedManager.connectSignalsToSlots finished")

    
    ################ LIST HANDLING

    def setStockList(self, buffering_stocks):
        self.initial_fetch = True
        self._buffering_stocks = buffering_stocks.copy()
        self.data_buffers.loadBuffers(self._buffering_stocks)


    ################ CALLBACK

    @pyqtSlot(str, dict)
    def apiUpdate(self, signal, data_dict):
        if signal == Constants.HISTORICAL_GROUP_COMPLETE or signal == Constants.HISTORICAL_UPDATE_COMPLETE:
            if len(self.queued_update_requests) > 0:
                request = self.queued_update_requests.pop(0)
                self.requestUpdates(update_bar=request['bar_type'], keep_up_to_date=request['keep_up_to_date'], propagate_updates=True, update_list=request['update_list'], allow_splitting=request['allow_splitting'])
            else:
                self.api_updater.emit(Constants.ALL_DATA_LOADED, dict())
                self.initial_fetch = False


    ################ CREATING AND TRIGGERING HISTORIC REQUESTS

    def fetchLatestStockDataWithCancelation(self, bar_types=MAIN_BAR_TYPES):
        self.history_manager.cleanup_done_signal.connect(lambda: self.fetchLatestStockData(bar_types, True), Qt.QueuedConnection)
        self.reset_signal.emit(self.hist_id)
        

    @pyqtSlot()
    @pyqtSlot(list)
    def fetchLatestStockData(self, bar_types=MAIN_BAR_TYPES, needs_disconnect=False):
        if needs_disconnect: self.history_manager.cleanup_done_signal.disconnect()

        self.stocks_to_fetch = self.findStockInNeedOfDownload()

        print(self.stocks_to_fetch)
        self.fetching_bars = bar_types

        if len(self.stocks_to_fetch) > 0:

            for uid, stock_inf in self.stocks_to_fetch.items():
                self.queStockRequestsFor(uid, stock_inf, bar_types=bar_types)
                #if there is a mix, we mark this as a partial update to ensure updates are done after the initial fetch                
            self.group_request_signal.emit('full_update')
            
            self.queued_update_requests.append({'bar_type': Constants.ONE_MIN_BAR, 'update_list': self._buffering_stocks, 'keep_up_to_date': False, 'allow_splitting': True})
            self.execute_request_signal.emit(4_000)
        else:
            self.requestUpdates(update_list=self._buffering_stocks, propagate_updates=True)
            

    def findStockInNeedOfDownload(self):
        stocks_to_fetch = dict()
        for uid, value in self._buffering_stocks.items():
            all_ranges_within = self.allRangesWithinUpdate(uid)
            print(f"Do we get a negative for: {all_ranges_within}")
            if not all_ranges_within    :
                stocks_to_fetch[uid] = value
            
        return stocks_to_fetch

    def allRangesWithinUpdate(self, uid, bar_types=MAIN_BAR_TYPES):
        for bar_type in bar_types:
            if self.data_buffers.bufferExists(uid, bar_type):
                last_timestamp = self.data_buffers.getIndexAtPos(uid, bar_type, pos=-1)
                if not self.isRecent(last_timestamp):
                    return False
            else:
                return False

        return True


    def isRecent(self, timestamp):
        current_dateTime = getCurrentUtcTime()
        dt_object = datetime.utcfromtimestamp(timestamp)
        utc_aware_dt = dt_object.replace(tzinfo=utc)
        day_diff = (current_dateTime-utc_aware_dt).days
        return day_diff < self.max_day_diff


    def queStockRequestsFor(self, uid, stock_inf, bar_types=None):
        print("BufferedManager.queStockRequestsFor")
        if bar_types is None: bar_types = MAIN_BAR_TYPES

        details = DetailObject(numeric_id=uid, **stock_inf)

        for bar_type in bar_types:
            date_ranges = self.getDateRanges(uid, bar_type, False)
            for begin_date, end_date in date_ranges:
                downloadable_bar = DOWNLOADABLE_BAR_TYPES[bar_type]
                self.create_request_signal.emit(self.hist_id, details, begin_date, end_date, downloadable_bar, True)
        


    @pyqtSlot(str, bool, bool)
    def requestUpdates(self, update_bar=Constants.ONE_MIN_BAR, keep_up_to_date=False, propagate_updates=False, update_list=None, needs_disconnect=False, allow_splitting=True):
        print(f"BufferedManager.requestUpdates {update_bar} {keep_up_to_date} {propagate_updates}")

        if needs_disconnect: self.history_manager.cleanup_done_signal.disconnect()
        
        if update_list is None:
            update_list = self._buffering_stocks.copy()

        update_bar = DOWNLOADABLE_BAR_TYPES[update_bar]
        if allow_splitting and self.smallerThanFiveMin(update_bar):
            self.requestUpdatesWithSplitting(update_bar, keep_up_to_date, propagate_updates, update_list)
        else:
            self.requestUpdatesWithMinimum(update_bar, keep_up_to_date, propagate_updates, update_list)


    def requestUpdatesWithMinimum(self, update_bar, keep_up_to_date, propagate_updates, update_list):
        print(f"BufferedManager.requestUpdatesWithMinimum {self.hist_id}")
        now_time = getCurrentUtcTime()
        begin_dates = dict()
        for uid in update_list:
            min_end_date = self.getUpdateStart(uid)
            max_begin_date = now_time - relativedelta(minutes=180)
            begin_dates[uid] = min(min_end_date, max_begin_date)
        self.request_update_signal.emit(self.hist_id, update_list, begin_dates, update_bar, keep_up_to_date, propagate_updates)


    def requestUpdatesWithSplitting(self, update_bar, keep_up_to_date, propagate_updates, update_list):
        print(f"BufferedManager.requestUpdatesWithSplitting {self.hist_id}")
        now_time = getCurrentUtcTime()
        five_min_update_list = dict()
        for uid in update_list:
            begin_date = self.getUpdateStart(uid)
            total_seconds = int((now_time-begin_date).total_seconds())
            if total_seconds > 10800:
                five_min_update_list[uid] = update_list[uid]
                five_min_update_list[uid]['begin_date'] = begin_date

        
        begin_dates = dict()
        for uid in update_list:
            begin_dates[uid] = now_time - relativedelta(minutes=180)
        
        if len(five_min_update_list) > 0:
            self.request_update_signal.emit(self.hist_id, five_min_update_list, begin_dates, Constants.FIVE_MIN_BAR, False, propagate_updates)
            self.queued_update_requests.append({'bar_type': update_bar, 'update_list': update_list, 'keep_up_to_date': keep_up_to_date, 'allow_splitting': False})
        else:
            self.request_update_signal.emit(self.hist_id, update_list, begin_dates, update_bar, keep_up_to_date, propagate_updates)


    ################ DATE AND RANGE HANDLING


    def getUpdateStart(self, uid, bar_types=MAIN_BAR_TYPES):
        minimum_date = None
        for bar_type in bar_types:
            print(f"For {bar_type} we get {self.data_buffers.bufferExists(uid, bar_type)}")
            if self.data_buffers.bufferExists(uid, bar_type):
                existing_ranges = self.data_buffers.getRangesForBuffer(uid, bar_type)
                print(f"Never here {existing_ranges[-1]}")
                if len(existing_ranges) > 0:
                    if minimum_date is None:
                        minimum_date = existing_ranges[-1][1]
                    elif existing_ranges[-1][1] < minimum_date:
                        minimum_date = existing_ranges[-1][1]

        if minimum_date is None:
            current_dt = getCurrentUtcTime()
            minimum_date = current_dt - timedelta(days=3)

        return minimum_date


    def smallerThanFiveMin(self, bar_type):
        return ((bar_type == Constants.ONE_MIN_BAR) or (bar_type == Constants.TWO_MIN_BAR) or (bar_type == Constants.THREE_MIN_BAR))


    def getDateRanges(self, uid, bar_type, full_fetch=False):
        end_date = getCurrentUtcTime()

        if full_fetch:
            return self.getFullRanges(uid, bar_type, end_date)
        else:
            return self.getStandardRanges(uid, bar_type, end_date)
        

    def getStandardRanges(self, uid, bar_type, end_date):
        standard_begin_date = standardBeginDateFor(end_date, bar_type)
        desired_range = (standard_begin_date, end_date)
        if self.data_buffers.bufferExists(uid, bar_type):
            return self.data_buffers.getMissingRangesFor(uid, bar_type, desired_range)
        else:
            return [desired_range]


    def getFullRanges(self, uid, bar_type, end_date):
        print("BufferedManager.getFullRanges")
            #TODO: this code should be updated
        if uid in self.history_manager.earliest_date_by_uid:
            earliest_date = self.history_manager.earliest_date_by_uid[uid]
        else:
            now = getCurrentUtcTime()
            earliest_date = now - relativedelta(years=10)

        if (uid, bar_type) in self.existing_buffers:
            begin_date = earliest_date
            missing_ranges = self.data_buffers.getMissingRangesFor(uid, bar_type, (begin_date, end_date))
            return missing_ranges
        else:
            return [(earliest_date, end_date)]


    def deregister(self):
        print(f"We deregister {self.hist_id}")
        self.history_manager.deregisterOwner(self.hist_id)
        print(f"Which leaves us with: {self.history_manager.owner_count}")
        if self.history_manager.owner_count == 0:
            print("So we finish up")
            self.history_manager.finished.emit()
        

    @pyqtSlot()
    def cancelUpdates(self):
        print("We ask for cancelling")
        if self.history_manager.is_updating:
            print("We trigger a reset in history_manager")
            self.reset_signal.emit(self.hist_id)


