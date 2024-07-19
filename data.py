import csv
import sqlite3

# Define database and CSV file paths
db_file = "fighter.db"
csv_file = "fighters.csv"

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table (assuming the CSV file has matching column names)
table = """CREATE TABLE IF NOT EXISTS profile(
             NAME VARCHAR(255),
             WON DECIMAL(10, 2),
             LOST DECIMAL(10, 2),
             DRAW DECIMAL(10, 2),
             KO_RATE VARCHAR(255),
             STANCE VARCHAR(255),
             AGE VARCHAR(255),
             COUNTRY VARCHAR(255)
             );"""
cursor.execute(table)

# Check if table is empty
cursor.execute("SELECT COUNT(*) FROM profile")
with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    insert_statement = '''INSERT INTO profile (NAME, WON, LOST, DRAW, KO_RATE, STANCE, AGE, COUNTRY) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    for row in csv_reader:
        data_to_insert = (row['NAME'], row['WON'], row['LOST'], row['DRAW'], row['KO_RATE'], row['STANCE'], row['AGE'], row['COUNTRY'])
        cursor.execute(insert_statement, data_to_insert)

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM profile''') 
for row in data: 
   print(row) 

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Data inserted.")