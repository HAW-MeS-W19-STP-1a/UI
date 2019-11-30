from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        # self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        # self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))
        self._ui.pushButton_clear_window.clicked.connect(
            self._main_controller.clear_console_window)
        self._ui.action_enable_debug.triggered.connect(
            lambda: self._main_controller.set_debug_mode(True))
        self._ui.action_disable_debug.triggered.connect(
            lambda: self._main_controller.set_debug_mode(False))

        # listen for model event signals
        # self._model.amount_changed.connect(self.on_amount_changed)
        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)
        self._model.debug_mode_changed.connect(self.on_debug_mode_changed)

        # set a default value
        # self._main_controller.change_amount(42)
        self._main_controller.set_debug_mode(True)
    # @pyqtSlot(int)
    # def on_amount_changed(self, value):
    #     self._ui.spinBox_amount.setValue(value)

    # @pyqtSlot(str)
    # def on_even_odd_changed(self, value):
    #     self._ui.label_even_odd.setText(value)

    # @pyqtSlot(bool)
    # def on_enable_reset_changed(self, value):
    #     self._ui.pushButton_reset.setEnabled(value)

    @pyqtSlot(bool)
    def on_debug_mode_changed(self, value):
        self._ui.action_enable_debug.setChecked(value)
        self._ui.action_disable_debug.setChecked(not value)
