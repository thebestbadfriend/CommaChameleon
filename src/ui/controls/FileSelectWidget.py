from PySide6 import QtWidgets as qw


class FileSelectWidget(qw.QWidget):
    def __init__(self, button_text='Browse...', label_text='No File Selected'):
        super().__init__()

        self.selected_file = None

        self.button = qw.QPushButton(button_text)
        self.button.setSizePolicy(qw.QSizePolicy.Policy.Minimum, qw.QSizePolicy.Policy.Fixed)
        self.button.clicked.connect(self.button_clicked)

        self.label = qw.QLabel(label_text)

        self.layout = qw.QHBoxLayout()
        self.layout.addWidget(self.button, stretch=0)
        self.layout.addWidget(self.label, stretch=1)

        self.setLayout(self.layout)

    def button_clicked(self, e):
        file_path, _ = qw.QFileDialog.getOpenFileName(
            self,
            "Select CSV File",
            "/",
            "CSV Files (*.csv);;All Files (*)")

        self.selected_file = file_path
        self.label.setText(file_path)

        print(f"{self.selected_file} is selected")
