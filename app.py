import sys

from ui_main import Ui_ErrorMassage
from ui_main import Ui_MainWindow
from ui_main import Ui_SearchPassword
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
import json
from password_generator import PasswordGenerator

# Load Requirements
with open('requirements.txt') as f:
    requirements = f.readlines()

# Creating the class for the main window
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_add.clicked.connect(self.add_password) # Adding action to when the add button is clicked
        self.ui.bt_password.clicked.connect(self.generate_password_open) # Adding action to when the generate password button is clicked
        self.ui.bt_sp.clicked.connect(self.search_password) # Adding action to when the search password button is clicked
        self.setWindowIcon(QIcon("\Icon.png")) # Setting window Icon

# Function for the error pop up window
    def show_error_massage(self, massage):
        self.window = QMainWindow()
        self.error = Ui_ErrorMassage()
        self.error.setupUi(self.window)
        self.window.show()
        self.error.lb_em.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">{massage}</span></p></body></html>")
        self.window.setWindowIcon(QIcon("Icon.png"))

# Function to add a password with json
    def add_password(self):
        website = self.ui.et_website.text().title() # Getting the text in the entry
        email = self.ui.et_email.text()
        password = self.ui.et_password.text()

# Adding password dic to the json file
        new_password = {
            website: {
                "email": email,
                "password": password
            }
        }
        if len(website) == 0 or len(email) == 0 or len(password) ==0:
            Window.show_error_massage(self, "Please make sure you haven't left any fild empty")
            pass
        else:
            try:
                with open('Passwords.json', 'r') as f:
                    data = json.load(f)
                    data.update(new_password)
                with open('Passwords.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
            except:
                with open('Passwords.json', 'w', encoding='utf-8') as f:
                    json.dump(new_password, f, indent=4)

        self.ui.et_password.setText("")
        self.ui.et_website.setText("")
        if self.ui.keep_check.isChecked():
            pass
        else:
            self.ui.et_email.setText("")

# Opening the password generator
    def generate_password_open(self):
        self.password_generator = PasswordGenerator()
        self.password_generator.show()

# Loading the password from the json file and displaying it
    def search_password(self):

        website = self.ui.et_website.text().title()

        try:
            with open('Passwords.json') as f:
                data = json.load(f)
                if website in data:
                    email = data[website]['email']
                    password = data[website]['password']
                    self.window = QMainWindow()
                    self.sp = Ui_SearchPassword()
                    self.sp.setupUi(self.window)
                    self.window.show()
                    self.sp.in_ema.setText(
                        f"<html><head/><body><span style=\" color:#ffffff;\">{email}</span></p></body></html>")
                    self.sp.in_web.setText(
                        f"<html><head/><body><span style=\" color:#ffffff;\">{website}</span></p></body></html>")
                    self.sp.in_pass.setText(
                        f"<html><head/><body><span style=\" color:#ffffff;\">{password}</span></p></body></html>")
                    self.window.setWindowIcon(QIcon("Icon.png"))

                else:
                    Window.show_error_massage(self, "Couldn't find any password in this website")
        except:
            Window.show_error_massage(self, "Couldn't find any password in this website")

#Creating main window and showing it
app = QApplication(sys.argv)
window = Window()
window.show()


sys.exit(app.exec())