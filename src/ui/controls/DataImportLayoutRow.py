import PySide6.QtCore as qc
import PySide6.QtWidgets as qw


class DataImportLayoutRow(qw.QWidget):
    delete_button_clicked = qc.Signal(int)

    def __init__(self, row_id, file_path):
        super().__init__()
        self.row_id = row_id

        self.delete_button = qw.QPushButton("Remove File")
        self.delete_button.setSizePolicy(qw.QSizePolicy.Policy.Minimum, qw.QSizePolicy.Policy.Fixed)
        self.delete_button.clicked.connect(self._on_delete_button_clicked)

        self.file_path_label = qw.QLabel(file_path)

        self.layout = qw.QHBoxLayout()
        self.layout.addWidget(self.file_path_label, stretch=1)
        self.layout.addWidget(self.delete_button, stretch=0)

        self.setLayout(self.layout)

    def _on_delete_button_clicked(self):
        self.delete_button_clicked.emit(self.row_id)
