def popcsv(file_name,known_list,pos):
    import csv
    with open(file_name,'w',newline='') as file_obj:
        file_popper=known_list.pop(pos-1)
        file_writer=csv.writer(file_obj)
        for row in known_list:
            file_writer.writerow(row)
        return file_popper