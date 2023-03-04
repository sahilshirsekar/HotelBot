class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles in it.")

    def update_odometer(self, mileage):  #m2 : modifying the car attribute by creating method 
        if mileage >= self.odometer_reading :
            self.odometer_reading= mileage
        else :
            print("You can't roll back the odometer value.")

    def increment_odometer(self, miles): #m3: incrementing the value of attribute
        self.odometer_reading += miles
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23 #m1 : directly modifying the attribute through an instance.
my_new_car.read_odometer()
my_new_car.update_odometer(25000)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()