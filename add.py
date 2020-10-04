"""
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
"""

def hireStaff(cur,con):
    try:
        row = {}
        print("Enter new staff's details: ")
        row["Staff_id"] = input("Staff ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["doj"] = input("Date of joining (YYYY-MM-DD): ")
        row["Salary"] = float(input("Salary: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["sup"] = input("Supervisor staff ID: ")
        row["Login_id"] = "STAFF" + row["Staff_id"]

        if row["sup"]=='' or row["sup"]=='NULL':
            row["sup"]='NULL'
        else:
            row["sup"]= "'"+row["sup"]+"'"
        
        row["Password"] = input("Password: ")
        row["Contact"] = int(input("Contact Number: "))
        row["Address"] = input("Address: ")


        query = "INSERT INTO USER(Login_id, Password, Contact, Address) VALUES('%s', '%s', '%d', '%s')" % (
            row["Login_id"], row["Password"], row["Contact"], row["Address"])

        print(query)
        cur.execute(query)
        con.commit()

        query = "INSERT INTO STAFF(First_name, Last_name, Staff_id, Birth_date, Salary, Date_of_joining, Supervisor, Login_id, Age) VALUES('%s', '%s', '%s', '%s', %f, '%s', %s, '%s', 28)" % (
            row["Fname"], row["Lname"], row["Staff_id"], row["Bdate"], row["Salary"], row["doj"], row["sup"], row["Login_id"])

        print(query)
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
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addDep(cur,con):
    try:
        row = {}
        print("Enter new dependent's details: ")
        row["Staff_id"] = input("Staff ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["gend"] = input("Gender (F,M,T,O): ")
        row["rel"] = input("Relationship: ")
        row["age"] = int(input("Age: "))

        query = "INSERT INTO DEPENDENT(First_name, Last_name, Staff_id, Gender, Relationship, Age) VALUES('%s', '%s', '%s', '%c', '%s', '%d')" % (
            row["Fname"], row["Lname"], row["Staff_id"], row["gend"], row["rel"], row["age"])

        print(query)
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
        row["Vehicle_type"] = input("Vehicle_type (HCV, LCV, Two-wheeler, Car): ")
        row["Availability"] = int(input("Vehicle Availability (1, 0): "))
        row["Deliveries"] = input("Number of deliveries: ")
        row["Department_id"] = input("Department_id: ")

        query = "INSERT INTO LOGISTICS(Vehicle_id, Vehicle_type, Availability, Deliveries, Department_id) VALUES('%s', '%s', '%d', '%d', %s)" % (
            row["Vehicle_id"], row["Vehicle_type"], row["Availability"], row["Deliveries"], row["Department_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return