def readcsv(file_name,ask):
    import csv
    with open(file_name,"r") as file_obj:
        data_list=['h','i','t','e','s']
        file_reader=csv.reader(file_obj)
        file_reader=list(file_reader)
        if ask[0].lower()=="y":
            print(file_reader)
            print("\n")
            for rows in file_reader:
                print(rows)
    return file_reader
        # file_reader.append(data_list)
        # print("\n")
        # print(file_reader)
        # print("\n")
        # for rows in file_reader:
        #     print(rows)