# Get the name of the donor with maximum number of donations
# Get average salary of staff members
# Get the average number of donations per month for a particular year
# Get the average number of orders placed per month for a particular year

import pretty
from pretty import *

def donorMaxDons(cur,con):
	try:
		query = "SELECT * FROM DONOR WHERE Number_of_donations IN (SELECT MAX(Number_of_donations) FROM DONOR) "
		if cur.execute(query):
			pretty(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find donors with max donations")
		print(">>>>>>>>>>>>>", e)

	return

def avgSal(cur,con):
	try:
		query = "SELECT AVG(Salary) FROM STAFF"
		if cur.execute(query):
			averagesal = cur.fetchall()
			pretty(averagesal)
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find avg salary")
		print(">>>>>>>>>>>>>", e)

	return

def avgDons(cur,con):
	try:
		year = int(input("Enter year for which you want to see average number of donations per month: "))
		query = "SELECT AVG(num) AS AvgDonations FROM (SELECT COUNT(*) AS num ,MONTH(Donation_date) FROM PLASMA WHERE YEAR(Donation_date) = '%d' GROUP BY MONTH(Donation_date)) AS TAB;" % (year)
		if cur.execute(query):
			pretty(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find average number of donations per month for given year")
		print(">>>>>>>>>>>>>", e)

	return

def avgOrders(cur,con):
	try:
		year = int(input("Enter year for which you want to see average number of orders placed per month: "))
		query = "SELECT AVG(num) AS AvgNumOrder FROM (SELECT COUNT(Order_id) AS num,MONTH(Order_date) FROM ORDER_REQUEST WHERE YEAR(Order_date) = '%d' GROUP BY MONTH(Order_date)) AS TAB" %(year)
		if cur.execute(query):
			pretty(cur.fetchall())
		con.commit()

	except Exception as e:
		con.rollback()
		print("Failed to find average number of orders placed per month for given year")
		print(">>>>>>>>>>>>>", e)

	return


