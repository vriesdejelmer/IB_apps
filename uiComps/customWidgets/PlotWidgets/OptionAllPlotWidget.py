from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMenu, QAction

import pyqtgraph as pg

import numpy as np
import time

pg.setConfigOption("background", "w")
pg.setConfigOptions(antialias=False)

from matplotlib.pyplot import cm

class OptionAllPlotWidget(pg.PlotWidget):    

    option_frame = None
    curve_data = None

    moving_line = False
    price_line = None

    current_selection = None

    min_key = None
    max_key = None

    def __init__(self, delegate, plot_type, bottom_label, legend_alignment='right', difference_plot=False):
        super().__init__()

        self.delegate = delegate
        self.plot_type = plot_type
        self.difference_plot = difference_plot
        self.legend_alignment = legend_alignment
        self.setupGraphs(bottom_label)
        self.addLegend()

        
    def generateColorList(self, count):
        colors = cm.rainbow(np.linspace(0, 1, count))
        rgba_tuples =[c for c in colors]
        rgb_colors = [[x[0]*255, x[1]*255, x[2]*255] for x in rgba_tuples]
        return rgb_colors


    def setupGraphs(self, bottom_label, inverted=False):

        self.addCrossHair()
        self.proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
            
        # self.setMouseEnabled(y=False) 
        self.setLabels(left='Option Price', bottom=bottom_label)


    def setupCurves(self):

        self.plotItem.legend.setColumnCount(7)
        self.plotItem.legend.setOffset((30,5))
        if self.legend_alignment == 'right':
            self.plotItem.legend.setOffset((0, 1))
        elif self.legend_alignment == 'left':
            self.plotItem.legend.setOffset((1, 1))

        print("I'm guessing we will be kept waiting?")
        self.curve_data = self.option_frame.getLinesFor(self.plot_type)
        print("duurt lang")
            
        if self.curve_data is not None:
            # print("Any hope?")
            # print(len(self.curve_data))
            
            self.curve_data = self.filterCurves(self.curve_data)

            self.curve_hooks = dict()

            if -1 in self.curve_data:
                color_list = [(200,200,200)] + self.generateColorList(len(self.curve_data)-1)
            else:
                color_list = self.generateColorList(len(self.curve_data))
            #print(len(self.curve_data))

            for index, (data_name, data_line) in enumerate(self.curve_data.items()):

                #print(f"For curve #{index} ({data_name}) we get {data_line['x']} and {data_line['y']}")
                
                pen = pg.mkPen(color=color_list[index],width=2)
                if len(data_line['x']) > 0:    
                    try:
                        has_plots = True
                        start_plot = time.time()
                        curve_mid = self.plot(data_line['x'], data_line['y'], pen=pen, symbol='o', symbolPen=pen, name=data_line['display_name'])
                        curve_mid.setSymbolSize(1)
                        self.curve_hooks[data_name] = pg.CurvePoint(curve_mid)
                        self.addItem(self.curve_hooks[data_name])
                    except TypeError as e:
                        print(f"If only we got here once...: {e}")    

            self.arrow_mid = pg.ArrowItem(angle=240,pen=(255,255,0),brush=(255,0,0))
            self.text_mid = pg.TextItem('',color=(80,80,80),fill=pg.mkBrush('w'),anchor=(0.5,2.0))

            if self.plot_type == 'price_est':
                self.updateBackground()





    def updateBackground(self, y=0.0):

        # Create a LinearRegionItem
        top_region = pg.LinearRegionItem(brush=(200, 255, 200), orientation='horizontal', movable=False)  # Blue color region
        bottom_region = pg.LinearRegionItem(brush=(255, 200, 200), orientation='horizontal', movable=False)  # Blue color region
        top_region.setZValue(-10)  # Ensure the region is drawn below the data curve
        bottom_region.setZValue(-10)  # Ensure the region is drawn below the data curve

        # Add the LinearRegionItem to the plot
        self.addItem(top_region)
        self.addItem(bottom_region)

        # Set the limits of the linear region
        top_region.setRegion([0, 100])
        bottom_region.setRegion([-100, 0])

        

    
    def filterCurves(self, curve_data):
        
        keys_out_of_range = []
        for key in curve_data.keys():
            if (self.max_key is not None) and (key > self.max_key):
                keys_out_of_range.append(key)
            if (self.min_key is not None) and (key < self.min_key):
                keys_out_of_range.append(key)
        
        for key in keys_out_of_range:
            del curve_data[key]

        return curve_data


    # def drawBackground(self, painter: QPainter, rect: QRectF):

    #     if self.plot_type == 'price_est':
    #         print(f"What is this rect? {rect}")

    #         # Set the default background color
    #         painter.fillRect(rect, Qt.white)

    #         # Iterate through items in the scene and color the background based on y-value
    #         for item in self.scene().items():
    #             print(item)

    #             if hasattr(item, 'y_value'):
    #                 print(item.y_value)
    #                 if item.y_value > 0:
    #                     background_color = QColor(200, 255, 200)  # Light green for positive values
    #                 else:
    #                     background_color = QColor(255, 200, 200)  # Light red for negative values

    #                 # Calculate the item's rectangle in view coordinates
    #                 item_rect = self.mapFromScene(item.sceneBoundingRect())

    #                 # Fill the background with the appropriate color
    #                 painter.fillRect(item_rect, QBrush(background_color))
    #     else:
    #         super().drawBackground(painter, rect)


    def setPriceLine(self, price):
        # if self.price_line is None:
        self.price_line = pg.InfiniteLine(pos=price, angle=90, pen=pg.mkPen(color=(160,160,160), width=2, style=Qt.DashLine),movable=True)
        self.price_line.sigPositionChanged.connect(self.lineMoved)
        self.price_line.sigPositionChangeFinished.connect(self.enableMouseMovedSignal)

        self.addItem(self.price_line)
       # else:
       #     self.price_line.setPos(price)

    # Define a function to temporarily disconnect the sigMouseMoved signal
    def disableMouseMovedSignal(self):
        self.proxy.disconnect()
        

    # Define a function to reconnect the sigMouseMoved signal
    def enableMouseMovedSignal(self):
        self.moving_line = False
        self.proxy = pg.SignalProxy(self.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        

    def lineMoved(self):
        if not self.moving_line:
            self.disableMouseMovedSignal()
            self.moving_line = True


    def addCrossHair(self):
        self.vLine = pg.InfiniteLine(pos=0.0, angle=90, pen=pg.mkPen(color=(170,170,170), width=2, style=Qt.DashLine), movable=False)
        self.hLine = pg.InfiniteLine(pos=0.0, angle=0, pen=pg.mkPen(color=(170,170,170), width=2, style=Qt.DashLine), movable=False)
        self.addItem(self.vLine,ignoreBounds=True)
        self.addItem(self.hLine,ignoreBounds=True)
        

    def resetData(self, option_frame):
        self.clear()
        self.curve_data = dict()
        self.curve_hooks = dict()
        self.addCrossHair()
        self.setPriceLine(option_frame.getUnderlyingPrice())
        self.option_frame = option_frame
        if (option_frame is not None) and option_frame.has_data:
            self.setupCurves()
        

    def findNearestDataPoint(self, mouse_x, mouse_y):
        closest_distance = float('inf')  # start with a very high distance
        closest_key = None
        closest_index = None

        for key, line in self.curve_data.items():

            # Compute the Euclidean distances for all points in the current line
            distances = np.sqrt((line['x'] - mouse_x) ** 2 + (line['y'] - mouse_y) ** 2)
            
            # Find the minimum distance and its index for the current line
            min_distance = distances.min()
            index = distances.argmin()

            # Check if this distance is the smallest across all lines checked so far
            if min_distance < closest_distance:
                closest_distance = min_distance
                closest_key = key
                closest_index = index

        return closest_key, closest_index


    def contextMenuEvent(self, event):
        # Create a custom context menu
        context_menu = QMenu(self)

        # Add custom actions to the menu
        action_1 = QAction("Request Live Graph", self)
        action_2 = QAction("Show PL for Price", self)

        # Connect actions to functions you want to execute
        action_1.triggered.connect(self.requestLiveUpdates)
        action_2.triggered.connect(self.showPL)

        # Add actions to the menu
        context_menu.addAction(action_1)
        context_menu.addAction(action_2)

        # Show the context menu at the mouse cursor position
        context_menu.popup(event.globalPos())


    def requestLiveUpdates(self):
        if self.current_selection is not None:
            self.delegate.requestLiveUpdates(self.current_selection)


    def showPL(self):
        if self.current_selection is not None:
            self.delegate.requestPL(self.current_selection)
        
    
    def mouseMoved(self, evt):

        pos = evt[0]
        found_match = False
        
        if self.sceneBoundingRect().contains(pos) and (self.curve_data is not None):
            mousePoint = self.plotItem.vb.mapSceneToView(pos)
            x_mouse = mousePoint.x()
            y_mouse = mousePoint.y()
    
            min_key, min_index = self.findNearestDataPoint(x_mouse, y_mouse)
        

            if min_key is not None:
                self.arrow_mid.setParentItem(self.curve_hooks[min_key])
                self.text_mid.setParentItem(self.curve_hooks[min_key])

                y_mouse = self.curve_data[min_key]['y'][min_index]
                x_mouse = self.curve_data[min_key]['x'][min_index]

                y_details = self.curve_data[min_key]['y_detail'][min_index]

                min_point_count = len(self.curve_data[min_key]['x'])
                if min_point_count == 1:
                    self.curve_hooks[min_key].setPos(0)
                else:
                    self.curve_hooks[min_key].setPos(min_index/(min_point_count-1))

                self.arrow_mid.show()
                self.text_mid.show()

                if self.plot_type == 'expiration_grouped':
                    self.text_mid.setText(f"{min_key} dte: ${x_mouse}, {y_mouse:.2f}, ({y_details})")
                elif self.plot_type == 'strike_grouped':
                    self.text_mid.setText(f"${min_key}: {x_mouse}dte, {y_mouse:.2f}, ({y_details})")
                elif self.plot_type == 'price_est':
                    if min_key >= 0:
                        self.text_mid.setText(f"{min_key} dte: ${x_mouse:.2f}, {y_mouse:.2f}, ({y_details})")
                    else:
                        self.text_mid.setText(f"At expiration: ${x_mouse:.2f}, {y_mouse:.2f}, ({y_details})")


                self.current_selection = {'plot_type': self.plot_type, 'key': min_key, 'x_value': x_mouse, 'y_value': y_mouse, 'y_details': y_details}
                found_match = True

            self.hLine.setPos(y_mouse)
            self.vLine.setPos(x_mouse)

        
        # if not found_match:
            
        #     self.arrow_mid.hide()
        #     self.high_low_band.hide()
        #     self.text_mid.hide()
        
                # self.arrow_mid.setParentItem(self.curvePoints[min_key])
                # self.text_mid.setParentItem(self.curvePoints[min_key])
                # if min_point_count == 1:
                #     self.curvePoints[min_key].setPos(0)
                # else:
                #     self.curvePoints[min_key].setPos(min_index/(min_point_count-1))

                # self.arrow_mid.show()
                # self.high_low_band.show()
                # self.text_mid.show()
                # self.text_mid.setText(f"{min_symbol}: {min_original_line[min_index]:.2f}")

                # self.curve_low.setData(index_data, low_data)
                # self.curve_high.setData(index_data, high_data)
                # found_match = True

    # def updatePlot(self, strike_comp_frame):
    #     pass
        # self.data_frame = strike_comp_frame
        
        # if self.data_frame.has_data:
        #     pen = pg.mkPen(color=(80,80,80),width=5)
        #     self.curve_mid.setData(self.data_frame.data_x, self.data_frame.data_y, pen=pen, clickable=True)

        #     if len(self.data_frame.data_y_lower) > 0 and len(self.data_frame.data_y_upper) > 0:
        #         self.curve_ask.setData(self.data_frame.data_x, self.data_frame.data_y_lower)
        #         self.curve_bid.setData(self.data_frame.data_x, self.data_frame.data_y_upper)

        #     self.setYRange(0, self.data_frame.data_y.max()*self.range_multiplier)


    def setMinimumKey(self, min_key):
        self.min_key = min_key
        self.resetData(self.option_frame)


    def setMaximumKey(self, max_key):
        self.max_key = max_key
        self.resetData(self.option_frame)