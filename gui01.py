from PyQt5.QtWidgets import QApplication, QWidget
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("A First Window")
        self.resize(250, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.move(1920/2-250/2,1080/2-150/2)
    mywindow.show()
    sys.exit(app.exec_())
