import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_PasswordGenerator
from PySide6.QtGui import QIcon
import string
import random

password = ""

# Password Generator main window
class PasswordGenerator(QMainWindow):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.ui = Ui_PasswordGenerator()
        self.ui.setupUi(self)
        self.slide_spinbox_password_connector()
        self.ui.btn_select.clicked.connect(self.copy_password) # Adding action to when the select button is clicked
        self.setWindowIcon(QIcon("\Icon.png"))  # Setting window Icon

    def generate_password(self):
        password_characters = ""
        buttons = [self.ui.btn_az, self.ui.btn_AZ, self.ui.btn_09, self.ui.btn_symbols]
        chars = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
        for button in buttons:
            if button.isChecked():
                index = buttons.index(button)
                password_characters += chars[index]
            else:
                pass

        length = self.ui.spin_lenght.value()
        try:
            password = ''.join(random.choice(password_characters) for i in range(length))
        except:
            self.ui.line_password.setText("")
        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        self.ui.line_password.setText(password)

# Function to connect the slider, spin and the generate password function
    def slide_spinbox_password_connector(self) -> None:
        self.ui.slider_lenght.valueChanged.connect(self.ui.spin_lenght.setValue)
        self.ui.spin_lenght.valueChanged.connect(self.ui.slider_lenght.setValue)
        self.ui.spin_lenght.valueChanged.connect(self.generate_password)

# Function to copy the password from the entry to the clipboard
    def copy_password(self):
        generated_password = self.ui.line_password.text()
        QApplication.clipboard().setText(generated_password)
