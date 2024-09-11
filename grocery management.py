import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="roja2021")
mycursor=mydb.cursor()
'''mycursor.execute("CREATE DATABASE GROCERY_MNGMNT48")'''
mycursor.execute("USE GROCERY_MNGMNT48")
'''mycursor.execute("CREATE TABLE SEASONAL_FRUITS(SNO INT,NAME VARCHAR(15),PRICE FLOAT,UNITS VARCHAR(10),QUANTITY INT)")
mycursor.execute("CREATE TABLE PERSONAL_CARE(SNO INT,NAME VARCHAR(15),BRAND VARCHAR(10),QUANTITY INT,PRICE FLOAT)")
mycursor.execute("CREATE TABLE STAPLES(SNO INT,NAME VARCHAR(15),BRAND VARCHAR(20),QUANTITY INT,PRICE FLOAT,UNITS VARCHAR(10))")'''
def INSERT():
    mycursor.execute("INSERT INTO SEASONAL_FRUITS(SNO,NAME,PRICE,UNITS)VALUES(1,'ORANGE',35.0,'PERKG')")
    mycursor.execute("INSERT INTO SEASONAL_FRUITS(SNO,NAME,PRICE,UNITS)VALUES(2,'MANGO',66.0,'PERKG')")
    mycursor.execute("INSERT INTO SEASONAL_FRUITS(SNO,NAME,PRICE,QUANTITY)VALUES(3,'PINEAPPLE',78.0,1)")
    mycursor.execute("INSERT INTO SEASONAL_FRUITS(SNO,NAME,PRICE,QUANTITY)VALUES(4,'WATERMELON',60.0,1)")
    mycursor.execute("INSERT INTO SEASONAL_FRUITS(SNO,NAME,PRICE,UNITS)VALUES(5,'GRAPEFRUIT',54.0,'PERKG')")
    mydb.commit()
    mycursor.execute("INSERT INTO PERSONAL_CARE VALUES(1,'ORALCARE','COLGATE',1,35.0)")
    mycursor.execute("INSERT INTO PERSONAL_CARE VALUES(2,'HAIRCARE','PANTENE',2,70.0)")
    mycursor.execute("INSERT INTO PERSONAL_CARE VALUES(3,'BATHINGACC','CINTHOL',4,40.0)")
    mycursor.execute("INSERT INTO PERSONAL_CARE VALUES(4,'PERFUMES','YARDLEY',1,120.0)")
    mycursor.execute("INSERT INTO PERSONAL_CARE VALUES(5,'MAKEUP','NAILENAMAL',5,200.0)")
    mydb.commit()
    mycursor.execute("INSERT INTO STAPLES VALUES(1,'RICE','INDIAGATE',1,500.0,'PERKG')")
    mycursor.execute("INSERT INTO STAPLES VALUES(2,'WHEAT','AASHIRVAAD',2,300.0,'PERKG')")
    mycursor.execute("INSERT INTO STAPLES VALUES(3,'PULSES','MOONGDAL',4,100.0,'PERKG')")
    mycursor.execute("INSERT INTO STAPLES VALUES(4,'EDIBLEOILS','FORTUNE',1,200.0,'PERLITRE')")
    mycursor.execute("INSERT INTO STAPLES VALUES(5,'SPICES','SAKTHIMASALA',1,50.0,'HALFKG')")
    mydb.commit()

def SEARCH(x,y):
    if x=="SEASONAL_FRUITS":
        mycursor.execute("select * from SEASONAL_FRUITS where name='{}'".format(y))
        for i in mycursor:
            print(i)
    if x=="PERSONAL_CARE":
        mycursor.execute("select * from PERSONAL_CARE where name='{}'".format(y))
        for i in mycursor:
            print(i)
    if x=="STAPLES":
        mycursor.execute("select * from STAPLES where name='{}'".format(y))
        for i in mycursor:
            print(i)

def UPDATE(m,n):
    if m=="SEASONAL_FRUITS":
        mycursor.execute("update SEASONAL_FRUITS set PRICE=PRICE*2 where name='{}'".format(n))
        print("successfully updated")
        mydb.commit()
        mycursor.execute("select * from SEASONAL_FRUITS")
        for i in mycursor:
            print(i)
    if m=="PERSONAL_CARE":
        mycursor.execute("update PERSONAL_CARE set PRICE=PRICE*2 where name='{}'".format(n))
        print("successfully updated")
        mydb.commit()
        mycursor.execute("select * from PERSONAL_CARE")
        my=mycursor.fetchall()
        for i in my:
            print(i)
    if m=="STAPLES":
        mycursor.execute("update STAPLES set PRICE=PRICE*2 where name='{}'".format(n))
        print("successfully updated")
        mydb.commit()
        mycursor.execute("select * from STAPLES")
        for i in mycursor:
            print(i)

def DELETE(a,r):    
    if a=="SEASONAL_FRUITS":
        mycursor.execute("delete from SEASONAL_FRUITS where name='{}'".format(r))
        mycursor.execute("select * from SEASONAL_FRUITS")
        for i in mycursor:
            print(i)
        print("successfelly deleted")
    if a=="PERSONAL_CARE":
        mycursor.execute("delete from PERSONAL_CARE where name='{}'".format(r))
        mycursor.execute("select * from PERSONAL_CARE")
        for i in mycursor:
            print(i)
        print("successfelly deleted")
    if a=="STAPLES":
        mycursor.execute("delete from STAPLES where name='{}'".format(r))
        mycursor.execute("select * from STAPLES")
        for i in mycursor:
            print(i)
        print("successfelly deleted")

def DISPLAY(t,p,qty):
    if t=="SEASONAL_FRUITS":
        mycursor.execute("select * from SEASONAL_FRUITS where name='{}'".format(p))
        prod=mycursor.fetchall()
        for i in prod:
            v=i[2]
            total=qty*v
            print(total)
    if t=="PERSONAL_CARE":
        mycursor.execute("select * from PERSONAL_CARE where name='{}'".format(p))
        prod=mycursor.fetchall()
        for i in prod:
            v=i[4]
            total=qty*v
            print(total)
    if t=="STAPLES":
        mycursor.execute("select * from STAPLES where name='{}'".format(p))
        prod=mycursor.fetchall()
        for i in prod:
            v=i[4]
            total=qty*v
            print(total)
ans="y"
while ans=="y":
    print("1.INSERT")
    print("2.SEARCH")
    print("3.UPDATE")
    print("4.DELETE")
    print("5.DISPLAY")
    c=int(input("enter 1 to 6"))
    if c==1:
        INSERT()
        ans=input("do you want to continue ?")
    elif c==2:
        x=input("enter seasonal_fruits or personal_care or staples")
        y=input("enter the orders")
        SEARCH(x,y)
        ans=input("do you want to continue ?")
    elif c==3:
        m=input("enter the seasonal_fruits or personal_care or staples")
        n=input("enter the products name to be updated")
        UPDATE(m,n)
        ans=input("do you want to continue ?")
    elif c==4:
        a=input("enter seasonal_fruits or personal_care or staples")
        r=input("enter the products name to be delete")
        DELETE(a,r)
        ans=input("do you want to continue ?")
    elif c==5:
        t=input("enter seasonal_fruits or personal_care or staples") 
        p=input("enter the product name to display the bill")
        qty=int(input("enter quantity"))
        DISPLAY(t,p,qty)
        ans=input("do you want to continue ?")

        





        











        
    
