import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Вкладки")
window.setGeometry(100, 100, 400, 300)

layout = QVBoxLayout()

tabs = QTabWidget()

tab1 = QWidget()
tab1_layout = QVBoxLayout()
tab1_layout.addWidget(QLabel("Это первая вкладка"))
tab1.setLayout(tab1_layout)

tab2 = QWidget()
tab2_layout = QVBoxLayout()
tab2_layout.addWidget(QLabel("Это вторая вкладка"))
tab2.setLayout(tab2_layout)

tabs.addTab(tab1, "Вкладка 1")
tabs.addTab(tab2, "Вкладка 2")

layout.addWidget(tabs)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
