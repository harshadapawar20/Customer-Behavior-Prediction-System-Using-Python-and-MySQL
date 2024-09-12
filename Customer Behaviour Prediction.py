### Customer Behaviour Prediction with Menu-Driven Interface ###

import pandas as pd
import numpy as np
import mysql.connector 
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)
con = mysql.connector.connect(host='localhost',user ='root', password ='root',database='customerbevaiour')
mycursor = con.cursor()
logging.info("Database connection eatablished.")

df = pd.read_csv("C:\\Users\\HARSHADA PAWAR\\OneDrive\\Desktop\\CSV files\\Ecommerce Customers.csv")

s1 = 'create table customers(ID int,Name varchar(30), Address varchar(500), price float)'
# myycursor.excecute(s1)
for i,j in df.iterrows():
    s1 = 'insert into customers(ID,Name,Address,price) values(%s,%s,%s,%s)'
    values = (j['id'],j['Name'],j['Address'],j['price'])
#     mycursor.execute(s1,values)
# con.commit()

while True:
    choice = int(input("Enter your choice:\nPress 1 to Load CSV Data\nPress 2 to Segment Customers\nPress 3 to load segmented data into MySQL\nPress 4 to Display report of Customer Segments\nPress 5 to Exit\n"))
    
    if(choice==1):
        print(df)
        print()

    elif(choice==2):
        for i,j in df.iterrows():
            p = j['price']
            conditions = [p>1000, (500<p<=1000), p<500]
            choices = ['High_spender','Medium_spender','Low_spender']
            spender_type =np.select(conditions,choices,default="None")

            if spender_type=='High_spender':
                s1='update customers set High_spender = True, Medium_spender=False, Low_spender=False where ID =%s'
                mycursor.execute(s1,(j['id'],))
            elif spender_type=='Medium_spender':
                s1='update customers set High_spender = False, Medium_spender=True, Low_spender=False where ID =%s'
                mycursor.execute(s1,(j['id'],))
            elif spender_type=='Low_spender':
                s1='update customers set High_spender = False, Medium_spender=False, Low_spender=True where ID =%s'
                mycursor.execute(s1,(j['id'],))
        con.commit()
        print("Customers segmented successfully")
        print()

    elif(choice==3):
        print("Re-validating and confirming segmented data...")
        for i,j in df.iterrows():
            p = j['price']
            conditions = [p>1000, (500<p<=1000), p<500]
            choices = ['High_spender','Medium_spender','Low_spender']
            spender_type =np.select(conditions,choices,default="None")

            if spender_type=='High_spender':
                s1='update customers set High_spender = True, Medium_spender=False, Low_spender=False where ID =%s'
                mycursor.execute(s1,(j['id'],))
            elif spender_type=='Medium_spender':
                s1='update customers set High_spender = False, Medium_spender=True, Low_spender=False where ID =%s'
                mycursor.execute(s1,(j['id'],))
            elif spender_type=='Low_spender':
                s1='update customers set High_spender = False, Medium_spender=False, Low_spender=True where ID =%s'
                mycursor.execute(s1,(j['id'],))
        con.commit()
        print("Segmented data has been re-validated and updated in MySQL.")
        print()
        
    elif(choice==4):
        s1='select * from customers'
        mycursor.execute(s1)
        x=mycursor.fetchall()
        for i in x:
            print(i)
        print()
        
    elif(choice==5):
        print("Exit")
        break
    
    else:
        print("Enter valid input.")