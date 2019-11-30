from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    def clear_console_window(self):
        if self._model.debug_mode:
            print("Clear Window Button pressed.")
        # TODO: clear console window

    def set_debug_mode(self, value):
        print("Setting Debug Mode to " + str(value))
        self._model.debug_mode = value
    # @pyqtSlot(int)
    # def change_amount(self, value):
    #     self._model.amount = value

    #     # calculate even or odd
    #     self._model.even_odd = 'odd' if value % 2 else 'even'

    #     # calculate button enabled state
    #     self._model.enable_reset = True if value else False
