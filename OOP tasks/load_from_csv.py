import csv


f = open("C:\python project\coursera_week3_cars(1).csv", 'r')

my_list = []
with f:
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        next(reader)
        if 'truck' in row:
            my_list = row
            print(my_list)


print(type(my_list))






