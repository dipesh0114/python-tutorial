class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"  
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"


class electricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size   

    def fuel_type(self):
        return "Electric charge"
       


my_car = Car("Toyota", "Corolla")
# print(my_car.__brand)  
print(my_car.model)  

my_new_car = Car("Honda", "Civic")
# print(my_new_car.__brand)  


print(my_car.full_name())
print(my_new_car.full_name())

my_tesla = electricCar("Tesla", "Model S", "100kwh")
# print(my_tesla.__brand)  
print(my_tesla.get_brand())  
print(my_tesla.model)  
print(my_tesla.battery_size)

print(my_tesla.fuel_type())
print(my_car.fuel_type())

print(Car.total_cars)  # Output the total number of cars created

