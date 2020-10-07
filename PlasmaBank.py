import subprocess as sp
import pymysql
import pymysql.cursors
import options
from options import *

def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")

def checkID(id):
    if id.find("STAFF")>=0:
        staffOpt(cur,con,id)
    elif id.find("HOSP")>=0:
        hospOpt(cur,con,id)
    elif id.find("DONOR")>=0:
        donorOpt(cur,con,id)
    elif id.find("ADMIN")>=0:
        adminOpt(cur,con,id)
    else:
        print("Invalid id. You have no permissions")

def loginUser(): # to determine access
    try:
        # Takes login details as input
        row = {}
        row["Login_id"] = input("Login ID: ")
        row["Password"] = input("Password: ")
        #if(row["Login_id"] != "Admin"):
        query = "SELECT * FROM USER WHERE Login_id like '%s' AND Password like '%s'" % (row["Login_id"], row["Password"])
        #print(query)
        if cur.execute(query):
            print("Login Successful")
            con.commit()
            checkID(row["Login_id"])
        else:
            print("Login failed")
            con.commit()
        

    except Exception as e:
        con.rollback()
        print("Failed attempt to login")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        loginUser()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("MYSQL Username: ")
    password = input("MYSQL Password: ")
    dbname = input("Database Name: ")
    port = (input("Port (if you are using docker):"))
    if port=="":
        port=''
    else:
        port=int(port)

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db=dbname,
                              port=port,
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Login")  # Hire an Employee
                print("2. Exit")  # Fire an Employee
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 2:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")
        if ch == 2:
            break

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
