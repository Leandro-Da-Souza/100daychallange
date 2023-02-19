from Car import Car


class CarManager:
    def __init__(self):
        self.car_amount = 6
        self.all_cars = []
        self.create_cars()

    def create_cars(self):
        for car in range(0, self.car_amount):
            self.all_cars.append(Car())

    def increase_cars(self):
        for _ in range(0, 2):
            self.all_cars.append(Car())
