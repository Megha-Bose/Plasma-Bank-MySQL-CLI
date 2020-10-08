import retrieve_id
from retrieve_id import *
import retrieve_other
from retrieve_other import *


def getStaff(cur,con):
    while(1):
        print("Get by:\n")
        print("1. Staff ID")
        print("2. Department")
        print("3. Name")
        print("4. Go back")
        ch = int(input("Enter choice> "))
        if ch==4:
            return
        elif ch==1:
            staffid = input("Enter Staff ID: ")
            retrieveStaffById(cur,con,staffid)
        elif ch==2:
            deptid = input("Enter Department ID: ")
            retrieveStaffByDeptId(cur,con,deptid)
        elif ch==3:
            name = (input("Enter Name (Fname Lname): ")).split(' ')
            fname = name[0]
            lname = name[1]
            retrieveStaffByName(cur,con,fname,lname)
            

def getDonor(cur,con):
    while(1):
        print("Get by:\n")
        print("1. Donor ID")
        print("2. Blood Type")
        print("3. Name")
        print("4. Go back")
        ch = int(input("Enter choice> "))
        if ch==4:
            return
        elif ch==1:
            donorid = input("Enter Donor ID: ")
            retrieveDonorById(cur,con,donorid)
        elif ch==2:
            bloodtype = input("Enter Blood Type: ")
            retrieveDonorByBloodType(cur,con,bloodtype)
        elif ch==3:
            name = input("Enter Name (Fname Lname): ")
            retrieveDonorByName(cur,con,name)


def getPlasma(cur,con):
    while(1):
        print("Get by:\n")
        print("1. Donor ID")
        print("2. Blood Type")
        print("3. Used")
        print("4. Go back")
        ch = int(input("Enter choice> "))
        if ch==4:
            return
        elif ch==1:
            donorid = input("Enter Donor ID: ")
            retrievePlasmaById(cur,con,donorid)
        elif ch==2:
            bloodtype = input("Enter Blood Type: ")
            retrievePlasmaByBloodType(cur,con,bloodtype)
        elif ch==3:
            used = int(input("Used (0/1): "))
            retrievePlasmaByUsed(cur,con,used)


def getOrder(cur,con):
    while(1):
        print("Get by:\n")
        print("1. Order ID")
        print("2. Hospital ID")
        print("3. Accepted")
        print("4. Go back")
        ch = int(input("Enter choice> "))
        if ch==4:
            return
        elif ch==1:
            orderid = input("Enter Order ID: ")
            retrieveOrderById(cur,con,orderid)
        elif ch==2:
            hospid = input("Enter Hospital ID: ")
            retrieveOrderByHospId(cur,con,hospid)
        elif ch==3:
            accepted = int(input("Accepted (0/1): "))
            retrieveOrderByAccepted(cur,con,accepted)


def getInv(cur,con):
    while(1):
        print("1. Get")
        print("2. Go back")
        ch = int(input("Enter choice> "))
        if ch==2:
            return
        elif ch==1:
            invid = input("Enter Inventory ID: ")
            retrieveInvById(cur,con,invid)
        

def getVehi(cur,con):
    while(1):
        print("1. Get")
        print("2. Go back")
        ch = int(input("Enter choice> "))
        if ch==2:
            return
        elif ch==1:
            vehid = input("Enter Vehicle ID: ")
            retrieveVehiById(cur,con,vehid)


def getDept(cur,con):
    while(1):
        print("1. Get")
        print("2. Go back")
        ch = int(input("Enter choice> "))
        if ch==2:
            return
        elif ch==1:
            deptid = input("Enter Department ID: ")
            retrieveDeptById(cur,con,deptid)


def getDepen(cur,con):
    while(1):
        print("1. Get")
        print("2. Go back")
        ch = int(input("Enter choice> "))
        if ch==2:
            return
        elif ch==1:
            staffid = input("Enter Staff ID: ")
            retrieveDepenByStaffId(cur,con,staffid)


def getPatient(cur,con):
    while(1):
        print("1. Get")
        print("2. Go back")
        ch = int(input("Enter choice> "))
        if ch==2:
            return
        elif ch==1:
            hospid = input("Enter Hospital ID: ")
            retrievePatByHospId(cur,con,hospid)

