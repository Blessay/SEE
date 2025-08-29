# Base class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Child class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    # Method to simulate making a call
    def make_call(self, contact):
        return f"📞 Calling {contact} using {self.info()}..."

    # Method to check battery
    def check_battery(self):
        return f"🔋 Battery: {self.battery}%"

    # Method to upgrade storage
    def upgrade_storage(self, new_storage):
        self.storage = new_storage
        return f"💾 Storage upgraded to {self.storage}GB"


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 128, 85)
phone2 = Smartphone("Samsung", "Galaxy S23", 256, 90)

# Test methods
print(phone1.make_call("Alice"))
print(phone1.check_battery())
print(phone2.upgrade_storage(512))
print(phone2.make_call("Bob"))

# Assignment 2
class Vehicle:
    def move(self):
        pass  # Empty method to be overridden by child classes


class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "🚤 Sailing on water"


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

