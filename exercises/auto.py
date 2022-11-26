import time


class Auto:

    def __init__(self, brand, age, mark, color='white'):
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
        return self.age

    def __str__(self):
        return f'{self.brand} * {self.age} * {self.color} * {self.mark}'


class Truck (Auto):

    def __init__(self, brand, age, mark, max_load, color='silver'):
        super().__init__(brand, age, mark, color)
        self.max_load = max_load

    def move(self):
        auto_move = super().move()
        return f'Attention! {auto_move}'

    def time_sleep(func):
        def wrapper(self):
            time.sleep(1)
            res = func(self)
            print(f'{func.__name__}')
            time.sleep(1)
            return res
        return wrapper
    @time_sleep
    def load(self):
        return f'load'

    def __str__(self):
        super.__str__({self.max_load})
        return f'{self.brand} * {self.age} * {self.color} * {self.mark} * {self.max_load}'

class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color='red'):
        super().__init__(brand, age, mark, color)
        self.max_speed = max_speed

    def move(self):
        auto_move = super().move()
        return f'{auto_move} Max speed is {self.max_speed}'

    def __str__(self):
        super.__str__({self.max_speed})
        return f'{self.brand} * {self.age} * {self.color} * {self.mark} * {self.max_speed}'


truck1 = Truck('Volvo', 2, 'silver', 'FH13', '44t')
truck2 = Truck('Ford', 3, 'brown', '1835T HR Air', '30t')
car1 = Car('Honda', 1, 'black', 'Civic', '270 kph')
car2 = Car('Ford', 5, 'red', 'Mustang', '250 kph')

print(truck1)
print(truck1.move())
print(truck1.stop())
print(truck1.load())
print(truck1.birthday())
print(truck2)
print(truck2.move())
print(truck2.stop())
print(truck2.load())
print(truck2.birthday())
print(car1)
print(car1.move())
print(car1.birthday())
print(car2)
print(car2.move())
print(car2.birthday())








