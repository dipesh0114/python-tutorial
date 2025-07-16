class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"  
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_info():
        return "cars are a common mode of transportation"

    @property
    def model(self):
        return self.__model

class electricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size   

    def fuel_type(self):
        return "Electric charge"
    
    @staticmethod
    def general_info():
        return "cars are a electric mode of transportation"
       


my_car = Car("Toyota", "Corolla")
my_car.__brand = "city"  # This will not change the private attribute
# print(my_car.__brand)  
# print(my_car.__model)  

my_new_car = Car("Honda", "Civic")
# print(my_new_car.__brand)  


print(my_car.full_name())
print(my_new_car.full_name())

my_tesla = electricCar("Tesla", "Model S", "100kwh")
# print(my_tesla.__brand)  
print(my_tesla.get_brand())  
# print(my_tesla.__model)  
print(my_tesla.battery_size)

print(my_tesla.fuel_type())
print(my_car.fuel_type())

print(Car.total_cars)  # Output the total number of cars created

print(Car.general_info())  # Output general information about cars
print(electricCar.general_info())  # Output general information about electric cars

print(my_car.model)  # Accessing the model property

print(isinstance(my_tesla, electricCar))  # Check if my_tesla is an instance of electricCar
print(isinstance(my_tesla, Car))  # Check if my_tesla is also an instance of Car

class Battery:
    def battery_info(self):
        return "This is a battery for electric cars"

class Engine:
    def engine_info(self):
        return "This is an engine for electric cars"

class ElectricCarTwo(Car, Battery, Engine):  
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_new_tesla = ElectricCarTwo("Tesla", "Model X", "120kwh")
print(my_new_tesla.battery_info())              
print(my_new_tesla.engine_info())              

