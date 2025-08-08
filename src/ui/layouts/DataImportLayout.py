from PySide6.QtCore import Signal
import PySide6.QtWidgets as qw

from ui import controls


class DataImportLayout(qw.QWidget):
    row_created = Signal(int, str)

    def __init__(self):
        super().__init__()

        self.layout = qw.QVBoxLayout(self)

        self.rows = []

        self.add_file_button = qw.QPushButton("Add File...")
        self.add_file_button.clicked.connect(
            self._on_add_file_button_clicked)

        self.layout.addWidget(self.add_file_button)

    def _on_add_file_button_clicked(self, e):
        file_path, _ = qw.QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "/",
            "CSV Files (*.csv);;All Files (*)")
        row_id = len(self.rows)

        row = controls.DataImportLayoutRow(row_id, file_path)
        self.rows.append(row)
        self.layout.addWidget(row)

        self.row_created.emit(row_id, file_path)
