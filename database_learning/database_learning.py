import sqlite3
from employee import Employee


conn = sqlite3.connect('spanish.db')
c = conn.cursor()

emp1 = Employee('John', 'Doe', 80000)
emp2 = Employee('Jane', 'Doe', 90000)
emp3 = Employee('Bill', 'Wicky', 90000)
emp4 = Employee('Neil', 'Johnson', 90000)
emp5 = Employee('Jenny', 'Polo', 90000)

c.execute('DROP TABLE employees')
c.execute("CREATE TABLE employees(first text, last text, pay integer)")
c.execute("INSERT INTO employees VALUES(?,?,?)", (emp1.first,emp1.last,emp1.pay))
c.execute("INSERT INTO employees VALUES(?,?,?)", (emp2.first,emp2.last,emp2.pay))
c.execute("INSERT INTO employees VALUES(?,?,?)", (emp3.first,emp3.last,emp3.pay))
c.execute("INSERT INTO employees VALUES(?,?,?)", (emp4.first,emp4.last,emp4.pay))
c.execute("INSERT INTO employees VALUES(?,?,?)", (emp5.first,emp5.last,emp5.pay))
conn.commit()

c.execute("SELECT last FROM employees WHERE first='John'")


conn.close()