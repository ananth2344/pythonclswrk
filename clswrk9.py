from abc import ABC, abstractmethod
from datetime import datetime
class User(ABC):
    def __init__(self, name, join_year):
        self.name = name
        self.join_year = join_year

    def years_on_platform(self):
        current_year = 2025
        return current_year - self.join_year

    @abstractmethod
    def show_role(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.show_role()}) has been using the platform for {self.years_on_platform()} years."

class Customer(User):
    def show_role(self):
        return "Customer"
class Vendor(User):
    def show_role(self):
        return "Vendor"
customer1 = Customer("Alice", 2020)
vendor1 = Vendor("Bob", 2018)
print(customer1)
print(vendor1)
