from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGroupBox, QLabel, QPushButton, QRadioButton,
    QHBoxLayout, QVBoxLayout, QButtonGroup, QComboBox, QLineEdit
)
import requests

app = QApplication([])
wind = QWidget()
wind.resize(500, 300)
wind.setWindowTitle('Конвертация')

def get_exchange_rate(target_cyrrency):
    url = f"https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    data = response.json()
    return data['rates'] [target_cyrrency]

def convert_currency():
    target_currency = need_currency_list.currentText()
    amount = float(select_value.text())
    exchange_rate = get_rate(target_currency)
    result = amount * exchange_rate
    result_label.setText(f"{result:.2f} {target_currency}")



total = QLabel('0.00')
convert = QPushButton('Конвертировать')

cyrrency1 = QComboBox()
cyrrency2 = QComboBox()

summa = QLineEdit('Введите сумму')

layout_total = QVBoxLayout()
layout_convert = QVBoxLayout()
layout_cyrrency1 = QHBoxLayout()
layout_cyrrency2 = QHBoxLayout()
layout_summa = QVBoxLayout()

layout_total.addWidget(total, alignment = Qt.AlignCenter)
layout_convert.addWidget(convert, alignment = Qt.AlignCenter)
layout_cyrrency1.addWidget(cyrrency1, alignment = Qt.AlignCenter)
layout_cyrrency2.addWidget(cyrrency2, alignment = Qt.AlignCenter)
layout_summa.addWidget(summa, alignment = Qt.AlignCenter)

wind.setLayout(layout_total)
wind.setLayout(layout_convert)
wind.setLayout(layout_cyrrency1)
wind.setLayout(layout_cyrrency2)
wind.setLayout(layout_summa)


wind.show()
app.exec_()