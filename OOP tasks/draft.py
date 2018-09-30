car_type = property()


@car_type.setter
def car_type_checker(self, value):
    if value == "car":
        self._car_type = "caaaar"
    else:
        print("Car type can be car, truck or scep_machine")


@car_type.getter
def car_type_checker(self):
    return self._car_type


@property
def cat_type_checker(self, car_type):
    if car_type == "car":
        return self._car_type
    else:
        print("11111")
