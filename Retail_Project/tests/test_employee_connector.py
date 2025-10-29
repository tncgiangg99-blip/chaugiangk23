from Retail_Project.connectors.employee_connector import EmployeeConnector

ec = EmployeeConnector()
ec.connect()
em = ec.login("Omaba@gmail.com","123")

if em == None:
    print("Login failed?")
else:
    print("Login successful")
    print(em)
#tdxt
print("List of Emps")
ds = ec.get_all_employee()
print(ds)
for emp in ds:
    print(emp)

id = 3
emp=ec.get_detail_infor(id)
if emp==None:
    print("Ko co NV co ma =", id)
else:
    print("Tim thay nhan vien co ma=", id)
    print(emp)