import sys
import io
import csv
from datetime import datetime, date
import sqlite3
import os
from PyQt5.QtGui import QFont
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QFileDialog, \
    QGridLayout
from resources import *
from res import *

registration_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>536</width>
    <height>292</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>-40</y>
      <width>541</width>
      <height>371</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">image: url(:/newPrefix/на регистрацию.jpg);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>10</y>
      <width>371</width>
      <height>221</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="3" column="1">
      <widget class="QLineEdit" name="password_edit"/>
     </item>
     <item row="4" column="1">
      <widget class="QLineEdit" name="replay_password_edit"/>
     </item>
     <item row="0" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt; font-weight:600;&quot;&gt;Регистрация&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QLineEdit" name="login_edit"/>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Имя      &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Повторите пароль&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Логин&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="name_edit"/>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Пароль                  &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="5" column="0">
      <widget class="QPushButton" name="come_back">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(173, 184, 154);</string>
       </property>
       <property name="text">
        <string>Назад</string>
       </property>
      </widget>
     </item>
     <item row="5" column="1">
      <widget class="QPushButton" name="button_complete_registration">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(168, 183, 154);</string>
       </property>
       <property name="text">
        <string> Завершить регистрацию</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="ress.qrc"/>
 </resources>
 <connections/>
</ui>'''

main_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>915</width>
    <height>611</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <widget class="QTabWidget" name="tabWidget">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 210, 127);</string>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="tab">
       <attribute name="title">
        <string>Добавить задачу</string>
       </attribute>
       <layout class="QGridLayout" name="gridLayout_2">
        <item row="0" column="0">
         <widget class="QLabel" name="label_3">
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Выберите дату дедлайна в календаре&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item row="0" column="1">
         <widget class="QLabel" name="label_2">
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Выберите уровень приоритета&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item row="1" column="0" rowspan="3">
         <widget class="QCalendarWidget" name="calendarWidget">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 170, 0);</string>
          </property>
         </widget>
        </item>
        <item row="1" column="1">
         <widget class="QComboBox" name="priority_combo">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(85, 119, 134);
background-color: rgb(255, 255, 255);</string>
          </property>
         </widget>
        </item>
        <item row="2" column="1">
         <widget class="QLabel" name="label_4">
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Напишите категорию задачи&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item row="3" column="1">
         <widget class="QPlainTextEdit" name="category_edit">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);</string>
          </property>
         </widget>
        </item>
        <item row="4" column="0" colspan="2">
         <widget class="QLabel" name="label_5">
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:12pt;&quot;&gt;Напишите задачу&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item row="5" column="0" colspan="2">
         <widget class="QPlainTextEdit" name="task_edit">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);</string>
          </property>
         </widget>
        </item>
        <item row="6" column="0" colspan="2">
         <widget class="QPushButton" name="add_an_entry">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 170, 127);</string>
          </property>
          <property name="text">
           <string>Добавить задачу</string>
          </property>
          <property name="iconSize">
           <size>
            <width>16</width>
            <height>16</height>
           </size>
          </property>
          <property name="autoRepeatDelay">
           <number>300</number>
          </property>
          <property name="autoRepeatInterval">
           <number>102</number>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
      <widget class="QWidget" name="tab_2">
       <attribute name="title">
        <string>Посмотреть задачи</string>
       </attribute>
       <layout class="QGridLayout" name="gridLayout_3">
        <item row="0" column="0" rowspan="2">
         <layout class="QVBoxLayout" name="verticalLayout_2">
          <item>
           <widget class="QPushButton" name="updateButton">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Обновить</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="clear_table">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Очистить таблицу</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="mark_completed_tasks">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Отметить задачу как выполненную</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="view_completed_tasks">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Посмотреть выполненные задачи</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="delete_task">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Удалить задачу</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="import_button">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Import таблицы</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QPushButton" name="export_button">
            <property name="styleSheet">
             <string notr="true">background-color: rgb(255, 170, 127);</string>
            </property>
            <property name="text">
             <string>Export таблицы</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
        <item row="0" column="1">
         <widget class="QLabel" name="label_6">
          <property name="text">
           <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Как отсортировать данные в таблице&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
          </property>
         </widget>
        </item>
        <item row="0" column="2">
         <widget class="QComboBox" name="sorting">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);</string>
          </property>
         </widget>
        </item>
        <item row="1" column="1" colspan="2">
         <widget class="QTableWidget" name="tableWidget">
          <property name="styleSheet">
           <string notr="true">background-color: rgb(255, 255, 255);</string>
          </property>
         </widget>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''

password_login_request_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>518</width>
    <height>292</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>-20</y>
      <width>521</width>
      <height>331</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">image: url(:/newPrefix/на регистрацию.jpg);</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>10</y>
      <width>417</width>
      <height>228</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="5" column="0">
      <widget class="QPushButton" name="login_button">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(160, 180, 152);</string>
       </property>
       <property name="text">
        <string>Войти</string>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QLabel" name="label_3">
       <property name="styleSheet">
        <string notr="true">alternate-background-color: rgb(170, 170, 0);</string>
       </property>
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:14pt;&quot;&gt;Авторизация&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1" colspan="2">
      <widget class="QLineEdit" name="login_input">
       <property name="styleSheet">
        <string notr="true"/>
       </property>
      </widget>
     </item>
     <item row="5" column="1" colspan="2">
      <widget class="QLabel" name="label_5">
       <property name="text">
        <string/>
       </property>
       <property name="pixmap">
        <pixmap>asd.jpg</pixmap>
       </property>
      </widget>
     </item>
     <item row="6" column="2">
      <widget class="QPushButton" name="registration_button">
       <property name="styleSheet">
        <string notr="true">background-color: rgb(155, 179, 153);</string>
       </property>
       <property name="text">
        <string>Регистрация</string>
       </property>
      </widget>
     </item>
     <item row="3" column="1" colspan="2">
      <widget class="QLineEdit" name="entering_password"/>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Код с картинки&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1" colspan="2">
      <widget class="QLineEdit" name="name_button">
       <property name="styleSheet">
        <string notr="true">border-color: rgb(170, 170, 0);</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Пароль               &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="4" column="1" colspan="2">
      <widget class="QLineEdit" name="input_cod"/>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label_7">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Имя&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Логин                 &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="6" column="0" colspan="2">
      <widget class="QLabel" name="label_4">
       <property name="styleSheet">
        <string notr="true">font: 75 8pt &quot;MS Shell Dlg 2&quot;;</string>
       </property>
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt; font-weight:600;&quot;&gt;Ещё не зарегистрированы ?&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
'''

