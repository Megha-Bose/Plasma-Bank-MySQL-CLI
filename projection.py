# Get the names of all donors with greater than x donations
# Get the vehicle type from logistics depending on the distance in an order

import pretty
from pretty import *

def donorGrtrX(cur, con):
	try:
		x = int(input("Enter x: "))
		query = "SELECT * FROM DONOR WHERE Number_of_donations > '%d' " %(x)
		if cur.execute(query):
			pretty(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to perform projection")
		print(">>>>>>>>>>>>>", e)

	return

def getVehicle(cur, con):
	try:
		distmin = int(input("Enter lower limit distance: "))
		distmax = int(input("Enter upper limit distance: "))
		query = "SELECT Vehicle_type FROM LOGISTICS WHERE distance >= '%d' AND distance <= '%d'" %(distmin, distmax)
		if cur.execute(query):
			pretty(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to perform projection")
		print(">>>>>>>>>>>>>", e)

	return

