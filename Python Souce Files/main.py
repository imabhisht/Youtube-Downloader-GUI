import sys
from bridge import Window
from PyQt5.QtWidgets import QApplication

app =  QApplication(sys.argv)

calculator = Window()


sys.exit(app.exec_())