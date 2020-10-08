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
import placeOrder
from placeOrder import *
import retrieve_id
from retrieve_id import *
import retrieve_other
from retrieve_other import *
import showall
from showall import *


def manageStaff(cur, con):
    while(1):
        print("1. Hire staff")
        print("2. Update staff")  # Hire an Employee
        print("3. Delete staff")
        print("4. Exit")
        ch = int(input("Enter choice> "))
        if ch==1:
            hireStaff(cur, con)
        elif ch==2:
            updateStaff(cur, con)
        elif ch==3:
            delStaff(cur, con)
        elif ch==4:
            return
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")

def manageDep(cur, con):
    while(1):
        print("1. Add dependent of staff")
        print("2. Update dependent")
        print("3. Delete dependent")
        print("4. Exit")  
        ch = int(input("Enter choice> "))
        if ch==1:
            addDep(cur, con)
        elif ch==2:
            delDep(cur, con)
        elif ch==3:
            updateDependent(cur, con)
        elif ch==4:
            return
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")

       
def manageDonor(cur, con):
    while(1):
        print("1. Add donor")
        print("2. Update donor")
        print("3. Delete donor")
        print("4. Exit")
        ch = int(input("Enter choice> "))
        if ch==1:
            addDonor(cur, con)
        elif ch==2:
            updateDonor(cur, con)
        elif ch==3:
            delDonor(cur, con)
        elif ch==4:
            return
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")

def manageVeh(cur, con):
    while(1):
        print("1. Add vehicle")
        print("2. Update vehicle availability")
        print("3. Delete vehicle")
        print("4. Exit")
        ch = int(input("Enter choice> "))
        if ch==1:
            addVehi(cur, con)
        elif ch==2:
            updateVehAv(cur, con)
        elif ch==3:
            delVehi(cur, con)
        elif ch==4:
            return
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")

def getInfo(cur, con, loginid):
    while(1):
        print("1. View your details") 
        print("2. Get staff")  
        print("3. Get donor")
        print("4. Get plasma samples")
        print("5. Get order")  
        print("6. Get inventory")
        print("7. Get vehicle")
        print("8. Get department")  
        print("9. Get dependent")
        print("10. Get patient")
        print("11. Average salary of staff")
        print("12. Donors with more than x donations")
        print("13. Donor with maximum number of donations")
        print("14. Average number of donations per month in a particular year")
        print("15. Average number of orders placed per month in a particular year")
        print("16. Get the donor details for a particular order")
        print("17. Get all successful orders that are completed by a particular vehicle type")
        print("18. Get donors in a particular age group whose plasmas have been successfully delivered to a patient")
        print("19. Exit")
        ch = int(input("Enter choice> "))
        if ch==1:
            displayMyDetails(cur, con, loginid)     
        elif ch==2:
            getStaff(cur, con)
        elif ch==3:
            getDonor(cur,con)
        elif ch==4:
            getPlasma(cur, con)
        elif ch==5:
            getOrder(cur, con)
        elif ch==6:
            getInv(cur, con)
        elif ch==7:
            getVehi(cur, con)
        elif ch==8:
            getDept(cur, con)
        elif ch==9:
            getDepen(cur, con)
        elif ch==10:
            getPatient(cur, con)
        elif ch==11:
            avgSal(cur, con)
        elif ch==12:
            donorGrtrX(cur,con)
        elif ch==13:
            donorMaxDons(cur,con)
        elif ch==14:
            avgDons(cur,con)
        elif ch==15:
            avgOrders(cur,con)
        elif ch==16:
            getDonorOrder(cur, con)
        elif ch==17:
            getOrderVehicle(cur, con)
        elif ch==18:
            getDonAge(cur,con)
        elif ch==19:
            return
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")

def showAllDetails(cur, con):
    while(1):
        print("1. Show all plasma")
        print("2. Show all staff")
        print("3. Show all donors")
        print("4. Show all orders")
        print("5. Show all hospitals")
        print("6. Show all inventories")
        print("7. Show all vehicles")
        print("8. Exit")
        ch = int(input("Enter choice> "))
        if ch==1:
            showAllPlasma(cur, con)
        elif ch==2:
            showAllStaff(cur, con)
        elif ch==3:
            showAllDonor(cur, con)
        elif ch==4:
            showAllOrder(cur, con)
        elif ch==5:
            showAllHospital(cur, con)
        elif ch==6:
            showAllInv(cur, con)
        elif ch==7:
            showAllVehi(cur, con)
        elif ch==8:
            return
        else:
            print("Invalid choice")
        tmp = input("Enter any key to CONTINUE>")