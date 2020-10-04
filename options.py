import subprocess as sp
import pymysql
import pymysql.cursors
import add
from add import * 
import updating
from updating import *

def adminOpt(cur, con):
    while(1):
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
        elif ch==2:
            hireStaff(cur, con)
        elif ch==3:
            updateStaff(cur, con)
        elif ch==7:
            addDep(cur, con)

def staffOpt(cur,con):
    print("1. Add vehicle")
    print("2. Update vehicle availability")
    print("3. Delete vehicle")
    print("4. Update department")
    print("5. Add plasma sample")
    print("6. Update plasma sample")
    print("7. Plasma samples of a blood type")
    print("8. Add donor")
    print("9. Update donor")
    print("10. Delete donor")
    print("11. Donors with more than x donations")
    print("12. Donor with maximum number of donations")
    print("13. Average number of donations per month in a particular year")
    print("14. Average number of orders placed per month in a particular year")
    print("15. Average number of donations per month in a particular year")
    print("16. Logout")
    ch = int(input("Enter choice> "))
    if ch==16:
    	return
    elif ch==1:
        addVehi(cur, con)	
    elif ch==2:
        updateVehAv(cur, con)

def donorOpt(cur,con):
    print("1. Plasma sample details") # based on donor id
    print("2. Logout")
    ch = int(input("Enter choice> "))
    if ch==2:
    	return	

def hospOpt(cur,con):
    print("1. Place order")
    print("2. Logout")
    ch = int(input("Enter choice> "))
    if ch==2:
    	return