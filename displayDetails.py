import pretty
from pretty import *

def displayUserDetails(cur,con,loginid):
    try:
        query = "SELECT * FROM USER WHERE Login_id='%s'" % (loginid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Display Details failed")
        print(">>>>>>>>>>>>>", e)
    return



def displayHospitalDetails(cur,con,loginid):
    try:
        query = "SELECT * FROM HOSPITAL WHERE Login_id='%s'" % (loginid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Display Details failed")
        print(">>>>>>>>>>>>>", e)
    return



def displayDonorDetails(cur,con,loginid):
    try:
        query = "SELECT * FROM DONOR WHERE Login_id='%s'" % (loginid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Display Details failed")
        print(">>>>>>>>>>>>>", e)
    return



def displayStaffDetails(cur,con,loginid):
    try:
        query = "SELECT * FROM STAFF NATURAL JOIN WORKS_FOR WHERE Login_id='%s'" % (loginid)
        if cur.execute(query):
            pretty(cur.fetchall())
            con.commit()
        staffid = loginid[5:len(loginid)]
        print("Skills:")
        query = "SELECT * FROM STAFF_SKILLS WHERE Staff_id='%s'" % (staffid)
        if cur.execute(query):
            prettySkills(cur.fetchall())
            con.commit()
        print("")
    except Exception as e:
        con.rollback()
        print("Display Details failed")
        print(">>>>>>>>>>>>>", e)
    return



def displayMyDetails(cur,con,loginid):
    displayUserDetails(cur,con,loginid)
    if loginid.find("STAFF")>=0:
        displayStaffDetails(cur,con,loginid)
    elif loginid.find("HOSP")>=0:
        displayHospitalDetails(cur,con,loginid)
    elif loginid.find("DONOR")>=0:
        displayDonorDetails(cur,con,loginid)
    return