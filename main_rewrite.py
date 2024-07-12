import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, QEvent
import json


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("/home/gluon/TimeInRep/mainwind.ui", self)  # Підключення візуалу з дизайнера
        
########################################################################################*
        
       
#* Хня якась
        self.setFixedSize(674, 584)
        self.move(700, 80)
        self.widget = QWidget()
        self.scrollLayout = QVBoxLayout(self.widget)
            

#
        

        
        
#* ховаємо кнопки(геній) 
        
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
#
        
#* глобалки типа
        self.button_count = 1
        self.buttons = {}    
        self.timer = QTimer(self)
        self.auto_save = QTimer(self)
        self.elapsed_time = 0
        self.start_butt.setCheckable(True)
        self.current_button = None
        self.choice_butt = 0
        self.small_formatted_time = f"{00:2d}s"
        self.butt_num = self.habit_2
#! таймерасти0
        self.time_button_2 = {'name': 'Timer 2', 'status': False, 'seconds': 0, 'f_seconds': 0}
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
            # Добавьте остальные таймеры по аналогии
        }        #* коннекти
        self.pushButton.clicked.connect(self.open_addGameWidget)
        self.pushButton.clicked.connect(self.counter)
        self.start_butt.clicked.connect(self.start_timer)
        self.start_butt.clicked.connect(self.value_changer)
        self.time_butt_2.clicked.connect(self.open_addTimeWidget)
        self.timer.timeout.connect(self.zapuskator)
        # self.timer.timeout.connect(self.update_timer_forStart)
        # self.timer.timeout.connect(self.time_formattor)
        # self.timer.timeout.connect(self.timer_sync)
        self.auto_save.timeout.connect(self.save_data)
       
        
        
        
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
        
        self.choose = 'habit_'
        
        # self.load_data()
        # self.load_game()
        
        self.saver_timer()
        self.value_on_start_updator()
        
        
