# Main UI Design
print("\n\n"," * * * Welcome User * * * ","\n\n")
print(" - - CSV Manipulating Application - - ",'\n\n')
ans="y"
try:
    while ans[0].lower()=="y":
    
        file_name=input("Enter The (Complete Name) Of Your Selected CSV File :- ")
        print("\n\nOK User Please Choose One Of The Options Below : \n(r) To Read\n(w) To Overrwrite\n(a) To Append/Add\n(p) To Remove \n")
        operation=input("Enter Your Choice Here :- ")

        if operation.lower()=="r":
            import readmod
            print("The Contents Of The File Are As : \n")
            readmod.readcsv(file_name,"y")
            print("\n")
        elif operation.lower()=="w":
            import writemod
            print("""Dear User Kindly Input Your Data in format of \"[["row data","row data",...],["row data","row data",...],["row data","row data,..."]]\"\n\n""")
            data_rows=eval(input("Enter Here In (Proper Format) :- "))
            writemod.writecsv(file_name,data_rows)
            print("Data Is Updated!\n")
        elif operation.lower()=="a":
            import appendmod
            print("""Dear User Kindly Input Your Data in format of \"["row data","row data",...]\"\n\n""")
            data_list=eval(input("Enter Here In (Proper Format) :- "))
            appendmod.appendcsv(file_name,data_list)
            print("Data Is Updated!\n")
        elif operation.lower()=="p":
            import readmod
            import popmod
            a=readmod.readcsv(file_name,"n")
            print(a)
            print("The Contents Of The File Are As : \n")
            readmod.readcsv(file_name,"y")
            print("\n")
            pos=int(input("Enter A Number Of The Row That Should Be Removed ! :-"))
            b=popmod.popcsv(file_name,a,pos)
            print(f"{b} Entry Is Removed And Updated File Is : \n")
            readmod.readcsv(file_name,"y")
        else:
            print("Sorry Your Input Was Inappropriate, Please Try Again !")
        ans=input("Do You Want To Continue? (\"y\"/\"n\") :- ")
        print("\n\n")
except Exception as e:
    print("Oops An Error Occured!\n")
    print(f"Error Was '{e}'\n")
    print("Sorry For Inconvenience, Please Try Again!")
finally:
    print("\nThank You User For Trying This Program :)  \n\n - - See You Soon! - -")
