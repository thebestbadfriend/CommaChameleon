import pandas as pd
import PySide6.QtWidgets as qw

from ui.abstract_entities import PandasModel
from ui.layouts.DataSelectionLayout import DataSelectionLayout


class MainWindowLayout(qw.QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.data_selection_layout = DataSelectionLayout()
        self.data_selection_layout.file_select_widget_selected_file_changed.connect(
            self._on_file_select_widget_selected_file_changed)

        self.output_preview_widget = qw.QTableView()
        self.model = PandasModel(pd.DataFrame())
        self.output_preview_widget.setModel(self.model)

        self.addWidget(self.data_selection_layout)
        self.addWidget(self.output_preview_widget)

    def _on_file_select_widget_selected_file_changed(self, selected_file):
        self.model.add_csv(selected_file)
