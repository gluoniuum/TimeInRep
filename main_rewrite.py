from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox, QMenu, QAction
from PyQt5.QtCore import QTimer, Qt, QEvent
from PyQt5 import uic

import json
import time
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi('/home/gluon/TimeInRep/mainwind.ui', self)  # Підключення візуалу з дизайнера
        
########################################################################################*
        
       
#?    Маячня якась
        self.setFixedSize(674, 600)
        self.move(700, 80)
        self.widget = QWidget()
        self.scrollLayout = QVBoxLayout(self.widget)

#*    Ховаємо кнопки(геній) 
        
        self.buttons = [
            self.habit_2, self.habit_3, self.habit_4,self.habit_5,
            self.habit_6,self.habit_7,self.habit_8,self.habit_9,self.habit_10,self.habit_11
        ]
        for button in self.buttons:
            button.hide()

        self.labels = [
           self.statusOn_1, self.statusOn_2, self.statusOn_3, self.statusOn_4, self.statusOn_5, self.statusOn_6, self.statusOn_7,
           self.statusOn_8, self.statusOn_11, self.statusOn_9, self.statusOn_10,  self.statusOn_11
        ]
        for label in self.labels:
            label.hide()
        self.timeLabels = [
            self.timeLabel_2,self.timeLabel_3,self.timeLabel_4,self.timeLabel_5,self.timeLabel_6,self.timeLabel_7,self.timeLabel_8,self.timeLabel_9,
            self.timeLabel_10,self.timeLabel_11,self.timeLabel_12
        ]
        for label in self.timeLabels:
            label.hide()
      
#!    Глобалки типа
        self.button_count = 1
        self.buttons = {}    
        self.timer = QTimer(self)
        self.auto_save = QTimer(self)
        self.elapsed_time = 0
        self.start_butt.setCheckable(False)
        self.current_button = None
        self.choice_butt = 0
        self.small_formatted_time = f'{00:2d}s'
        self.startButtonStatus = False
        self.butt_num = self.habit_2
        self.curent_date = 20240802
        self.previosly_date = 20240801

