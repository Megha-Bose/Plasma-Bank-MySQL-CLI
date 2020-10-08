# Plasma-Bank-MySQL-CLI

## About
 A command line interface in Python3 using PyMySQL to manage a blood plasma bank.


## Run the script

Run `pip3 install tabular` if tabular is not installed.
Execute the script in the directory that contains the source files:
    ```
    $ python3 PlasmaBank.py
    ```

## User options

There are 4 types of users who can login and options are shown according to the user type.
1. Admin
2. Staff
3. Donor
4. Hospital

The following users have been entered in the database already.

Login_id | ADMIN | STAFFk | DONORk | HOSPITALk
--- | --- | --- | --- |--- 
Password | admin | sk | dk | hk 

Here, k belongs to {1,2,3}.
There is only one Admin account for the system.

When adding a new Staff, Donor or Hospital only the Staff ID, Donor ID or Hospital ID is required as input. The Login IDs will be created automatically as follows:
- For Staff:
		Login ID = "STAFF" + Staff ID
		Ex: Staff ID is "5", Login ID will be "STAFF5"
- For Donor:
		Login ID = "DONOR" + Donor ID
- For Hospital:
		Login ID = "HOSPITAL" + Hospital ID
		
NOTE: To add a plasma sample, the staff must add a donor first and use that donor id to add the plasma sample. 

