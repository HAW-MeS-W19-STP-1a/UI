# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './resources/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 908)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_main = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_main.setOrientation(QtCore.Qt.Vertical)
        self.splitter_main.setOpaqueResize(False)
        self.splitter_main.setHandleWidth(30)
        self.splitter_main.setObjectName("splitter_main")
        self.verticalWidget_Graph = QtWidgets.QWidget(self.splitter_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget_Graph.sizePolicy().hasHeightForWidth())
        self.verticalWidget_Graph.setSizePolicy(sizePolicy)
        self.verticalWidget_Graph.setObjectName("verticalWidget_Graph")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_Graph)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalFrame_dateTimeLabel = QtWidgets.QFrame(self.verticalWidget_Graph)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_dateTimeLabel.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_dateTimeLabel.setSizePolicy(sizePolicy)
        self.horizontalFrame_dateTimeLabel.setObjectName("horizontalFrame_dateTimeLabel")
        self.layout_start_end_label = QtWidgets.QHBoxLayout(self.horizontalFrame_dateTimeLabel)
        self.layout_start_end_label.setObjectName("layout_start_end_label")
        self.verticalWidget_start = QtWidgets.QWidget(self.horizontalFrame_dateTimeLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_start.sizePolicy().hasHeightForWidth())
        self.verticalWidget_start.setSizePolicy(sizePolicy)
        self.verticalWidget_start.setObjectName("verticalWidget_start")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget_start)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_start = QtWidgets.QLabel(self.verticalWidget_start)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_start.sizePolicy().hasHeightForWidth())
        self.label_start.setSizePolicy(sizePolicy)
        self.label_start.setMinimumSize(QtCore.QSize(115, 0))
        self.label_start.setAlignment(QtCore.Qt.AlignCenter)
        self.label_start.setObjectName("label_start")
        self.verticalLayout_5.addWidget(self.label_start)
        self.dateTimeEdit_start = QtWidgets.QDateTimeEdit(self.verticalWidget_start)
        self.dateTimeEdit_start.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_start.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_start.setSizePolicy(sizePolicy)
        self.dateTimeEdit_start.setMinimumSize(QtCore.QSize(200, 0))
        self.dateTimeEdit_start.setReadOnly(False)
        self.dateTimeEdit_start.setDate(QtCore.QDate(2019, 1, 1))
        self.dateTimeEdit_start.setObjectName("dateTimeEdit_start")
        self.verticalLayout_5.addWidget(self.dateTimeEdit_start)
        self.layout_start_end_label.addWidget(self.verticalWidget_start)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_start_end_label.addItem(spacerItem)
        self.verticalWidget_Data1 = QtWidgets.QWidget(self.horizontalFrame_dateTimeLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_Data1.sizePolicy().hasHeightForWidth())
        self.verticalWidget_Data1.setSizePolicy(sizePolicy)
        self.verticalWidget_Data1.setObjectName("verticalWidget_Data1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_Data1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_Data1 = QtWidgets.QLabel(self.verticalWidget_Data1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Data1.sizePolicy().hasHeightForWidth())
        self.label_Data1.setSizePolicy(sizePolicy)
        self.label_Data1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Data1.setObjectName("label_Data1")
        self.verticalLayout_6.addWidget(self.label_Data1)
        self.comboBox_Data1 = QtWidgets.QComboBox(self.verticalWidget_Data1)
        self.comboBox_Data1.setObjectName("comboBox_Data1")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.comboBox_Data1.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_Data1)
        self.layout_start_end_label.addWidget(self.verticalWidget_Data1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_start_end_label.addItem(spacerItem1)
        self.pushButton_update = QtWidgets.QPushButton(self.horizontalFrame_dateTimeLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        self.pushButton_update.setObjectName("pushButton_update")
        self.layout_start_end_label.addWidget(self.pushButton_update)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_start_end_label.addItem(spacerItem2)
        self.verticalWidget_Data2 = QtWidgets.QWidget(self.horizontalFrame_dateTimeLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_Data2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_Data2.setSizePolicy(sizePolicy)
        self.verticalWidget_Data2.setObjectName("verticalWidget_Data2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalWidget_Data2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_Data2 = QtWidgets.QLabel(self.verticalWidget_Data2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Data2.sizePolicy().hasHeightForWidth())
        self.label_Data2.setSizePolicy(sizePolicy)
        self.label_Data2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Data2.setObjectName("label_Data2")
        self.verticalLayout_7.addWidget(self.label_Data2)
        self.comboBox_Data2 = QtWidgets.QComboBox(self.verticalWidget_Data2)
        self.comboBox_Data2.setObjectName("comboBox_Data2")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.comboBox_Data2.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_Data2)
        self.layout_start_end_label.addWidget(self.verticalWidget_Data2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_start_end_label.addItem(spacerItem3)
        self.verticalWidget_stop = QtWidgets.QWidget(self.horizontalFrame_dateTimeLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_stop.sizePolicy().hasHeightForWidth())
        self.verticalWidget_stop.setSizePolicy(sizePolicy)
        self.verticalWidget_stop.setObjectName("verticalWidget_stop")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalWidget_stop)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_stop = QtWidgets.QLabel(self.verticalWidget_stop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_stop.sizePolicy().hasHeightForWidth())
        self.label_stop.setSizePolicy(sizePolicy)
        self.label_stop.setMinimumSize(QtCore.QSize(115, 0))
        self.label_stop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stop.setObjectName("label_stop")
        self.verticalLayout_8.addWidget(self.label_stop)
        self.dateTimeEdit_stop = QtWidgets.QDateTimeEdit(self.verticalWidget_stop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateTimeEdit_stop.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit_stop.setSizePolicy(sizePolicy)
        self.dateTimeEdit_stop.setMinimumSize(QtCore.QSize(200, 0))
        self.dateTimeEdit_stop.setDate(QtCore.QDate(2019, 1, 1))
        self.dateTimeEdit_stop.setObjectName("dateTimeEdit_stop")
        self.verticalLayout_8.addWidget(self.dateTimeEdit_stop)
        self.layout_start_end_label.addWidget(self.verticalWidget_stop)
        self.verticalLayout_2.addWidget(self.horizontalFrame_dateTimeLabel)
        self.graphicsLabel = QtWidgets.QLabel(self.verticalWidget_Graph)
        self.graphicsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphicsLabel.setObjectName("graphicsLabel")
        self.verticalLayout_2.addWidget(self.graphicsLabel)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalWidget_Graph)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_graph = QtWidgets.QWidget()
        self.tab_graph.setObjectName("tab_graph")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_graph)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = PlotWidget(self.tab_graph)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_graph, "")
        self.tab_overview = QtWidgets.QWidget()
        self.tab_overview.setObjectName("tab_overview")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_overview)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = TableWidget(self.tab_overview)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_overview, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalWidget_Console = QtWidgets.QWidget(self.splitter_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_Console.sizePolicy().hasHeightForWidth())
        self.verticalWidget_Console.setSizePolicy(sizePolicy)
        self.verticalWidget_Console.setObjectName("verticalWidget_Console")
        self.layout_Console = QtWidgets.QVBoxLayout(self.verticalWidget_Console)
        self.layout_Console.setContentsMargins(0, 0, 0, 0)
        self.layout_Console.setObjectName("layout_Console")
        self.textBrowser_Console = QtWidgets.QTextBrowser(self.verticalWidget_Console)
        self.textBrowser_Console.setObjectName("textBrowser_Console")
        self.layout_Console.addWidget(self.textBrowser_Console)
        self.layout_send_command = QtWidgets.QHBoxLayout()
        self.layout_send_command.setObjectName("layout_send_command")
        self.line_send_command = QtWidgets.QLineEdit(self.verticalWidget_Console)
        self.line_send_command.setText("")
        self.line_send_command.setObjectName("line_send_command")
        self.layout_send_command.addWidget(self.line_send_command)
        self.pushButton_clear_window = QtWidgets.QPushButton(self.verticalWidget_Console)
        self.pushButton_clear_window.setObjectName("pushButton_clear_window")
        self.layout_send_command.addWidget(self.pushButton_clear_window)
        self.layout_Console.addLayout(self.layout_send_command)
        self.gridLayout.addWidget(self.splitter_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menucontrol = QtWidgets.QMenu(self.menubar)
        self.menucontrol.setObjectName("menucontrol")
        self.menuSet_Time = QtWidgets.QMenu(self.menucontrol)
        self.menuSet_Time.setObjectName("menuSet_Time")
        self.menuSet_Position = QtWidgets.QMenu(self.menucontrol)
        self.menuSet_Position.setObjectName("menuSet_Position")
        self.menuSet_Update_Intervall = QtWidgets.QMenu(self.menucontrol)
        self.menuSet_Update_Intervall.setObjectName("menuSet_Update_Intervall")
        self.menuSet_Messearing_Intervall = QtWidgets.QMenu(self.menucontrol)
        self.menuSet_Messearing_Intervall.setObjectName("menuSet_Messearing_Intervall")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action_set_time_utc = QtWidgets.QAction(MainWindow)
        self.action_set_time_utc.setObjectName("action_set_time_utc")
        self.action_set_time_custom = QtWidgets.QAction(MainWindow)
        self.action_set_time_custom.setObjectName("action_set_time_custom")
        self.action_set_localtion_hamburg = QtWidgets.QAction(MainWindow)
        self.action_set_localtion_hamburg.setObjectName("action_set_localtion_hamburg")
        self.action_set_location_custom = QtWidgets.QAction(MainWindow)
        self.action_set_location_custom.setObjectName("action_set_location_custom")
        self.action_adjust_orientation = QtWidgets.QAction(MainWindow)
        self.action_adjust_orientation.setObjectName("action_adjust_orientation")
        self.action_set_update_interval_5_sec = QtWidgets.QAction(MainWindow)
        self.action_set_update_interval_5_sec.setCheckable(True)
        self.action_set_update_interval_5_sec.setObjectName("action_set_update_interval_5_sec")
        self.action_set_update_interval_1_min = QtWidgets.QAction(MainWindow)
        self.action_set_update_interval_1_min.setCheckable(True)
        self.action_set_update_interval_1_min.setObjectName("action_set_update_interval_1_min")
        self.action_set_update_interval_15_min = QtWidgets.QAction(MainWindow)
        self.action_set_update_interval_15_min.setCheckable(True)
        self.action_set_update_interval_15_min.setObjectName("action_set_update_interval_15_min")
        self.action_set_update_interval_1_h = QtWidgets.QAction(MainWindow)
        self.action_set_update_interval_1_h.setCheckable(True)
        self.action_set_update_interval_1_h.setObjectName("action_set_update_interval_1_h")
        self.action_set_meas_interval_1_sec = QtWidgets.QAction(MainWindow)
        self.action_set_meas_interval_1_sec.setCheckable(True)
        self.action_set_meas_interval_1_sec.setObjectName("action_set_meas_interval_1_sec")
        self.action_set_meas_interval_5_sec = QtWidgets.QAction(MainWindow)
        self.action_set_meas_interval_5_sec.setCheckable(True)
        self.action_set_meas_interval_5_sec.setObjectName("action_set_meas_interval_5_sec")
        self.action_set_meas_interval_15_sec = QtWidgets.QAction(MainWindow)
        self.action_set_meas_interval_15_sec.setCheckable(True)
        self.action_set_meas_interval_15_sec.setObjectName("action_set_meas_interval_15_sec")
        self.action_set_meas_interval_1_min = QtWidgets.QAction(MainWindow)
        self.action_set_meas_interval_1_min.setCheckable(True)
        self.action_set_meas_interval_1_min.setObjectName("action_set_meas_interval_1_min")
        self.action_set_view_1_minute = QtWidgets.QAction(MainWindow)
        self.action_set_view_1_minute.setCheckable(True)
        self.action_set_view_1_minute.setObjectName("action_set_view_1_minute")
        self.action_set_view_15_minute = QtWidgets.QAction(MainWindow)
        self.action_set_view_15_minute.setCheckable(True)
        self.action_set_view_15_minute.setObjectName("action_set_view_15_minute")
        self.action_set_view_1_h = QtWidgets.QAction(MainWindow)
        self.action_set_view_1_h.setCheckable(True)
        self.action_set_view_1_h.setObjectName("action_set_view_1_h")
        self.action_set_view_1_d = QtWidgets.QAction(MainWindow)
        self.action_set_view_1_d.setCheckable(True)
        self.action_set_view_1_d.setObjectName("action_set_view_1_d")
        self.action_set_view_1_w = QtWidgets.QAction(MainWindow)
        self.action_set_view_1_w.setCheckable(True)
        self.action_set_view_1_w.setObjectName("action_set_view_1_w")
        self.action_set_view_1_m = QtWidgets.QAction(MainWindow)
        self.action_set_view_1_m.setCheckable(True)
        self.action_set_view_1_m.setObjectName("action_set_view_1_m")
        self.action_set_view_custom = QtWidgets.QAction(MainWindow)
        self.action_set_view_custom.setCheckable(True)
        self.action_set_view_custom.setObjectName("action_set_view_custom")
        self.action_enable_debug = QtWidgets.QAction(MainWindow)
        self.action_enable_debug.setCheckable(True)
        self.action_enable_debug.setObjectName("action_enable_debug")
        self.action_disable_debug = QtWidgets.QAction(MainWindow)
        self.action_disable_debug.setCheckable(True)
        self.action_disable_debug.setObjectName("action_disable_debug")
        self.action_set_update_interval_manuel = QtWidgets.QAction(MainWindow)
        self.action_set_update_interval_manuel.setCheckable(True)
        self.action_set_update_interval_manuel.setObjectName("action_set_update_interval_manuel")
        self.action_enable_com = QtWidgets.QAction(MainWindow)
        self.action_enable_com.setCheckable(True)
        self.action_enable_com.setObjectName("action_enable_com")
        self.action_disable_com = QtWidgets.QAction(MainWindow)
        self.action_disable_com.setCheckable(True)
        self.action_disable_com.setObjectName("action_disable_com")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuSet_Time.addAction(self.action_set_time_utc)
        self.menuSet_Time.addAction(self.action_set_time_custom)
        self.menuSet_Position.addAction(self.action_set_localtion_hamburg)
        self.menuSet_Position.addAction(self.action_set_location_custom)
        self.menuSet_Update_Intervall.addAction(self.action_set_update_interval_5_sec)
        self.menuSet_Update_Intervall.addAction(self.action_set_update_interval_1_min)
        self.menuSet_Update_Intervall.addAction(self.action_set_update_interval_15_min)
        self.menuSet_Update_Intervall.addAction(self.action_set_update_interval_1_h)
        self.menuSet_Update_Intervall.addAction(self.action_set_update_interval_manuel)
        self.menuSet_Messearing_Intervall.addAction(self.action_set_meas_interval_1_sec)
        self.menuSet_Messearing_Intervall.addAction(self.action_set_meas_interval_5_sec)
        self.menuSet_Messearing_Intervall.addAction(self.action_set_meas_interval_15_sec)
        self.menuSet_Messearing_Intervall.addAction(self.action_set_meas_interval_1_min)
        self.menucontrol.addAction(self.menuSet_Time.menuAction())
        self.menucontrol.addAction(self.menuSet_Position.menuAction())
        self.menucontrol.addAction(self.action_adjust_orientation)
        self.menucontrol.addAction(self.menuSet_Update_Intervall.menuAction())
        self.menucontrol.addAction(self.menuSet_Messearing_Intervall.menuAction())
        self.menuView.addAction(self.action_set_view_1_minute)
        self.menuView.addAction(self.action_set_view_15_minute)
        self.menuView.addAction(self.action_set_view_1_h)
        self.menuView.addAction(self.action_set_view_1_d)
        self.menuView.addAction(self.action_set_view_1_w)
        self.menuView.addAction(self.action_set_view_1_m)
        self.menuView.addAction(self.action_set_view_custom)
        self.menuMode.addAction(self.action_enable_debug)
        self.menuMode.addAction(self.action_disable_debug)
        self.menuMode.addAction(self.action_enable_com)
        self.menuMode.addAction(self.action_disable_com)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menucontrol.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_start.setText(_translate("MainWindow", "Start"))
        self.dateTimeEdit_start.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm:ss"))
        self.label_Data1.setText(_translate("MainWindow", "Data1"))
        self.comboBox_Data1.setItemText(0, _translate("MainWindow", "t_bme"))
        self.comboBox_Data1.setItemText(1, _translate("MainWindow", "t_cpu"))
        self.comboBox_Data1.setItemText(2, _translate("MainWindow", "t_qmc"))
        self.comboBox_Data1.setItemText(3, _translate("MainWindow", "t_mpu"))
        self.comboBox_Data1.setItemText(4, _translate("MainWindow", "w_dir"))
        self.comboBox_Data1.setItemText(5, _translate("MainWindow", "w_spd"))
        self.comboBox_Data1.setItemText(6, _translate("MainWindow", "pres"))
        self.comboBox_Data1.setItemText(7, _translate("MainWindow", "hum"))
        self.comboBox_Data1.setItemText(8, _translate("MainWindow", "zen"))
        self.comboBox_Data1.setItemText(9, _translate("MainWindow", "azm"))
        self.comboBox_Data1.setItemText(10, _translate("MainWindow", "lat"))
        self.comboBox_Data1.setItemText(11, _translate("MainWindow", "lon"))
        self.comboBox_Data1.setItemText(12, _translate("MainWindow", "alt"))
        self.comboBox_Data1.setItemText(13, _translate("MainWindow", "v_bat"))
        self.comboBox_Data1.setItemText(14, _translate("MainWindow", "i_bat"))
        self.comboBox_Data1.setItemText(15, _translate("MainWindow", "v_solar"))
        self.comboBox_Data1.setItemText(16, _translate("MainWindow", "i_solar"))
        self.comboBox_Data1.setItemText(17, _translate("MainWindow", "v_sys"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.label_Data2.setText(_translate("MainWindow", "Data2"))
        self.comboBox_Data2.setItemText(0, _translate("MainWindow", "t_bme"))
        self.comboBox_Data2.setItemText(1, _translate("MainWindow", "t_cpu"))
        self.comboBox_Data2.setItemText(2, _translate("MainWindow", "t_qmc"))
        self.comboBox_Data2.setItemText(3, _translate("MainWindow", "t_mpu"))
        self.comboBox_Data2.setItemText(4, _translate("MainWindow", "w_dir"))
        self.comboBox_Data2.setItemText(5, _translate("MainWindow", "w_spd"))
        self.comboBox_Data2.setItemText(6, _translate("MainWindow", "pres"))
        self.comboBox_Data2.setItemText(7, _translate("MainWindow", "hum"))
        self.comboBox_Data2.setItemText(8, _translate("MainWindow", "zen"))
        self.comboBox_Data2.setItemText(9, _translate("MainWindow", "azm"))
        self.comboBox_Data2.setItemText(10, _translate("MainWindow", "lat"))
        self.comboBox_Data2.setItemText(11, _translate("MainWindow", "lon"))
        self.comboBox_Data2.setItemText(12, _translate("MainWindow", "alt"))
        self.comboBox_Data2.setItemText(13, _translate("MainWindow", "v_bat"))
        self.comboBox_Data2.setItemText(14, _translate("MainWindow", "i_bat"))
        self.comboBox_Data2.setItemText(15, _translate("MainWindow", "v_solar"))
        self.comboBox_Data2.setItemText(16, _translate("MainWindow", "i_solar"))
        self.comboBox_Data2.setItemText(17, _translate("MainWindow", "v_sys"))
        self.label_stop.setText(_translate("MainWindow", "End"))
        self.dateTimeEdit_stop.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy HH:mm:ss"))
        self.graphicsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_graph), _translate("MainWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), _translate("MainWindow", "Overview"))
        self.pushButton_clear_window.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menucontrol.setTitle(_translate("MainWindow", "Control"))
        self.menuSet_Time.setTitle(_translate("MainWindow", "Set Time"))
        self.menuSet_Position.setTitle(_translate("MainWindow", "Set Position"))
        self.menuSet_Update_Intervall.setToolTip(_translate("MainWindow", "Set the Intervall in which to download the data from the Station."))
        self.menuSet_Update_Intervall.setTitle(_translate("MainWindow", "Set Update Interval"))
        self.menuSet_Messearing_Intervall.setToolTip(_translate("MainWindow", "Set the intervall in which the station should take measurements."))
        self.menuSet_Messearing_Intervall.setTitle(_translate("MainWindow", "Set Messearing Interval"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.action_set_time_utc.setText(_translate("MainWindow", "UTC"))
        self.action_set_time_custom.setText(_translate("MainWindow", "Custom"))
        self.action_set_localtion_hamburg.setText(_translate("MainWindow", "Hamburg"))
        self.action_set_location_custom.setText(_translate("MainWindow", "Custom"))
        self.action_adjust_orientation.setText(_translate("MainWindow", "Adjust Orientation"))
        self.action_set_update_interval_5_sec.setText(_translate("MainWindow", "5 sec"))
        self.action_set_update_interval_1_min.setText(_translate("MainWindow", "1 min"))
        self.action_set_update_interval_15_min.setText(_translate("MainWindow", "15 min"))
        self.action_set_update_interval_1_h.setText(_translate("MainWindow", "1 h"))
        self.action_set_meas_interval_1_sec.setText(_translate("MainWindow", "1 sec"))
        self.action_set_meas_interval_5_sec.setText(_translate("MainWindow", "5 sec"))
        self.action_set_meas_interval_15_sec.setText(_translate("MainWindow", "15 sec"))
        self.action_set_meas_interval_1_min.setText(_translate("MainWindow", "1 min"))
        self.action_set_view_1_minute.setText(_translate("MainWindow", "Last Minute"))
        self.action_set_view_15_minute.setText(_translate("MainWindow", "Last 15 Minutes"))
        self.action_set_view_1_h.setText(_translate("MainWindow", "Last Hour"))
        self.action_set_view_1_d.setText(_translate("MainWindow", "Last Day"))
        self.action_set_view_1_w.setText(_translate("MainWindow", "Last Week"))
        self.action_set_view_1_m.setText(_translate("MainWindow", "Last Month"))
        self.action_set_view_custom.setText(_translate("MainWindow", "Custom"))
        self.action_enable_debug.setText(_translate("MainWindow", "Enable Debug"))
        self.action_disable_debug.setText(_translate("MainWindow", "Disable Debug"))
        self.action_set_update_interval_manuel.setText(_translate("MainWindow", "Manuel"))
        self.action_enable_com.setText(_translate("MainWindow", "Enable Com"))
        self.action_disable_com.setText(_translate("MainWindow", "Disable Com"))
from pyqtgraph import PlotWidget, TableWidget
import mvc_app_rc
