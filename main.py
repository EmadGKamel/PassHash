import hashlib
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_ui()
        self.handle_buttons()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(543, 217)
        self.center()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calc_btn = QPushButton(self.centralwidget)
        self.calc_btn.setGeometry(QRect(310, 20, 99, 27))
        self.calc_btn.setObjectName("calc_btn")
        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QRect(420, 20, 99, 27))
        self.clear_btn.setObjectName("clear_btn")
        self.text = QLineEdit(self.centralwidget)
        self.text.setGeometry(QRect(30, 20, 271, 27))
        self.text.setObjectName("text")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QRect(30, 80, 491, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.md5_sum = QLabel(self.horizontalLayoutWidget)
        self.md5_sum.setText("")
        self.md5_sum.setObjectName("md5_sum")
        self.horizontalLayout.addWidget(self.md5_sum)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 130, 491, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sha_sum = QLabel(self.horizontalLayoutWidget_2)
        self.sha_sum.setText("")
        self.sha_sum.setObjectName("sha_sum")
        self.horizontalLayout_2.addWidget(self.sha_sum)
        self.horizontalLayout_2.setStretch(1, 1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(97, 190, 341, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.calc_btn.setText(_translate("MainWindow", "Calculate"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "MD5 Sum :    "))
        self.label_2.setText(_translate("MainWindow", "SHA-1 Sum : "))
        self.label_3.setText(_translate("MainWindow", "Done By Emad G.Kamel      github.com/EmadGKamel"))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_hashing(self):
        raw = self.text.text()
        self.md5_sum.setText(hashlib.md5(raw.encode()).hexdigest())
        self.sha_sum.setText(hashlib.sha1(raw.encode()).hexdigest())

    def handle_clear(self):
        self.text.clear()
        self.md5_sum.clear()
        self.sha_sum.clear()

    def handle_buttons(self):
        self.calc_btn.clicked.connect(self.handle_hashing)
        self.clear_btn.clicked.connect(self.handle_clear)

    def init_ui(self):
        self.setWindowTitle('PassHash')
        self.setWindowIcon(QIcon('Softies-icons-lock_256px.png'))
        self.calc_btn.setDefault(1)
        self.text.setPlaceholderText('Enter Text Here!')
        self.md5_sum.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.sha_sum.setTextInteractionFlags(Qt.TextSelectableByMouse)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()