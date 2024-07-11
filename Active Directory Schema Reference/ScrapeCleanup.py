#Script to take a CSV and move data.
# Created by:  Lucas Kowe
import csv

# Open the input CSV file
input_csv = "ADScrape.csv"
output_csv = "ADScrape_Clean.csv"

#take values from and store each of them in an array
#find all rows that have "CN" in column 1 and store column 2 in an array called "CN"
def getCN(input_csv):
    CN = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "CN":  # Check if row has at least 2 elements
                CN.append(row[1])
    return CN

#find all rows that have "Ldap-Display-Name" in column 1 and store column 2 in an array called "Ldap-Display-Name"
def getLdapDisplayName(input_csv):
    Ldap_Display_Name = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "Ldap-Display-Name":  # Check if row has at least 2 elements
                Ldap_Display_Name.append(row[1])
    return Ldap_Display_Name

#find all rows that have "Size" in column 1 and store column 2 in an array called "Size"
def getSize(input_csv):
    Size = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "Size":  # Check if row has at least 2 elements
                Size.append(row[1])
    return Size

#find all rows that have "Update Privilege" in column 1 and store column 2 in an array called "Update Privilege"
def getUpdatePrivilege(input_csv):
    Update_Privilege = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "Update Privilege":  # Check if row has at least 2 elements
                Update_Privilege.append(row[1])
    return Update_Privilege

#find all rows that have "Update Frequency" in column 1 and store column 2 in an array called "Update Frequency"
def getUpdateFrequency(input_csv):
    Update_Frequency = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "Update Frequency":  # Check if row has at least 2 elements
                Update_Frequency.append(row[1])
    return Update_Frequency

#find all rows that have "Attribute-Id" in column 1 and store column 2 in an array called "Attribute-Id"
def getAttributeId(input_csv):
    Attribute_Id = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "Attribute-Id":  # Check if row has at least 2 elements
                Attribute_Id.append(row[1])
    return Attribute_Id

#find all rows that have "System-Id-Guid" in column 1 and store column 2 in an array called "System-Id-Guid"
def getSystemIdGuid(input_csv):
    System_Id_Guid = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "System-Id-Guid":  # Check if row has at least 2 elements
                System_Id_Guid.append(row[1])
    return System_Id_Guid

#find all rows that have "Syntax" in column 1 and store column 2 in an array called "Syntax"
def getSyntax(input_csv):
    Syntax = []
    with open(input_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 1 and row[0] == "Syntax":  # Check if row has at least 2 elements
                Syntax.append(row[1])
    return Syntax

#print(getCN(input_csv))
#print(getLdapDisplayName(input_csv))
#print(getSize(input_csv))
#print(getUpdatePrivilege(input_csv))
#print(getUpdateFrequency(input_csv))
#print(getAttributeId(input_csv))
#print(getSystemIdGuid(input_csv))
#print(getSyntax(input_csv))

# Open the output CSV file, add the contents of each array to new columns in the output CSV file'
with open(output_csv, 'w', newline='') as out_f:
    writer = csv.writer(out_f)
    writer.writerow(["CN", "Ldap-Display-Name", "Size", "Update Privilege", "Update Frequency", "Attribute-Id", "System-Id-Guid", "Syntax"])
    for i in range(len(getCN(input_csv))):
        writer.writerow([getCN(input_csv)[i], getLdapDisplayName(input_csv)[i], getSize(input_csv)[i], getUpdatePrivilege(input_csv)[i], getUpdateFrequency(input_csv)[i], getAttributeId(input_csv)[i], getSystemIdGuid(input_csv)[i], getSyntax(input_csv)[i]])
