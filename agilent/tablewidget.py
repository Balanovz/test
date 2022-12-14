from PySide6.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from header import Header
from monitoring import Monitoring

class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Initialize header
        self.header_widget = Header()

        # Initialize tab screen
        self.tabs = QTabWidget()

        self.monitoring_tab = Monitoring()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.monitoring_tab, "Monitoring")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.addTab(self.tab4, "Tab 4")
        
        # Add tabs and header to widget
        self.layout.addWidget(self.header_widget)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        