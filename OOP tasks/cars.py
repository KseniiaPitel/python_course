class CarBase:
    def __init__(self, photo_file_name):  # brand, carrying
        self.photo_file_name = photo_file_name

    def get_photo_file_ext(self):
        import os
        dirname, extname = os.path.splitext(self.photo_file_name)
        return extname


basecar = CarBase("C:\python project\python_course\OOP tasks\draft.py")
print(basecar.get_photo_file_ext())


class Car(CarBase):
    def __init__(self, photo_file_name):  # brand, photo_file_name, carrying, passenger_seats_count
        super().__init__(photo_file_name)


car = Car("C:\python project\sample.txt")
print(Car.__dict__)


class Truck(CarBase):
    def __init__(self, body_whl):  # brand, photo_file_name, carrying, body_whl
        self.body_whl = body_whl

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

mytruck = Truck("10x15x11.2")
print(mytruck.get_body_volume())

class SpecMachine(CarBase):
    def __init__(self):  # brand, photo_file_name, carrying, extra
        pass


def get_car_list(csv_filename):
    car_list = []
    return car_list
