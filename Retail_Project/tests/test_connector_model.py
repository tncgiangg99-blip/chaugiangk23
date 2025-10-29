import traceback

import mysql.connector

from Retail_Project.model.customer import Customer

server="localhost"
port=3306
database="k234161830_retail"
username="root"

password="@Obama123"
try:
    conn = mysql.connector.connect(
                    host=server,
                    port=port,
                    database=database,
                    user=username,
                    password=password)
except:
    traceback.print_exc()
#1. Đăng nhập
def log_in (email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
      "where Email='"+email+"' and Password='"+pwd+"'"
    cust = None
    cursor.execute(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        cust = Customer()
        print("ID ==",dataset[0],dataset[1],dataset[2],dataset[3],dataset[4],dataset[5])
        cust.ID,cust.Name, cust.Phone, cust.Email, cust.Password, cust.IsDeleted = dataset
    else:
        print("Login failed")
    cursor.close()
    return cust
cust = log_in ("a.nguyen@example.com","pass123A")
if cust == None:
    print("Login failed")
else:
    print("Login succeeded")
    print(cust)
