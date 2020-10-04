
def placeOrder(cur,con):
    try:
        row = {}
        print("Enter details to place order: ")
        row["Hospital_id"] = input("Hospital ID:")
        row["name"] = (input("Hospital Name: "))
        row["dist"] = float(input("Hospital Distance from plasma bank: "))
        row["Login_id"] = "HOSP"+row["Hospital_id"]
        newUser(cur,con,row["Login_id"])
        
        query = "INSERT INTO HOSPITAL(Hospital_id,Hospital_name,Distance,Login_id) VALUES('%s','%s',%f,'%s')"%(
            row["Hospital_id"], row["name"], row["dist"], row["Login_id"])
        cur.execute(query)
        con.commit()

        row["Patient_id"] = input("Patient ID: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        row["Blood_type"] = input("Blood Type (A+/-,B+/-,O+/-,AB+/-): ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")

        query = "INSERT INTO PATIENT(First_name, Last_name, Patient_id, Birth_date, Hospital_id, Blood_type, Age) VALUES('%s', '%s', '%s', '%s', '%s', '%s', 28)" % (
            row["Fname"], row["Lname"], row["Patient_id"], row["Bdate"], row["Hospital_id"], row["Blood_type"])

        print(query)
        cur.execute(query)
        con.commit()

        row["Order_id"] = input("Order ID:")
        row["Order_date"] = (input("Order date: "))
        query = "INSERT INTO ORDER_REQUEST(Order_id, Vehicle_id, Order_date, Hospital_id, Blood_type, Accepted, Distance, Donor_id) VALUES('%s', NULL, '%s', '%s', '%s', 0, %f, NULL)" % (
            row["Order_id"], row["Order_date"], row["Hospital_id"], row["Blood_type"], row["dist"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

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

        inventory_id = cur.fetchall()[0][0]
        con.commit()
        print("We got a plasma sample for you")
        
        # get a vehicle
        query1 = "SELECT Vehicle_id FROM LOGISTICS NATURAL JOIN VEHICLE_DETAILS WHERE Max_dist>=%f AND Availability==1" %(row["dist"])

        if cur.execute(query1)==0:
            con.commit()
            vehicle_id == 'NULL'
            print("No vehicle found, you will have to pick up if you confirm order")
            
        else:
            vehicle_id = cur.fetchall()[0][0]
            con.commit()
            print("Vehicle found pls confirm")
        
        confirm = int(input("Enter 1 to confirm, 0 to go back: "))

        if(confirm == 0):
            return
        else:

            """
            UPDATE THE INVENTORY SPECIFIED BY inventory_id AND USED STATUS OF PLASMA
            """

            """
            UPDATE THE NUMBER OF DONATIONS FOR DONOR WHOSE PLASMA SAMPLE U MARKED AS USED ABOVE
            store donor_id in "donor_id" variable pls
            """
                
            """
            if vehicle_id not equal to 'NULL' then,
            UPDATE VEHICLE AVAILABILITY AND NUMBER OF DELIVERIES FOR VEHICLE WITH ID vehicle_id
            """

            query = "INSERT INTO SUPPLY (Order_id,Donor_id,Vehicle_id,Inventory_id) VALUES ('%s', '%s', '%s', '%s')" %(
                row["Order_id"],onor_id, vehicle_id, inventory_id)
            cur.execute(query)
            con.commit()
            print("Order confirmed Thank you!")


    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
