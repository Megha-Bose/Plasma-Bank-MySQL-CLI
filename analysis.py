# Get the donor details for a particular order (relationship between order and donor)
# Get all successful orders that are completed by a particular vehicle type (relationship between logistics and order)
# Get donors in a particular age group whose plasmas have been successfully delivered to a patient (this shows relationship between donor, plasma, order, hospital and patient)

def getDonorOrder(cur, con):
	try:
		oid = input("Enter order_id: ")
		query = "SELECT DONOR.* FROM DONOR INNER JOIN ORDER_REQUEST ON DONOR.Donor_id = ORDER_REQUEST.Donor_id WHERE ORDER_REQUEST.Order_id LIKE '%s'" %(oid)
		if cur.execute(query):
			print(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find donors with max donations")
		print(">>>>>>>>>>>>>", e)

	return

def getOrderVehicle(cur, con):
	try:
		vtype = input("Enter vehicle type: ")
		query = "SELECT ORDER_REQUEST.* FROM ORDER_REQUEST INNER JOIN LOGISTICS ON ORDER_REQUEST.Vehicle_id = LOGISTICS.Vehicle_id WHERE ORDER_REQUEST.Accepted = 1 AND LOGISTICS.Vehicle_type LIKE '%s'" %(vtype)
		if cur.execute(query):
			print(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find donors with max donations")
		print(">>>>>>>>>>>>>", e)

	return

def getDonAge(cur,con):
	try:
		mini = input("Enter minimum age: ")
		maxi = input("Enter maximum age: ")
		query = "SELECT DONOR.* FROM DONOR NATURAL JOIN PLASMA WHERE Age>=%d AND Age<=%d AND Used=1" % (mini, maxi)
		if cur.execute(query):
			print(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find donors with max donations")
		print(">>>>>>>>>>>>>", e)

	return
