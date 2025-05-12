# Read Module
'''
import readmod
# readmod.readcsv("file1.csv","y")
a=readmod.readcsv("file1 copy.csv","n")
# readmod.readcsv("file1 copy.csv","y")
# readmod.readcsv("file1 copy 2.csv","n")
'''
# Write Module
'''
import writemod
writemod.writecsv("file1 copy 2.csv")
'''
# Append Module
'''
import appendmod
appendmod.appendcsv("file1 copy.csv")
'''
# Pop Module
'''
import popmod
print(a)
b=popmod.popcsv("file1 copy.csv",a,3)
print(b)
'''
# Main UI Design
ans="1"
try:
    while ans[0].lower()=="y":
    
        print("\n\n"," * * * Welcome User * * * ","\n\n")
        print(" - - CSV Manipulating Application - - ",'\n\n')
        file_name=input("Enter The (Complete Name) Of Your Selected CSV File :- ")
        print("\n\nOK User Please Choose One Of The Options Below : \n(r) To Read\n(w) To Overrwrite\n(a) To Append/Add\n(p) To Remove \n")
        operation=input("Enter Your Choice Here :- ")

        if operation.lower()=="r":
            pass
        elif operation.lower()=="w":
            pass 
        elif operation.lower()=="a":
            pass 
        elif operation.lower()=="p":
            pass 
        else:
            print("Sorry Your Input Was Inappropriate, Please Try Again !")
        ans=input("Do You Want To Continue? (\"y\"/\"n\")")
except Exception as e:
    print("Oops An Error Occured!\n")
    print(f"Error Was {e}\n")
    print("Sorry For Inconvenience, Please Try Again!")
else:
    print("Something Wrong Happened!, Please Try Again.")
finally:
    print("Thank You User For Trying This Program :)  \n - - See You Soon! - -")
