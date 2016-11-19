from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("A First Window")
        self.mybutton = QPushButton(self)
        self.mybutton.setText("Ok!")

        self.mytext = QLineEdit(self)
        self.mytext.setText("Egg Tart")

        filepath = "logo.png"
        self.mypixmap = QPixmap(filepath)
        self.myimg = QLabel(self)
        self.myimg.setPixmap(self.mypixmap)

        pixrect = self.mypixmap.rect()
        self.setGeometry(10, 10, pixrect.width(), pixrect.height() + 50)
        self.mytext.move(20, pixrect.height() + 20)
        self.mybutton.move(150, pixrect.height() +15)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow1 = MyWindow()
    mywindow2 = MyWindow()
    mywindow2.move(20, 500)
    sys.exit(app.exec_())
