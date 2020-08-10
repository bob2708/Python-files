import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        try:
            self.body_length, self.body_width, self.body_height = [float(x) for x in body_whl.split('x')]
        except ValueError:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
    
    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"

def is_float(num=None):
    try:
        if not num:
            return False
        float(num)
        return True
    except ValueError:
        return False

def is_photo_valid(photo):
    splited_photo = os.path.splitext(photo)
    if splited_photo[1] and '.' not in splited_photo[0]:
        return True
    return False

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if row['photo_file_name'] and is_photo_valid(row['photo_file_name']) and row['brand'] and is_float(row['carrying']):
                if row['car_type'] == 'car' and (row['passenger_seats_count']).isdigit():
                    car_list.append(Car(row['brand'], row['photo_file_name'], row['carrying'], row['passenger_seats_count']))
                if row['car_type'] == 'truck':
                    car_list.append(Truck(row['brand'], row['photo_file_name'], row['carrying'], row['body_whl']))
                if row['car_type'] == 'spec_machine' and row['extra']:
                    car_list.append(SpecMachine(row['brand'], row['photo_file_name'], row['carrying'], row['extra']))
    return car_list


'''
def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                # print(row)
                if row['photo_file_name'] and '.' in row['photo_file_name'] and row['brand'] and is_float(row['carrying']):
                    if row['car_type'] == 'car' and (row['passenger_seats_count']).isnumeric():
                        car_list.append(Car(row['brand'], row['photo_file_name'], row['carrying'], row['passenger_seats_count']))
                    if row['car_type'] == 'truck':
                        car_list.append(Truck(row['brand'], row['photo_file_name'], row['carrying'], row['body_whl']))
                    if row['car_type'] == 'spec_machine' and row['extra']:
                        car_list.append(SpecMachine(row['brand'], row['photo_file_name'], row['carrying'], row['extra']))
    except (ValueError):	
        False
    return car_list
'''
# print(get_car_list("C:\\Users\\Vova\\Desktop\\test.csv"))