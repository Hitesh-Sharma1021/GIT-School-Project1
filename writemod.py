def writecsv(file_name,data_rows):
    import csv
    with open(file_name,"w",newline='') as file_obj:
        file_writer=csv.writer(file_obj)
        file_writer.writerows(data_rows)

