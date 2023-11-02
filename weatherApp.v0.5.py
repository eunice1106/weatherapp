import sys
import requests
from bs4 import beautifulsoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("UI/weatherAppUI.ui")[0]

class WeatherWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오늘의 날씨")
        self.setWindowIcon(QIcon('img/weather_icon.png'))
        self.statusBar().showMessage("Weather Application Ver0.5")

        self.weather_btn.clicked.connect(self.request_weather)

    def request_weather(self):
        area = self.input_areabox.text()  # 사용자가 입력한 지역이름을 가져오기
        weather_html = requests.get

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WeatherWin()
    win.show()
