from exercises import time


class Auto:

    def __init__(self, brand, age, color, mark):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark

    def move(self):
        return 'move'

    def stop(self):
        return 'stop'

    def birthday(self):
        self.age += 1


class Truck (Auto):

    def __init__(self, brand, age, color, mark,  max_load,):
        super().__init__(self, brand, age, color, mark)
        self.max_load = max_load

    def move(self):
        auto_move = super().move()
        return 'Attention!' + auto_move


def time_sleep(func):
    def wrapper(*arg):
        time.sleep(1)
        result = func(*arg)
        time_sleep(1)
        print(f'{func.__name__}')
        return result
    return wrapper


@time_sleep
def __load__(self):
    print('load')

class Car:
    def __init__(self, brand, age, color, mark,  max_speed):
        super().__init__(self, brand, age, color, mark)
        self.max_speed = max_speed

    def move(self):
        auto_move = super().move()
        return auto_move + 'max speed is' + self.max_speed


truck1 = Truck('Volvo', 2, 'silver', 'FH13', '44t')
truck2 = Truck('Ford', 3, 'brown', '1835T HR Air', '30t')
car1 = Car('Honda', 1, 'black', 'Civic', '270 kph')
car2 = Car('Ford', 5, 'red', 'Mustang', '250 kph')

print(truck1)
print(truck1.move())
print(truck1.stop())
print(truck2)
print(truck2.move())
print(truck2.stop())
print(car1)
print(car1.move())
print(car2)
print(car2.move())









