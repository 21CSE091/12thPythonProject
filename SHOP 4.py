import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE GROCERY_MNGMNT7")
mycursor.execute("USE GROCERY_MNGMNT7")
mycursor.execute("CREATE TABLE SEASONAL_FRUITS(SNO INT,NAME VARCHAR(15),PRICE FLOAT,UNITS VARCHAR(10),QUANTITY INT)")
mycursor.execute("CREATE TABLE PERSONAL_CARE(SNO INT,NAME VARCHAR(15),BRAND VARCHAR(10),QUANTITY INT,PRICE FLOAT)")
mycursor.execute("CREATE TABLE STAPLES(SNO INT,NAME VARCHAR(15),BRAND VARCHAR(20),QUANTITY INT,PRICE FLOAT,UNITS VARCHAR(10))")
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
def SEARCH(rsh):
    mycursor.execute("SELECT*FROM SEASONAL_FRUITS WHERE NAME=rsh")
    s=mycursor[1]
    qty=s*mycursor[4]
    print(qty)
rsh=input(
    



