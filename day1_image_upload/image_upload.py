from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("이미지 등록하기")
        Dialog.resize(588, 556)

        self.image_label = QtWidgets.QLabel('이미지를 선택하세요.', Dialog)
        self.image_label.setGeometry(QtCore.QRect(120, 40, 391, 361))
        self.image_label.setStyleSheet("border: 1px solid black; background-color: gray")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setObjectName("label")

        self.upload_button = QtWidgets.QPushButton('이미지 불러오기', Dialog)
        self.upload_button.setGeometry(QtCore.QRect(230, 440, 161, 51))

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.upload_button.clicked.connect(self.load_image)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "이미지 선택", "", "Images (*.png *.jpg *.jpeg)")

        if file_path:
            pixmap = QPixmap(file_path).scaled(300, 300, Qt.KeepAspectRatio)
            self.ui.image_label.setPixmap(pixmap)

# 실행하기
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

