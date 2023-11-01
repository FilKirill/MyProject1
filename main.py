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
    <width>371</width>
    <height>223</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>371</width>
      <height>221</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="0" column="0">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Регистрация&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Имя      &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QLineEdit" name="name_edit"/>
     </item>
     <item row="2" column="0">
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Логин&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QLineEdit" name="login_edit"/>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Пароль                  &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="3" column="1">
      <widget class="QLineEdit" name="password_edit"/>
     </item>
     <item row="4" column="0">
      <widget class="QLabel" name="label_6">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:10pt;&quot;&gt;Повторите пароль&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="4" column="1">
      <widget class="QLineEdit" name="replay_password_edit"/>
     </item>
     <item row="5" column="0" colspan="2">
      <widget class="QPushButton" name="button_complete_registration">
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

window_adding_record = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>646</width>
    <height>422</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>20</y>
      <width>141</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Напишите дату дедлайна</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>20</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Выберите уровень приоритета</string>
    </property>
   </widget>
   <widget class="QComboBox" name="priority">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>90</y>
      <width>171</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Напишите запись</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="text_entry">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>90</y>
      <width>211</width>
      <height>131</height>
     </rect>
    </property>
   </widget>
   <widget class="QDateEdit" name="dateEdit">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>90</y>
      <width>161</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>270</y>
      <width>591</width>
      <height>141</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout" stretch="10,0,10">
     <item>
      <widget class="QPushButton" name="return_home_screen">
       <property name="text">
        <string>Вернутся на главный экран</string>
       </property>
      </widget>
     </item>
     <item>
      <spacer name="horizontalSpacer">
       <property name="orientation">
        <enum>Qt::Horizontal</enum>
       </property>
       <property name="sizeHint" stdset="0">
        <size>
         <width>40</width>
         <height>20</height>
        </size>
       </property>
      </spacer>
     </item>
     <item>
      <widget class="QPushButton" name="add_an_entry">
       <property name="text">
        <string>Добавить запись </string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>646</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""

main_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>616</width>
    <height>346</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(0, 85, 0);
background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>20</y>
      <width>481</width>
      <height>61</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:22pt;&quot;&gt;Добро пожаловать в планировщик&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="wordWrap">
     <bool>false</bool>
    </property>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>80</y>
      <width>341</width>
      <height>201</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QPushButton" name="pushButton_2">
       <property name="styleSheet">
        <string notr="true">alternate-background-color: rgb(255, 255, 255);
border-color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>Добавить запись</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="pushButton">
       <property name="text">
        <string>Посмотреть записи</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>616</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''

table_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>710</width>
    <height>484</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>5</x>
      <y>1</y>
      <width>691</width>
      <height>421</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>420</y>
      <width>261</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Вернуться на главный экран</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>710</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
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
    <width>364</width>
    <height>292</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>321</width>
      <height>111</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_4">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>Логин                 </string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="login_input"/>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout_3">
       <item>
        <widget class="QLabel" name="label_2">
         <property name="text">
          <string>Пароль               </string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="entering_password"/>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:11pt;&quot;&gt;Вход&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>250</y>
      <width>331</width>
      <height>25</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_5">
     <item>
      <widget class="QLabel" name="label_4">
       <property name="text">
        <string>Ещё не зарегестрированы ?</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="registration_button">
       <property name="text">
        <string>Регистрация</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="login_button">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>210</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>180</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;img src=&quot;:/newPrefix/asd.jpg&quot;/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>160</y>
      <width>81</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string> Код с картинки</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="input_cod">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>160</y>
      <width>231</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources>
  <include location="капча.webp"/>
 </resources>
 <connections/>
</ui>'''


class class_user_registration(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(registration_window)
        uic.loadUi(f, self)


class class_password_login_request(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(password_login_request_window)
        uic.loadUi(f, self)
        self.registration_button.clicked.connect(self.open_registration_window)

    def open_registration_window(self):
        self.w2 = class_user_registration()
        self.w2.show()
        self.close()


class Adding_entry(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(window_adding_record)
        uic.loadUi(f, self)
        self.priority.addItem("Низкий")
        self.priority.addItem("Средний")
        self.priority.addItem("Высокий")
        self.text = self.text_entry.text()
        self.return_home_screen.clicked.connect(self.show_Main_screen)
        self.add_an_entry.clicked.connect(self.pop_up_windows)

    def show_Main_screen(self):
        self.w2 = Main_screen()
        self.w2.show()
        self.close()

    def pop_up_windows(self):
        question = QMessageBox()
        question.setWindowTitle('Запись')
        question.setText('Вы точно хотите добавить запись?')
        question.setIcon(QMessageBox.Information)
        question.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)
        question.buttonClicked.connect(self.processing_button_actions)
        question.exec_()

    def processing_button_actions(self, btn):
        if btn.text() == 'Ok':
            pass
        elif btn.text() == 'Reset':
            self.lineEdit.setText('')


class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(main_window)
        uic.loadUi(f, self)
        self.pushButton_2.clicked.connect(self.show_Adding_entry)
        self.pushButton.clicked.connect(self.show_Table_window)

    def show_Adding_entry(self):
        self.w2 = Adding_entry()
        self.w2.show()
        self.close()

    def show_Table_window(self):
        self.w3 = Table_window()
        self.w3.show()
        self.close()


class Table_window(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(table_window)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.go_over_Main_screen)

    def go_over_Main_screen(self):
        self.w2 = Main_screen()
        self.w2.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = class_password_login_request()
    ex.show()
    sys.exit(app.exec_())
