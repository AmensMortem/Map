import sys
import requests

from templates.mainDesign import Ui_Form
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class App(QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.outButton.clicked.connect(self.getImage)

    def getImage(self, scale):
        coords = self.xInput.text() + ',' + self.yInput.text()
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}" \
                      f"&z={self.scaleInput.text()}&l=map"

        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.mapOut.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()  # получаем данные о нажитиях
        if key == Qt.Key_Plus:
            self.getImage(int(self.scaleInput.text()) + 1)
            print(123)
        elif key == Qt.Key_Minus:
            pass
        if key == Qt.Key_Up:  # если стрелка влево
            print(1223)
        elif key == Qt.Key_Down:  # если стрелка вправо
            pass
        elif key == Qt.Key_Left:  # если стрелка вправо
            pass
        elif key == Qt.Key_Right:  # если стрелка вправо
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
