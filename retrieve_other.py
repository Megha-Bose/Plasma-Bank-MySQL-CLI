def retrieveStaffByName(cur,con,fname,lname):
    try:
        query = "SELECT * FROM STAFF WHERE First_name='%s' AND Last_name='%s'" % (fname, lname)
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
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveDonorByName(cur,con,fname,lname):
    try:
        query = "SELECT * FROM DONOR WHERE First_name='%s' AND Last_name='%s'" % (fname, lname)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveDonorByBloodType(cur,con,bloodtype):
    try:
        query = "SELECT * FROM DONOR WHERE Blood_type='%s'" % (bloodtype)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return
    

def retrievePlasmaByBloodType(cur,con,bloodtype):
    try:
        query = "SELECT * FROM PLASMA WHERE Blood_type='%s'" % (bloodtype)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrievePlasmaByUsed(cur,con,used):
    try:
        query = "SELECT * FROM PLASMA WHERE Used='%d'" % (used)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveOrderByHospId(cur,con,hospid):
    try:
        query = "SELECT * FROM ORDER_REQUEST WHERE Hospital_id='%s'" % (hospid)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveOrderByAccepted(cur,con,accepted):
    try:
        query = "SELECT * FROM ORDER_REQUEST WHERE Accepted='%d'" % (accepted)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveStaffByDeptId(cur,con,deptid):
    try:
        query = "SELECT * FROM STAFF NATURAL JOIN WORKS_FOR WHERE Department_id='%s'" % (deptid)
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
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrieveDepenByStaffId(cur,con,staffid):
    try:
        query = "SELECT * FROM DEPENDENT WHERE Staff_id='%s'" % (staffpid)
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return


def retrievePatByHospId(cur,con,hospid):
    try:
        query = "SELECT * FROM PATIENT WHERE Hospital_id='%s'" % (hospid)
        if cur.execute(query):
            result = cur.fetchall()
            for row in result:
                print(row)
                for key, value in row.items():
                    if key=="Patient_id":
                        query = "SELECT * FROM PATIENT_ALLERGIES WHERE Patient_id='%s'" % (value)
                        if cur.execute(query):
                            print(cur.fetchall())
                        con.commit()
        con.commit()
        if cur.execute(query):
            print(cur.fetchall())
            con.commit()
    except Exception as e:
        con.rollback()
        print("Retrieve failed")
        print(">>>>>>>>>>>>>", e)
    return