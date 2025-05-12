def writecsv(file_name):
    import csv
    with open(file_name,"w",newline='') as file_obj:
        data_row=[1,2,3,4,5]
        data_rows=[
            ['H','S'],
            ['N','R'],
            ['A','K','S'],
            ['S','M'],
            [1,2,3,4,5,6,7,8,9,0]
        ]
        file_writer=csv.writer(file_obj)
        file_writer.writerow(data_row)
        file_writer.writerows(data_rows)

# with open("file1 copy 2.csv","r") as file_obj:
#     file_reader=csv.reader(file_obj)
#     file_reader=list(file_reader)
#     print(file_reader)
#     print("\n")
#     for rows in file_reader:
#         print(rows)
