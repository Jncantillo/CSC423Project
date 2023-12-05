import sqlite3
import pandas as pd
from datetime import date

#connect to or create cleaning database
db_connect = sqlite3.connect('cleaning.db')

#create cursor to run queries
cursor = db_connect.cursor()

#---------PART A---------
#Query to create Client table 
query = """
    CREATE TABLE Client(
        clientNo INT,
        firstName VARCHAR(100),
        lastName VARCHAR(100),
        address VARCHAR(100),
        phoneNumber INT,
        PRIMARY KEY(clientNo)
        CONSTRAINT clientNo_uniqueness UNIQUE(clientNo)
        );
"""

cursor.execute(query)

#Query to create Requirement table 
query = """
    CREATE TABLE Requirement(
        requirementId INT,
        clientNo INT,
        startDate DATE,
        StartTime TIME,
        duration TIME
        CHECK(duration > '00:00:00'),
        comments VARCHAR(1000),
        FOREIGN KEY (clientNo) REFERENCES Client(clientNo)
        PRIMARY KEY(requirementId)
        CONSTRAINT requirementId_uniqueness UNIQUE(requirementId)
        );
"""

cursor.execute(query)

#Query to create Equipment table 
query = """
    CREATE TABLE Equipment(
        equipmentId INT,
        description VARCHAR(1000),
        usage REAL,
        cost REAL,
        PRIMARY KEY(equipmentId)
        CONSTRAINT equipmentId_uniqueness UNIQUE(equipmentId)
        );
"""

cursor.execute(query)

#Query to create Employee table 
query = """
    CREATE TABLE Employee(
        staffNo INT,
        firstName VARCHAR(100),
        lastName VARCHAR(100),
        address VARCHAR(100),
        salary REAL,
        phoneNumber INT,
        PRIMARY KEY(staffNo)
        CONSTRAINT staffNo_uniqueness UNIQUE(staffNo)
        );
"""

cursor.execute(query)

#Query to create EquipmentRequirement table 
query = """
    CREATE TABLE EquipmentRequirement(
        equipmentId INT,
        requirementId INT,
        quantity INT,
        FOREIGN KEY (equipmentId) REFERENCES Equipment(equipmentId)
        FOREIGN KEY (requirementId) REFERENCES Requirement(requirementId)
        PRIMARY KEY(equipmentId, requirementId)
        CONSTRAINT equipmentId_uniqueness UNIQUE(equipmentId)
        CONSTRAINT requirementId_uniqueness UNIQUE(requirementId)
        );
"""

cursor.execute(query)

#Query to create EmployeeRequirement table 
query = """
    CREATE TABLE EmployeeRequirement(
        staffNo INT,
        requirementId INT,
        FOREIGN KEY (staffNo) REFERENCES Employee(employeeId)
        FOREIGN KEY (requirementId) REFERENCES Requirement(requirementId)
        PRIMARY KEY(staffNo, requirementId)
        CONSTRAINT staffNo_uniqueness UNIQUE(staffNo)
        CONSTRAINT requirementId_uniqueness UNIQUE(requirementId)
        );
"""

cursor.execute(query)

#--------PART B--------
#Query to add to Client table
query = "INSERT INTO Client (clientNo, firstName, lastName, address, phoneNumber) VALUES (?,?,?,?,?)"
data = [
        (5849,'tim','apple', '7471 Glenridge Street', 5849573846),
        (2956, 'jeff', 'bezos', '9602 Windfall Court', 2859305860),
        (2947, 'alan', 'turing', '9856 Beach Street', 2053659385),
        (1047, 'steve', 'jobs', '397 Fairfield Drive', 5864937584),
        (5837, 'george', 'washington', '454 George Drive', 2054869483)
        ]
cursor.executemany(query,data)

#Query to display Client table
query = """
    SELECT *
    FROM Client;
"""
frame = pd.read_sql_query(query,db_connect)
print("\nClient Table:")
print(frame.head())

