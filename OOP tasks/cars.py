class CarBase:
    def __init__(self, brand, photo_file_name, carrying):  # brand, carrying
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def __str__(self):
        return self.brand


    def get_photo_file_ext(self):
        import os
        dirname, extname = os.path.splitext(self.photo_file_name)
        return extname


#basecar = CarBase("Nisan", "C:\python project\python_course\OOP tasks\draft.py", 2.5)
#print(basecar.get_photo_file_ext())
#print(basecar.carrying)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying, passenger_seats_count)
        self.car_type = "car"


#car = Car("C:\python project\sample.txt")
#print(Car.__dict__)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = "truck"

    def get_body_volume(self):
        whl = self.body_whl
        if whl == "":
            body_width = 0
            body_height = 0
            body_length = 0
            body_volume = body_width * body_height * body_length
            return body_volume

        else:
            whl = whl.split('x')
            body_width = float(whl[0])
            body_height = float(whl[1])
            body_length = float(whl[2])
            body_volume = body_width * body_height * body_length
            return body_volume

#mytruck = Truck("10x15x11.2")
#print(mytruck.get_body_volume())

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    import csv
    f = open(csv_filename, 'r')

    car_list = []
    with f:
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            next(reader)
            car_list = row
            if car_list[0] == "car":
                new_car = Car(car_list[2], car_list[3], car_list[5])
                print(new_car)
            print(car_list[0])

    return car_list

print(get_car_list("C:\python project\coursera_week3_cars(1).csv"))