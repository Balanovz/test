from PySide6.QtWidgets import QMainWindow
from tablewidget import TableWidget



class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Test project"
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = TableWidget()
        self.setCentralWidget(self.table_widget)


        self.show()