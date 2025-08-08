import PySide6.QtWidgets as qw

from ui.layouts import MainWindowLayout


class MainWindow(qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_meta_ui()
        self.setup_layout()

    def setup_meta_ui(self):
        self.setWindowTitle("Comma Chameleon")
        self.setGeometry(200, 100, 1500, 800)

    def setup_layout(self):
        layout = MainWindowLayout()
        layout_wrapper = qw.QWidget()
        layout_wrapper.setLayout(layout)

        self.setCentralWidget(layout_wrapper)
