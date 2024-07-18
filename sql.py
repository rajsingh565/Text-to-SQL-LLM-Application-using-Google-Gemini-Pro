import sqlite3

## Connecting to sqlite
connection=sqlite3. connect ("student.db")

## Creating a curosr object to insert record,create table,retrieve
cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENTS(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Insterting the records
cursor.execute('''Insert Into STUDENTS values('Raj','Data Science','O',98)''')
cursor.execute('''Insert Into STUDENTS values('Manoj','Web dev','E',84)''')
cursor.execute('''Insert Into STUDENTS values('Vishal','Andriod dev','A',77)''')
cursor.execute('''Insert Into STUDENTS values('Shubham','Data Science','E',88)''')
cursor.execute('''Insert Into STUDENTS values('Om','ML Engg','O',95)''')
cursor.execute('''Insert Into STUDENTS values('Aryan','DL Engg','E',85)''')
cursor.execute('''Insert Into STUDENTS values('Ravi','Full Stack','A',76)''')
cursor.execute('''Insert Into STUDENTS values('Divyanshu','Front end','D',50)''')
cursor.execute('''Insert Into STUDENTS values('Shivam','Back end','D',45)''')
cursor.execute('''Insert Into STUDENTS values('Rahul','Software dev','F',33)''')
cursor.execute('''Insert Into STUDENTS values('Rohit','Data Science','F',79)''')

## Displaying all the records
print("The inserted records are")

data=cursor.execute('''Select * From STUDENTS''')

for row in data:
    print(row)
    
## Closing the Connections  
  
connection.commit()
connection.close()
