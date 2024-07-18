import csv
import sqlite3

# Define database and CSV file paths
db_file = "test2.db"
csv_file = "testing_data.csv"

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table (assuming the CSV file has matching column names)
table = """CREATE TABLE IF NOT EXISTS salesrec(
             Name VARCHAR(255),
             Target_sales DECIMAL(10, 2),
             Target_achieved DECIMAL(5, 2)
             );"""
cursor.execute(table)

# Check if table is empty
cursor.execute("SELECT COUNT(*) FROM salesrec")
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    insert_statement = '''INSERT INTO salesrec (Name, Target_sales, Target_achieved) VALUES (?, ?, ?)'''
    for row in csv_reader:
        data_to_insert = (row['Name'], row['Target_sales'], row['Target_achieved'])
        cursor.execute(insert_statement, data_to_insert)

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM salesrec''') 
for row in data: 
   print(row) 

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Data inserted.")