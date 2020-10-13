def delUser(cur,con,loginid):
    try:
        query = "DELETE FROM USER WHERE Login_id='%s'" % (loginid)

        #print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def delStaff(cur,con):
    try:
        row = {}
        row["Staff_id"] = input("Enter Staff ID to delete: ")
        row["Login_id"] = "STAFF" + row["Staff_id"]

        query = "SELECT Department_id FROM WORKS_FOR WHERE Staff_id='%s'" % (row["Staff_id"])
        cur.execute(query)
        row["dep"] = cur.fetchone()['Department_id']
        con.commit()

        query = "UPDATE DEPARTMENT SET No_of_employees=No_of_employees - 1 WHERE Department_id='%s'" % (row["dep"])
        cur.execute(query)
        con.commit()

        query = "DELETE FROM WORKS_FOR WHERE Staff_id='%s'" % (row["Staff_id"])

        #print(query)
        cur.execute(query)
        con.commit()

        query = "DELETE FROM STAFF_SKILLS WHERE Staff_id='%s'" % (row["Staff_id"])

        #print(query)
        cur.execute(query)
        con.commit()

        query = "DELETE FROM STAFF WHERE Login_id='%s'" % (row["Login_id"])

        #print(query)
        cur.execute(query)
        con.commit()

        delUser(cur,con,row["Login_id"])

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def delDonor(cur,con):
    try:
        row = {}
        row["Donor_id"] = input("Enter Donor ID to delete: ")
        row["Login_id"] = "DONOR" + row["Donor_id"]

        query = "DELETE FROM DONOR WHERE Donor_id='%s'" % (row["Donor_id"])

        #print(query)
        cur.execute(query)
        con.commit()

        delUser(cur,con,row["Login_id"])

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def delVehi(cur,con):
    try:
        row = {}
        row["Vehicle_id"] = input("Enter Vehicle ID to delete: ")
        
        query = "DELETE FROM LOGISTICS WHERE Vehicle_id='%s'" % (row["Vehicle_id"])

        #print(query)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return


def delDep(cur,con):
    try:
        row = {}
        row["Staff_id"] = input("Enter Staff ID associated: ")
        name = (input("Name (Fname Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Lname"] = name[1]
        
        query = "DELETE FROM DEPENDENT WHERE Staff_id='%s' AND First_name='%s' AND Last_name='%s'" % (row["Staff_id"], row["Fname"], row["Lname"])

        #print(query)
        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)

    return

