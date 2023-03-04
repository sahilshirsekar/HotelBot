class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}.")
        print(f"Today, we have {self.cuisine_type} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!!")

restaurant = Restaurant("Family-Friendly", "Indian")
restaurant.describe_restaurant()
restaurant.open_restaurant()