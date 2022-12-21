import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('calc.ui', self)
        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)

    def add_num(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        self.output.setText("Ответ: " + str(num1 + num2))

    def sub_num(self):
        num1 = int(self.input1.text())
        num2 = int(self.input2.text())
        self.output.setText("Ответ: " + str(num1 - num2))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()