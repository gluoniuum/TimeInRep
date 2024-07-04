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
        uic.loadUi("mainwind.ui", self)  # Підключення візуалу з дизайнера
        
########################################################################################*
        
       
#* Хня якась
        self.setFixedSize(674, 584)
        self.move(700, 80)
        self.widget = QWidget()
        self.scrollLayout = QVBoxLayout(self.widget)
            

#
        

        
        
#* ховаємо кнопки(геній) 
        
        self.buttons = [
            self.habit, self.habit_2, self.habit_3, self.habit_4,self.habit_5,
            self.habit_6,self.habit_7,self.habit_8,self.habit_9,self.habit_10,self.habit_11
        ]
        for button in self.buttons:
            button.hide()

        self.labels = [
           self.statusOn_1, self.statusOn_2, self.statusOn_2, self.statusOn_3, self.statusOn_4, self.statusOn_5, self.statusOn_6, self.statusOn_7,
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
        
#! таймерасти
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
        self.time_button_7 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_8 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_9 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_10 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_11 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_button_12 = {
            'status' : False,
            'seconds': 0,
        }
        self.time_buttonss = {
        'time_button_2': self.time_button_2,
        'time_button_3': self.time_button_3,
    }


#* коннекти
        self.pushButton.clicked.connect(self.open_addGameWidget)
        self.pushButton.clicked.connect(self.counter)
        self.start_butt.clicked.connect(self.start_timer)
        self.start_butt.clicked.connect(self.value_changer)
        self.time_butt_2.clicked.connect(self.open_addTimeWidget)
        self.timer.timeout.connect(self.update_timer_forStart)
        self.auto_save.timeout.connect(self.save_data)
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
        
        
        self.load_data()
        self.load_game()
        self.saver_timer()

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
        if self.whozis.objectName() == "habit_3":
            self.timeLabel_3.hide()
        if self.whozis.objectName() == "habit_4":
            self.timeLabel_4.hide()
        if self.whozis.objectName() == "habit_5":
            self.timeLabel_5.hide()
        if self.whozis.objectName() == "habit_6":
            self.timeLabel_6.hide()             
        if self.whozis.objectName() == "habit_6":
            self.timeLabel_7.hide() 
        if self.whozis.objectName() == "habit_7":
            self.timeLabel_8.hide() 
        if self.whozis.objectName() == "habit_8":
            self.timeLabel_9.hide() 
        if self.whozis.objectName() == "habit_9":
            self.timeLabel_10.hide() 
        if self.whozis.objectName() == "habit_10":
            self.timeLabel_11.hide() 
        if self.whozis.objectName() == "habit_11":
            self.timeLabel_12.hide() 
        
            self.timeLabel_13.hide() 
       
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
        self.button_count += 1
        print(self.button_count)
        return self.button_count
    
# 
       
#?    Секундомір і тд      
    def start_timer(self):
        self.timer.start(1000)  
    def saver_timer(self):
        self.auto_save.start(10000)       
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
            
            
                
    def update_timer_forStart(self):
##* маячня вся

    ###? маячня 1         
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

    ###? маячня 2
        if self.time_button_3['status'] == True:
            
            self.statusOn_2.show()
            
            self.time_button_3['seconds'] += 1  # Оновлюємо кількість секунд на 1
            if self.time_button_3['seconds'] < 60:
               decimal_minutes = (self.time_button_3['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_3['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 60
                
                small_formatted_time = f"{minutes:3d}m"

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
    ###? маячня 3
        if self.time_button_4['status'] == True:
            
            self.statusOn_3.show()
            
            self.time_button_4['seconds'] += 1  # Оновлюємо кількість секунд на 1
            if self.time_button_4['seconds'] < 60:
               decimal_minutes = (self.time_button_4['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_4['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 60
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_4['seconds'] < 3600:
                decimal_hours = (self.time_button_4['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_4['seconds'] // 3600
            minutes = (self.time_button_4['seconds'] % 3600) // 60
            seconds = self.time_button_4['seconds'] % 60
            
            self.formatted_time_5 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_4.setText(small_formatted_time)
           
        if self.time_button_4['status'] == False:
            self.statusOn_3.hide()

    ###? маячня 4
        if self.time_button_5['status'] == True:
            
            self.statusOn_4.show()
            
            self.time_button_5['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_5['seconds'] < 60:
               decimal_minutes = (self.time_button_5['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_5['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 60
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_5['seconds'] < 3600:
                decimal_hours = (self.time_button_5['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_5['seconds'] // 3600
            minutes = (self.time_button_5['seconds'] % 3600) // 60
            seconds = self.time_button_5['seconds'] % 60
            
            self.formatted_time_5 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_5.setText(small_formatted_time)
           
        if self.time_button_5['status'] == False:
            self.statusOn_4.hide()

    ###? маячня 5
        if self.time_button_5['status'] == True:
            
            self.statusOn_5.show()
            
            self.time_button_6['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_6['seconds'] < 60:
               decimal_minutes = (self.time_button_6['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_6['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 60
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_6['seconds'] < 3600:
                decimal_hours = (self.time_button_6['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_6['seconds'] // 3600
            minutes = (self.time_button_6['seconds'] % 3600) // 60
            seconds = self.time_button_6['seconds'] % 60
            
            self.formatted_time_5 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_6.setText(small_formatted_time)
           
        if self.time_button_5['status'] == False:
            self.statusOn_5.hide()
    ###? маячня 6
        if self.time_button_6['status'] == True:
            
            self.statusOn_6.show()
            
            self.time_button_6['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_6['seconds'] < 60:
               decimal_minutes = (self.time_button_6['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_6['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 60
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_6['seconds'] < 3600:
                decimal_hours = (self.time_button_6['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_6['seconds'] // 3600
            minutes = (self.time_button_6['seconds'] % 3600) // 60
            seconds = self.time_button_6['seconds'] % 60
            
            self.formatted_time_5 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_6.setText(small_formatted_time)
           
        if self.time_button_6['status'] == False:
            self.statusOn_6.hide()         

    ###? маячня 6
        if self.time_button_7['status'] == True:
            
            self.statusOn_7.show()
            
            self.time_button_7['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_7['seconds'] < 60:
               decimal_minutes = (self.time_button_7['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_7['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 602
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_7['seconds'] < 3600:
                decimal_hours = (self.time_button_7['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_7['seconds'] // 3600
            minutes = (self.time_button_7['seconds'] % 3600) // 60
            seconds = self.time_button_7['seconds'] % 60
            
            self.formatted_time_6 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_7.setText(small_formatted_time)
           
        if self.time_button_7['status'] == False:
            self.statusOn_7.hide()  

    ###? маячня 7
        if self.time_button_8['status'] == True:
            
            self.statusOn_8.show()
            
            self.time_button_8['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_8['seconds'] < 60:
               decimal_minutes = (self.time_button_8['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_8['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 602
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_8['seconds'] < 3600:
                decimal_hours = (self.time_button_8['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_8['seconds'] // 3600
            minutes = (self.time_button_8['seconds'] % 3600) // 60
            seconds = self.time_button_8['seconds'] % 60
            
            self.formatted_time_7 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_8.setText(small_formatted_time)
           
        if self.time_button_8['status'] == False:
            self.statusOn_8.hide()  
    ###? маячня 8
        if self.time_button_9['status'] == True:
            
            self.statusOn_9.show()
            
            self.time_button_9['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_9['seconds'] < 60:
               decimal_minutes = (self.time_button_9['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_9['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 602
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_9['seconds'] < 3600:
                decimal_hours = (self.time_button_9['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_9['seconds'] // 3600
            minutes = (self.time_button_9['seconds'] % 3600) // 60
            seconds = self.time_button_9['seconds'] % 60
            
            self.formatted_time_8 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_9.setText(small_formatted_time)
           
        if self.time_button_9['status'] == False:
            self.statusOn_9.hide()  
    ###? маячня 9
        if self.time_button_10['status'] == True:
            
            self.statusOn_10.show()
            
            self.time_button_10['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_10['seconds'] < 60:
               decimal_minutes = (self.time_button_10['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_10['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 602
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_10['seconds'] < 3600:
                decimal_hours = (self.time_button_10['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_10['seconds'] // 3600
            minutes = (self.time_button_10['seconds'] % 3600) // 60
            seconds = self.time_button_10['seconds'] % 60
            
            self.formatted_time_9 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_10.setText(small_formatted_time)
           
        if self.time_button_10['status'] == False:
            self.statusOn_10.hide()  
    ###? маячня 10
        if self.time_button_11['status'] == True:
            
            self.statusOn_11.show()
            
            self.time_button_11['seconds'] += 1  # Оновлюємо кількість секунд на 1

            if self.time_button_11['seconds'] < 60:
               decimal_minutes = (self.time_button_11['seconds']) / 60
               small_formatted_time = f"{decimal_minutes:.1f}m"
             
            elif self.time_button_11['seconds'] < 360:
                minutes = (self.time_button_3['seconds']) // 602
                
                small_formatted_time = f"{minutes:3d}m"

            elif self.time_button_11['seconds'] < 3600:
                decimal_hours = (self.time_button_11['seconds']) / 3600
                small_formatted_time = f"{decimal_hours:.1f}h"

            hours = self.time_button_11['seconds'] // 3600
            minutes = (self.time_button_11['seconds'] % 3600) // 60
            seconds = self.time_button_11['seconds'] % 60
            
            self.formatted_time_10 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_sync()
             
            self.timeLabel_11.setText(small_formatted_time)
           
        if self.time_button_11['status'] == False:
            self.statusOn_11.hide() 
    # # ###? маячня 10
    #     if self.time_button_12['status'] == True:
            
    #         self.statusOn_12.show()
            
    #         self.time_button_12['seconds'] += 1  # Оновлюємо кількість секунд на 1

    #         if self.time_button_12['seconds'] < 60:
    #            decimal_minutes = (self.time_button_12['seconds']) / 60
    #            small_formatted_time = f"{decimal_minutes:.1f}m"
             
    #         elif self.time_button_12['seconds'] < 360:
    #             minutes = (self.time_button_3['seconds']) // 602
                
    #             small_formatted_time = f"{minutes:3d}m"

    #         elif self.time_button_12['seconds'] < 3600:
    #             decimal_hours = (self.time_button_12['seconds']) / 3600
    #             small_formatted_time = f"{decimal_hours:.1f}h"

    #         hours = self.time_button_12['seconds'] // 3600
    #         minutes = (self.time_button_12['seconds'] % 3600) // 60
    #         seconds = self.time_button_12['seconds'] % 60
            
    #         self.formatted_time_11 = f" {hours:02d}:{minutes:02d}:{seconds:02d}"
    #         self.timer_sync()
             
    #         self.timeLabel_12.setText(small_formatted_time)
           
    # #     if self.time_button_12['status'] == False:
    #         self.statusOn_12.hide() 
#

    
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
        
        if self.button_count == 1:
            self.habit.show()
            self.timeLabel_2.show()
            self.habit.setText(game_name)
        if self.button_count == 2:
            self.habit_2.show()
            self.timeLabel_2.show()
            self.habit_2.setText(game_name)
    
        if self.button_count == 3:
            self.habit_3.show()
            self.timeLabel_3.show()
            self.habit_3.setText(game_name)

        if self.button_count == 4:
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
      
        
        else:
            QMessageBox.critical(self, "fck its error///", "You reached maximum", QMessageBox.Ok)

        self.new_window.hide()
    def load_game(self):
        if self.button_count >= 2:
            self.habit_2.show()
            self.timeLabel_2.show()
            
        if self.button_count >= 3:
            self.habit_3.show()
            self.timeLabel_3.show()
            
        if self.button_count >= 4:
            self.habit_4.show()
            self.timeLabel_4.show()
            
        if self.button_count >= 5:
            self.habit_5.show()
            self.timeLabel_5.show()
            
        if self.button_count >= 6:
            self.habit_6.show()
            self.timeLabel_6.show()  

        if self.button_count >= 7:
            self.habit_7.show()
            self.timeLabel_7.show() 
            
        if self.button_count >= 8:
            self.habit_8.show()
            self.timeLabel_8.show()  

        if self.button_count >= 9:
            self.habit_9.show()
            self.timeLabel_9.show() 
        
        if self.button_count >= 10:
            self.habit_10.show()
            self.timeLabel_10.show()  

        if self.button_count >= 11:
            self.habit_11.show()
            self.timeLabel_11.show() 
    
#? ну собсно вибирання звички
    def chose_activity(self):
        self.chosedActivity = self.sender()
        print(f"Chosed activity: {self.chosedActivity.objectName()}")
        self.choose = self.chosedActivity.objectName()
        print(self.choose)
        choice = self.chosedActivity 
        self.choose_indicator(choice)
        self.timer_sync()
        
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
        with open('timers_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print('Data saved successfully.')
    
    def load_data(self):
        try:
            with open('timers_data.json', 'r') as file:
                data = json.load(file)
                self.time_button_2.update({'seconds': data.get('time_button_2', {}).get('seconds', self.time_button_2['seconds']), 'status': False}),
                self.time_button_3.update({'seconds': data.get('time_button_3', {}).get('seconds', self.time_button_3['seconds']), 'status': False})
                self.time_button_4.update({'seconds': data.get('time_button_4', {}).get('seconds', self.time_button_4['seconds']), 'status': False})
                self.time_button_5.update({'seconds': data.get('time_button_5', {}).get('seconds', self.time_button_5['seconds']), 'status': False})
                self.time_button_6.update({'seconds': data.get('time_button_6', {}).get('seconds', self.time_button_6['seconds']), 'status': False})
                self.time_button_7.update({'seconds': data.get('time_button_7', {}).get('seconds', self.time_button_7['seconds']), 'status': False})
                self.time_button_8.update({'seconds': data.get('time_button_8', {}).get('seconds', self.time_button_8['seconds']), 'status': False})
                self.time_button_9.update({'seconds': data.get('time_button_9', {}).get('seconds', self.time_button_9['seconds']), 'status': False})
                self.time_button_10.update({'seconds': data.get('time_button_10', {}).get('seconds', self.time_button_10['seconds']), 'status': False})
                self.time_button_11.update({'seconds': data.get('time_button_11', {}).get('seconds', self.time_button_11['seconds']), 'status': False})
                self.button_count = data.get('button_count', {})
            print('Data loaded successfully.')
        except FileNotFoundError:
            print('No data file found.')

#########################################################################################*
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()      
    sys.exit(app.exec_())
