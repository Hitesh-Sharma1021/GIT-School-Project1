def appendcsv(file_name):
    import csv
    with open(file_name,"a",newline='') as file_obj:
        data_list=[1,2,3,4,5]
        file_writer=csv.writer(file_obj)
        file_writer.writerow(data_list)
    # reading block
# with open("file1 copy.csv","r") as file_obj:
#     file_reader=csv.reader(file_obj)
#     file_reader=list(file_reader)
#     print(file_reader)
#     print("\n")
#     for rows in file_reader:
#         print(rows)