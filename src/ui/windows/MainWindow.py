import PySide6.QtCore as qc
import PySide6.QtGui as qg
import PySide6.QtWidgets as qw

import ui.controls as controls


class MainWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_meta_ui()
        self.process_widgets()

    def setup_meta_ui(self):
        self.setWindowTitle("Comma Chameleon")
        self.setGeometry(200, 100, 1500, 800)

    def process_widgets(self):
        layout = qw.QGridLayout()
        layout_wrapper = qw.QWidget()
        layout_wrapper.setLayout(layout)

        file_select_widget = controls.FileSelectWidget()
        layout.addWidget(file_select_widget, 0, 0)

        self.setCentralWidget(layout_wrapper)
