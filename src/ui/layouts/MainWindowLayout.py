import PySide6.QtWidgets as qw

from ui.layouts.DataImportLayout import DataImportLayout
from ui.layouts.OutputPreviewLayout import OutputPreviewLayout


class MainWindowLayout(qw.QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.tabs = qw.QTabWidget()

        # Data Selection Tab
        self.data_selection_tab = DataImportLayout()
        self.data_selection_tab.row_created.connect(
            self._on_data_import_layout_row_created)
        self.tabs.addTab(self.data_selection_tab, "Data Import")

        # Select & Filter Tab
        self.select_and_filter_tab = qw.QWidget()
        self.tabs.addTab(self.select_and_filter_tab, "Select && Filter")

        # Output Tab
        self.output_tab = qw.QWidget()
        self.tabs.addTab(self.output_tab, "Output")

        # Output Preview Pane
        self.output_preview_pane = OutputPreviewLayout()

        self.addWidget(self.tabs)
        self.addWidget(self.output_preview_pane)

    def _on_data_import_layout_row_created(self, file_id, selected_file):
        self.output_preview_pane.model.add_csv(file_id, selected_file)
