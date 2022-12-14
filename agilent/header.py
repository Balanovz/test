from PySide6.QtWidgets import QPushButton,QHBoxLayout, QWidget

class Header(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QHBoxLayout()

        self.multimetr_button = QPushButton("multimetr")
        self.toggle_button = QPushButton("turn on")

        self.layout.addWidget(self.multimetr_button)
        self.layout.addWidget(self.toggle_button)

        self.setLayout(self.layout)