window_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>821</width>
    <height>678</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 210, 127);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <widget class="QPushButton" name="updateButton">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 170, 127);</string>
      </property>
      <property name="text">
       <string>Обновить</string>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLabel" name="label">
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Как отсортировать данные в таблице&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </item>
    <item row="0" column="2">
     <widget class="QComboBox" name="sort_comboBox">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
    </item>
    <item row="2" column="0">
     <widget class="QPushButton" name="back">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 170, 127);</string>
      </property>
      <property name="text">
       <string>Назад</string>
      </property>
     </widget>
    </item>
    <item row="2" column="1">
     <widget class="QPushButton" name="export_button">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 170, 127);</string>
      </property>
      <property name="text">
       <string>Export таблицы</string>
      </property>
     </widget>
    </item>
    <item row="2" column="2">
     <widget class="QPushButton" name="deleteButton">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 170, 127);</string>
      </property>
      <property name="text">
       <string>Удалить</string>
      </property>
     </widget>
    </item>
    <item row="1" column="0" colspan="3">
     <widget class="QTableWidget" name="tableWidget">
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>"""


class class_user_registration(QMainWindow):
    '''
    Класс для регистрации пользователя
    '''

    def __init__(self):
        super().__init__()
        f = io.StringIO(registration_window)
        uic.loadUi(f, self)
        # Установливаю размер окна
        self.setFixedSize(536, 292)
        # Создал название окна
        self.setWindowTitle('Регистрация пользователя')
        # Запускаю функцию registration_completed если нажата кнопка button_complete_registration
        self.button_complete_registration.clicked.connect(self.registration_completed)
        # Запускаю функцию fun_come_back если нажата кнопка come_back
        self.come_back.clicked.connect(self.fun_come_back)

    def fun_come_back(self):
        '''
        Функция  для открытия другого окна
        '''
        self.w2 = class_password_login_request()
        self.w2.show()
        self.close()

    def registration_completed(self):
        '''
        Функция которая  регистрирует пользователя и записывает его данные в базу данных password.db
        '''
        # Считываю данные с name_edit
        self.name = self.name_edit.text()
        # Считываю данные с login_edit
        self.login = self.login_edit.text()
        # Считываю данные с password_edit
        self.password = self.password_edit.text()
        # Считываю данные с replay_password_edit
        self.replay_password = self.replay_password_edit.text()

        # Проверяю ввел ли пользователь все данные и проверяю их корректность
        if self.name != '' and self.login != '' and self.password != '' and self.password == self.replay_password:
            # Создаю QMessageBox
            question = QMessageBox()
            # Даю название QMessageBox
            question.setWindowTitle('регистрация')
            # Вставил текст в QMessageBox
            question.setText('Вы успешно зарегистрировались')
            # Выбрал тип QMessageBox
            question.setIcon(QMessageBox.Information)
            # Добавил кнопку Ок в QMessageBox
            question.setStandardButtons(QMessageBox.Ok)
            # Подключаю базу данных
            conn = sqlite3.connect('password.db')
            cur = conn.cursor()
                # Добавляю данные пользователя в базу данных
            cur.execute("""INSERT INTO users(name,
             login,
              password) VALUES(?, ?, ?);""",
                        (self.name, self.login, self.password))
            # Делаю commit
            conn.commit()
            question.exec_()
            self.w2 = class_password_login_request()
            # открываю новое окно
            self.w2.show()
            # закрываю старое
            self.close()

        else:
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы неправильно ввели логин или пароль')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            question.buttonClicked.connect(self.processing_button_actions)
            question.exec_()

    def processing_button_actions(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки
        '''
        if btn.text() == 'OK':
            self.name_edit.setText('')
            self.login_edit.setText('')
            self.password_edit.setText('')
            self.replay_password_edit.setText('')


class class_password_login_request(QMainWindow):
    '''
    Класс для авторизации пользователя
    '''

    def __init__(self):
        super().__init__()
        f = io.StringIO(password_login_request_window)
        uic.loadUi(f, self)
        self.setFixedSize(510, 280)
        self.setWindowTitle('Вход пользователя')
        self.registration_button.clicked.connect(self.open_registration_window)
        self.login_button.clicked.connect(self.login_password_verification)

    def login_password_verification(self):
        '''
        Функция которая производит авторизацию пользователя
        '''
        name = self.name_button.text()
        login = self.login_input.text()
        password = self.entering_password.text()
        cod = self.input_cod.text()
        con = sqlite3.connect('password.db')
        cur = con.cursor()
        c = 0
        # Считываю данные с базы данных и проверя есть ли пользовтель в базе данных
        result = cur.execute("""SELECT * From users""").fetchall()
        for i in result:
            if login in i and password in i and name in i:
                c += 1
        con.close()
        # если пользователь есть то отрывается новое окно
        if cod == 'W68HP' and c > 0:
            self.w2 = Main_screen()
            self.w2.show()
            self.close()
        # если пользователь ввел неправильно капчу то выходит ошибка и стираются все поля ввода
        elif cod != 'W68HP' and c > 0:
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы неправильно ввели код с картинки')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            question.exec_()
            self.name_button.setText('')
            self.login_input.setText('')
            self.entering_password.setText('')
            self.input_cod.setText('')
        # в другом случае выходит ошибка
        else:
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы неправильно ввели логин или пароль')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            question.buttonClicked.connect(self.processing_button_actions)
            question.exec_()

    def processing_button_actions(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки
        '''
        if btn.text() == 'OK':
            self.name_button.setText('')
            self.login_input.setText('')
            self.entering_password.setText('')
            self.input_cod.setText('')

    def open_registration_window(self):
        '''
        Функция  для открытия другого окна
        '''
        self.w2 = class_user_registration()
        self.w2.show()
        self.close()


class Completed_tasks(QMainWindow):
    '''
    Класс для отображения выполненных задач пользователя
    '''

    def __init__(self):
        super().__init__()
        f = io.StringIO(window_template)
        uic.loadUi(f, self)
        # добовляю значания в sort_comboBox
        self.sort_comboBox.addItem('Без сортировки')
        self.sort_comboBox.addItem('По лексикографическому порядку')
        self.sort_comboBox.addItem('По категориям')
        self.sort_comboBox.addItem('По приоритету')
        self.back.clicked.connect(self.open_Main_screen)
        # даю название окну
        self.setWindowTitle('Выполненые задания')
        self.updateButton.clicked.connect(self.fun_update)
        self.deleteButton.clicked.connect(self.fun_deleteButton)
        self.export_button.clicked.connect(self.fun_export_button)

    def fun_export_button(self):
        '''
        Функция которая производит Export таблицы
        '''
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, 'Export file', '', 'CSV files (*.csv)')

        if file_path:
            with open(file_path, mode="w", encoding='utf-8') as file:
                file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
                con = sqlite3.connect('password.db')
                cur = con.cursor()
                result = cur.execute("""SELECT * FROM tasks""").fetchall()
                result.insert(0, ["Задача", "Категория", "Приоритет", "Кол-во дней до дедлайна"])

                for i in range(len(result)):
                    file_writer.writerow(result[i])

    def fun_deleteButton(self):
        '''
        Функция которая создает QMessageBox
        '''
        question = QMessageBox()
        question.setWindowTitle('Планировщик')
        question.setText('Вы точно хотитие очистить таблицу?')
        question.setIcon(QMessageBox.Information)
        question.setStandardButtons(QMessageBox.Ok)
        question.buttonClicked.connect(self.button_status)
        question.exec_()

    def button_status(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки.
        И при нажатии  кнопки ОК удаляет таблицу tasks в базе данных password.db
        '''
        if btn.text() == 'OK':
            conn = sqlite3.connect('password.db')
            c = conn.cursor()
            c.execute('DELETE FROM tasks;', )
            conn.commit()
            conn.close()
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            data = [["Задача", "Категория", "Приоритет", "Кол-во дней до дедлайна"]]
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setHorizontalHeaderLabels(data[0])
            for i in range(0, len(data)):
                for j in range(len(data[i])):
                    item = QTableWidgetItem(data[i][j])
                    self.tableWidget.setItem(i - 1, j, item)

    def fun_update(self):
        '''
        Функция которая сортирует таблицу
        '''
        con = sqlite3.connect('password.db')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM tasks""").fetchall()
        if len(result) == 0:
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            data = [["Задача", "Категория", "Приоритет", "Кол-во дней до дедлайна"]]
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setHorizontalHeaderLabels(data[0])
            for i in range(0, len(data)):
                for j in range(len(data[i])):
                    item = QTableWidgetItem(data[i][j])
                    self.tableWidget.setItem(i - 1, j, item)
        else:
            self.combo = self.sort_comboBox.currentText()
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            result.insert(0, ["Задача", "Категория", "Приоритет", "Кол-во дней до дедлайна"])
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(result[0])
            if self.combo == 'Без сортировки':
                for i in range(1, len(result)):
                    for j in range(len(result[i])):
                        item = QTableWidgetItem(result[i][j])
                        self.tableWidget.setItem(i - 1, j, item)
            else:
                if self.combo == 'По лексикографическому порядку':
                    sort_sp = sorted(result[1:], key=lambda row: row[0], reverse=False)
                elif self.combo == 'По категориям':
                    sort_sp = sorted(result[1:], key=lambda row: row[1], reverse=False)
                elif self.combo == 'По приоритету':
                    sort_sp = sorted(result[1:],
                                     key=lambda x: 0 if x[2] == 'Низкий' else (1 if x[2] == 'Средний' else 2))
                sort_sp.insert(0, result[0])
                for i in range(1, len(sort_sp)):
                    for j in range(len(sort_sp[i])):
                        item = QTableWidgetItem(sort_sp[i][j])
                        self.tableWidget.setItem(i - 1, j, item)
            con.close()

    def open_Main_screen(self):
        '''
        Функция  для открытия другого окна
        '''
        self.w2 = Main_screen()
        self.w2.show()
        self.close()


