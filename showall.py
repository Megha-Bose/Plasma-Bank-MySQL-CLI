import pretty
from pretty import *

def showAllPlasma(cur,con):
    try:
        query = "SELECT * FROM PLASMA"
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllStaff(cur,con):
    try:
        query = "SELECT * FROM STAFF"
        if cur.execute(query):
            result = cur.fetchall()
            for row in result:
                print(row)
                for key, value in row.items():
                    if key=="Staff_id":
                        query = "SELECT * FROM STAFF_SKILLS WHERE Staff_id='%s'" % (value)
                        if cur.execute(query):
                            print(cur.fetchall())
                        con.commit()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllDonor(cur,con):
    try:
        query = "SELECT * FROM DONOR"
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
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return


def showAllHospital(cur,con):
    try:
        query = "SELECT * FROM HOSPITAL"
        if cur.execute(query):
            print(cur.fetchall())
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
            print(cur.fetchall())
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
                print(row)
                for key, value in row.items():
                    if key=="Vehicle_type":
                        query = "SELECT * FROM VEHICLE_DETAILS WHERE Vehicle_type='%s'" % (value)
                        if cur.execute(query):
                            print(cur.fetchall())
                        con.commit()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Show All failed")
        print(">>>>>>>>>>>>>", e)
    return

