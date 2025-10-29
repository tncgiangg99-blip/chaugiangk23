from Retail_Project.connectors.employee_connector import EmployeeConnector
from Retail_Project.model.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.EmployeeCode = "EMP888"
emp.Name = "Doramon"
emp.Phone = "0123456789"
emp.Email = "dora@gmail.com"
emp.Password = "456"
emp.IsDeleted = 0
result = ec.insert_one_employee(emp)
if result>0:
    print("Inserted Employee successfully")
else:
    print("That dang thuong")
