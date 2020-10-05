import placeOrder
from placeOrder import calcAge

def updateStaff(cur,con):
	
	try:
		value=0
		row = {}
		
		while(value==0):
			row["sid"] = input("Enter Staff_id of staff whose details you wish to update: ")
			que = "SELECT * FROM STAFF WHERE Staff_id LIKE '%s'" % (row["sid"])
			value = cur.execute(que)
			if value == 0:
				print("Invalid Staff_id")
			con.commit()
        #row = {}
        #print("Enter new staff's details: ")
        #row["Staff_id"] = input("Staff ID: ")
        #update
		print("Do you want to edit the following field? ")
		cha = int(input("First name (1/0) : "))
		if cha == 1:
			row["Newfname"] = input("Enter new First name : ")
			query = "UPDATE STAFF SET First_name = '%s' WHERE Staff_id LIKE '%s'" % (row["Newfname"], row["sid"])
			#value=cur.execute(query)
			
			#print(value)
			con.commit()
		elif cha != 0:
			print("Enter 0 or 1")
		
		cha = int(input("Last name (1/0) : "))
		if cha == 1:
			row["Newlname"] = input("Enter new Last name : ")
			query = "UPDATE STAFF SET Last_name = '%s' WHERE Staff_id LIKE '%s'" % (row["Newlname"], row["sid"])
			cur.execute(query)
			con.commit()
	
		cha = int(input("Birth date (1/0) : "))
		if cha == 1:
			row["Newbd"] = input("Enter new Birth date (YYYY-MM-DD) : ")
			bdate = row["Newbd"].split('-')
			row["Age"] = calcAge(int(bdate[0]),int(bdate[1]), int(bdate[2]))
			query = "UPDATE STAFF SET Birth_date = '%s', Age = %d WHERE Staff_id LIKE '%s'" % (row["Newbd"], row["Age"], row["sid"])
			cur.execute(query)
			con.commit()

		
		cha = int(input("Salary (1/0) : "))
		if cha == 1:
			row["Newsal"] = float(input("Enter new Salary : "))
			query = "UPDATE STAFF SET Salary = '%f' WHERE Staff_id LIKE '%s'" % (row["Newsal"], row["sid"])
			cur.execute(query)
			con.commit()
		
		cha = int(input("Date of joining (1/0) : "))
		if cha == 1:
			row["Newdoj"] = input("Enter new Date of joining : ")
			query = "UPDATE STAFF SET Date_of_joining = '%s' WHERE Staff_id LIKE '%s'" % (row["Newdoj"], row["sid"])
			cur.execute(query)
			con.commit()
	
		cha = int(input("Supervisor (1/0) : "))
		if cha == 1:
			row["Newsup"] = input("Enter new Supervisor : ")
			if row["Newsup"]=='' or row["Newsup"]=='NULL':
				row["Newsup"]='NULL'
			else:
				row["Newsup"]= "'"+row["Newsup"]+"'"
			query = "UPDATE STAFF SET Supervisor = '%s' WHERE Staff_id LIKE '%s'" % (row["Newsup"], row["sid"])
			cur.execute(query)
			con.commit()
		
        #ch = int(input("Staff skills (1/0) : "))  
        
		print("Updated Database")

	except Exception as e:
		con.rollback()
		print("Failed to update staff")
		print(">>>>>>>>>>>>>", e)

	return


def updateVehAv(cur,con):
		
	try:
		value=0
		row = {}
			
		while(value==0):
			row["vid"] = input("Enter vehicle id of vehicle where availability needs to be changed: ")
			que = "SELECT * FROM LOGISTICS WHERE Vehicle_id LIKE '%s'" % (row["vid"])
			value = cur.execute(que)
			if value == 0:
				print("Invalid vehicle id")
			con.commit()	
		x = 1
		while(x):
			cha = bool(input("Enter new availability (1/0): "))
			if cha in [1, 0]:
				x=0
			else:
				print("Please enter 0 or 1")		
		
		query = "UPDATE LOGISTICS SET Availability = '%b' WHERE Vehicle_id LIKE '%s'" % (cha, row["vid"])
		cur.execute(query)
		con.commit()	        
		print("Updated Database")

	except Exception as e:
			con.rollback()
			print("Failed to update vehicle")
			print(">>>>>>>>>>>>>", e)

	return
