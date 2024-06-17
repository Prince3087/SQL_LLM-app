import sqlite3

##Connect to sqlite
connection=sqlite3.connect("student.db")


##Create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

##Insert some more records

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',100)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',87)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',56)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Dipesh', 'Data Analyst', 'A',35)''')

##Display all the records
print("The inserted records are")


data=cursor.execute(''' Select * From STUDENT''')

for row in data:
    print(row)

##Close the connection
connection.commit()
connection.close()

