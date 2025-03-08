import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QRadioButton,
    QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QGroupBox
)
from PyQt5.QtGui import QPalette, QColor

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2")
        self.resize(500, 400) 
        self.initUI()
        self.setStyle()
        
        # Owner
    def initUI(self):
        main_layout = QVBoxLayout()

        identity_box = QGroupBox("OWNER")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama  : Andi Sibwayiq Abi Mahmud"))
        identity_layout.addWidget(QLabel("NIM   : F1D022002"))
        identity_layout.addWidget(QLabel("Kelas : Pemrograman Visual"))
        identity_box.setLayout(identity_layout)
        main_layout.addWidget(identity_box)

        # Navigation 
        nav_box = QGroupBox("NAVIGATION")
        nav_layout = QHBoxLayout()
        home_btn = QPushButton("HOME")
        about_btn = QPushButton("ABOUT")
        contact_btn = QPushButton("CONTACT")
        
        home_btn.setStyleSheet("background-color: lightblue;")
        about_btn.setStyleSheet("background-color: lightgreen;")
        contact_btn.setStyleSheet("background-color: lightcoral;")
        
        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(about_btn)
        nav_layout.addWidget(contact_btn)
        nav_box.setLayout(nav_layout)
        main_layout.addWidget(nav_box)

        # Registration
        form_box = QGroupBox("REGISTRATION HERE")
        form_layout = QVBoxLayout()
        
        form_layout.addWidget(QLabel("Full Name:"))
        form_layout.addWidget(QLineEdit())
        
        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(QLineEdit())
        
        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(QLineEdit())
        
        form_layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QRadioButton("Male"))
        gender_layout.addWidget(QRadioButton("Female"))
        form_layout.addLayout(gender_layout)

        form_layout.addWidget(QLabel("Country:"))
        country_dropdown = QComboBox()
        country_dropdown.addItems(["Select", "Indonesia", "Malaysia", "Singapore", "JApan", "Korea", "China", "USA", "UK", "Australia"])
        form_layout.addWidget(country_dropdown)
        
        form_box.setLayout(form_layout)
        main_layout.addWidget(form_box)

        # Action 
        action_box = QGroupBox("ACTION")
        action_layout = QHBoxLayout()
        success_button = QPushButton("SUCCES")
        cancel_button = QPushButton("CANCEL")
        
        success_button.setFixedSize(120, 40)
        cancel_button.setFixedSize(120, 40)
        
        success_button.setStyleSheet("background-color: lightgreen; border: 1px solid green;")
        cancel_button.setStyleSheet("background-color: lightcoral; border: 1px solid red;")
        
        action_layout.addWidget(success_button)
        action_layout.addWidget(cancel_button)
        action_box.setLayout(action_layout)
        main_layout.addWidget(action_box)

        self.setLayout(main_layout)

    def setStyle(self):
        palette = self.palette()
        # palette.setColor(QPalette.Window, QColor("brown"))  
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
