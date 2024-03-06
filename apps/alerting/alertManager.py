# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionsGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore #, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from dataHandling.HistoryManagement.HistoricalDataManagement import HistoricalDataManager
from dataHandling.HistoryManagement.FinazonDataManager import FinazonDataManager
from dataHandling.Constants import Constants, DT_BAR_TYPES
from .AlertWindow import AlertWindow

from PyQt5.QtWidgets import QMainWindow

import json
import requests

import re

from .AlertProcessor import AlertProcessorFinazon, AlertProcessorIB
from dataHandling.TradeManagement.UserDataManagement import getStockListNames, readStockList
from dataHandling.HistoryManagement.BufferedManager import BufferedDataManager

from itertools import cycle


class AlertManager(AlertWindow):

    selection_signal_change = pyqtSignal(str, dict)
    threshold_signal_change = pyqtSignal(str, dict)
    update_signal = pyqtSignal(bool)
    list_addition_signal = pyqtSignal(str)
    list_removal_signal = pyqtSignal(str)
    alerting_signal = pyqtSignal(bool)

    updating = False
    message_listening = False
    controller_delegate = None
    last_update_id = 0
    

    def __init__(self, delegate, history_manager, telegram_signal):
        super().__init__()

        self.controller_delegate = delegate

        history_manager.api_updater.connect(self.apiUpdate, Qt.QueuedConnection)

        self.bot_info = self.readBotInfo()
        self.loadLists()
        file_name, _ = self.stock_lists[0]
        self.history_manager = history_manager
        self.prepAlertProcessor(history_manager, telegram_signal)


    def prepAlertProcessor(self, history_manager, telegram_signal):
        if isinstance(history_manager, FinazonDataManager):
            self.alert_processor = AlertProcessorFinazon(history_manager)
        elif isinstance(history_manager, HistoricalDataManager):
            self.alert_processor = AlertProcessorIB(history_manager, telegram_signal)
        self.processor_thread = QThread()
        self.alert_processor.moveToThread(self.processor_thread)
        
        self.update_signal.connect(self.alert_processor.runUpdates, Qt.QueuedConnection)
        self.list_addition_signal.connect(self.alert_processor.addStockList, Qt.QueuedConnection)
        self.list_removal_signal.connect(self.alert_processor.removeStockList, Qt.QueuedConnection)
        self.alerting_signal.connect(self.alert_processor.toggleAlerts, Qt.QueuedConnection)
        self.alert_processor.stock_count_signal.connect(self.stockCountUpdated, Qt.QueuedConnection)
        self.selection_signal_change.connect(self.alert_processor.selectionSignalChange, Qt.QueuedConnection)
        self.threshold_signal_change.connect(self.alert_processor.thresholdChangeSignal, Qt.QueuedConnection)

        self.processor_thread.started.connect(self.alert_processor.run)
        self.processor_thread.start()
        self.processor_thread.setPriority(QThread.HighestPriority)

        self.signalAlertPreferences()


    def signalAlertPreferences(self):
        self.updateCheckListFor("cross_box", "cross_checks")
        self.updateCheckListFor("reversal_box", "reversal_checks")
        self.updateCheckListFor("up_check", "up_checks")
        self.updateCheckListFor("down_check", "down_checks")
        self.updateThresholds("lower_spin", "cross_down_threshold")
        self.updateThresholds("higher_spin", "cross_up_threshold")
        self.updateThresholds("down_spin", "step_down_threshold")
        self.updateThresholds("up_spin", "step_up_threshold")


    def startUpdating(self):
        if not self.updating:
            self.updating = True
            # self.history_manager.lockForCentralUpdating(self)
            self.comp_checkable_lists.disableSelection()
            self.list_selection_button.setEnabled(False)
            self.rotation_button.setText("Stop Updates")
            self.update_signal.emit(True)
        else:
            self.update_signal.emit(False)
            self.comp_checkable_lists.enableSelection()
            # self.history_manager.unlockCentralUpdating()
            self.list_selection_button.setEnabled(True)
            self.rotation_button.setText("Rotating Updates")

            self.updating = False


    def loadLists(self):
        
        self.stock_lists = getStockListNames()
        #check_list = {k: False for k in range(len(self.stock_lists))}

        self.comp_checkable_lists.blockSignals(True)

        file_list = dict()

        for index, (file_name, list_name) in enumerate(self.stock_lists):

            file_list[index] = file_name
            self.comp_checkable_lists.key_list = file_list
            self.comp_checkable_lists.addItem(list_name)

            item = self.comp_checkable_lists.model().item(index, 0)
            item.setCheckState(QtCore.Qt.Unchecked)

        self.comp_checkable_lists.blockSignals(False)            

    
    def toggleDataListening(self, value):
        self.alerting_signal.emit(value)

    
    def stockCountUpdated(self, value):
        self.stock_count_label.setText(str(value))


    def updateCheckListFor(self, button_name, signal_type):
        check_list = dict()
        for tf in self.time_frame_names:
            if tf != 'all':
                check_list[self.bar_type_conv[tf]] = self.widgetFor(f"{button_name}_{tf}").isChecked()
        self.selection_signal_change.emit(signal_type, check_list)


    def updateThresholds(self, button_name, signal_type):
        threshold_list = dict()
        for tf in self.time_frame_names:
            if tf != 'all':
                threshold_list[self.bar_type_conv[tf]] = self.widgetFor(f"{button_name}_{tf}").value()
        self.threshold_signal_change.emit(signal_type, threshold_list)


    def closeEvent(self, *args, **kwargs):
        
        self.alert_processor.deleteLater()
        self.processor_thread.quit()
        self.processor_thread.wait()
        super(QMainWindow, self).closeEvent(*args, **kwargs)


    def listSelection(self, value):
        toggle, list_name = self.comp_checkable_lists.getSelectionAt(value)
        if toggle:
            self.list_addition_signal.emit(list_name)
        else:
            self.list_removal_signal.emit(list_name)


    def toggleSelection(self):
        if self.list_selection_button.text() == "All Off":
            self.list_selection_button.setText("All On")
            self.comp_checkable_lists.deselectAll()
        else:
            self.list_selection_button.setText("All Off")
            self.comp_checkable_lists.selectAll()

        print("Not here right?")


    def getStockList(self, for_index):            
        file_name, _ = self.stock_lists[for_index]


    def checkData(self):
        print("We check the data every so often")


    def checkMessages(self, dont_reply=False):

        method = 'getUpdates'
        api_url = f"https://api.telegram.org/bot{self.bot_info['token']}/"
        params = {'offset': self.last_update_id}
        resp = requests.post(api_url + method, params)
        
        json_dict = json.loads(resp.text)
        print(json.dumps(json_dict, sort_keys=True, indent=4, separators=(',', ': ')))
        messages = json_dict["result"]
        for message in messages:
            message_details = message["message"]
            self.parseMessage(message_details)
            self.last_update_id = message["update_id"] + 1

    
    def parseMessage(self, message_details):    
        if "text" in message_details:
            
            command, params = self.parseCommands(message_details["text"])
            response = self.controller_delegate.request(command, params)
            
            if response is not None:
                if "photo" in response:
                    self.sendPhoto(open(response["photo"], 'rb'))
                if "text" in response:
                    self.sendTextMessage(response["text"])
                
                # url = f"https://api.telegram.org/bot{self.bot_info['token']}/sendMessage?chat_id={self.bot_info['chat_id']}&parse_mode=HTML&text={return_message}"
                # requests.get(url)
                return
            else:
                self.sendTextMessage("No apps responding")


    def parseCommands(self, message):
        token_list = re.split("[., !?:()]+", message)
        print(token_list)
        command = token_list[0]
        param_dict = dict()
        for token in token_list[1:]:
            param = re.split("=", token)
            print(param)
            param_dict[param[0]] = param[1]
        return command, param_dict


    def sendTextMessage(self, message_text):
        print("Maybe this aint working")
        url = f"https://api.telegram.org/bot{self.bot_info['token']}/sendMessage?chat_id={self.bot_info['chat_id']}&parse_mode=HTML&text={message_text}"
        print(requests.get(url))


    @pyqtSlot(str, dict)
    def apiUpdate(self, signal, sub_signal):
        pass
        #super().apiUpdate(signal, sub_signal)
        # print(f"AlertManager.apiUpdate {signal}")
        # if signal == Constants.HISTORICAL_UPDATE_COMPLETE or signal == Constants.HISTORICAL_REQUESTS_COMPLETED:
        #     if self.rotating:
        #         self.fetchNextList()


    def accepts(self, value):
        return False


        # url = f"https://api.telegram.org/bot{bot_info['token']}/getUpdates"
        # anything = requests.get(url)
        # print(anything.text)
        #https://api.telegram.org/botyour_telegram_key/getUpdates
        #self.send_photo(bot_info, open('funny_image.jpg', 'rb'))
        #return

    # def lookForAlertables(self):
    #     pass
    #     bot_info = self.readBotInfo()

    #     method = 'getUpdates'
    #     #params = {'chat_id': bot_info['chat_id']}
    #     #files = {'photo': file_opened}
    #     api_url = f"https://api.telegram.org/bot{bot_info['token']}/"
    #     resp = requests.post(api_url + method)
    #     json_dict = json.loads(resp.text)
    #     print(json_dict["result"])
    #     print("Do we get anything good?")
    #     print(resp.text)
    #     # url = f"https://api.telegram.org/bot{bot_info['token']}/getUpdates"
    #     # anything = requests.get(url)
    #     # print(anything.text)
    #     #https://api.telegram.org/botyour_telegram_key/getUpdates
    #     #self.send_photo(bot_info, open('funny_image.jpg', 'rb'))
    #     return


    #     if self.previousDataFrame is not None:
    #         previous_numeric = self.previousDataFrame.select_dtypes(include=[np.float])
    #         current_numeric = self.stock_df.select_dtypes(include=[np.float])
    #         time_between_calc = self.stock_df[Constants.CALCULATED_AT].astype('datetime64[ns]') - self.previousDataFrame[Constants.CALCULATED_AT].astype('datetime64[ns]')
    #         # print("Classic")
    #         # print(pd.to_datetime(datetime.now(timezone(Constants.NYC_TIMEZONE))))
    #         # print("Pandas with EST")
    #         # print(pd.Timestamp.now(timezone(Constants.NYC_TIMEZONE)))
    #         # print(type(pd.Timestamp.now(Constants.NYC_TIMEZONE)))
    #         # print("Pandas without EST")
    #         # print(pd.Timestamp.now())
    #         # print(type(pd.Timestamp.now()))
    #         # print("And this is what's in the array")
    #         # print(self.stock_df['LAST_FIVE_AT'].iloc[0])
    #         # print(type(self.stock_df['LAST_FIVE_AT'].iloc[0]))
    #         # forced_type = self.stock_df['LAST_FIVE_AT'].astype('datetime64[ns]')
    #         # print("And this is what's in the forced array")
    #         # print(forced_type.iloc[0])
    #         # print(type(forced_type.iloc[0]))
            
    #         time_to_bars = self.stock_df[Constants.LAST_FIVE_AT].astype('datetime64[ns]') - self.previousDataFrame[Constants.LAST_FIVE_AT].astype('datetime64[ns]')
            
    #         #time_to_bars = self.stock_df['LAST_FIVE_AT'].astype('datetime64[ns]') - pd.to_datetime(datetime.now(timezone(Constants.NYC_TIMEZONE)))
    #         seconds_diff_calc = time_between_calc.apply(lambda x: x.total_seconds())
    #         seconds_to_bars = time_to_bars.apply(lambda x: x.total_seconds())
    #         difference_frame = current_numeric - previous_numeric
    #         self.checkForMomentumShifts(bot_info, difference_frame, seconds_diff_calc, seconds_to_bars)
                

    # def checkForMomentumShifts(self, bot_info, difference_frame, seconds_diff_calc, seconds_to_bars):

    #     for time_frame in self.bar_minutes:
    #         rsi_column = time_frame + '_RSI'
    #         row_selection = (seconds_to_bars < 360) & (seconds_diff_calc < 15) & (abs(difference_frame[rsi_column]) > 4) & ((self.stock_df[rsi_column] > 65) | (self.stock_df[rsi_column] < 35))
    #         up_movers = self.stock_df.index.values[(difference_frame[rsi_column] > 4) & row_selection]
            
    #         # print("BUT THIS SHOULD BE A LOT OF FALSE??!!?")
    #         # print(seconds_to_bars)
    #         # print(seconds_diff_calc)
    #         # print((seconds_to_bars < 360))
    #         # print((seconds_diff_calc < 15))
    #         moving_uids = self.stock_df.index.values[row_selection]
    #         # print(moving_uids)

    #         for key in moving_uids:
    #             # print("Is it always in there?")
    #             # print(key)
    #             # print(up_movers)
    #             direction = "UP" if key in up_movers else "DOWN"
    #             message = f"<b>{self.stock_list[key][Constants.SYMBOL]}</b> (<b>{self.stock_df.loc[key,'PRICE']:.2f}</b>): {time_frame} RSI is {direction} to <b>{self.stock_df.loc[key,rsi_column]:.1f}</b>"
    #             url = f"https://api.telegram.org/bot{bot_info['token']}/sendMessage?chat_id={bot_info['chat_id']}&parse_mode=HTML&text={message}"
    #             requests.get(url).json()


    def sendPhoto(self, file_name):
        method = 'sendPhoto'
        params = {'chat_id': self.bot_info['chat_id']}
        files = {'photo': file_name}
        api_url = f"https://api.telegram.org/bot{self.bot_info['token']}/"
        resp = requests.post(api_url + method, params, files=files)
        return resp


    def readBotInfo(self):
        file_name = './data/bot_info.json'
        try:
            with open(file_name) as json_file:
                json_dict = json.load(json_file)
                return json_dict
        except (IOError, OSError) as e:
            return dict()
    
    