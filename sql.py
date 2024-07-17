import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('sales.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE employee(Name VARCHAR(255), Target_sales DECIMAL(10, 2), Target_achieved DECIMAL(5, 2));"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO employee VALUES ('Tony', '75000', '100')''') 
cursor.execute('''INSERT INTO employee VALUES ('Bruce', '69000', '85')''') 
cursor.execute('''INSERT INTO employee VALUES ('Clark', '75000', '59.3')''') 
cursor.execute('''INSERT INTO employee VALUES ('Steve', '72000', '72.6')''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM employee''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()
