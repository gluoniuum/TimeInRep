import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/TimeInRep/mainwind.ui", self)  # Підключення візуалу з дизайнера
        
########################################################################################*
        
        
#* Хня якась
        self.setFixedSize(640, 632)
        self.move(700, 80)
        self.widget = QWidget()
        self.scrollLayout = QVBoxLayout(self.widget)
        # self.scrollArea.setWidget(self.widget)        

#
        
#* Табла тіпа sql але поки просто образний пітон
        
        
        
        
#* ховаємо кнопки(геній) 
        
        self.buttons = [
            self.habit, self.habit_2, self.habit_3, self.habit_4,self.habit_5,
            self.habit_6,self.habit_7,self.habit_8,self.habit_9,self.habit_10,self.habit_11, self.habit_12,      
        ]
        for button in self.buttons:
            button.hide()

        self.labels = [
           self.statusOn_1, self.statusOn_2, self.statusOn_2, self.statusOn_3, self.statusOn_4, self.statusOn_5,
        ]
        for label in self.labels:
            label.hide()
        self.timeLabels = [
            self.timeLabel_2,self.timeLabel_3,self.timeLabel_4,self.timeLabel_5,self.timeLabel_6
        ]
        for label in self.timeLabels:
            label.hide()
#
        
#* глобалки типа
        self.button_count = 1
        self.buttons = {}    
        self.timer = QTimer(self)
        self.elapsed_time = 0
        self.start_butt.setCheckable(True)
        self.current_button = None
        

        self.time_button_2 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_3 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_4 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_5 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_6 = {
            'status' : False,
            'seconds': 0,
        }
#* коннекти
        self.pushButton.clicked.connect(self.open_addGameWidget)
        self.pushButton.clicked.connect(self.counter)
        self.start_butt.clicked.connect(self.start_timer)
        self.start_butt.clicked.connect(self.value_changer)
        self.time_butt_2.clicked.connect(self.open_addTimeWidget)
        self.timer.timeout.connect(self.update_timer_forStart)
        # self.pushButton.clicked.connect(self.contextMenuEvent)
        
        self.habit.clicked.connect(self.chose_activity)
        
        self.habit_2.clicked.connect(self.chose_activity)
        self.habit_3.clicked.connect(self.chose_activity)
        self.habit_4.clicked.connect(self.chose_activity)
        self.habit_5.clicked.connect(self.chose_activity)
        self.habit_6.clicked.connect(self.chose_activity)
        self.habit_7.clicked.connect(self.chose_activity)
        self.habit_8.clicked.connect(self.chose_activity)
        self.habit_9.clicked.connect(self.chose_activity)
        self.habit_10.clicked.connect(self.chose_activity)
        self.habit_11.clicked.connect(self.chose_activity)
        self.habit_12.clicked.connect(self.chose_activity)

#
##? Контекстне меню
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        
        newAct = QAction('Edit', self)
        openAct = QAction('Delete', self)
        # quitAct = QAction('Quit', self)

        contextMenu.addAction(newAct)
        contextMenu.addSeparator()
        contextMenu.addAction(openAct)
        # contextMenu.addSeparator()
        # contextMenu.addAction(quitAct)

        # Встановлюємо стиль для меню (це змінить колір тексту всіх пунктів меню)
        contextMenu.setStyleSheet("""QMenu { 
        font-size: 15px;
        color: #a5adce;
        font-family: Liberation Mono;
        background-color: #363a4f;
        border-radius: 10%; }""")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        


#?    Кнопарики сайдбари, сотворення і тд                                                                                                                                                             #?
    def counter(self):
        self.button_count += 1
        print(self.button_count)
        return self.button_count
    
# 
       
#?    Секундомір і тд      
    def start_timer(self):
        self.timer.start(1000)  
        
    def value_changer(self):
        if self.start_butt.isChecked():
            if self.choose == 'habit_2':
                self.time_button_2['status'] = not self.time_button_2['status']
                print(self.time_button_2['status'])
                
                self.update_timer_forStart()

            if self.choose == 'habit_3':
                self.time_button_3['status'] = not self.time_button_3['status']
                print(self.time_button_3['status'])
                
                self.update_timer_forStart()
            
            if self.choose == 'habit_4':
                self.time_button_4['status'] = not self.time_button_4['status']
                print(self.time_button_4['status'])
                
                self.update_timer_forStart()
            if self.choose == 'habit_5':
                self.time_button_5['status'] = not self.time_button_5['status']
                print(self.time_button_5['status'])
                
                self.update_timer_forStart()


    def update_timer_forStart(self):
        pass
