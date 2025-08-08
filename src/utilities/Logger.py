from datetime import datetime

class Logger():
    def __init__(self, name="Logger"):
        self.name = name

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {self.name}: {message}")
