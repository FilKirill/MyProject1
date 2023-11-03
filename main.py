import sys
import io
import datetime
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

registration_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>330</height>
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
      <y>0</y>
      <width>511</width>
      <height>331</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>на регистрацию.jpg</pixmap>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>50</y>
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
 <resources/>
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
    <width>653</width>
    <height>601</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(122, 122, 122);
background-color: rgb(179, 179, 179);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTabWidget" name="tabWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>651</width>
      <height>601</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(179, 179, 179);</string>
    </property>
    <property name="currentIndex">
     <number>0</number>
    </property>
    <widget class="QWidget" name="tab">
     <attribute name="title">
      <string>Добавить задачу</string>
     </attribute>
     <layout class="QVBoxLayout" name="verticalLayout">
      <item>
       <widget class="QLabel" name="label_3">
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Выберите дату дедлайна в календаре&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QCalendarWidget" name="calendarWidget">
        <property name="styleSheet">
         <string notr="true">background-color: rgb(255, 255, 255);
background-color: rgb(85, 119, 134);</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Выберите уровень приоритета&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QComboBox" name="priority">
        <property name="styleSheet">
         <string notr="true">background-color: rgb(85, 119, 134);
background-color: rgb(255, 255, 255);</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_4">
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Напишите категорию задачи&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="category">
        <property name="styleSheet">
         <string notr="true">background-color: rgb(85, 119, 134);
background-color: rgb(255, 255, 255);</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLabel" name="label_5">
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:12pt;&quot;&gt;Напишите задачу&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="task">
        <property name="styleSheet">
         <string notr="true">background-color: rgb(255, 255, 255);</string>
        </property>
        <property name="text">
         <string/>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="add_an_entry">
        <property name="styleSheet">
         <string notr="true"> Background-color: rgb(59, 59, 59);
background-color: rgb(85, 119, 134);</string>
        </property>
        <property name="text">
         <string>Добавить задачу</string>
        </property>
       </widget>
      </item>
     </layout>
    </widget>
    <widget class="QWidget" name="tab_2">
     <attribute name="title">
      <string>Посмотреть задачи</string>
     </attribute>
     <widget class="QTableWidget" name="tableWidget">
      <property name="geometry">
       <rect>
        <x>-10</x>
        <y>40</y>
        <width>661</width>
        <height>481</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
     <widget class="QPushButton" name="updateButton">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>161</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 119, 134);</string>
      </property>
      <property name="text">
       <string>Обновить</string>
      </property>
     </widget>
     <widget class="QComboBox" name="sorting">
      <property name="geometry">
       <rect>
        <x>430</x>
        <y>0</y>
        <width>211</width>
        <height>31</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(255, 255, 255);</string>
      </property>
     </widget>
     <widget class="QLabel" name="label_6">
      <property name="geometry">
       <rect>
        <x>170</x>
        <y>0</y>
        <width>251</width>
        <height>31</height>
       </rect>
      </property>
      <property name="text">
       <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Выберите сортировку&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
     <widget class="QPushButton" name="download_table">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>530</y>
        <width>201</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 119, 134);</string>
      </property>
      <property name="text">
       <string>Скачать таблицу</string>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_3">
      <property name="geometry">
       <rect>
        <x>440</x>
        <y>530</y>
        <width>201</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgb(85, 119, 134);</string>
      </property>
      <property name="text">
       <string>Удалить задачу</string>
      </property>
     </widget>
    </widget>
   </widget>
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
    <width>501</width>
    <height>330</height>
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
      <x>-10</x>
      <y>-20</y>
      <width>511</width>
      <height>351</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>на регистрацию.jpg</pixmap>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>40</y>
      <width>371</width>
      <height>228</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="2" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Логин                 &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
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
     <item row="1" column="1" colspan="2">
      <widget class="QLineEdit" name="name_button">
       <property name="styleSheet">
        <string notr="true">border-color: rgb(170, 170, 0);</string>
       </property>
      </widget>
     </item>
     <item row="4" column="1" colspan="2">
      <widget class="QLineEdit" name="input_cod"/>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Код с картинки&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
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
     <item row="3" column="1" colspan="2">
      <widget class="QLineEdit" name="entering_password"/>
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
     <item row="1" column="0">
      <widget class="QLabel" name="label_7">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Имя&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
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
     <item row="2" column="1" colspan="2">
      <widget class="QLineEdit" name="login_input">
       <property name="styleSheet">
        <string notr="true"/>
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
    </layout>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>'''


class class_user_registration(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(registration_window)
        uic.loadUi(f, self)
        self.setWindowTitle('Регистрация пользователя')
        self.button_complete_registration.clicked.connect(self.registration_completed)
        self.come_back.clicked.connect(self.fun_come_back)

    def fun_come_back(self):
        self.w2 = class_password_login_request()
        self.w2.show()
        self.close()

    def registration_completed(self):
        self.name = self.name_edit.text()
        self.login = self.login_edit.text()
        self.password = self.password_edit.text()
        self.replay_password = self.replay_password_edit.text()

        if self.name != '' and self.login != '' and self.password != '' and self.password == self.replay_password:
            question = QMessageBox()
            question.setWindowTitle('регистрация')
            question.setText('Вы успешно зарегистрировались')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok)
            conn = sqlite3.connect('password.db')
            cur = conn.cursor()
            cur.execute("""INSERT INTO users(name, login, password) 
                                   VALUES(?, ?, ?);""", (self.name, self.login, self.password))
            conn.commit()
            question.exec_()
            self.w2 = class_password_login_request()
            self.w2.show()
            self.close()

        else:
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы неправильно ввели логин или пароль')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.name_edit.setText('')
            self.login_edit.setText('')
            self.password_edit.setText('')
            self.replay_password_edit.setText('')
            question.exec_()


class class_password_login_request(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(password_login_request_window)
        uic.loadUi(f, self)
        self.setWindowTitle('Вход пользователя')
        self.registration_button.clicked.connect(self.open_registration_window)
        self.login_button.clicked.connect(self.login_password_verification)

    def login_password_verification(self):
        name = self.name_button.text()
        login = self.login_input.text()
        password = self.entering_password.text()
        cod = self.input_cod.text()
        con = sqlite3.connect('password.db')
        cur = con.cursor()
        c = 0
        # Выполнение запроса и получение всех результатов
        result = cur.execute("""SELECT * From users""").fetchall()
        for i in result:
            if login in i and password in i and name in i:
                c += 1
        con.close()
        if cod == 'W68HP' and c > 0:
            self.w2 = Main_screen()
            self.w2.show()
            self.close()
        else:
            question = QMessageBox()
            question.setWindowTitle('Запись')
            question.setText('Вы неправильно ввели логин или пароль')
            question.setIcon(QMessageBox.Information)
            question.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.name_button.setText('')
            self.login_input.setText('')
            self.entering_password.setText('')
            self.input_cod.setText('')
            question.exec_()

    def open_registration_window(self):
        self.w2 = class_user_registration()
        self.w2.show()
        self.close()


class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(main_window)
        uic.loadUi(f, self)
        self.priority.addItem("Низкий")
        self.priority.addItem("Средний")
        self.priority.addItem("Высокий")
        self.add_an_entry.clicked.connect(self.fun_add_an_entry)

    def fun_add_an_entry(self):
        priority = self.priority.currentText()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_screen()
    ex.show()
    sys.exit(app.exec_())
