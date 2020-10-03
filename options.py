import subprocess as sp
import pymysql
import pymysql.cursors

def adminOpt():
    print("1. View your details")  # view details
    print("2. Hire staff")
    print("3. Update staff")  # Hire an Employee
    print("4. Delete staff")
    print("5. Search for staff")  # based undecided
    print("6. Average salary of staff")  # Hire an Employee
    print("7. Add dependent of staff")
    print("8. Delete dependent")  # based undecided
    print("9. Logout")
    ch = int(input("Enter choice> "))
    if ch==9:
    	return

def staffOpt():
    print("6. Logout")	

def donorOpt():
    print("6. Logout")	

def hospOpt():
    print("1. Place order")
    print("2. Logout")
    ch = int(input("Enter choice> "))
    if ch==2:
    	return