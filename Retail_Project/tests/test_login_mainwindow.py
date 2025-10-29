from PyQt6.QtWidgets import QApplication, QMainWindow

from Retail_Project.UI.LoginMainWindowEx import LoginMainWindowEx

app = QApplication([])
login_ui = LoginMainWindowEx()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()