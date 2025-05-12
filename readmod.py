def readcsv(file_name,ask):
    import csv
    with open(file_name,"r") as file_obj:
        a=0
        file_reader=csv.reader(file_obj)
        file_reader=list(file_reader)
        if ask[0].lower()=="y":
            for rows in file_reader:
                a+=1
                print(f"{a})",rows)
    return file_reader