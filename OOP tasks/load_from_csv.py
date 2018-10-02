class CarBase:
    def __init__(self, brand, photo_file_name, carrying):  # brand, carrying
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = "base"

    def __str__(self):
        return self.brand, self.carrying, self.photo_file_name

import csv

with open("C:\python project\origin-file.csv", encoding="utf8") as csv_fd:
    reader = csv.reader(csv_fd, delimiter=';')
    next(reader)  # пропускаем заголовок
    raw_car_list = []
    for row in reader:
        if len(row) == 0:
            continue
        if row[0] == "car":
            new_car = CarBase(brand=row[1], photo_file_name=row[3], carrying=row[5])
            raw_car_list.append(new_car)
        elif row[0] == "truck":
            new_truck = CarBase (brand=row[1], photo_file_name=row[3], carrying=row[5])
            raw_car_list.append(new_truck)
        elif row[0] == "spec_machine":
            new_machine = CarBase (brand=row[1], photo_file_name=row[3], carrying=row[5])
            raw_car_list.append(new_machine)



print(raw_car_list)