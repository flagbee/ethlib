import sys
from ethlib import get_devlist
from PyQt5.QtWidgets import QWidget, QGridLayout, QComboBox, QApplication

class EthDevlistComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.insertItems(0, [str(dev) for dev in get_devlist()])

class TestMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        devlist = EthDevlistComboBox()
        layout = QGridLayout()
        layout.addWidget(devlist)
        self.setWindowTitle('TestMainWindow')
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TestMainWidget()
    ex.show()
    sys.exit(app.exec_())
