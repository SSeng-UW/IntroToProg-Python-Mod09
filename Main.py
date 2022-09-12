# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# SSeng,9.4.2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #


# TODO: Import Modules
if __name__ == "__main__":
    from FileProcessor import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
    from DataClasses import Employee as Emp
    import DataClasses as DC
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
strFileName = "EmployeeData.txt"
lstTable = []
lstFileData = Fp.read_data_from_file(strFileName)
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2]. strip()))


while(True):
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    choice_str = Eio.input_menu_options()
    # Show user current data in the list of employee objects
    if choice_str == '1':
        Eio.print_current_list_items(lstTable)
        continue
    # Let user add data to the list of employee objects
    elif choice_str == '2':
        lstTable.append(Eio.input_employee_data())
        continue
    # let user save current data to file
    elif choice_str == '3':
        Fp.save_data_to_file(strFileName, lstTable)
        print("Data Saved!")
        continue
    # Let user exit program
    elif choice_str == '4':
        print("Thank You, Goodbye!")
        break