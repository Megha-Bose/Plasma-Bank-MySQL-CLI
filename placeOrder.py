from datetime import date 


def newUser(cur,con,login):
    
    row={}
    row["Password"] = input("Login Password: ")
    row["Contact"] = int(input("Contact Number: "))
    row["Address"] = input("Address: ")

    query = "INSERT INTO USER(Login_id, Password, Contact, Address) VALUES('%s', '%s', '%d', '%s')" % (
            login, row["Password"], row["Contact"], row["Address"])

#    print(query)
    cur.execute(query)
    con.commit()


def calcAge(bDate): 
    today = date.today() 
    age = today.year - bDate.year - ((today.month, today.day) < (bDate.month, bDate.day)) 
  
    return age 
    """try:  
        birthday = bdate.replace(year = today.year) 
  
    # raised when birth date is February 29 
    # and the current year is not a leap year 
    except ValueError:  
        birthday = bdate.replace(year = today.year, 
                  month = bdate.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - bdate.year - 1
    else: 
        return today.year - bdate.year 
    """
def placeOrder(cur,con,loginid):
    try:
        row = {}
        print("Enter details to place order: ")
        row["Hospital_id"] = loginid[8:len(loginid)]
        #row["dist"] = float(input("Hospital Distance from plasma bank: "))
        query6 = "SELECT Distance FROM HOSPITAL WHERE Hospital_id LIKE '%s'" %(row["Hospital_id"])
        cur.execute(query6)
        row["dist"] = cur.fetchone()['Distance']
        row["Patient_id"] = input("Patient ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]

        x = 1
        while(x):
            row["Blood_type"] = input("Blood Type (A+/-,B+/-,O+/-,AB+/-): ")
            if row["Blood_type"] in ["A+","A-","B+","B-","O+","O-","AB+","AB-"]:
                x=0
            else:
                print("Invalid blood_type")
        
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        bdate = row["Bdate"].split('-')
        row["Age"] = int(calcAge(date(int(bdate[0]),int(bdate[1]),int(bdate[2]))))
        allergies = (input("Patient allergies (comma separated): ")).split(',')

        row["Order_id"] = row["Hospital_id"] + row["Patient_id"]

        row["Order_date"] = (input("Order date: "))
        query = "INSERT INTO ORDER_REQUEST(Order_id, Vehicle_id, Order_date, Hospital_id, Blood_type, Accepted, Distance, Donor_id) VALUES('%s', NULL, '%s', '%s', '%s', 0, %f, NULL)" % (
            row["Order_id"], row["Order_date"], row["Hospital_id"], row["Blood_type"], row["dist"])

        #print(query)
        cur.execute(query)
        con.commit()

        query = "INSERT INTO PATIENT(First_name, Last_name, Patient_id, Birth_date, Hospital_id, Blood_type, Age) VALUES('%s', '%s', '%s', '%s', '%s', '%s', %d)" % (
            row["Fname"], row["Lname"], row["Patient_id"], row["Bdate"], row["Hospital_id"], row["Blood_type"], row["Age"])

        #print(query)
        cur.execute(query)
        con.commit()
        
        for allergy in allergies:
            query = "INSERT INTO PATIENT_ALLERGIES(Patient_id, Allergies) VALUES('%s','%s')"%(row["Patient_id"],allergy)
            cur.execute(query)
            con.commit()

        print("Registered your request")
        print("Order id of the request is ",row["Order_id"])
        #check plasma inventory 
        if row["Blood_type"] == "A+":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_Aplus >0"
        if row["Blood_type"] == "A-":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_Aminus >0"
        if row["Blood_type"] == "B+":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_Bplus >0"
        if row["Blood_type"] == "B-":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_Bminus >0"
        if row["Blood_type"] == "O+":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_Oplus >0"
        if row["Blood_type"] == "O-":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_Ominus >0"
        if row["Blood_type"] == "AB+":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_ABplus >0"
        if row["Blood_type"] == "AB-":
            quer = "SELECT Inventory_id FROM PLASMA_INVENTORY WHERE No_of_ABminus >0"
        
        if cur.execute(quer)==0:
            con.commit()
            print("No plasma sample found for the given blood type")
            return

        inventory_id = cur.fetchall()[0]['Inventory_id']
        con.commit()
        print("We got a plasma sample for you")
        
        # get a vehicle
        query1 = "SELECT Vehicle_id FROM LOGISTICS NATURAL JOIN VEHICLE_DETAILS WHERE Max_dist>=%f AND Availability=1" %(row["dist"])
        vehicle_id=''
        if cur.execute(query1)==0:
            con.commit()
            vehicle_id == 'NULL'
            print("No vehicle found, you will have to pick up if you confirm order")
            
        else:
            vehicle_id = cur.fetchall()[0]['Vehicle_id']
            con.commit()
            print("Vehicle found pls confirm")
        
        confirm = int(input("Enter 1 to confirm, 0 to go back: "))

        if(confirm == 0):
            return
        else:

            #UPDATE THE INVENTORY SPECIFIED BY inventory_id 
            if row["Blood_type"] == "A+":
                que = "UPDATE PLASMA_INVENTORY SET No_of_Aplus = No_of_Aplus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "A-":
                que = "UPDATE PLASMA_INVENTORY SET No_of_Aminus = No_of_Aminus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "B+":
                que = "UPDATE PLASMA_INVENTORY SET No_of_Bplus = No_of_Bplus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "B-":
                que = "UPDATE PLASMA_INVENTORY SET No_of_Bminus = No_of_Bminus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "O+":
                que = "UPDATE PLASMA_INVENTORY SET No_of_Oplus = No_of_Oplus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "O-":
                que = "UPDATE PLASMA_INVENTORY SET No_of_Ominus = No_of_Ominus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "AB+":
                que = "UPDATE PLASMA_INVENTORY SET No_of_ABplus = No_of_ABplus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            if row["Blood_type"] == "AB-":
                que = "UPDATE PLASMA_INVENTORY SET No_of_ABminus = No_of_ABminus - 1, Vacancy = Vacancy + 1 WHERE Inventory_id LIKE '%s'" %(inventory_id)
            cur.execute(que)
            con.commit()

            #UPDATE USED STATUS OF PLASMA
            donor_id=''
            query3 = "SELECT Donor_id FROM PLASMA WHERE Inventory_id LIKE '%s' AND Used = 0 AND Donor_id IN (SELECT Donor_id FROM DONOR WHERE Blood_type LIKE '%s')" %(inventory_id, row["Blood_type"])
            if cur.execute(query3):
                donor_id = cur.fetchone()['Donor_id']
            con.commit()

            query2 = "UPDATE PLASMA SET Used = 1 WHERE Inventory_id LIKE '%s' AND Used = 0 AND Donor_id LIKE '%s'" %(inventory_id, donor_id)

            cur.execute(query2)
            con.commit()
        
                
            #if vehicle_id not equal to 'NULL' then   UPDATE VEHICLE AVAILABILITY AND NUMBER OF DELIVERIES FOR VEHICLE WITH ID vehicle_id
            
            query4 = "UPDATE LOGISTICS SET Availability = 0, Deliveries = Deliveries + 1 WHERE Vehicle_id LIKE '%s'" % (vehicle_id)
            cur.execute(query4)
            con.commit()

            #update order
            query5 = "UPDATE ORDER_REQUEST SET Vehicle_id = '%s', Accepted = 1, Donor_id = '%s' WHERE Order_id LIKE '%s'" %(vehicle_id, donor_id, row["Order_id"])
            cur.execute(query5)
            con.commit

            query = "INSERT INTO SUPPLY (Order_id,Donor_id,Vehicle_id,Inventory_id) VALUES ('%s', '%s', '%s', '%s')" %(row["Order_id"],donor_id, vehicle_id, inventory_id)
            cur.execute(query)
            con.commit()
            print("Order confirmed Thank you!")


    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
