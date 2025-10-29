from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Retail_Project.UI.EmployeeMainWindowEx import EmployeeMainWindow
from Retail_Project.UI.LoginMainWindow import Ui_MainWindow
from Retail_Project.connectors.employee_connector import EmployeeConnector


class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.button_login.clicked.connect(self.process_login)
    def process_login(self):
        email=self.le_email.text()
        password=self.le_password.text()
        ec = EmployeeConnector()
        ec.connect()
        em = ec.login(email,password)

        if em == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login failed,pls check ur account again")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
           self.gui_emp = EmployeeMainWindow()
           self.gui_emp.setupUi(QMainWindow())
           self.gui_emp.showWindow()
           self.MainWindow.close()