import csv 
with open("file1 copy 2.csv","r") as file_obj:
    file_reader=csv.reader(file_obj)
    file_reader=list(file_reader)
    print(file_reader,"\n")
    for row in file_reader:
        print(row)

