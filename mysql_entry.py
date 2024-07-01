#%%dependencies
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

#%%credential
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="329MYinsert#",
  database="firstdatabase"
)
print(mydb) #checking connection

#%% medium
pointer=mydb.cursor()

#%%creating db
pointer.execute("CREATE DATABASE firstdatabase")

#%%creating table
pointer.execute("CREATE TABLE collector1 (calories VARCHAR(255),duration VARCHAR(255))")

#%%INSERTION
sql = "INSERT INTO collector (sample) VALUES (%s)" # if direct values than ""present""
val=('HELLO',)
pointer.execute(sql, val)
mydb.commit()
print(pointer.rowcount)

#%%select
pointer.execute("SELECT * FROM collector1")
myresult = pointer.fetchall()
for x in myresult:
  print(x)

#%%close collection
pointer.close()
mydb.close()

#%%dataframe to db
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

#LOAD INTO DATABASE
engine = create_engine('mysql+mysqlconnector://root:329MYinsert#@localhost:3306/firstdatabase', echo=False)
df.to_sql(name='collector1', con=engine, if_exists = 'append', index=False)
