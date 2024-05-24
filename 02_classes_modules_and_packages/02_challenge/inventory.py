import re

class Inventory():
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def apply_discount(self, func, discount):
        for vehicle in self.vehicles:
            if func(vehicle):
                vehicle.set_discount(discount)

    def search_vehicles(self, model):
        return [vehicle for vehicle in self.vehicles if re.findall(model, vehicle.model)]

    def retrieve_vehicles(self):
        for vehicle in self.vehicles:
            yield vehicle