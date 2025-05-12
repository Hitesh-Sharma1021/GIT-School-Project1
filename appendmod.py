def appendcsv(file_name,data_list):
    import csv
    with open(file_name,"a",newline='') as file_obj:
        file_writer=csv.writer(file_obj)
        file_writer.writerow(data_list)