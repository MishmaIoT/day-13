
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.available = True

class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model and car.available:
                car.available = False
                print(f"Rented {make} {model} from {self.name}.")
                return
        print(f"{make} {model} not available for rent at {self.name}.")

    def return_car(self, make, model):
        for car in self.cars:
            if car.make == make and car.model == model and not car.available:
                car.available = True
                print(f"Returned {make} {model} to {self.name}.")
                return
        print(f"No record found for {make} {model} at {self.name}.")

# Correct instantiation and usage
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

rental_agency = RentalAgency("Rent-A-Car")
rental_agency.add_car(car1)
rental_agency.add_car(car2)

rental_agency.rent_car("Toyota", "Camry")
rental_agency.return_car("Toyota", "Camry")


