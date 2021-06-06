from PyQt5.QtWidgets import QApplication
from MainFrame import MainFrame
import sys

app = QApplication(sys.argv)
ex = MainFrame()
sys.exit(app.exec_())