#Query to add to Requirement table
query = "INSERT INTO Requirement (requirementId, clientNo, startDate, startTime, duration, comments) VALUES (?,?,?,?,?,?)"
data = [
        (68463, 5849, date(2023, 12, 15), '08:00:00', '08:00:00', "Client requested fresh fruit placed on kitchen table after service concludes"),
        (23647, 2956, date(2023, 12, 17), '09:00:00', '06:00:00', "Client's boathouse also needs cleaning"),
        (56783, 2947, date(2023, 12, 19), '09:30:00', '04:00:00', "Client requested that the roped-off machines must not be touched"),
        (68464, 1047, date(2023, 12, 16), '08:45:00', '10:00:00', "Client requested that no animal products be used during cleaning"),
        (56834, 5837, date(2023, 12, 20), '12:30:00', '05:00:00', "Client specifically mentioned that there must be no parties on the premises")
        ]
cursor.executemany(query,data)

#Query to display Requirement table
query = """
    SELECT *
    FROM Requirement;
"""
frame = pd.read_sql_query(query,db_connect)
print("\n Requirement Table:")
print(frame.head())

#Query to add to Equipment table
query = "INSERT INTO Equipment (equipmentId, description, usage, cost) VALUES (?,?,?,?)"
data = [
        (123, 'Mop', 'Mops floors', 15.00),
        (456, 'Vaccuum', 'Cleans up debris', 75.00),
        (789, 'Duster', 'Removes dust', 1.00),
        (234, 'Ladder', 'Helps get to high places', 25.00),
        (678, 'floor buffer', 'Shines floors', 200)
        ]
cursor.executemany(query,data)

#Query to display Equipment table
query = """
    SELECT *
    FROM Equipment;
"""
frame = pd.read_sql_query(query,db_connect)
print("\n Equipment Table:")
print(frame.head())

#Query to add to Employee table
query = "INSERT INTO Employee (staffNo, firstName, lastName, address, salary, phoneNumber) VALUES (?,?,?,?,?,?)"
data = [
        (1234,'john','deer', '123 Sesame Street', 50000.00, 1234567890),
        (5678, 'jane', 'doe', '365 Ocean Drive', 55000.00, 3056748395),
        (9012, 'bob', 'smith', '583 Apollo Lane', 75000.00, 7707483745),
        (3456, 'real', 'person', '5643 S Miami Avenue', 80000.00, 6709483756),
        (6789, 'definitely_not', 'a_cat', '1600 Penn Avenue', 250000.00, 5866844758)
        ]
cursor.executemany(query,data)

#Query to display Employee table
query = """
    SELECT *
    FROM Employee;
"""
frame = pd.read_sql_query(query,db_connect)
print("\nEmployee Table:")
print(frame.head())

#Query to add to EquipmentRequirement table
query = "INSERT INTO EquipmentRequirement (equipmentId, requirementId, Quantity) VALUES (?,?,?)"
data = [
        (123, 68463, 15),
        (456, 23647, 4),
        (789, 56783, 20),
        (234, 68464, 3),
        (678, 56834, 2)
        ]

cursor.executemany(query,data)

#Query to display EquipmentRequirement table
query = """
    SELECT *
    FROM EquipmentRequirement;
"""
frame = pd.read_sql_query(query,db_connect)
print("\n EquipmentRequirement Table:")
print(frame.head())

#Query to add to EmployeeRequirement table
query = "INSERT INTO EmployeeRequirement (staffNo, requirementId) VALUES (?,?)"
data = [
        (1234, 68463),
        (5678, 23647),
        (9012, 56783),
        (3456, 68464),
        (6789, 56834)
        ]

cursor.executemany(query,data)

#Query to display EmployeeRequirement table
query = """
    SELECT *
    FROM EmployeeRequirement;
"""
frame = pd.read_sql_query(query,db_connect)
print("\n EmployeeRequirement Table:")
print(frame.head())

#commit changes to cleaning database
db_connect.commit()

#close the database connection before terminating
db_connect.close()