##? Контекстне меню
        self.habit_2.installEventFilter(self)
        self.habit_3.installEventFilter(self)
        self.habit_4.installEventFilter(self)
        self.habit_5.installEventFilter(self)
        self.habit_6.installEventFilter(self)
        self.habit_7.installEventFilter(self)
        self.habit_8.installEventFilter(self)
        self.habit_9.installEventFilter(self)
        self.habit_10.installEventFilter(self)
        self.habit_11.installEventFilter(self)
        

        

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.RightButton and obj == self.habit_2:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_3:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_4:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_5:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_6:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_7:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_8:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_9:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_10:
                self.context_menu(obj)
                return True
            if event.button() == Qt.RightButton and obj == self.habit_11:
                self.context_menu(obj)
                return True
            



        return super().eventFilter(obj, event)

    def context_menu(self, button):
        
        self.whozis = button
        print(self.whozis.objectName)
        self.edit_window = QDialog()
        uic.loadUi('ActivityEdit.ui', self.edit_window)        
        self.edit_window.buttSave.clicked.connect(self.edit_game)
        self.edit_window.deleteButt.clicked.connect(self.delete_game)
        self.edit_window.buttCancel.clicked.connect(self.butt_cancel)
   
            
        self.edit_window.show()
    def butt_cancel(self):
        self.edit_window.hide()
    def delete_game(self, button):
        self.whozis.hide()
        
        self.button_count -= 1
        print(f'мінус: {self.button_count}')
        self.edit_window.hide()
        print(f' flfllf {self.whozis.objectName()}')
        
        if self.whozis.objectName() == "habit_2":
            self.timeLabel_2.hide()
            
            self.update_timer_forStart()

            
        if self.whozis.objectName() == "habit_3":
            self.timeLabel_3.hide()
            self.statusOn_2.hide()
            self.time_button_3['status'] = False
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()


            
        if self.whozis.objectName() == "habit_4":
            self.timeLabel_4.hide()
            self.statusOn_3.hide()
            self.time_button_4['status'] = False
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_5":
            self.timeLabel_5.hide()
            self.statusOn_4.hide()
            self.time_button_5['status'] = False
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_6":
            self.timeLabel_6.hide()
            self.statusOn_5.hide()
            self.time_button_6['status'] = False
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_6":
            self.timeLabel_7.hide() 
            self.statusOn_6.hide()
            self.time_button_7['status'] = False
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_7":
            self.time_button_8['status'] = False
            self.timeLabel_8.hide() 
            self.statusOn_7.hide()
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_8":
            self.time_button_9['status'] = False
            self.timeLabel_9.hide() 
            self.statusOn_8.hide()
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_9":
            self.time_button_10['status'] = False
            self.timeLabel_10.hide() 
            self.statusOn_9.hide()
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_10":
            self.time_button_11['status'] = False
            self.timeLabel_11.hide() 
            self.statusOn_10.hide()
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()



        if self.whozis.objectName() == "habit_11":
            self.time_button_12['status'] = False
            self.statusOn_11.hide()
            self.timeLabel_12.hide()
            self.time_button_3['seconds'] = 0
            self.update_timer_forStart()

        
            
       
    def edit_game(self):
        if self.edit_window.comboBox.currentText() == 'Edit':
            new_name = self.edit_window.lineEdit.text()
            self.whozis.setText(new_name)
            self.edit_window.hide()
        if self.edit_window.comboBox.currentText() == 'Set Time':
            self.time_button_2['seconds'] = int(self.edit_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()

#?    Кнопарики сайдбари, сотворення і тд                                                                                                                                                             #?
    def counter(self):
        if self.button_count < 12:
            self.button_count += 1
            print(self.button_count)
            return self.button_count
        if self.button_count > 12:
            
            print(self.button_count)
            
# 
       
#?    Секундомір і тд      
    def start_timer(self):
        # for timer_id in self.timer:
            # timer = QTimer(self)
            # timer.timeout.connect(lambda timer_id=timer_id: self.update_timer(timer_id))
        self.timer.start(1000)  
    def saver_timer(self):
        self.auto_save.start(10000)       
    def value_changer(self):
        if self.start_butt.isChecked():
            if self.choose == 'habit_2':
                self.time_button_2['status'] = not self.time_button_2['status']
                print(f't butt 2 status: {self.time_button_2['status']}')
                
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


            if self.choose == 'habit_6':
                            self.time_button_6['status'] = not self.time_button_6['status']
                            print(self.time_button_6['status'])
                            
                            self.update_timer_forStart()
            if self.choose == 'habit_7':
                            self.time_button_7['status'] = not self.time_button_7['status']
                            print(self.time_button_7['status'])
                            
                            self.update_timer_forStart()
            if self.choose == 'habit_8':
                            self.time_button_8['status'] = not self.time_button_8['status']
                            print(self.time_button_8['status'])
                            
                            self.update_timer_forStart()
            if self.choose == 'habit_9':
                            self.time_button_9['status'] = not self.time_button_9['status']
                            print(self.time_button_9['status'])
                            
                            self.update_timer_forStart()
            if self.choose == 'habit_10':
                            self.time_button_10['status'] = not self.time_button_10['status']
                            print(self.time_button_10['status'])
                            
                            self.update_timer_forStart()
            if self.choose == 'habit_11':
                            self.time_button_11['status'] = not self.time_button_11['status']
                            print(self.time_button_11['status'])
                            
                            self.update_timer_forStart()
            
                            self.time_button_12['status'] = not self.time_button_12['status']
                            print(self.time_button_12['status'])
                            
                            self.update_timer_forStart()
            
    def value_on_start_updator(self):
            self.time_button_2['status'] = True
            self.update_timer_forStart()
            self.time_button_2['status'] = False
            
            self.time_button_3['status'] = True
            self.update_timer_forStart()
            self.time_button_3['status'] = False
           
            self.time_button_4['status'] = True
            self.update_timer_forStart()
            self.time_button_4['status'] = False

            self.time_button_5['status'] = True
            self.update_timer_forStart()
            self.time_button_5['status'] = False

            self.time_button_5['status'] = True
            self.update_timer_forStart()
            self.time_button_5['status'] = False

            self.time_button_6['status'] = True
            self.update_timer_forStart()
            self.time_button_6['status'] = False

            self.time_button_7['status'] = True
            self.update_timer_forStart()
            self.time_button_7['status'] = False

            self.time_button_8['status'] = True
            self.update_timer_forStart()
            self.time_button_8['status'] = False

            self.time_button_9['status'] = True
            self.update_timer_forStart()
            self.time_button_9['status'] = False

            self.time_button_10['status'] = True
            self.update_timer_forStart()
            self.time_button_10['status'] = False

            self.time_button_11['status'] = True
            self.update_timer_forStart()
            self.time_button_11['status'] = False

            self.time_button_12['status'] = True
            self.update_timer_forStart()
            self.time_button_12['status'] = False
    
        
##? замiна маячнi
    
    # def set_value(self, number):
    #     setattr(self, f"time_button_{number}", {'seconds': value})
        
    
        
    def get_value(self, number):
        
        timer_key = f"time_button_{number}"
        selected_timer = self.time_buttons.get(timer_key)
        print (f'get_value: {selected_timer['status']}')
       # self.timer_po_sut(selected_timer)

    def zapuskator(self):
        print(self.time_button_2['seconds'])
        if self.time_button_2['status'] == True:
            self.time_button_2['seconds'] += 1
            self.time_formattor(self.time_button_2)

        if self.time_button_3['status'] == True:
            self.time_button_3['seconds'] += 1
            self.time_formattor(self.time_button_3)
                
        if self.time_button_4['status'] == True:
            self.time_button_4['seconds'] += 1
            self.time_formattor(self.time_button_4)
                
        if self.time_button_5['status'] == True:
            self.time_button_5['seconds'] += 1
            self.time_formattor(self.time_button_5)
                
        if self.time_button_6['status'] == True:
            self.time_button_6['seconds'] += 1
            self.time_formattor(self.time_button_6)
            
        if self.time_button_7['status'] == True:
            self.time_button_7['seconds'] += 1
            self.time_formattor(self.time_button_3)  

        if self.time_button_8['status'] == True:
            self.time_button_8['seconds'] += 1
            self.time_formattor(self.time_button_3)  

        if self.time_button_9['status'] == True:
            self.time_button_9['seconds'] += 1
            self.time_formattor(self.time_button_3)
                
        if self.time_button_10['status'] == True:
            self.time_button_10['seconds'] += 1
            self.time_formattor(self.time_button_3)
                
        if self.time_button_11['status'] == True:
            self.time_button_11['seconds'] += 1
            self.time_formattor(self.time_button_3)   

        if self.time_button_12['status'] == True:
            self.time_button_12['seconds'] += 1
            self.time_formattor(self.time_button_12)
            

   

    def time_formattor(self, button):
        seconds = button['seconds']
        
        if seconds < 60:
            small_formatted_time = f"{seconds:.1f}s"
        elif seconds < 3600:
            minutes = seconds // 60
            small_formatted_time = f"{minutes:02d}m"
        elif seconds > 3600:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            small_formatted_time = f"{hours:02d}h {minutes:02d}m"
        button['f_seconds'] = small_formatted_time
        self.small_timers()
        

    def update_timer_forStart(self):
        # it just nedeed because dependies {crying emojii ;( }
        self.timer_sync()
        
    def small_timers(self):
        for number in range(2, 13):
            timer_key = f"timeLabel_{number}"
            button_key = f"time_button_{number}"
            
            label = getattr(self, timer_key)
            button = self.time_buttons.get(button_key)
            
            if button:
                label.setText(str(button['f_seconds']))
    
#
        

#? Додавання часу       
    def open_addTimeWidget(self):
        self.new_window = QDialog()
        uic.loadUi("naoborot.ui", self.new_window)
        
        self.new_window.cancel_button.clicked.connect(self.buttonsss)
        self.new_window.save_button.clicked.connect(self.buttonsss)
        
        self.new_window.show()
        
    def buttonsss(self):
        whois = self.sender()
        print(whois.text())
        if whois.text() == 'Save':
            print(self.choose)    
            if self.choose == 'habit_2':
                print('son')
                self.time_button_2['seconds']  = self.time_button_2['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_3':
                print('son')
                self.time_button_3['seconds']  = self.time_button_3['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_4':
                print('son')
                self.time_button_4['seconds']  = self.time_button_4['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_5':
                print('son')
                self.time_button_5['seconds']  = self.time_button_5['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_6':
                print('son')
                self.time_button_6['seconds']  = self.time_button_6['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_7':
                print('son')
                self.time_button_7['seconds']  = self.time_button_7['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_8':
                print('son')
                self.time_button_8['seconds']  = self.time_button_8['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_9':
                print('son')
                self.time_button_9['seconds']  = self.time_button_9['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            if self.choose == 'habit_10':
                print('son')
                self.time_button_11['seconds']  = self.time_button_11['seconds'] + int(self.new_window.lineEdit.text())
            self.new_window.hide()
            self.timer_sync()
            

        elif whois.text() == 'Cancel':
            self.new_window.hide()
        else: 
            print('щзх')    

#
    def activityEdit():
        self.new_window = QDialog()
        uic.loadUi("ActivityEdit.ui", self.new_window)
        
        self.new_window.show()
#? кнопка ігор додавання
    def open_addGameWidget(self):
        self.new_window = QDialog()
        uic.loadUi("timedialog.ui", self.new_window)
        
        self.new_window.cancel_button.clicked.connect(self.add_game)
        self.new_window.save_button.clicked.connect(self.add_game)
        
       
        self.new_window.show()
        
        
        self.crnt_butt_name = self.new_window.gameName.text()
        print(self.crnt_butt_name)
        return self.crnt_butt_name


    def add_game(self):
       
        game_name = self.new_window.gameName.text()
        
        
           
        if self.button_count == 2:
            self.habit_2.show()
            self.timeLabel_2.show()
            self.habit_2.setText(game_name)
            
            self.time_button_2['name'] = self.habit_2.text()
            self.update_timer_forStart()
    
        if self.button_count == 3:
            self.habit_3.show()
            self.timeLabel_3.show()
            self.habit_3.setText(game_name)
            
            
            self.update_timer_forStart()

        if self.button_count == 4:
            self.habit_4.show()
            self.timeLabel_4.show()
            self.habit_4.setText(game_name)
           
            self.update_timer_forStart()
        if self.button_count == 5:
            self.habit_5.show()
            self.timeLabel_5.show()
            self.habit_5.setText(game_name)
            
            self.update_timer_forStart()

        if self.button_count == 6:
            self.habit_6.show()
            self.timeLabel_6.show()
            self.habit_6.setText(game_name)
            
            self.update_timer_forStart()

        if self.button_count == 7:
            self.habit_7.show()
            self.habit_7.setText(game_name)
            self.timeLabel_7.show()
            
            self.update_timer_forStart()

        if self.button_count == 8:
            self.habit_8.show()
            self.habit_8.setText(game_name)
            self.timeLabel_8.show()
            
            self.update_timer_forStart()

        if self.button_count == 9:
            self.habit_9.show()
            self.timeLabel_9.show()
            
            self.update_timer_forStart()

        if self.button_count == 10:
            self.habit_10.show()
            self.habit_10.setText(game_name)
            self.timeLabel_10.show()
            
            self.update_timer_forStart()

        if self.button_count == 11:
            self.habit_11.show()
            self.habit_11.setText(game_name)
            self.timeLabel_11.show()
            
            self.update_timer_forStart()
      
        
        if self.button_count == 12:
            QMessageBox.critical(self, "fck its error///", "You reached maximum", QMessageBox.Ok)

        self.new_window.hide()
    def load_game(self):
        if self.button_count >= 2:
            self.habit_2.show()
            self.timeLabel_2.show()
            self.habit_2.setText(self.time_button_2['name'])
            
        if self.button_count >= 3:
            self.habit_3.show()
            self.timeLabel_3.show()
            self.habit_3.setText(self.time_button_3['name'])
            
        if self.button_count >= 4:
            self.habit_4.show()
            self.timeLabel_4.show()
            self.habit_4.setText(self.time_button_4['name'])
            
        if self.button_count >= 5:
            self.habit_5.show()
            self.timeLabel_5.show()
            self.habit_5.setText(self.time_button_2['name'])
            
        if self.button_count >= 6:
            self.habit_6.show()
            self.timeLabel_6.show()  
            self.habit_6.setText(self.time_button_2['name'])

        if self.button_count >= 7:
            self.habit_7.show()
            self.timeLabel_7.show() 
            self.habit_7.setText(self.time_button_2['name'])
            
        if self.button_count >= 8:
            self.habit_8.show()
            self.timeLabel_8.show()  
            self.habit_8.setText(self.time_button_2['name'])

        if self.button_count >= 9:
            self.habit_9.show()
            self.timeLabel_9.show() 
            self.habit_9.setText(self.time_button_2['name'])
        
        if self.button_count >= 10:
            self.habit_10.show()
            self.timeLabel_10.show()  
            self.habit_10.setText(self.time_button_2['name'])

        if self.button_count >= 11:
            self.habit_11.show()
            self.timeLabel_11.show() 
            self.habit_2.setText(self.time_button_2['name'])
    
#? ну собсно вибирання звички
    def chose_activity(self):
        self.chosedActivity = self.sender()
        print(f"Chosed activity: {self.chosedActivity.objectName()}")
        self.choose = self.chosedActivity.objectName()
        choice = self.chosedActivity 
        
        self.choose_indicator(choice)
        print(f'geg{self.choose}')


        for number in range(2, 11):
            choose = f"habit_{number}"
            
            if self.choose == choose:
                choice_butt = number
                self.get_value(choice_butt)
                print(choose)
                print(f'kruk:{choice_butt}')
            

        
        
    # Добавьте условия для остальных активностей, если нужно
    
    # Вызов функции get_value() с правильным параметром
    
        
    def choose_indicator(self,choice):
        if hasattr(self, 'previous_choice') and self.previous_choice:
            self.previous_choice.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #232634;
            border-radius: 0%; ''')  # Reset previous button style
        
        choice.setStyleSheet('''background-color: #232634; 
            color: #a5adce;
            font-family: Liberation Mono;
            background-color: #181926;
            border-radius: 0%; ''')  
        self.previous_choice = choice  # Store the current choice as previous
        
        
    def timer_sync(self):
        if self.choose == 'habit_2' and self.time_button_2['status'] == True :
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
                                                                        
        if self.choose == 'habit_4':
            hours = self.time_button_4['seconds'] // 3600
            minutes = (self.time_button_4['seconds'] % 3600) // 60
            seconds = self.time_button_4['seconds'] % 60
            
            self.formatted_time_3 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_3)
        if self.choose == 'habit_5':
            hours = self.time_button_5['seconds'] // 3600
            minutes = (self.time_button_5['seconds'] % 3600) // 60
            seconds = self.time_button_5['seconds'] % 60
            
            self.formatted_time_4 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_4)    
        if self.choose == 'habit_6':
            hours = self.time_button_6['seconds'] // 3600
            minutes = (self.time_button_6['seconds'] % 3600) // 60
            seconds = self.time_button_6['seconds'] % 60
            
            self.formatted_time_5 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_5)    
        if self.choose == 'habit_7':
            hours = self.time_button_7['seconds'] // 3600
            minutes = (self.time_button_7['seconds'] % 3600) // 60
            seconds = self.time_button_7['seconds'] % 60
            
            self.formatted_time_6 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_6) 
        if self.choose == 'habit_8':
            hours = self.time_button_8['seconds'] // 3600
            minutes = (self.time_button_8['seconds'] % 3600) // 60
            seconds = self.time_button_8['seconds'] % 60
            
            self.formatted_time_7 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_7)
        if self.choose == 'habit_9':
            hours = self.time_button_9['seconds'] // 3600
            minutes = (self.time_button_9['seconds'] % 3600) // 60
            seconds = self.time_button_9['seconds'] % 60
            
            self.formatted_time_8 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_8)    
        if self.choose == 'habit_10':
            hours = self.time_button_10['seconds'] // 3600
            minutes = (self.time_button_10['seconds'] % 3600) // 60
            seconds = self.time_button_10['seconds'] % 60
            
            self.formatted_time_9 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_9)  
        if self.choose == 'habit_11':
            hours = self.time_button_11['seconds'] // 3600
            minutes = (self.time_button_11['seconds'] % 3600) // 60
            seconds = self.time_button_11['seconds'] % 60
            
            self.formatted_time_10 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_10)  
       
            hours = self.time_button_12['seconds'] // 3600
            minutes = (self.time_button_12['seconds'] % 3600) // 60
            seconds = self.time_button_12['seconds'] % 60
            
            self.formatted_time_12 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timeLabel.setText(self.formatted_time_12)  
        else:
            pass
##! джуйсон
        
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
        with open('timers_data46784678.json', 'w') as file:
            json.dump(data, file, indent=4)
        print('Data saved successfully.')

    
    def load_data(self):
        try:
            with open('timers_data2.json', 'r') as file:
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()      
    sys.exit(app.exec_())
