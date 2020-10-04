import subprocess as sp
import pymysql
import pymysql.cursors
import add
from add import * 
import updating
from updating import *
import delete
from delete import *
import displayDetails
from displayDetails import *
import aggr
from aggr import *


def adminOpt(cur,con,loginid):
    while(1):
        print("1. View your details")  # view details
        print("2. Hire staff")
        print("3. Update staff")  # Hire an Employee
        print("4. Delete staff")
        print("5. Get staff")  # based undecided
        print("6. Average salary of staff")  # Hire an Employee
        print("7. Add dependent of staff")
        print("8. Delete dependent")  # based undecided
        print("9. Donors with more than x donations")
        print("10. Donor with maximum number of donations")
        print("11. Average number of donations per month in a particular year")
        print("12. Average number of orders placed per month in a particular year")
        print("13. Logout")
        ch = int(input("Enter choice> "))
        if ch==13:
        	return
        elif ch==1:
            displayMyDetails(cur, con, loginid)
        elif ch==2:
            hireStaff(cur, con)
        elif ch==3:
            updateStaff(cur, con)
        elif ch==4:
            delStaff(cur, con)
        # elif ch==5:
        #     getStaff(cur, con)
        elif ch==6:
            avgSal(cur, con)
        elif ch==7:
            addDep(cur, con)
        elif ch==8:
            delDep(cur, con)
        # elif ch==9:
        #     donorMoreXDons(cur,con)
        elif ch==10:
            donorMaxDons(cur,con)
        elif ch==11:
            avgDons(cur,con)
        elif ch==12:
            avgOrders(cur,con)


def invStaffOpt(cur,con,loginid):
    print("1. View your details")
    print("2. Add plasma sample")
    print("3. Update plasma sample")
    print("4. Get Plasma samples")
    print("5. Add donor")
    print("6. Update donor")
    print("7. Delete donor")
    print("8. Get Donor")
    print("9. Update department")
    print("10. Logout")
    ch = int(input("Enter choice> "))
    if ch==10:
    	return
    elif ch==1:
        displayMyDetails(cur, con, loginid)
    elif ch==2:
        addPlasma(cur, con)
    


def logStafOpt(cur,con,loginid):
    print("1. View your details")
    print("2. Add vehicle")
    print("3. Update vehicle availability")
    print("4. Delete vehicle")
    print("5. Update department")
    print("6. Logout")
    ch = int(input("Enter choice> "))
    if ch==6:
    	return
    elif ch==1:
        displayMyDetails(cur, con, loginid)

# for testing purpose, this needs to be changed
def staffOpt(cur,con,loginid):
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
    print("11. Logout")
    ch = int(input("Enter choice> "))
    if ch==11:
    	return
    elif ch==8:
        addDonor(cur,con)
    elif ch==1:
        addVehi(cur, con)	
    elif ch==2:
        updateVehAv(cur, con)


def donorOpt(cur,con,loginid):
    print("1. View my details")
    print("2. Plasma sample details") # based on donor id
    print("3. Logout")
    ch = int(input("Enter choice> "))
    if ch==3:
    	return
    elif ch==1:
        displayMyDetails(cur, con, loginid)
    elif ch==2:
        retrievePlasmaById(cur,con,loginid)


def hospOpt(cur,con,loginid):
    print("1. View my details")
    print("2. Place order")
    print("3. Logout")
    ch = int(input("Enter choice> "))
    if ch==3:
    	return
    elif ch==1:
        displayMyDetails(cur, con, loginid)
    