###? хуйня 1         
        if self.time_button_2['status'] == True:
            
            self.statusOn_1.show()
            
            self.time_button_2['seconds'] += 1  # Оновлюємо кількість секунд на 1
            if self.time_button_2['seconds'] < 60:
               decimal_minutes = (self.time_button_2['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_2['seconds'] < 360:
                minutes = (self.time_button_2['seconds']) // 60
                
                small_formatted_time = f"{minutes:2d}m"

            elif self.time_button_2['seconds'] < 3600:
                decimal_hours = (self.time_button_2['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_2['seconds'] // 3600
            minutes = (self.time_button_2['seconds'] % 3600) // 60
            seconds = self.time_button_2['seconds'] % 60
            
            self.formatted_time_1 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_2.setText(small_formatted_time)
           
        if self.time_button_2['status'] == False:
            self.statusOn_1.hide()
#
###? хуйня 2

        if self.time_button_3['status'] == True:
            
            self.statusOn_2.show()
            self.time_button_3['seconds'] += 1  # Оновлюємо кількість секунд на 1
            if self.time_button_3['seconds'] < 60:
               decimal_minutes = (self.time_button_3['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_3['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 60
                
                small_formatted_time = f"{minutes:2d}m"

            elif self.time_button_3['seconds'] < 3600:
                decimal_hours = (self.time_button_3['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_3['seconds'] // 3600
            minutes = (self.time_button_3['seconds'] % 3600) // 60
            seconds = self.time_button_3['seconds'] % 60
            
            self.formatted_time_2 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_3.setText(small_formatted_time)
           
        if self.time_button_3['status'] == False:
            self.statusOn_2.hide()
            
#
###? хуйня 3

        if self.time_button_4['status'] == True:
            
            self.statusOn_3.show()
            
            self.time_button_4['seconds'] += 1  # Оновлюємо кількість секунд на 1

            hours = self.time_button_4['seconds'] // 3600
            minutes = (self.time_button_4['seconds'] % 3600) // 60
            seconds = self.time_button_4['seconds'] % 60
            formatted_time = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            small_formatted_time = f" {hours:02d}:{minutes:02d}"
            
            self.timeLabel_2.setText(small_formatted_time)
            print(formatted_time)
            
        if self.time_button_4['status'] == False:
            self.statusOn_3.hide() 
#     
###? хуйня 4

        if self.time_button_5['status'] == True:
            
            self.statusOn_4.show()
            
            self.time_button_5['seconds'] += 1  # Оновлюємо кількість секунд на 1

            hours = self.time_button_5['seconds'] // 3600
            minutes = (self.time_button_5['seconds'] % 3600) // 60
            seconds = self.time_button_5['seconds'] % 60
            formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            print(formatted_time)
            
            small_formatted_time = f" {hours:02d}:{minutes:02d}"
            
            self.timeLabel_5.setText(small_formatted_time)
            self.statusOn_4.show()
        if self.time_button_5['status'] == False:
            self.statusOn_4.hide() 
        
# *  центральний таймер      
   
    
    
   
        
    
#
        

#? Додавання часу       
    def open_addTimeWidget(self):
        self.new_window = QDialog()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/TimeInRep/naoborot.ui", self.new_window)
        
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
    def activityEdit():
        self.new_window = QDialog()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/TimeInRep/ActivityEdit", self.new_window)
        
        self.new_window.show()
#? кнопка ігор додавання
    def open_addGameWidget(self):
        self.new_window = QDialog()
        uic.loadUi("/home/quakr/CompurutureScientology/Projectttttss/TimeInRep/timedialog.ui", self.new_window)
        
        self.new_window.cancel_button.clicked.connect(self.add_game)
        self.new_window.save_button.clicked.connect(self.add_game)
        
       
        self.new_window.show()
        
        
        self.crnt_butt_name = self.new_window.gameName.text()
        print(self.crnt_butt_name)
        return self.crnt_butt_name


    def add_game(self):
       
        game_name = self.new_window.gameName.text()
        
        if self.button_count == 1:
            self.habit.show()
            self.timeLabel_2.show()
            self.habit.setText(game_name)
        elif self.button_count == 2:
            self.habit_2.show()
            self.timeLabel_2.show()
            self.habit_2.setText(game_name)
    
        elif self.button_count == 3:
            self.habit_3.show()
            self.timeLabel_3.show()
            self.habit_3.setText(game_name)

        elif self.button_count == 4:
            self.habit_4.show()
            self.timeLabel_4.show()
            self.habit_4.setText(game_name)
        
        elif self.button_count == 5:
            self.habit_5.show()
            self.timeLabel_5.show()
            self.habit_5.setText(game_name)

        elif self.button_count == 6:
            self.habit_6.show()
            self.timeLabel_6.show()
            self.habit_6.setText(game_name)

        elif self.button_count == 7:
            self.habit_7.show()
            self.habit_7.setText(game_name)

        elif self.button_count == 8:
            self.habit_8.show()
            self.habit_8.setText(game_name)

        elif self.button_count == 9:
            self.habit_9.show()
            self.habit_9.setText(game_name)

        elif self.button_count == 10:
            self.habit_10.show()
            self.habit_10.setText(game_name)

        elif self.button_count == 11:
            self.habit_11.show()
            self.habit_11.setText(game_name)

        elif self.button_count == 12:
            self.habit_12.show()
            self.habit_12.setText(game_name)
        else:
            QMessageBox.critical(self, "fck its error///", "You reached maximum", QMessageBox.Ok)

        self.new_window.hide()

#? ну собсно вибирання звички
    def chose_activity(self):
        self.chosedActivity = self.sender()
        print(f"Chosed activity: {self.chosedActivity.objectName()}")
        self.choose = self.chosedActivity.objectName()
        print(self.choose)
        choice = self.chosedActivity 
        self.choose_indicator(choice)
        
    def choose_indicator(self,choice):
        if hasattr(self, 'previous_choice') and self.previous_choice:
            self.previous_choice.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #232634;
            border-radius: 5%; ''')  # Reset previous button style
        
        choice.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #181926;
            border-radius: 5%; ''')  
        self.previous_choice = choice  # Store the current choice as previous
        
        
    def timer_sync(self):
        if self.choose == 'habit_2':
            hours = self.time_button_2['seconds'] // 3600
            minutes = (self.time_button_2['seconds'] % 3600) // 60
            seconds = self.time_button_2['seconds'] % 60
            
            self.formatted_time_1 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_1)
            
        if self.choose == 'habit_3':
            hours = self.time_button_3['seconds'] // 3600
            minutes = (self.time_button_3['seconds'] % 3600) // 60
            seconds = self.time_button_3['seconds'] % 60
            
            self.formatted_time_2 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_2)

#########################################################################################*
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
