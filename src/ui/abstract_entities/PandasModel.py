import pandas as pd
import PySide6.QtCore as qc

from utilities import Logger


class PandasModel(qc.QAbstractTableModel):
    logger = Logger("PandasModel")

    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self._df = df
        self._files = {}

    def rowCount(self, parent=None):
        return len(self._df)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    def data(self, index, role=qc.Qt.ItemDataRole.DisplayRole):
        if role == qc.Qt.ItemDataRole.DisplayRole:
            return str(self._df.iat[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=qc.Qt.ItemDataRole.DisplayRole):
        if role == qc.Qt.ItemDataRole.DisplayRole:
            if orientation == qc.Qt.Orientation.Horizontal:
                return str(self._df.columns[section])
            else:
                return str(self._df.index[section])

        return None

    def add_csv(self, file_id, file_path):
        self._files[file_id] = file_path
        self.logger.log(f"Added {file_path} to self._files as file_id {file_id}")

    def read_csv(self, file_id):
        file_path = self._files[file_id]
        valid_encodings = ('utf-8',
                           'windows-1252',
                           'ISO-8859-1',
                           'latin1',
                           'utf-16')

        df = pd.DataFrame()
        for encoding in valid_encodings:
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                self.logger.log(f"Successfully read {file_path} with encoding {encoding}")
                break
            except UnicodeDecodeError:
                continue

        return df

    def refresh_model(self):
        self.beginResetModel()

        frames = []
        for file_id in self._files.keys():
            frame = self.read_csv(file_id)
            frames.append(frame)

        self._df = frames[0]

        self.endResetModel()
