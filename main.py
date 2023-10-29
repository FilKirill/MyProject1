import sys
import io
import datetime

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>646</width>
    <height>433</height>
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
   <widget class="QComboBox" name="comboBox">
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
   <widget class="QLineEdit" name="lineEdit">
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

template2 = '''<?xml version="1.0" encoding="UTF-8"?>
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

template3 = '''<?xml version="1.0" encoding="UTF-8"?>
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


class Adding_entry(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.comboBox.addItem("Низкий")
        self.comboBox.addItem("Средний")
        self.comboBox.addItem("Высокий")
        self.text = self.lineEdit.text()
        self.return_home_screen.clicked.connect(self.show_Main_screen)
        self.add_an_entry.clicked.connect(self.entry)

    def show_Main_screen(self):
        self.w2 = Main_screen()
        self.w2.show()
        self.close()

    def adding_value_to_table(self):
        priority_level = self.comboBox.currentText()



class Main_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template2)
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
        f = io.StringIO(template3)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.go_over_Main_screen)

    def go_over_Main_screen(self):
        self.w2 = Main_screen()
        self.w2.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_screen()
    ex.show()
    sys.exit(app.exec_())
