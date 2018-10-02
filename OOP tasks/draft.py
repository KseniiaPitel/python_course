import csv

with open("C:\python project\coursera_week3_cars(1).csv") as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    for row in reader:
        if len(row)!=7:

        print(row)

