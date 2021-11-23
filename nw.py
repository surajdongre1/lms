import mysql.connector
import re
import datetime
password="suraj"
cnx= mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd='Suraj',
    db='register',
    
)
if cnx.is_connected:
    cursor= cnx.cursor()
    
def register():
    try:
        sname=input("Enter the name which you want to Register: \t")
        nname=sname.capitalize()
        age=input("Enter age ")
        cid=int(input("Choose an Id number for you"))
    
        try:
            sql= 'create table dataentry(id int(225) ,name varchar(225), age int(225))'
            cursor.execute(sql)
            print("table created") 
            cnx.commit()
        except:
            try:
                print("Table is already created.///")
                val=(cid,)
                ql= '''create table ID%s (bookname varchar(255), issuedate varchar(255), returndate varchar (255) )'''%val
                cursor.execute(ql)
                cnx.commit()
                print(val)
                
                try:
                    insql= "insert into dataentry (id,name,age) VALUES(%s,%s,%s)"
                    newval=(cid,nname,age)
                    cursor.execute(insql,newval)
                    cnx.commit()
                except ValueError as v:
                    print("There is a value error")
                    print(v)
            except:
                print("There is some error")
            

        print("Table is already Created trying to insert the values")
    except ValueError as v:
        print("Please enter a number value for ID/Age:")
        print(v)
class viewdata:
    def viewAllData():

        cursor.execute("select * from dataentry")
        # mycursor.fetchall()
        print("Id.     Name     Age")
        for i in cursor:
            print(i)
    def viewPersonalData():
        nid=input("Please Enter ID to view your personal Data")
        sql= "SELECT * FROM id%s"%nid
        cursor.execute(sql)
        print("\n bookname     issuedate    returndate \n")
        for i in cursor:
            print(i)

class datainsert:  
    def insert_data():
        try:
            dt= datetime.datetime.now()
            new_date=str(dt)
            idname=input("Please enter Your Id.  ")
            bname= input("Please Enter name of book which you want to Issue: ")
            idn=(idname,)
            sql="insert into id%s (bookname,issuedate)"%idn +"values (%s,%s)"
            val=(bname,new_date)
            cursor.execute(sql,val)
            cnx.commit()
            if True:
                print("You've Successfully Issued a book")
        except:
            print("Sorry...Please Enter a valid ID number")
    def returnBook():
        try:
            dt= datetime.datetime.now()
            new_date=str(dt)
            idname=input("Please enter Your Id.  ")
            bname= input("Please Enter name of book which you want to Return: ")
            idn=(idname,)
            sql="insert into id%s (bookname,returndate)"%idn +"values (%s,%s)"
            val=(bname,new_date)
            cursor.execute(sql,val)
            cnx.commit()
            if True:
                print(f"You've Succesfully Returned '{bname}' book.")
        except:
            print("Sorry...Please Enter a valid Id number.")

def delete_data():
    sname=input("Enter the id/Name for which you want to delete all records \n \t")
    l=(sname,) 
    regex="\d+"
    match=re.findall(regex,sname)
    # print(match)
    del_val= "SELECT name FROM dataentry WHERE id=%s"
    sql="DELETE FROM dataentry WHERE id = %s "
    
    try:
        if match:
            del_val= "SELECT name FROM dataentry WHERE id=%s"%l
            sql="DELETE FROM dataentry WHERE id = %s "
            cursor.execute(del_val)
            result= cursor.fetchall()   
            for k in result:
                print(f"Deleted all records of{k}")
            cnx.commit()

            val=(sname,)
            cursor.execute(sql,val)
            match=str(match)
            ql="drop table id%s"%val
            cursor.execute(ql)
            
            cnx.commit()
        else:
            del_val= "SELECT id FROM dataentry WHERE name=%s" 
            sql="DELETE FROM dataentry WHERE name = %s "
            cursor.execute(del_val,l)
            result= cursor.fetchall() 
            for i in result:
                print(f"Successfully DELETED All records of {l}")
              
        
            val=(sname,)
            cursor.execute(sql,val)
            nr=cursor.fetchall()
            
            # for j in result:
            #     print(f"Successfully DELETED all records of {j}")
            
            
                
            newdel="DROP TABLE id%s"%i
            cursor.execute(newdel)
            
            

        cnx.commit()
    except:
        print("Oops,Enter valid id number")
        cnx.rollback()
welcome_msg= '''====Welcome to dataEntry====
Choose the following option for dataEntry'''

welcome_msg='''
=====  WELCOME TO E-LIBRARY MANAGEMENT SYSTEM  =====
1.  Register
2.  Issue/Return book 
3.  View Data
4.  Delete Data \n'''
if __name__=="__main__":
    user="y"
    while user=="y":
        print(welcome_msg)
        user1= input("choose option: \t")
        if user1=="1":
            register()
        elif user1=="2":
            a= input('''1. To Issue a book
            2. To Return a book
            ''')
            if a=="1":
                datainsert.insert_data()
            elif a=="2":
                datainsert.returnBook()
            

        elif user1=="3":
            a=input('''
            1. To view Personal Data: 
            2. To view all Data: 
                        ''')
            if a=="1":
                viewdata.viewPersonalData()
            elif a=="2":
                password="Admin"
                pd=input("Please Enter The PASSWORD:  ")
                if password==pd:
                    viewdata.viewAllData()
                else:
                    print("WRONG PASSWORD")
                    
        elif user1=="4":
        
            delete_data()
        else:
            print("Please Enter a Valid Numeric Input:")
        user=input("Do you want to continue (y/n): \t")
    else:
        print("Thanks for using Our software")
        exit()

cnx.close()