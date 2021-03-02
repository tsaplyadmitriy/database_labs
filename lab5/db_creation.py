from faker import Faker
import psycopg2 as db

from random import seed
from random import randint


fake = Faker()
r = 100000
connection = db.connect(database='postgres', user='postgres',password='lnn1337213',host='127.0.0.1',port='5432')
print("Connection established!")

cursor = connection.cursor()

cursor.execute('''

    CREATE TABLE CUSTOMER (
        ID INT PRIMARY KEY NOT NULL,
         Name TEXT NOT NULL,
         Address TEXT NOT NULL,
        Age INT NOT NULL,
        Review TEXT);
        
        ''')


for i in range(r):
    cursor.execute("INSERT INTO CUSTOMER (ID,Name,Address,Age,Review) VALUES ('" + str(
        i) + "','" + fake.name() + "','" + fake.address() + "','" + str(randint(18, 90)) + "','" +  fake.text() + "')")
    connection.commit()
