import csv
with open("file1.csv","r") as file_obj:
    data_list=['h','i','t','e','s']
    file_reader=csv.reader(file_obj)
    file_reader=list(file_reader)
    print(file_reader)
    print("\n")
    for rows in file_reader:
        print(rows)
    file_reader.append(data_list)
    print("\n")
    print(file_reader)
    print("\n")
    for rows in file_reader:
        print(rows)