class Main_screen(QMainWindow):
    '''
    Класс для добавления и отображения задач пользователя
    '''

    def __init__(self):
        super().__init__()
        f = io.StringIO(main_window)
        uic.loadUi(f, self)
        self.setLayout(QGridLayout())
        self.priority_combo.addItem("Низкий")
        self.priority_combo.addItem("Средний")
        self.priority_combo.addItem("Βысокий")
        self.sorting.addItem('Без сортировки')
        self.sorting.addItem('По лексикографическому порядку')
        self.sorting.addItem('По категориям')
        self.sorting.addItem('По приоритету')
        self.setWindowTitle('Планировщик')
        self.add_an_entry.setFont(QFont('Добавить задачу', 12))
        self.updateButton.setFont(QFont('Обновить', 10))
        self.clear_table.setFont(QFont('Очистить таблицу', 10))
        self.mark_completed_tasks.setFont(QFont('Отметить задачу как выполненную', 10))
        self.view_completed_tasks.setFont(QFont('Посмотреть выполненные задачи', 10))
        self.delete_task.setFont(QFont('Удалить задачу', 10))
        self.import_button.setFont(QFont('Import таблицы', 10))
        self.export_button.setFont(QFont('Export таблицы', 10))
        self.add_an_entry.clicked.connect(self.fun_add_an_entry)
        self.updateButton.clicked.connect(self.create_table)
        self.clear_table.clicked.connect(self.fun_clear_table)
        self.delete_task.clicked.connect(self.fun_delete_task)
        self.mark_completed_tasks.clicked.connect(self.fun_mark_completed_tasks)
        self.view_completed_tasks.clicked.connect(self.open_completed_tasks)
        self.export_button.clicked.connect(self.fun_export_button)
        self.import_button.clicked.connect(self.fun_import_button)

    def fun_import_button(self):
        '''
        Функция  которая производит Import данных
        '''
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Import file')

        if file_path:
            with open(file_path, mode="r", encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)
                csv_data = list(reader)
                os.remove("records.csv")
                with open("records.csv", mode='a', encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    for i in csv_data:
                        if len(i) != 0:
                            file_writer.writerow(i)

    def fun_export_button(self):
        '''
        Функция  которая производит Export данных
        '''
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, 'Export file', '', 'CSV files (*.csv)')

        if file_path:
            with open(file_path, mode="w", encoding='utf-8') as file:
                file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
                with open("records.csv", mode="r", encoding='utf-8') as f:
                    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
                    csv_data = list(reader)
                for i in csv_data:
                    print(i)
                    file_writer.writerow(i)

    def open_completed_tasks(self):
        '''
        Функция  для открытия другого окна
        '''
        self.w2 = Completed_tasks()
        self.w2.show()
        self.close()

    def fun_mark_completed_tasks(self):
        '''
        Функция  которая обрабатывает нажатие на таблицу
        '''
        self.row = self.tableWidget.currentRow()
        if self.row <= -1:
            question = QMessageBox()
            question.setWindowTitle('Планировщик')
            question.setText('Чтобы выполнить задачу нажмите на её название')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            question.exec_()
        if self.row > -1:
            question = QMessageBox()
            question.setWindowTitle('Планировщик')
            question.setText('Вы действительно хотите отметить  задачу как выполненную?')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            question.buttonClicked.connect(self.button_actions_OK)
            question.exec_()

    def button_actions_OK(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки.
        И при нажатии  кнопки ОК записывает данные в таблицу tasks в баззе данных password.db
        и удаляет данные из таблицы records.csv
        '''
        if btn.text() == 'OK':
            self.tableWidget.removeRow(self.row)
            self.tableWidget.selectionModel().clearCurrentIndex()
            with open("records.csv", mode="r", encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
                csv_data = list(reader)
            conn = sqlite3.connect('password.db')
            cur = conn.cursor()
            cur.execute("""INSERT INTO tasks(Task,
             Category,
              Priority,
               Deadline) VALUES(?, ?, ?, ?);""",
                        (csv_data[self.row + 1][0], csv_data[self.row + 1][1], csv_data[self.row + 1][2],
                         csv_data[self.row + 1][3]))
            conn.commit()
            del csv_data[self.row + 1]
            os.remove('records.csv')
            for i in range(len(csv_data)):
                with open("records.csv", mode="a", encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow(csv_data[i])

    def fun_delete_task(self):
        '''
        Функция  которая обрабатывает нажатие на таблицу
        '''
        self.row_del = self.tableWidget.currentRow()
        if self.row_del <= -1:
            question = QMessageBox()
            question.setWindowTitle('Планировщик')
            question.setText('Чтобы удалить запись нажмите на название задачи')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            question.exec_()
        if self.row_del > -1:
            question = QMessageBox()
            question.setWindowTitle('Планировщик')
            question.setText('Вы действительно хотите удалить задачу?')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            question.buttonClicked.connect(self.button_actions_fun_delete_task)
            question.exec_()

    def button_actions_fun_delete_task(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки.
        И при нажатии  кнопки ОК удаляет данные из таблицы records.csv
        '''
        if btn.text() == 'OK':
            self.tableWidget.removeRow(self.row_del)
            self.tableWidget.selectionModel().clearCurrentIndex()
            with open("records.csv", mode="r", encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
                csv_data = list(reader)
            del csv_data[self.row_del + 1]
            os.remove('records.csv')
            for i in range(len(csv_data)):
                with open("records.csv", mode="a", encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow(csv_data[i])

    def fun_clear_table(self):
        '''
        Функция которая создает QMessageBox
        '''
        question = QMessageBox()
        question.setWindowTitle('Планировщик')
        question.setText('Вы действительно хотите очистить таблицу?')
        question.setIcon(QMessageBox.Information)
        question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        question.buttonClicked.connect(self.button_status)
        question.exec_()

    def button_status(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки.
        И при нажатии  кнопки ОК удаляет таблицу records.csv
        '''
        if btn.text() == 'OK':
            file_path = "records.csv"
            if os.path.exists(file_path):
                os.remove(file_path)
                with open(file_path, mode="a", encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow(["Задача", "Категория", "Приоритет", "Кол-во дней до дедлайна"])
                    self.tableWidget.setRowCount(0)

    def create_table(self):
        '''
        Функция которая сортирует таблицу
        '''
        self.sort = self.sorting.currentText()
        file_path = "records.csv"
        if not (os.path.exists(file_path)) or os.stat(file_path).st_size == 0:
            with open("records.csv", mode="a", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                file_writer.writerow(["Задача", "Категория", "Приоритет", "Кол-во дней до дедлайна"])
                self.tableWidget.setRowCount(0)

        with open('records.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            data = []
            for row in reader:
                data.append(row)
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(data[0]))
            self.tableWidget.setHorizontalHeaderLabels(data[0])

        if self.sort == 'Без сортировки':
            for i in range(1, len(data)):
                for j in range(len(data[i])):
                    item = QTableWidgetItem(data[i][j])
                    self.tableWidget.setItem(i - 1, j, item)
        else:
            if self.sort == 'По лексикографическому порядку':
                sort_sp = sorted(data[1:], key=lambda row: row[0], reverse=False)
            elif self.sort == 'По категориям':
                sort_sp = sorted(data[1:], key=lambda row: row[1], reverse=False)
            elif self.sort == 'По приоритету':
                sort_sp = sorted(data[1:], key=lambda x: 0 if x[2] == 'Низкий' else (1 if x[2] == 'Средний' else 2))
            sort_sp.insert(0, data[0])
            for i in range(1, len(sort_sp)):
                for j in range(len(sort_sp[i])):
                    item = QTableWidgetItem(sort_sp[i][j])
                    self.tableWidget.setItem(i - 1, j, item)

    def fun_add_an_entry(self):
        '''
        Функция которая проверяет правильность вводимых пользователем данных
        '''
        self.priority = self.priority_combo.currentText()
        self.category = self.category_edit.toPlainText()
        self.task = self.task_edit.toPlainText()
        self.data = self.calendarWidget.selectedDate().getDate()
        self.data = (date(self.data[0], self.data[1], self.data[2]))
        today_date = date.today()
        self.difference_days = (self.data - today_date).days
        if self.category == '' and self.task != '':
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы не написали категорию задачи')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            question.exec_()
        elif self.category != '' and self.task == '':
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы не написали задачу')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            question.exec_()
        elif self.category == '' and self.task == '':
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы ввели не все поля.')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            question.exec_()
        else:
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы точно хотитие добавить запись?')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            question.buttonClicked.connect(self.processing_button_actions)
            question.exec_()

    def processing_button_actions(self, btn):
        '''
        Функция которая обрабатывает нажатие кнопки.
        И при нажатии  кнопки ОК записывает данные в таблицу records.csv
        '''
        if btn.text() == 'OK':
            if self.difference_days < 0:
                with open("records.csv", mode='a', encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow([self.task, self.category, self.priority, 'дедлайн прошёл'])
            elif self.difference_days == 0:
                with open("records.csv", mode='a', encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow([self.task, self.category, self.priority, 'дедлайн сегодня'])
            else:
                with open("records.csv", mode='a', encoding='utf-8') as w_file:
                    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                    file_writer.writerow([self.task, self.category, self.priority, self.difference_days])
        self.category_edit.setPlainText('')
        self.task_edit.setPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = class_password_login_request()
    ex.show()
    sys.exit(app.exec_())
