"""
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
"""

from datetime import date 
import placeOrder
from placeOrder import calcAge
from placeOrder import newUser

def hireStaff(cur,con):
    try:
        row = {}
        print("Enter new staff's details: ")
        row["Staff_id"] = input("Staff ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["Login_id"] = "STAFF"+row["Staff_id"]
        
        row["doj"] = input("Date of joining (YYYY-MM-DD): ")
        row["dep"] = input("Department ID:")
        query = "SELECT *FROM DEPARTMENT WHERE Department_id LIKE '%s'"%(row["dep"])
        if(cur.execute(query)==0):
            con.commit()
            print("wrong department id entered")
            return
        con.commit()
        row["Salary"] = int(input("Salary: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["sup"] = input("Supervisor staff ID: ")

        if row["sup"]=='' or row["sup"]=='NULL':
            row["sup"]='NULL'
        else:
            row["sup"]= "'"+row["sup"]+"'"
        
        bdate = row["Bdate"].split('-')
        """
        print(bdate[0])
        print(bdate[1])
        print(bdate[2])
        """
        row["Age"] = int(calcAge(date(int(bdate[0]),int(bdate[1]),int(bdate[2]))))


        newUser(cur,con,row["Login_id"])
        
        #print(row["Age"])
        query = "INSERT INTO STAFF(First_name, Last_name, Staff_id, Birth_date, Salary, Date_of_joining, Supervisor, Login_id, Age) VALUES('%s', '%s', '%s', '%s', %d, '%s', %s, '%s', %d)" % (
            row["Fname"], row["Lname"], row["Staff_id"], row["Bdate"], row["Salary"], row["doj"], row["sup"], row["Login_id"], row["Age"])

        #print(query)
        cur.execute(query)
        con.commit()

        query = "UPDATE DEPARTMENT SET No_of_employees=No_of_employees + 1 WHERE Department_id='%s'" % (row["dep"])
        cur.execute(query)
        con.commit()

        query = "INSERT INTO WORKS_FOR(Department_id,Staff_id) VALUES('%s','%s')" %(row["dep"], row["Staff_id"])
        cur.execute(query)
        con.commit()

        skills = (input("Skills (comma separated): ")).split(',')
        for skill in skills:
            query = "INSERT INTO STAFF_SKILLS(Staff_id,Skills) VALUES('%s','%s')"%(row["Staff_id"],skill)
            cur.execute(query)
            con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        try:
            query1 = "SELECT Staff_id FROM USER LEFT JOIN STAFF ON USER.Login_id=STAFF.Login_id WHERE USER.Login_id LIKE '%s'" %(row["Login_id"])
            if(cur.execute(query1)>0):
                con.commit()
                if cur.fetchall()[0]['Staff_id']=='NULL':
                    delUser(cur,con,row["Login_id"])
        except Exception as e:
            con.rollback()
            print("query failed")
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addDonor(cur,con):
    try:
        
        row = {}
        print("Enter new donor's details: ")
        row["Donor_id"] = input("Donor ID: ")
        row["name"] = (input("Name (Fname Lname): "))
        row["Login_id"] = "DONOR"+row["Donor_id"]
        newUser(cur,con,row["Login_id"])
        
        row["aadhar"] = int(input("Aadhar Number: "))

        x = 1
        while(x):
            row["Blood_type"] = input("Blood Type (A+/-,B+/-,O+/-,AB+/-): ")
            if row["Blood_type"] in ["A+","A-","B+","B-","O+","O-","AB+","AB-"]:
                x=0
            else:
                print("Invalid blood type")

        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["noDon"] = int(input("Number of donations: "))

        bdate = row["Bdate"].split('-')

        row["Age"] = int(calcAge(date(int(bdate[0]),int(bdate[1]),int(bdate[2]))))
        if(row["Age"]<18){
            printf("Sorry, donor can't be below 18 years")
            
        }
        else{
        query = "INSERT INTO DONOR(Name, Donor_id, Birth_date, Number_of_donations, Blood_type, Aadhar_num, Login_id, Age) VALUES('%s', '%s', '%s', %d, '%s', %d, '%s', %d)" % (
            row["name"], row["Donor_id"], row["Bdate"], row["noDon"], row["Blood_type"], row["aadhar"], row["Login_id"],row["Age"])

        #print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")
        }
    except Exception as e:
        con.rollback()
        try:
            query1 = "SELECT Donor_id FROM USER LEFT JOIN STAFF ON USER.Login_id=STAFF.Login_id WHERE USER.Login_id LIKE '%s'" %(row["Login_id"])
            if(cur.execute(query1)>0):
                con.commit()
                if cur.fetchone()['Donor_id']=='NULL':
                    delUser(cur,con,row["Login_id"])
        except Exception as e1:
            con.rollback()
            print("query failed")
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e1)

    return

def addDep(cur,con):
    try:
        row = {}
        print("Enter new dependent's details: ")
        row["Staff_id"] = input("Staff ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]

        x = 1
        while(x):
            row["gend"] = input("Gender (F,M,T,O): ")
            if row["gend"] in ["F","M","T","O"]:
                x=0
            else:
                print("Invalid gender input")

        row["rel"] = input("Relationship: ")
        row["age"] = int(input("Age: "))

        query = "INSERT INTO DEPENDENT(First_name, Last_name, Staff_id, Gender, Relationship, Age) VALUES('%s', '%s', '%s', '%c', '%s', '%d')" % (
            row["Fname"], row["Lname"], row["Staff_id"], row["gend"], row["rel"], row["age"])

        #print(query)
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
    
def addVehi(cur,con):
    try:
        row = {}
        print("Enter new vehicle's details: ")
        row["Vehicle_id"] = input("Vehicle ID: ")

        x = 1
        while(x):
            row["Vehicle_type"] = input("Vehicle_type (HCV, LCV, Two-wheeler, Car): ")
            if row["Vehicle_type"] in ["HCV","LCV","Two-wheeler","Car"]:
                x=0
            else:
                print("Invalid vehicle type")

        x = 1
        """        
        while(x):
            row["Availability"] = int(input("Vehicle Availability (1, 0): "))
            if row["Availability"] in [1, 0]:
                x=0
            else:
                print("Please enter 0 or 1")
        """
        row["Availability"] = 1
        row["Deliveries"] = 0
        row["Department_id"] = "DL"

        """query = "SELECT *FROM VEHICLE_DETAILS WHERE Vehicle_type LIKE '%s'" %(row["Vehicle_type"])
        if(cur.execute(query)==0)
            print("")


        row["Max_dist"] = int(input("What is the maximum distance(in km) this vehicle can travel? "))
        row["Speed"] = int(input("Average speed(in km/hr) with which it can travel: "))
        
        query1 = "INSERT INTO VEHICLE_DETAILS(Vehicle_type,Max_dist,Speed) VALUES('%s',%d,%d)"%(
            row["Vehicle_type"],row["Max_dist"],row["Speed"])
        cur.execute(query1)
        con.commit()
"""
        query = "INSERT INTO LOGISTICS(Vehicle_id, Vehicle_type, Availability, Deliveries, Department_id) VALUES('%s', '%s', %d, %d, '%s')" % (
            row["Vehicle_id"], row["Vehicle_type"], row["Availability"], row["Deliveries"], row["Department_id"])

        #print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addPlasma(cur, con):
    try:
        row = {}
        print("Enter plasma details: ")
        row["Donor_id"] = input("Donor ID: ")
        row["Donation_date"] = input("Donation date: ")
        
        x = 1
        while(x):
            row["Sample_no"] = int(input("Sample number (1, 2): "))
            if row["Sample_no"] in [1, 2]:
                x=0
            else:
                print("Please enter 1 or 2")
        
        query1 = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE Vacancy>0"

        if cur.execute(query1)==0:
            con.commit()
            print("Add an inventory with vacancy first")
            return

        inventory_id = cur.fetchone()
        #print(inventory_id)
        inventory_id = inventory_id['Inventory_id']
        #print(inventory_id)
        con.commit()
        query = "INSERT INTO PLASMA(Donor_id, Donation_date, Sample_no, Used, Inventory_id) VALUES('%s', '%s', %d, 0, '%s')" % (
            row["Donor_id"], row["Donation_date"], row["Sample_no"], inventory_id)

        #print(query)
        cur.execute(query)
        con.commit()


        #updating inventory
        que = "SELECT Blood_type FROM DONOR WHERE Donor_id LIKE '%s'" % (row["Donor_id"])     
        if cur.execute(que):
            btype = cur.fetchone()['Blood_type']

        if btype == "A+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Aplus = No_of_Aplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "A-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Aminus = No_of_Aminus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "B+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Bplus = No_of_Bplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "B-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Bminus = No_of_Bminus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "O+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Oplus = No_of_Oplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "O-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_Ominus = No_of_Ominus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "AB+":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_ABplus = No_of_ABplus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
        if btype == "AB-":
            quer = "UPDATE PLASMA_INVENTORY SET No_of_ABminus = No_of_ABminus + 1, Vacancy = Vacancy - 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)

        
        cur.execute(quer)
        con.commit()

        #update numofdonations in donor
        query2 = "UPDATE DONOR SET Number_of_donations = Number_of_donations+1 WHERE Donor_id = '%s'" %(row["Donor_id"])
        cur.execute(query2)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addInventory(cur, con):
    try:
        row = {}
        print("Enter new plasma inventory details: ")
        row["Inventory_id"] = input("Inventory ID:")
        row["Capacity"] = int(input("Capacity: "))

        query = "INSERT INTO PLASMA_INVENTORY(No_of_Aplus, No_of_Aminus, No_of_Bplus, No_of_Bminus, No_of_ABplus, No_of_ABminus, No_of_Oplus, No_of_Ominus,Capacity,Vacancy,Department_id, Inventory_id) VALUES(0, 0, 0, 0, 0,0,0,0,%d,%d,'DPI','%s')" % (
            row["Capacity"], row["Capacity"], row["Inventory_id"])

        #print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addHosp(cur,con):
    try:
        
        row = {}
        print("Enter new hospital details: ")
        row["Hospital_id"] = input("Hospital ID: ")
        row["name"] = (input("Hospital Name: "))
        row["dist"] = float(input("Hospital Distance(in km) from plasma bank: "))
        row["Login_id"] = "HOSPITAL"+row["Hospital_id"]
        newUser(cur,con,row["Login_id"])
        
        query = "INSERT INTO HOSPITAL(Hospital_id,Hospital_name,Distance,Login_id) VALUES('%s','%s',%f,'%s')"%(
            row["Hospital_id"], row["name"], row["dist"], row["Login_id"])
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
