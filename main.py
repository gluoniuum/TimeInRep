import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/timeIn/mainwind.ui", self)  # Підключення візуалу з дизайнера
########################################################################################*
        
        
#* Хня якась
        self.setFixedSize(640, 632)
        self.widget = QWidget()
        self.scrollLayout = QVBoxLayout(self.widget)
        # self.scrollArea.setWidget(self.widget)        

#

#* Табла тіпа sql але поки просто образний пітон

        self.pbutt2 = 130
        self.pbutt3 = 12
        self.pbutt4 = 560
        
        bubububuub = jsfkfjfj
#* ховаємо кнопки(геній) 
        
        self.buttons = [
            self.pushButton_2, self.pushButton_3, self.pushButton_4,
            self.pushButton_5, self.pushButton_6, self.pushButton_7,
            self.pushButton_8, self.pushButton_9, self.pushButton_10,
            self.pushButton_11, self.pushButton_12, self.pushButton_13
        ]
        for button in self.buttons:
            button.hide()

        self.labels = [
            self.label_2, self.label_3, self.label_4,
            self.label_5, self.label_6, self.label_7,
            self.label_8, self.label_9, self.label_10,
            self.label_11, self.label_12, self.label_13
        ]
        for label in self.labels:
            label.hide()
#
        
#* глобалки типа
        self.button_count = 0
        self.buttons = {}    
        self.timer = QTimer(self)
        self.elapsed_time = 0
        self.start_butt.setCheckable(True)
        self.current_button = None
        self.elapsed_time = 0
        self.time_button_2 = 0
        self.time_button_3 = 0
        self.time_button_4 = 0
#

#* коннекти
        self.pushButton.clicked.connect(self.open_addGameWidget)
        self.pushButton.clicked.connect(self.counter)
        self.start_butt.clicked.connect(self.start_timer)
        self.time_butt_2.clicked.connect(self.open_addTimeWidget)
        self.timer.timeout.connect(self.update_timer)
        self.pushButton_3.clicked.connect(self.habit_time)
        self.pushButton_2.clicked.connect(self.habit_time)
        self.pushButton_4.clicked.connect(self.habit_time)
#
        
    
#?    Кнопарики сайдбари, сотворення і тд                                                                                                                                                             #?
    def counter(self):
        self.button_count += 1
        print(self.button_count)
        return self.button_count
    
# 
       
#?    Секундомір і тд      
    def start_timer(self):
        self.timer.start(1000)  
        
    def update_timer(self):
        if self.start_butt.isChecked():
            self.start_butt.setText('Start')
           ##
            self.label_2.show()
            self.elapsed_time += 1

            minutes = self.elapsed_time // 60 % 60
            seconds = self.elapsed_time % 60
            hours = self.elapsed_time // 3600
            
            time_str = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            
            self.label_2.setText(time_str)
        else: 
            self.start_butt.setText('Stop')
            
#
        

#? Додавання часу       
    def open_addTimeWidget(self):
        self.new_window = QDialog()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/timeIn/naoborot.ui", self.new_window)
        
        self.new_window.cancel_button.clicked.connect(self.buttonsss)
        self.new_window.save_button.clicked.connect(self.buttonsss)
        
        self.new_window.show()

    def buttonsss(self):
        whois = self.sender()
        print(whois.text())
        if whois.text() == 'Save':
            
            self.elapsed_time = self.elapsed_time + int(self.new_window.lineEdit.text())
            self.new_window.hide()


        elif whois.text() == 'Cancel':
            self.new_window.hide()
        else: 
            print('щзх')    

#

#? кнопка ігор додавання
    def open_addGameWidget(self):
        self.new_window = QDialog()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/timeIn/timedialog.ui", self.new_window)
        
        self.new_window.cancel_button.clicked.connect(self.add_game)
        self.new_window.save_button.clicked.connect(self.add_game)
        
       
        self.new_window.show()
        
        
        self.crnt_butt_name = self.new_window.gameName.text()
        print(self.crnt_butt_name)
        return self.crnt_butt_name


    def add_game(self):
       
        game_name = self.new_window.gameName.text()
        
        if self.button_count == 1:
            self.pushButton_2.show()
            self.pushButton_2.setText(game_name)
        elif self.button_count == 2:
            self.pushButton_3.show()
            self.pushButton_3.setText(game_name)
    
        elif self.button_count == 3:
            self.pushButton_4.show()
            self.pushButton_4.setText(game_name)

        elif self.button_count == 4:
            self.pushButton_5.show()
            self.pushButton_5.setText(game_name)
        
        elif self.button_count == 5:
            self.pushButton_6.show()
            self.pushButton_6.setText(game_name)

        elif self.button_count == 6:
            self.pushButton_7.show()
            self.pushButton_7.setText(game_name)

        elif self.button_count == 7:
            self.pushButton_8.show()
            self.pushButton_8.setText(game_name)

        elif self.button_count == 8:
            self.pushButton_9.show()
            self.pushButton_9.setText(game_name)

        elif self.button_count == 9:
            self.pushButton_10.show()
            self.pushButton_10.setText(game_name)

        elif self.button_count == 10:
            self.pushButton_11.show()
            self.pushButton_10.setText(game_name)

        elif self.button_count == 11:
            self.pushButton_12.show()
            self.pushButton_10.setText(game_name)

        elif self.button_count == 12:
            self.pushButton_13.show()
            self.pushButton_10.setText(game_name)
        else:
            QMessageBox.critical(self, "fck its error///", "You reached maximum", QMessageBox.Ok)

        self.new_window.hide()

#? ну собсно вибирання звички

    def habit_time(self):
        whois = self.sender()
        print(f"Switching to: {whois.objectName()}")

        # Save current elapsed time before switching
        if self.current_button:
            if self.current_button == self.pushButton_2:
                self.time_button_2 = self.elapsed_time
            elif self.current_button == self.pushButton_3:
                self.time_button_3 = self.elapsed_time
            elif self.current_button == self.pushButton_4:
                self.time_button_4 = self.elapsed_time

        # Switch to the new button
        self.current_button = whois
        self.timer.stop()
        if whois == self.pushButton_2:
            
            self.elapsed_time = self.time_button_2
            
        elif whois == self.pushButton_3:
            
            self.elapsed_time = self.time_button_3
            
        elif whois == self.pushButton_4:
            
            self.elapsed_time = self.time_button_4

        self.timer.stop()

#########################################################################################*
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())










