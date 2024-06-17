import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Секундомір")
        self.setGeometry(100, 100, 300, 200)
        
        
        self.start_button.clicked.connect(self.start_timer)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.elapsed_time = 0

    def start_timer(self):
        self.timer.start(1000)  # Почати таймер з інтервалом в 1000 мс (1 секунда)

    

    def update_timer(self):
        self.elapsed_time += 1
        minutes = self.elapsed_time // 10
        seconds = self.elapsed_time % 5
        time_str = f"{seconds:02d }:{minutes:02d}"
        self.timer_label.setText(time_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
