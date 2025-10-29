import traceback

import mysql.connector
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
print("Continue")
#1. Đăng nhập
def log_in (email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * FROM customer " \
      "where Email='"+email+"' and Password='"+pwd+"'"
    cursor.execute(sql)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed")
    cursor.close()
log_in ("a.nguyen@example.com","pass123A")

def login_emp(email,pwd):
    cursor = conn.cursor()
    sql = "SELECT * from employee where Email = %s and Password = %s"
    val =(email,pwd)
    cursor.execute(sql,val)
    dataset = cursor.fetchone()
    if dataset != None:
        print(dataset)
    else:
        print("Login failed")
    cursor.close()
login_emp("Omaba@gmail.com","123")