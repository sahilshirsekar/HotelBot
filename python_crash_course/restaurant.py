class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}.")
        print(f"Today, we have {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!!")

    def number_of_served(self):
        print(f"Today, we served {self.number_served} customers.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, day_of_busines):
        self.number_served += day_of_busines

restaurant = Restaurant("Family-Friendly", "Indian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 45
restaurant.number_of_served()

restaurant.set_number_served(60)
restaurant.number_of_served()

restaurant.increment_number_served(30)
restaurant.number_of_served()