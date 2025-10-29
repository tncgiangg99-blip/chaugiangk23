from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush
from PyQt6.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox

from Retail_Project.UI.EmployeeMainWindow import Ui_MainWindow
from Retail_Project.connectors.employee_connector import EmployeeConnector
from Retail_Project.model.employee import Employee


class EmployeeMainWindow(Ui_MainWindow):
    def __init__(self):
        self.ec = EmployeeConnector()
        self.ec.connect()
        self.is_completed = False
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.displayEmployeesIntoTable()
        self.is_completed = True
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def displayEmployeesIntoTable(self):
        self.employees = self.ec.get_all_employee()
        self.tableWidget.setRowCount(0)
        for emp in self.employees:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            item_id = QTableWidgetItem(str(emp.ID))
            self.tableWidget.setItem(row, 0, item_id)
            if emp.IsDeleted ==1:
                item_id.setBackground(Qt.GlobalColor.red)
            item_code = QTableWidgetItem(str(emp.EmployeeCode))
            self.tableWidget.setItem(row, 1, item_code)
            item_name = QTableWidgetItem(str(emp.Name))
            self.tableWidget.setItem(row, 2, item_name)
            item_phone = QTableWidgetItem(str(emp.Phone))
            self.tableWidget.setItem(row, 3, item_phone)
            item_email = QTableWidgetItem(str(emp.Email))
            self.tableWidget.setItem(row, 4, item_email)
    def setupSignalAndSlot(self):
        self.pushButton_new.clicked.connect(self.clear_all)
        self.tableWidget.itemSelectionChanged.connect(self.show_detail)
        self.pushButton_save.clicked.connect(self.save_employee)
        self.pushButton_update.clicked.connect(self.update_employee)
        self.pushButton_delete.clicked.connect(self.delete_employee)
    def clear_all(self):
        self.le_id.clear()
        self.le_name.clear()
        self.le_code.clear()
        self.le_phone.clear()
        self.le_email.clear()
        self.le_phone.clear()
        self.le_id.setFocus()
    def show_detail(self):
        if self.is_completed == False:
            return
        row_index = self.tableWidget.currentIndex()
        print("you clicked at", row_index.row())
        id = self.tableWidget.item(row_index.row(), 0).text()
        print("Employee ID:", id)
        emp = self.ec.get_detail_infor(id)
        if emp != None:
            self.le_id.setText(str(emp.ID))
            self.le_code.setText(str(emp.EmployeeCode))
            self.le_name.setText(str(emp.Name))
            self.le_phone.setText(str(emp.Phone))
            self.le_email.setText(str(emp.Email))
        if emp.IsDeleted == 1:
            self.checkBox.setChecked(True)
    def save_employee(self):
        self.is_completed = False
        emp = Employee()
        emp.EmployeeCode = self.le_code.text()
        emp.Name = self.le_name.text()
        emp.Phone = self.le_phone.text()
        emp.Email = self.le_email.text()
        emp.Password = self.le_password.text()
        emp.IsDeleted = self.checkBox.isChecked()
        result = self.ec.insert_one_employee(emp)
        if result > 0:
            self.displayEmployeesIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Hahaha lỗi tè le")
            msg.setWindowTitle("Mẹ ơi con thất bại rồi")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        self.is_completed = True
    def update_employee(self):
        self.is_completed = False
        emp = Employee()
        emp.EmployeeCode = self.le_code.text()
        emp.ID = self.le_id.text()
        emp.Name = self.le_name.text()
        emp.Phone = self.le_phone.text()
        emp.Email = self.le_email.text()
        emp.Password = self.le_password.text()
        if self.checkBox.isChecked() == True:
            emp.IsDeleted = 1
        else:
            emp.IsDeleted = 0

        result = self.ec.update_one_employee(emp)
        if result > 0:
            self.displayEmployeesIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Hahaha lỗi tè le")
            msg.setWindowTitle("Mẹ ơi con thất bại rồi")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
        self.is_completed = True
    def delete_employee(self):
        self.is_completed = False
        emp = Employee()
        emp.ID = self.le_id.text()

        if self.checkBox.isChecked() == True:
            emp.IsDeleted = 1
        else:
            emp.IsDeleted = 0

        result = self.ec.delete_one_employee(emp)
        if result > 0:
            self.displayEmployeesIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Hahaha lỗi tè le")
            msg.setWindowTitle("Mẹ ơi con thất bại rồi")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()