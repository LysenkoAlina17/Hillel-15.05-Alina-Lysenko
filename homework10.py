class Transport:
    def __init__(self, view, brand, model, year):
        self.view = view
        self.brand = brand
        self.model = model
        self.year = year

    def say_about_transport(self):
        return f'Hello! This is {self.view}, brand - {self.brand}, model - {self.model}, {self.year} year.'


class Auto(Transport):
    def __init__(self):
        super().__init__("car", "Toyota", "Prius", 2019)
        self.fuel_type = "Бензин"
        self.num_doors = 4

    def say_about_transport(self):
        return f'{super().say_about_transport()}, fuel type - {self.fuel_type}, num doors - {self.num_doors}.'


class Plane(Transport):
    def __init__(self):
        super().__init__("plane", "Boeing", "747", 2015)
        self.airline = "United Airlines"
        self.seating_capacity = 416

    def say_about_transport(self):
        return f'{super().say_about_transport()}, airline - {self.airline}, seating capacity - {self.seating_capacity}.'


class Ship(Transport):
    def __init__(self):
        super().__init__("ship", "MSC", "Magna", 2018)
        self.ship_type = "Контейнеровоз"
        self.max_speed = 25

    def say_about_transport(self):
        return f'{super().say_about_transport()}, ship type - {self.ship_type}, max speed - {self.max_speed}.'


auto = Auto()
plane = Plane()
ship = Ship()

print(auto.say_about_transport())
print(plane.say_about_transport())
print(ship.say_about_transport())
