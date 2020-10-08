import pretty
from pretty import *

def retrieveStaffById(cur,con,staffid):
    try:
        query = "SELECT STAFF.*,Contact,Address FROM STAFF NATURAL JOIN USER WHERE Staff_id='%s'" % (staffid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
            print("Skills:")
        query = "SELECT * FROM STAFF_SKILLS WHERE Staff_id='%s'" % (staffid)
        if cur.execute(query):
            prettySkills(cur.fetchall())
            con.commit()
        print("")
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveDonorById(cur,con,donorid):
    try:
        query = "SELECT DONOR.*,Contact,Address FROM DONOR NATURAL JOIN USER WHERE Donor_id='%s'" % (donorid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrievePlasmaById(cur,con,donorid):
    try:
        query = "SELECT * FROM PLASMA WHERE Donor_id='%s'" % (donorid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveHospitalById(cur,con,hospid):
    try:
        query = "SELECT HOSPITAL.*,Contact,Address FROM HOSPITAL NATURAL JOIN USER WHERE Hospital_id='%s'" % (hospid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveOrderById(cur,con,orderid):
    try:
        query = "SELECT * FROM ORDER_REQUEST WHERE Order_id='%s'" % (orderid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveInvById(cur,con,invid):
    try:
        query = "SELECT * FROM PLASMA_INVENTORY WHERE Inventory_id='%s'" % (invid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveVehiById(cur,con,vehid):
    try:
        query = "SELECT * FROM LOGISTICS WHERE Vehicle_id='%s'" % (vehid)
        if cur.execute(query):
            row = cur.fetchall()
            pretty(row)
            for key, value in row.items():
                if key=="Vehicle_type":
                    query = "SELECT * FROM VEHICLE_DETAILS WHERE Vehicle_type='%s'" % (value)
                    if cur.execute(query):
                        pretty(cur.fetchall())
                    con.commit()
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveDeptById(cur,con,deptid):
    try:
        query = "SELECT * FROM DEPARTMENT WHERE Department_id='%s'" % (deptid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve by ID failed")
        print(">>>>>>>>>>>>>", e)
    return
