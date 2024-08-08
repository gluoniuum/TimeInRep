from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox, QMenu, QAction
from PyQt5.QtCore import QTimer, Qt, QEvent
from PyQt5 import uic
from PyQt5.QtGui import QFont
import json
from datetime import datetime, timedelta

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi('ui_files/mainwind.ui', self)  # Підключення візуалу з дизайнера
        
########################################################################################*
        
       
#?    Маячня якась
        self.setFixedSize(674, 600)
        self.resize(674, 600)
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
        self.pomodoro_timer = QTimer(self)
        self.elapsed_time = 0
        self.start_butt.setCheckable(False)
        self.current_button = None
        self.choice_butt = 0
        self.small_formatted_time = f'{00:2d}s'
        self.startButtonStatus = False
        self.butt_num = self.habit_2
        self.current_time = datetime.now()
        self.previosly_date = 0
        self.previosly_week = 0
        self.pomo_butt.setText('🍅')
        font = QFont('Segoe UI Emoji', 20)  
        self.pomo_butt.setFont(font)
        # self.current_date = 20240803
        
#?    Таймерасти
        self.time_button_2 = {'status': False, 'seconds': 0, 'f_seconds': 0, 'name': 'Timer 2', 'today_time':0,'t_seconds':0 }
        self.time_button_3 = {'name': 'Timer 3', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_4 = {'name': 'Timer 4', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_5 = {'name': 'Timer 5', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_6 = {'name': 'Timer 6', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_7 = {'name': 'Timer 7', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_8 = {'name': 'Timer 8', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_9 = {'name': 'Timer 9', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_10 = {'name': 'Timer 10', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_11 = {'name': 'Timer 11', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
        self.time_button_12 = {'name': 'Timer 12', 'status': False, 'seconds': 0, 'f_seconds': 0, 'today_time':0,'t_seconds':0 }
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

#*    Kонекти           
        }     
        self.start_butt.clicked.connect(self.startORstop)   
        self.pushButton.clicked.connect(self.open_addGameWidget)
        self.pushButton.clicked.connect(self.counter)
        self.start_butt.clicked.connect(self.start_timer)
        
        self.start_butt.clicked.connect(self.value_changer)
        self.time_butt_2.clicked.connect(self.open_addTimeWidget)
        self.pomo_butt.clicked.connect(self.pomo_ui)
        self.timer.timeout.connect(self.zapuskator)
        self.timer.timeout.connect(self.timer_sync)
        self.pomodoro_timer.timeout.connect(self.pomodoro)
        self.auto_save.timeout.connect(self.save_data)  
        self.auto_save.timeout.connect(self.curent_time) 
        self.dev_butt.clicked.connect(self.dev_button)
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
        

#?    Контекстне меню
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
        uic.loadUi('ui_files/ActivityEdit.ui', self.edit_window)        
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
                time_button['t_seconds'] = 0
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
                    time_button['t_seconds'] = int(self.edit_window.lineEdit.text())
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
    def pomo_timer(self):
        self.pomodoro_timer.start(1000)  
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

#*    Замiна маячнi   
    def get_value(self, number):  
            timer_key = f"time_button_{number}"
            selected_timer = self.time_buttons.get(timer_key)
    
    def dev_button(self):
        print('_______')
        print('yayy')
        print(self.time_button_6)
        print(self.current_time.strftime("%H:%M:%S"))
        print(f'pr: {self.previosly_date}')
        print(f'cr: {self.current_date}')
        print('_______')
        
    def zapuskator(self):
        
        for number in range(2, 12):
            button_key = f'time_button_{number}'
            button_key = getattr(self, button_key, None)
            if button_key['status'] == True:
                button_key['seconds'] += 1
                button_key['t_seconds'] += 1
                self.time_formattor(button_key)
                self.date_to_int()
                self.curent_time()
                
    def time_formattor(self, button):
        seconds = button['seconds']
        if seconds <= 60:
            decimal_minutes = seconds / 60
            small_formatted_time = f'{decimal_minutes:.1f}m  ' 
        elif seconds <= 360:
            minutes = seconds // 60
            small_formatted_time = f'{minutes:2d}m  '
        elif seconds <= 3600:
            decimal_hours = seconds / 3600
            
            small_formatted_time = f'{decimal_hours:.1f}h  '
            

        elif seconds >= 3600:
            hours = seconds // 3600
            
            small_formatted_time = f'{hours:2d}h  '
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
        uic.loadUi('ui_files/naoborot.ui', self.new_window)
        self.new_window.cancel_button.clicked.connect(self.buttonsss)
        self.new_window.save_button.clicked.connect(self.buttonsss)
        self.new_window.show()
        
    def buttonsss(self):
        whois = self.sender()
       
        if whois.objectName() == 'save_button':
               
            for number in range(2, 12) :
                if self.choose == f'habit_{number}':
                    time_button = f'time_button_{number}'
                    time_button = getattr(self, time_button, None)
                    time_button['seconds']  = time_button['seconds'] + int(self.new_window.lineEdit.text())
                    time_button['t_seconds']  = time_button['t_seconds'] + int(self.new_window.lineEdit.text())

            self.new_window.hide()
            self.timer_sync()
            
        elif whois.objectName()== 'cancel_button':
            self.new_window.hide()
        
        else: 
            pass

    def activityEdit():
        self.new_window = QDialog()
        uic.loadUi('ui_files/ActivityEdit.ui', self.new_window)
        self.new_window.show()

#*?   .time
    def curent_time(self):
        self.r_current_time = datetime.now()
        self.current_time = self.r_current_time + timedelta()
       
    def date_to_int(self):
        
        self.current_date = int(self.current_time.strftime('%Y%m%d'))

        
        if self.current_date > self.previosly_date:
            
            self.previosly_date = self.current_date
            for number in range(2, 12):
                button = f'time_button_{number}'
                button = getattr(self, button, None)
                button['today_time'] = 0
                button['t_seconds'] = 0
                print(button)
                
            #     self.previosly_date = self.current_date
            #     button['week_time'] = 0
            #     button['w_seconds'] = 0
            #     print(button)
                print('_________')

            print(f'pr_2: {self.previosly_date}')
            print('yay')

#*    Кнопка ігор додавання
    def open_addGameWidget(self):
        self.new_window = QDialog()
        uic.loadUi('ui_files/timedialog.ui', self.new_window)
        
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

                t_hours = time_button['t_seconds'] // 3600
                t_minutes = (time_button['t_seconds'] % 3600) // 60
                t_seconds = time_button['t_seconds'] % 60
                t_formatted_time = f' today: {t_hours:02d}:{t_minutes:02d}:{t_seconds:02d}'
                formatted_time = f'  {hours:02d}:{minutes:02d}:{seconds:02d}'
                self.timeLabel.setText(formatted_time)
                
                time_button['today_time'] = t_formatted_time
                self.todayTime.setText(time_button['today_time'])

##! pomodoro
    def pomo_ui(self):
        self.new_window = QDialog()
        uic.loadUi('ui_files/pomo.ui', self.new_window)
        self.new_window.show()
        self.new_window.buttCancel.clicked.connect(self.pomo_start)
        self.new_window.buttStart.clicked.connect(self.pomo_start)
    def pomo_start(self):
        whois = self.sender()
        print(self.sender)
        if whois.objectName() == 'buttCancel':
            self.new_window.hide()
        if whois.objectName() == 'buttStart':
            self.intial_longBreakPomo = int(self.new_window.longBreak_lineEdit.text())
            self.intial_workPomo = int(self.new_window.work_lineEdit.text())
            
            self.intial_breakPomo = int(self.new_window.break_lineEdit.text())
            
            self.intial_pomoCycles = int(self.new_window.pomoCycles_lineEdit.text())

            self.pomo_status = 'work'
            self.pomod_status()
            self.pomo_timer()
            self.new_window.hide()



    def pomod_status(self):
        
        self.workPomo = self.intial_workPomo 
        self.breakPomo = self.intial_breakPomo 
        self.longBreakPomo = self.intial_longBreakPomo
        self.pomoCycles = self.intial_pomoCycles
        self.cycles = self.pomoCycles
        self.pomoCount = 0
        self.cycleLabel.setText(str(self.cycles))
        

    
    def pomodoro(self):
    
        if self.pomo_status == 'work' and self.workPomo > 1:
            self.workPomo -= 1
            self.pomoLabel.setText(str(self.workPomo))
            self.pomoLabel.setStyleSheet('color: rgb(255, 99, 99); font-size: 20px;')  

            if self.workPomo <= 1:
                self.pomo_status = 'break'
                self.breakPomo = self.intial_breakPomo
                self.cycles -=1
                self.cycleLabel.setText(str(self.cycles))
                #alarm of message

            if self.cycles <= 0:
                self.pomo_status = 'longBreak'
                self.longBreakPomo = self.intial_longBreakPomo
                
        if self.pomo_status == 'longBreak' and self.longBreakPomo > 1:
            self.longBreakPomo -= 1
            self.cycles = self.pomoCycles
             
            self.pomoLabel.setText(str(self.longBreakPomo))
            self.pomoLabel.setStyleSheet('color: rgb(23, 194, 80); font-size: 20px;')  

            if self.longBreakPomo <= 1:
                self.pomo_status = 'work'
                self.workPomo = self.intial_workPomo
                print('yay')

        if self.pomo_status == 'break'and self.breakPomo > 1:
            self.breakPomo -= 1
            self.pomoLabel.setText(str(self.breakPomo))
            self.pomoLabel.setStyleSheet('color: rgb(23, 194, 71); font-size: 20px;')  
            if self.breakPomo <= 1:
                self.pomo_status = 'work'
                self.workPomo = self.intial_workPomo
                
                print('yay')
                self.pomoCount += 1
                
                #alarm and msg
        
##! Jsonn
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
            'button_count': self.button_count,
            'previosly_date' : self.previosly_date

        }
        with open('timers_dataa.json', 'w') as file:
            json.dump(data, file, indent=4)
        print('Data saved successfully.')
        
    
    def load_data(self):
        try:
            with open('timers_dataa.json', 'r') as file:
                data = json.load(file)
            for number in range(2, 12):
                time_button_name = f'time_button_{number}'
                time_button = getattr(self, time_button_name, {
                    'name': '',
                    'seconds': 0,
                    'f_seconds': '',
                    'status': False,
                    'today_time': 0,
                    't_seconds': 0})
                button_data = data.get(time_button_name, {})
                time_button.update({
                    'name': button_data.get('name', time_button.get('name')),
                    'seconds': button_data.get('seconds', 0),
                    'f_seconds': button_data.get('f_seconds', time_button.get('f_seconds')),
                    'today_time': button_data.get('today_time', time_button.get('today_time')),
                    't_seconds': button_data.get('t_seconds', time_button.get('t_seconds')),
                    'status': False,
                    
                })
                setattr(self, time_button_name, time_button)
            self.button_count = data.get('button_count', 0)
            self.previosly_date = data.get('previosly_date', 0)
            
            print('Data loaded successfully.')
            
        except FileNotFoundError:
            print('No data file found.')
##!     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()      
    sys.exit(app.exec_())