def updateDept(cur,con):

	try:
		value=0
		row = {}

		while(value==0):
			row["did"] = input("Enter department id of the department whose details you wish to change: ")
			que = "SELECT * FROM DEPARTMENT WHERE Department_id LIKE '%s'" % (row["did"])
			value = cur.execute(que)
			if value == 0:
				print("Invalid Department id")
			con.commit()

		print("Do you want to edit the following fields? ")
		cha = int(input("Manager (1/0) : "))
		if cha == 1:
			row["Newman"] = input("Enter new manager id : ")
			query = "UPDATE DEPARTMENT SET Manager = '%s' WHERE Department_id LIKE '%s'" % (row["Newman"], row["did"])
			cur.execute(query)
			con.commit()
	
		cha = int(input("Description (1/0) : "))
		if cha == 1:
			row["Newdes"] = input("Enter new description : ")
			if row["Newdes"]=='' or row["Newdes"]=='NULL':
				row["Newdes"]='NULL'
			else:
				row["Newdes"]= "'"+row["Newdes"]+"'"
			query = "UPDATE DEPARTMENT SET Description = '%s' WHERE Department_id LIKE '%s'" % (row["Newdes"], row["did"])
			cur.execute(query)
			con.commit()
		
		cha = int(input("Remarks (1/0) : "))
		if cha == 1:
			row["Newrem"] = input("Enter new remarks : ")
			if row["Newrem"]=='' or row["Newrem"]=='NULL':
				row["Newrem"]='NULL'
			else:
				row["Newrem"]= "'"+row["Newrem"]+"'"
			query = "UPDATE DEPARTMENT SET Remarks = '%s' WHERE Department_id LIKE '%s'" % (row["Newrem"], row["did"])
			cur.execute(query)
			con.commit()
	
		print("Updated Database")

	except Exception as e:
		con.rollback()
		print("Failed to update department")
		print(">>>>>>>>>>>>>", e)

	return

def updateDonor(cur,con):

	try:
		value=0
		row = {}

		while(value==0):
			row["did"] = input("Enter donor id of the donor whose details you wish to change: ")
			que = "SELECT * FROM DONOR WHERE Donor_id LIKE '%s'" % (row["did"])
			value = cur.execute(que)
			if value == 0:
				print("Invalid Donor id")
			con.commit()

		print("Do you want to edit the following fields? ")
		cha = int(input("Name (1/0) : "))
		if cha == 1:
			row["Newnam"] = input("Enter new name : ")
			query = "UPDATE DONOR SET Name = '%s' WHERE Donor_id LIKE '%s'" % (row["Newnam"], row["did"])
			cur.execute(query)
			con.commit()
	
		cha = int(input("Aadhar_num (1/0) : "))
		if cha == 1:
			row["NewnUm"] = input("Enter new Aadhar_num : ")
			query = "UPDATE DONOR SET Aadhar_num = '%d' WHERE Donor_id LIKE '%s'" % (row["Newnum"], row["did"])
			cur.execute(query)
			con.commit()
		
		cha = int(input("Blood_type (1/0) : "))
		if cha == 1:

			x = 1
			while(x):
				row["Newb"] = input("Enter new Blood_type : ")
				if row["Newb"] in ["A+","A-","B+","B-","O+","O-","AB+","AB-"]:
					x=0
				else:
					print("Invalid blood type")
			query = "UPDATE DONOR SET Blood_type = '%s' WHERE Donor_id LIKE '%s'" % (row["Newb"], row["did"])
			cur.execute(query)
			con.commit()
	
		cha = int(input("Number_of_donations (1/0) : "))
		if cha == 1:
			row["Newnd"] = input("Enter new Number_of_donations : ")
			query = "UPDATE DONOR SET Number_of_donations = '%d' WHERE Donor_id LIKE '%s'" % (row["Newnd"], row["did"])
			cur.execute(query)
			con.commit()
	
			cha = int(input("Birth date (1/0) : "))
		if cha == 1:
			row["Newbd"] = input("Enter new Birth date : ")
			bdate = row["Newbd"].split('-')
			row["Age"] = calcAge(int(bdate[0]),int(bdate[1]), int(bdate[2]))
			query = "UPDATE DONOR SET Birth_date = '%s', Age = %d WHERE Donor_id LIKE '%s'" % (row["Newbd"], row["Age"], row["did"])
			cur.execute(query)
			con.commit()
	
		print("Updated Database")

	except Exception as e:
		con.rollback()
		print("Failed to update donor")
		print(">>>>>>>>>>>>>", e)

	return






