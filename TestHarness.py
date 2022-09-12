# ---------------------------------------------------------- #
# Title: TestHarness
# Assignment 9
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SSeng,9.4.2022,Modify Script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # data classes
    from FileProcessor import FileProcessor as Fp  # processing classes
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp("Bob", "Smith")
objP2 = Emp("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(line)
for row in lstTable:
    print(row.to_string(), type(row))

# Test IO classes
# TODO: create and test IO module
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())