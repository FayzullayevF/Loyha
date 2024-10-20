import os
os.system("clear")

from PyQt5.QtWidgets import *
from Service import *
from User import *
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("LOYHA")
        self.vertical_main_layout = QVBoxLayout()
        self.ism_horizontal_layout = QHBoxLayout()
        self.sharif_horizontal_layout = QHBoxLayout()
        self.yosh_horizontal_layout = QHBoxLayout()
        self.jins_vertical_layout = QVBoxLayout()
        self.viloyat_horizontal_layout = QHBoxLayout()
        self.telefon_horizontal_layout = QHBoxLayout()
        self.fakultet_horizontal_layout = QHBoxLayout()
        self.kurs_horizontal_layout = QHBoxLayout()
        self.saqlash_horizontal_layout = QHBoxLayout()

        self.ism_label = QLabel("ISM:")
        self.ism_lineEdit = QLineEdit()
        self.ism_lineEdit.setPlaceholderText(" Ismingizni kiriting...")
        
        self.sharif_label = QLabel("SHARIF:")
        self.sharif_lineEdit = QLineEdit()
        self.sharif_lineEdit.setPlaceholderText(" Sharifingizni kiriting...")
        
        self.yosh_label = QLabel("YOSH:")
        self.yosh_lineEdit = QLineEdit()   
        self.yosh_lineEdit.setPlaceholderText(" Yoshingizni kiriting...")
        
        self.jins_radiobutton = QRadioButton("ERKAK") 
        self.jins1_radiobutton = QRadioButton("AYOL") 
        
        self.viloyat_label = QLabel("VILOYAT:")
        self.viloyat_comboBox = QComboBox()
        self.viloyat_comboBox.addItems(["Viloyat tanlang","Andijon viloyati", "Buxoro viloyati", "Farg'ona viloyati", "Jizzax viloyati", "Namangan viloyati","Navoiy viloyati", "Qashqadaryo viloyati","Samarqand viloyati","Sirdaryo viloyati","Surxandaryo viloyati", "Toshkent viloyati", "Toshkent shahri", "Xorazm viloyati","Qoraqalpog'iston Respublikasi"])
        
        self.nomer_label = QLabel("TELEFON:")
        self.nomer_lineEdit = QLineEdit()
        self.nomer_lineEdit.setPlaceholderText(" Raqamingizni kiriting...")
        
        self.fakultet_label = QLabel("FAKULTET:")
        self.fakultet_lineEdit = QLineEdit()
        self.fakultet_lineEdit.setPlaceholderText(" Fakultetingizni kiriting...")
        
        self.kurs_label = QLabel("KURS:")
        self.kurs_comboBox = QComboBox()
        self.kurs_comboBox.addItems(["1-kurs","2-kurs","3-kurs","4-kurs"])
        
        self.saqlash_button = QPushButton("SAQLASH")
        self.saqlash_button.clicked.connect(self.Saqlash)

        self.ism_horizontal_layout.addWidget(self.ism_label)
        self.ism_horizontal_layout.addWidget(self.ism_lineEdit)
        
        self.sharif_horizontal_layout.addWidget(self.sharif_label)
        self.sharif_horizontal_layout.addWidget(self.sharif_lineEdit)
        
        self.yosh_horizontal_layout.addWidget(self.yosh_label)
        self.yosh_horizontal_layout.addWidget(self.yosh_lineEdit)
        
        self.jins_vertical_layout.addWidget(self.jins_radiobutton)
        self.jins_vertical_layout.addWidget(self.jins1_radiobutton)
        
        self.viloyat_horizontal_layout.addWidget(self.viloyat_label)
        
        self.telefon_horizontal_layout.addWidget(self.nomer_label)
        self.telefon_horizontal_layout.addWidget(self.nomer_lineEdit)
        
        self.fakultet_horizontal_layout.addWidget(self.fakultet_label)
        self.fakultet_horizontal_layout.addWidget(self.fakultet_lineEdit)
        
        self.kurs_horizontal_layout.addWidget(self.kurs_label)
        
        self.saqlash_horizontal_layout.addWidget(self.saqlash_button)
    
        self.vertical_main_layout.addLayout(self.ism_horizontal_layout)
        self.vertical_main_layout.addLayout(self.sharif_horizontal_layout)
        self.vertical_main_layout.addLayout(self.yosh_horizontal_layout)
        self.vertical_main_layout.addLayout(self.jins_vertical_layout)
        self.vertical_main_layout.addLayout(self.viloyat_horizontal_layout)
        self.vertical_main_layout.addWidget(self.viloyat_comboBox)
        self.vertical_main_layout.addLayout(self.telefon_horizontal_layout)
        self.vertical_main_layout.addLayout(self.fakultet_horizontal_layout)
        self.vertical_main_layout.addLayout(self.kurs_horizontal_layout)
        self.vertical_main_layout.addWidget(self.kurs_comboBox)
        self.vertical_main_layout.addLayout(self.saqlash_horizontal_layout)  
        
        self.setLayout(self.vertical_main_layout)
        
        
    def Saqlash(self):
        
        currentUser = User(self.ism_lineEdit.text(),
                           self.sharif_lineEdit.text(),
                           self.nomer_lineEdit.text(),
                           self.yosh_lineEdit.text(),
                           self.fakultet_lineEdit.text(),
                           self.viloyat_comboBox.currentIndex(),
                           "None",
                           self.kurs_comboBox.currentIndex(),
                           self.jins_radiobutton.isChecked(),
                           self.jins1_radiobutton.isChecked()
                           ) 
        answer = Service.check_info(currentUser)
        if answer != None:
            self.ism_lineEdit.clear()
            self.sharif_lineEdit.clear()
            self.yosh_lineEdit.clear()
            self.nomer_lineEdit.clear()
            self.fakultet_lineEdit.clear()
            self.Error_info = QMessageBox()
            self.Error_info.setIcon(QMessageBox.Warning)
            self.Error_info.setText(answer) 
            self.Error_info.exec_()
        else:
            self.Suc_info = QMessageBox()
            self.Suc_info.setText("Ma'lumotlar faylga muvofaqiyatli yuklandi 🙂 ") 
            self.Suc_info.exec_()
            

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()