import pandas as pd
import PySide6.QtWidgets as qw

from ui.abstract_entities import PandasModel


class OutputPreviewLayout(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = qw.QVBoxLayout(self)

        self.refresh_preview_button = qw.QPushButton("Refresh Preview")
        self.refresh_preview_button.clicked.connect(self.refresh_preview)

        self.output_preview_widget = qw.QTableView()
        self.model = PandasModel(pd.DataFrame())
        self.output_preview_widget.setModel(self.model)

        self.layout.addWidget(self.refresh_preview_button)
        self.layout.addWidget(self.output_preview_widget)

    def refresh_preview(self):
        self.model.refresh_model()
