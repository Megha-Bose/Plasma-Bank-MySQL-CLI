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
import retrieve_id
from retrieve_id import *
import retrieve_other
from retrieve_other import *



def adminOpt(cur,con,loginid):
    while(1):
        print("1. Manage staff")
        print("2. Manage dependents")
        print("3. Update department")
        print("4. Add plasma samples")
        print("5. Manage donor")
        print("6. Manage vehicles")
        print("7. Get information")
        print("8. Add hospital")
        print("9. Show all details")
        print("10. Add inventory")
        print("11. Update user")
        print("12. Logout")
        ch = int(input("Enter choice> "))
        if ch==12:
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
            getInfo(cur, con, loginid)
        elif ch==8:
            addHosp(cur, con)
        elif ch==9:
            showAllDetails(cur, con)
        elif ch==10:
            addInventory(cur, con)
        elif ch==11:
            updateUser(cur, con)
        else:
            print("Invalid choice")
        


def invStaffOpt(cur,con,loginid):
    while(1):
        print("1. View your details")
        print("2. Add donor")
        print("3. Show all donors")
        print("4. Update donor")
        print("5. Delete donor")
        print("6. Get Donor")
        print("7. Add plasma sample")
        print("8. Show all plasma samples")
        print("9. View filtered Plasma samples")
        print("10. Add hospital")
        print("11. Show all hospitals")
        print("12. Add inventory")
        print("13. Show all inventories")
        print("14. Logout")
        ch = int(input("Enter choice> "))
        if ch==14:
            return
        elif ch==1:
            displayMyDetails(cur, con, loginid)
        elif ch==2:
            addDonor(cur, con)
        elif ch==4:
            updateDonor(cur, con)
        elif ch==5:
            delDonor(cur, con)
        elif ch==6:
            getDonor(cur, con)
        elif ch==7:
            addPlasma(cur, con)
        elif ch==9:
            getPlasma(cur, con)
        elif ch==10:
            addHosp(cur, con)
        elif ch==12:
            addInventory(cur, con)
        elif ch==3:
            showAllDonor(cur,con)
        elif ch==8:
            showAllPlasma(cur,con)
        elif ch==11:
            showAllHospital(cur,con)
        elif ch==13:
            showAllInv(cur,con)

        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")
    


def logStafOpt(cur,con,loginid):
    while(1):
        print("1. View your details")
        print("2. Add vehicle")
        print("3. Show all vehicles")
        print("4. Update vehicle availability")
        print("5. Delete vehicle")
        print("6. Logout")
        ch = int(input("Enter choice> "))
        if ch==6:
            return
        elif ch==1:
            displayMyDetails(cur, con, loginid)
        elif ch==2:
            addVehi(cur, con)
        elif ch==4:
            updateVehAv(cur, con)
        elif ch==5:
            delVehi(cur, con)
        elif ch==3:
            showAllVehi(cur,con)
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")


def staffOpt(cur,con,loginid):
    stid = loginid[5:len(loginid)]
    query = "SELECT Department_id FROM WORKS_FOR WHERE Staff_id LIKE '%s'" %(stid)
    #print(query)
    
    cur.execute(query)
    
    dept = ""
    result = cur.fetchall()
    for row in result:
        for key, value in row.items():
            if key=="Department_id":
                dept = value
    print(dept)
    if dept == "DPI":
        invStaffOpt(cur,con,loginid)
    else:
        logStafOpt(cur,con,loginid)
    tmp = input("Enter any key to CONTINUE>")


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
            donorid = loginid[5:len(loginid)]
            retrievePlasmaById(cur,con,donorid)
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")



def hospOpt(cur,con,loginid):
    while(1):
        print("1. View our details")
        print("2. View our patients")
        print("3. Place order")
        print("4. View our orders")
        print("5. Logout")
        ch = int(input("Enter choice> "))
        if ch==5:
            return
        elif ch==1:
            displayMyDetails(cur, con, loginid)
        elif ch==2:
            hospid = loginid[8:len(loginid)]
            retrievePatByHospId(cur,con,hospid)
        elif ch==3:
            placeOrder(cur, con, loginid)
        elif ch==4:
            hospid = loginid[8:len(loginid)]
            retrieveOrderByHospId(cur,con,hospid)
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")
    