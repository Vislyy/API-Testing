from PyQt6.QtWidgets import *
from scraper import *

app = QApplication([])
window = QWidget()

mainline = QVBoxLayout()

val_from_lbl = QLabel("З якої валюти потрібно перевести")
val_to_lbl = QLabel("В яку валюти потрібно перевести")
count_lbl = QLabel("Кількість")
result_lbl = QLabel("Результат")

val_from_tplain = QLineEdit()
val_to_tplain = QLineEdit()
count_tplain = QLineEdit()
result_tplain = QLineEdit()

exchange_btn = QPushButton("Перевести")

def base_for_scraper():
    converter_val(val_from_tplain.text(), val_to_tplain.text(), int(count_tplain.text()))

exchange_btn.clicked.connect(base_for_scraper)

mainline.addWidget(val_from_lbl)
mainline.addWidget(val_from_tplain)
mainline.addWidget(val_to_lbl)
mainline.addWidget(val_to_tplain)
mainline.addWidget(count_lbl)
mainline.addWidget(count_tplain)
mainline.addWidget(result_lbl)
mainline.addWidget(result_tplain)
mainline.addWidget(exchange_btn)

window.setLayout(mainline)
window.show()
app.exec()
