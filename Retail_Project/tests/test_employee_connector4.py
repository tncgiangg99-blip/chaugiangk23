from Retail_Project.connectors.employee_connector import EmployeeConnector
from Retail_Project.model.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.ID = 3

result = ec.delete_one_employee(emp)
if result>0:
    print("xóa Employee successfully")
else:
    print("That dang thuong")
