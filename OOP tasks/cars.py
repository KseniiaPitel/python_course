class CarBase:
    def __init__(self, brand="", photo_file_name="", carrying=0.0):  # brand, carrying
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def __str__(self):
        return self.brand, self.photo_file_name, self.carrying

    def get_photo_file_ext(self):
        import os
        dirname, extname = os.path.splitext(self.photo_file_name)
        return extname


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=0):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = "car"

    def __str__(self):
        return self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = "truck"

    body_width = 0
    body_height = 0
    body_length = 0

    def __str__(self):
        return self.brand, self.photo_file_name, self.carrying, self.body_whl

    def get_body_volume(self):
        whl = self.body_whl
        if whl == "":
            body_width = 0
            body_height = 0
            body_length = 0
            body_volume = body_width * body_height * body_length
            return float(body_volume)

        else:
            whl = whl.split('x')
            body_width = float(whl[0])
            body_height = float(whl[1])
            body_length = float(whl[2])
            body_volume = body_width * body_height * body_length
            return float(body_volume)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra=""):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"

    def __str__(self):
        return self.brand, self.photo_file_name, self.carrying, self.extra


def get_car_list(csv_filename):
    import csv
    try:
        with open(csv_filename, encoding="utf8") as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)
            car_list = []
            for row in reader:
                    if len(row) != 7:
                        continue
                    if row[0] == "car":
                        new_car = Car(brand=row[1], photo_file_name=row[3], carrying=float(row[5]), passenger_seats_count=int(row[2]))
                        car_list.append(new_car)
                    elif row[0] == "truck":
                        new_truck = Truck(brand=row[1], photo_file_name=row[3], carrying=float(row[5]), body_whl=row[4])
                        car_list.append(new_truck)
                    elif row[0] == "spec_machine":
                        new_machine = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=float(row[5]), extra=row[6])
                        car_list.append(new_machine)

            return car_list
    except FileNotFoundError:
        print("File not found")


print(get_car_list("C:\python project\origin-file.csv"))
#print(get_car_list("C:\python project\coursera_week3_cars(1).csv"))

