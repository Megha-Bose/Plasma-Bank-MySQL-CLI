import pretty
from pretty import *

def showAllPlasma(cur,con):
    try:
        query = "SELECT * FROM PLASMA"
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllStaff(cur,con):
    try:
        query = "SELECT STAFF.*,Contact,Address FROM STAFF NATURAL JOIN USER"
        if cur.execute(query):
            result = cur.fetchall()
            for row in result:
                pretty1(row)
                print("Skills:")
                for key, value in row.items():
                    if key=="Staff_id":
                        query = "SELECT * FROM STAFF_SKILLS WHERE Staff_id='%s'" % (value)
                        if cur.execute(query):
                            prettySkills(cur.fetchall())
                        con.commit()
                print("")
        con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllDonor(cur,con):
    try:
        query = "SELECT DONOR.*,Contact,Address FROM DONOR NATURAL JOIN USER"
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllOrder(cur,con):
    try:
        query = "SELECT * FROM ORDER_REQUEST"
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllHospital(cur,con):
    try:
        query = "SELECT HOSPITAL.*,Contact,Address FROM HOSPITAL NATURAL JOIN USER"
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllInv(cur,con):
    try:
        query = "SELECT * FROM PLASMA_INVENTORY"
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllVehi(cur,con):
    try:
        query = "SELECT * FROM LOGISTICS"
        if cur.execute(query):
            result = cur.fetchall()
            for row in result:
                pretty1(row)
                for key, value in row.items():
                    if key=="Vehicle_type":
                        query = "SELECT * FROM VEHICLE_DETAILS WHERE Vehicle_type='%s'" % (value)
                        if cur.execute(query):
                            pretty(cur.fetchall())
                        con.commit()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return

