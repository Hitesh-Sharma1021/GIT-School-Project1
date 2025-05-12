print("Hello world")
fnm=input("Enter file name:-")
mode=input("Enter mode:-")
first_file=open(fnm,mode)

a="y"
while a[0].lower()=="y":
    entry=input("Enter a name:-")
    ask=input("Want a next line?")
    first_file.write(entry)
    if ask.lower()=="y":
        first_file.write("\n")
    first_file.close()
    a=input("Do you want to continue? ")