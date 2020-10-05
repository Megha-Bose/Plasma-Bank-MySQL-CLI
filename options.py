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
import projection
from projection import *
import placeOrder
from placeOrder import *
import analysis
from analysis import *
import getby
from getby import *
import adminOptions
from adminOptions import *


def adminOpt(cur,con,loginid):
    while(1):
        print("1. Manage staff")
        print("2. Manage dependents")
        print("3. Update department")
        print("4. Add plasma samples")
        print("5. Manage donor")
        print("6. Manage vehicles")
        print("7. Get information")
        print("8. Logout")
        ch = int(input("Enter choice> "))
        if ch==8:
            return
        elif ch==1:
            manageStaff(cur, con)
        elif ch==2:
            manageDep(cur, con)
        elif ch==3:
            updateDept(cur, con)
        elif ch==4:
            addPlasma(cur, con)
        elif ch==5:
            manageDonor(cur, con)
        elif ch==6:
            manageVeh(cur, con)
        elif ch==7:
            getInfo(cur, con)
        else:
            print("Invalid choice")
        


def invStaffOpt(cur,con,loginid):
    while(1):
        print("1. View your details")
        print("2. Add donor")
        print("3. Update donor")
        print("4. Delete donor")
        print("5. Get Donor")
        print("6. Add plasma sample")
        print("7. Get Plasma samples")
        print("8. Update department")
        print("9. Logout")
        ch = int(input("Enter choice> "))
        if ch==9:
            return
        elif ch==1:
            displayMyDetails(cur, con, loginid)
        elif ch==2:
            addDonor(cur, con)
        elif ch==3:
            updateDonor(cur, con)
        elif ch==4:
            delDonor(cur, con)
        elif ch==5:
            getDonor(cur, con)
        elif ch==6:
            addPlasma(cur, con)
        elif ch==7:
            getPlasma(cur, con)
        elif ch==8:
            updateDept(cur, con)
        else:
            print("Invalid choice")
    


def logStafOpt(cur,con,loginid):
    while(1):
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
        elif ch==2:
            addVehi(cur, con)
        elif ch==3:
            updateVehAv(cur, con)
        elif ch==4:
            delVehi(cur, con)
        elif ch==5:
            updateDept(cur, con)
        else:
            print("Invalid choice")


def staffOpt(cur,con,loginid):
    stid = loginid[5:len(loginid)]
    query = "SELECT Department_id FROM WORKS_FOR WHERE Staff_id LIKE '%s'" %(stid)
    if cur.execute(query):
        deprt = cur.fetchall()
    con.commit()
    if deprt == "DPI":
        invStaffOpt(cur,con,loginid)
    else:
        logStafOpt(cur,con,loginid)


def donorOpt(cur,con,loginid):
    while(1):
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
        else:
            print("Invalid choice")



def hospOpt(cur,con,loginid):
    while(1):
        print("1. View my details")
        print("2. Place order")
        print("3. Logout")
        ch = int(input("Enter choice> "))
        if ch==3:
            return
        elif ch==1:
            displayMyDetails(cur, con, loginid)
        elif ch==2:
            placeOrder(cur, con)
        else:
            print("Invalid choice")
    