#?    Таймерасти
        self.time_button_2 = {'status': False, 'seconds': 0, 'f_seconds': 0, 'name': 'Timer 2',}
        self.time_button_3 = {'name': 'Timer 3', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_4 = {'name': 'Timer 4', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_5 = {'name': 'Timer 5', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_6 = {'name': 'Timer 6', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_7 = {'name': 'Timer 7', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_8 = {'name': 'Timer 8', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_9 = {'name': 'Timer 9', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_10 = {'name': 'Timer 10', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_11 = {'name': 'Timer 11', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_button_12 = {'name': 'Timer 12', 'status': False, 'seconds': 0, 'f_seconds': 0}
        self.time_buttons = {
            'time_button_2': self.time_button_2,
            'time_button_3': self.time_button_3,
            'time_button_4': self.time_button_4,
            'time_button_5': self.time_button_5,
            'time_button_6': self.time_button_6,
            'time_button_7': self.time_button_7,
            'time_button_8': self.time_button_8,
            'time_button_9': self.time_button_9,
            'time_button_10': self.time_button_10,
            'time_button_11': self.time_button_11,
            'time_button_12': self.time_button_12,
#*      конекти           
        }     
        self.start_butt.clicked.connect(self.startORstop)   
        self.pushButton.clicked.connect(self.open_addGameWidget)
        self.pushButton.clicked.connect(self.counter)
        self.start_butt.clicked.connect(self.start_timer)
        
        self.start_butt.clicked.connect(self.value_changer)
        self.time_butt_2.clicked.connect(self.open_addTimeWidget)
        self.timer.timeout.connect(self.zapuskator)
        self.timer.timeout.connect(self.timer_sync)
        self.auto_save.timeout.connect(self.save_data)  
        self.auto_save.timeout.connect(self.curent_time) 
        
        for number in range(2, 12):
            habit_key = f'habit_{number}'
            habit_key = getattr(self, habit_key, None)
            habit_key.clicked.connect(self.chose_activity)
        self.choose = 'habit_'
        self.load_data()
        self.load_game()
        self.small_timers()
        self.saver_timer()
        self.value_on_start_updator()
        self.timer_sync()
        self.start_timer()
        self.curent_time()

#*    Контекстне меню
        for number in range(2, 12):
            habit_key = f'habit_{number}'
            habit_key = getattr(self, habit_key, None)
            habit_key.installEventFilter(self)

    def eventFilter(self, obj, event):       
        if event.type() == QEvent.MouseButtonPress:          
            if event.button() == Qt.RightButton:
                for number in range(2, 12):
                    habit_key = f'habit_{number}'
                    obj_norm = obj.objectName()
                    self.whazis = getattr(self, habit_key, None)
                    
                    self.text_whozis = f'self.{habit_key}'
                    if obj_norm == habit_key:                   
                        self.context_menu(obj)
                        return True
        return super().eventFilter(obj, event)

    def context_menu(self, button):
        self.edit_window = QDialog()
        uic.loadUi('ActivityEdit.ui', self.edit_window)        
        self.edit_window.buttSave.clicked.connect(self.edit_game)
        self.edit_window.deleteButt.clicked.connect(self.delete_game)
        self.edit_window.buttCancel.clicked.connect(self.butt_cancel)          
        self.edit_window.show()
    def butt_cancel(self):
        self.edit_window.hide()
    def delete_game(self, button):
        self.whazis.hide()
        self.button_count = self.button_count - 1
        print(self.button_count)
        self.edit_window.hide()
        
        for number in range(2, 12):     
            if self.text_whozis == f'self.habit_{number}':
                timeLabel = f'timeLabel_{number}'        
                timeLabel = getattr(self, timeLabel, None)
                timeLabel.hide()
                statusOn = f'statusOn_{number - 1}'

                statusOn = getattr(self, statusOn, None)
                statusOn.hide()
                time_button = f'time_button_{number}'            
                time_button = getattr(self, time_button, None)                
                time_button['status'] = False
                time_button['seconds'] = 0
                self.timer_sync()
    
    def edit_game(self):
        if self.edit_window.comboBox.currentText() == 'Edit':
            new_name = self.edit_window.lineEdit.text()
            for number in range(2, 12):
                if self.text_whozis == f'self.habit_{number}':
                    self.whazis.setText(new_name)
                    time_button = f'time_button_{number}'
                    
                    time_button = getattr(self, time_button, None)
                    time_button['name'] = new_name
                    self.edit_window.hide()

        if self.edit_window.comboBox.currentText() == 'Set Time':
            for number in range(2, 12):
                if self.text_whozis == f'self.habit_{number}':
                    time_button = f'time_button_{number}'
                    time_button = getattr(self, time_button, None)
                    time_button['seconds'] = int(self.edit_window.lineEdit.text())
                    self.new_window.hide()
                    self.timer_sync()
                    
                self.new_window.hide()

#!    Кнопарики сайдбари, сотворення і тд                                                                                                                                                             #?
    def counter(self):
        if self.button_count < 12:
            self.button_count += 1
           
            return self.button_count
        if self.button_count > 12:
            pass

#?    Секундомір і тд      
    def start_timer(self):
        self.timer.start(1000)  

    def saver_timer(self):
        self.auto_save.start(10000)    

    def startORstop(self):
        self.startButtonStatus = not self.startButtonStatus 
        if  self.startButtonStatus == True:
            self.start_butt.setText('Stop')
        elif  self.startButtonStatus == False:
            self.start_butt.setText('Start')

   
                
    def value_changer(self):
        if self.startButtonStatus == True:
            for number in range(2, 12):
                if self.choose == f'habit_{number}':
                    button_key = f'time_button_{number}'
                    button_key = getattr(self, button_key, None)
                    button_key['status'] = True     

                    statusOn_key = f'statusOn_{number - 1}'
                    statusOn_key = getattr(self, statusOn_key, None)
                    statusOn_key.show()
                    self.timer_sync()      
             

        elif self.startButtonStatus == False:
            for number in range(2, 12):
                if self.choose == f'habit_{number}':
                    button_key = f'time_button_{number}'
                    button_key = getattr(self, button_key, None)
                    button_key['status'] = False          
                    statusOn_key = f'statusOn_{number - 1}'
                    statusOn_key = getattr(self, statusOn_key, None)
                    statusOn_key.hide()     
                    self.timer_sync()      

    def value_on_start_updator(self):
        for number in range(2, 12):            
            button_key = f'time_button_{number}'
            button_key = getattr(self, button_key, None)

            button_key['status'] = True
            self.zapuskator()
            button_key['status'] = False     

#*   Замiна маячнi   
    def get_value(self, number):  
            timer_key = f"time_button_{number}"
            selected_timer = self.time_buttons.get(timer_key)
            
    def zapuskator(self):
        
        for number in range(2, 12):
            button_key = f'time_button_{number}'
            button_key = getattr(self, button_key, None)
            if button_key['status'] == True:
                button_key['seconds'] += 1
                self.time_formattor(button_key)
                
              

    def time_formattor(self, button):
        seconds = button['seconds']
        
        if seconds <= 60:
            decimal_minutes = seconds / 60
            small_formatted_time = f'{decimal_minutes:.1f}m'
        elif seconds <= 360:
            minutes = seconds // 60
            small_formatted_time = f'{minutes:2d}m'
        elif seconds <= 3600:
            decimal_hours = seconds / 3600
            
            small_formatted_time = f'{decimal_hours:.1f}h'
            

        elif seconds >= 3600:
            hours = seconds // 3600
            
            small_formatted_time = f'{hours:2d}h'
        button['f_seconds'] = small_formatted_time
        self.small_timers()

    def small_timers(self):
        for number in range(2, 12):
            timer_key = f'timeLabel_{number}'
            button_key = f'time_button_{number}'
            
            label = getattr(self, timer_key)
            button = self.time_buttons.get(button_key)
            
            if button:
                label.setText(str(button['f_seconds']))

#!    Додавання часу       
    def open_addTimeWidget(self):
        self.new_window = QDialog()
        uic.loadUi('naoborot.ui', self.new_window)
        self.new_window.cancel_button.clicked.connect(self.buttonsss)
        self.new_window.save_button.clicked.connect(self.buttonsss)
        self.new_window.show()
        
    def buttonsss(self):
        whois = self.sender()
       
        if whois.text() == 'Save':
               
            for number in range(2, 12):
                if self.choose == f'habit_{number}':
                    time_button = f'time_button_{number}'
                    time_button = getattr(self, time_button, None)
                    time_button['seconds']  = time_button['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            
        elif whois.text() == 'Cancel':
            self.new_window.hide()
        else: 
            pass

    def activityEdit():
        self.new_window = QDialog()
        uic.loadUi('ActivityEdit.ui', self.new_window)
        self.new_window.show()
#*    .time
    def curent_time(self):
        self.current_time = time.localtime()
        self.date_to_int()
        
    
    def date_to_int(self):
        current_date = f"{self.current_time.tm_year}{self.current_time.tm_mon:02d}{self.current_time.tm_mday:02d}"
        print(f'pr: {self.previosly_date}')
        print(f'cr: {self.curent_date}')
        
        if self.curent_date > self.previosly_date:
            #todo логика для сброс таймера за сегодня и тд
            self.previosly_date = self.curent_date
            print(f'pr_2: {self.previosly_date}')
            print('yay')
        else:
            pass


    def fake_date(self):
        self.curent_date = self.curent_date + 1
        print(f'fk: {self.curent_date}')
        time.sleep(10)
        











#*    Кнопка ігор додавання
    def open_addGameWidget(self):
        self.new_window = QDialog()
        uic.loadUi('timedialog.ui', self.new_window)
        
        self.new_window.cancel_button.clicked.connect(self.add_game)
        self.new_window.save_button.clicked.connect(self.add_game)
         
        self.new_window.show()
        self.crnt_butt_name = self.new_window.gameName.text()
        return self.crnt_butt_name
    def add_game(self):     
        game_name = self.new_window.gameName.text()
        for number in range(2, 12):
            if self.button_count == number:
                habit = f'habit_{number}'
                label = f'timeLabel_{number}'
                time_button = f'time_button_{number}'

                habit = getattr(self, habit, None)
                label = getattr(self, label, None)
                time_button = getattr(self, time_button, None)
        
                habit.show()
                label.show()
                habit.setText(game_name)
                time_button['name'] = habit.text()
                
                self.timer_sync()
        if self.button_count >= 12:
            QMessageBox.critical(self, 'fck its error///', 'You reached maximum', QMessageBox.Ok)

        self.new_window.hide()
    def load_game(self):
        for number in range(2, 12):
            if self.button_count >= number:
                habit = f'habit_{number}'
                label = f'timeLabel_{number}'
                time_button = f'time_button_{number}'

                habit = getattr(self, habit, None)
                label = getattr(self, label, None)
                time_button = getattr(self, time_button, None)

                habit.show()
                label.show()
                print (time_button)
                habit.setText(time_button['name'])
                    
#?    Ну собсно вибирання звички
    def chose_activity(self):
        self.chosedActivity = self.sender()
        
        self.choose = self.chosedActivity.objectName()
        choice = self.chosedActivity 
        
        
        for number in range(2, 12): 
            
            choose = f'habit_{number}'
            
            if self.choose == choose:
                time_button = f'time_button_{number}'
                time_button = getattr(self, time_button, None)
                choice_butt = number
                
                self.get_value(choice_butt)
                self.choose_indicator(choice, number)
                if time_button['status'] == True:
                    self.startButtonStatus = False
                    self.startORstop()
                if time_button['status'] == False:
                    self.startButtonStatus = True
                    self.startORstop()
        print('_____________')
        
                
                
    def choose_indicator(self, choice, number):
        if hasattr(self, 'previous_choice') and self.previous_choice:
            self.previous_choice.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #232634;
            border-radius: 0%; ''')  
        
        if hasattr(self, 'previous_statusOn') and self.previous_statusOn:
            self.previous_statusOn.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            
            background-color: #232634;
            border-top-left-radius: 5%;
            border-bottom-left-radius: 5%; ''')  

        if hasattr(self, 'previous_label') and self.previous_label:
            self.previous_label.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #232634;
            border-top-right-radius: 5%;
            border-bottom-right-radius: 5%;''')  
        
        choice.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #181926;
            border-radius: 0%; ''')  
        statusOnTxt = f'statusOn_{number - 1}'
        
        chooseTxt = f'habit_{number}'
        
        statusOn = getattr(self, statusOnTxt)

        timeLabel = f'timeLabel_{number}'
        timeLabel = getattr(self, timeLabel)

        timeLabel.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #181926;
            border-top-right-radius: 5%;
            border-bottom-right-radius: 5%; ''')  

        statusOn.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #181926;
            border-top-left-radius: 5%;
            border-bottom-left-radius: 5%; ''')  
        self.previous_label = timeLabel
        self.previous_choice = choice  
        self.previous_statusOn = statusOn
        
    def timer_sync(self):
        for number in range(2, 12):
            if self.choose == f'habit_{number}':
                time_button = f'time_button_{number}'
                time_button = getattr(self, time_button, None) 
                hours = time_button['seconds'] // 3600
                minutes = (time_button['seconds'] % 3600) // 60
                seconds = time_button['seconds'] % 60
                
                formatted_time = f'  {hours:02d}:{minutes:02d}:{seconds:02d}'
                self.timeLabel.setText(formatted_time)
                
##!   Jsonn
    def save_data(self):
        data = {
            'time_button_2': self.time_button_2,
            'time_button_3': self.time_button_3,
            'time_button_4': self.time_button_4,
            'time_button_5': self.time_button_5,
            'time_button_6': self.time_button_6,
            'time_button_7': self.time_button_7,
            'time_button_8': self.time_button_8,
            'time_button_9': self.time_button_9,
            'time_button_10': self.time_button_10,
            'time_button_11': self.time_button_11,
            'button_count': self.button_count
        }
        with open('timers_dataa.json', 'w') as file:
            json.dump(data, file, indent=4)
        print('Data saved successfully.')
        
    
    def load_data(self):
        try:
            with open('timers_dataa.json', 'r') as file:
                data = json.load(file)
                self.time_button_2.update({'name': data.get('time_button_2', {}).get('name', self.time_button_2['name']), 'seconds': data.get('time_button_2', {}).get('seconds', 0), 'status': False})
                self.time_button_3.update({'name': data.get('time_button_3', {}).get('name', self.time_button_3['name']), 'seconds': data.get('time_button_3', {}).get('seconds', 0), 'status': False})
                self.time_button_4.update({'name': data.get('time_button_4', {}).get('name', self.time_button_4['name']), 'seconds': data.get('time_button_4', {}).get('seconds', 0), 'status': False})
                self.time_button_5.update({'name': data.get('time_button_5', {}).get('name', self.time_button_5['name']), 'seconds': data.get('time_button_5', {}).get('seconds', 0), 'status': False})
                self.time_button_6.update({'name': data.get('time_button_6', {}).get('name', self.time_button_6['name']), 'seconds': data.get('time_button_6', {}).get('seconds', 0), 'status': False})
                self.time_button_7.update({'name': data.get('time_button_7', {}).get('name', self.time_button_7['name']), 'seconds': data.get('time_button_7', {}).get('seconds', 0), 'status': False})
                self.time_button_8.update({'name': data.get('time_button_8', {}).get('name', self.time_button_8['name']), 'seconds': data.get('time_button_8', {}).get('seconds', 0), 'status': False})
                self.time_button_9.update({'name': data.get('time_button_9', {}).get('name', self.time_button_9['name']), 'seconds': data.get('time_button_9', {}).get('seconds', 0), 'status': False})
                self.time_button_10.update({'name': data.get('time_button_10', {}).get('name', self.time_button_10['name']), 'seconds': data.get('time_button_10', {}).get('seconds', 0), 'status': False})
                self.time_button_11.update({'name': data.get('time_button_11', {}).get('name', self.time_button_11['name']), 'seconds': data.get('time_button_11', {}).get('seconds', 0), 'status': False})
                self.button_count = data.get('button_count', 0)
            print('Data loaded successfully.')
        except FileNotFoundError:
            print('No data file found.')
     
#########################################################################################* 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()      
    sys.exit(app.exec_())