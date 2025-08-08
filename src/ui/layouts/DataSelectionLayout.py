from PySide6.QtCore import Signal
import PySide6.QtWidgets as qw

from ui import controls


class DataSelectionLayout(qw.QWidget):
    file_select_widget_selected_file_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.layout = qw.QVBoxLayout(self)

        self.file_select_widgets = []

        self.initial_file_select_widget = controls.FileSelectWidget()
        self.initial_file_select_widget.selected_file_changed.connect(
            self._on_file_select_widget_selected_file_changed)

        self.layout.addWidget(self.initial_file_select_widget)

    def _on_file_select_widget_selected_file_changed(self, selected_file):
        self.file_select_widget_selected_file_changed.emit(selected_file)