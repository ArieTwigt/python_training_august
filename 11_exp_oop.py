#%%
class Car:
    pass

#%%
my_instance = Car()
my_second_instance = Car()

# %%
class Car:
    # attributes
    purpose="transport"
    availability="available"
    
    # methods
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
        
    def present_car(self):
        print(f"This is a {self.brand} : {self.model}")
        
    def reserve(self):
        self.availability = "reserved"
        print(f"This car: {self.brand}:{self.model} is reserved")
        
        
    def sold(self):
        self.availability = "sold"
        print(f"This car: {self.brand}:{self.model} is sold")
        
    def change_price(self, amount):
        print(f"Previous price {self.price}")
        self.price += amount
        print(f"New price {self.price}")

# %%
my_car = Car("Volvo", "V40", 10000)
# %%
my_car.brand
# %%
my_car.present_car()
# %%
my_car.purpose

# %%
my_car.availability
# %%
my_car.reserve()
# %%
my_car.availability
# %%
my_car.sold()
#%%
my_car.availability


#%%
my_car.price
# %%
my_car.change_price(1000)
# %%
my_car.price
# %%
my_car.change_price(-5000)
# %%
