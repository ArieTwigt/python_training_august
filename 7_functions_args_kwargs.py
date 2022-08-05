#%%
import math

def calc_multiple_circles(multiplier, *args):
    
    circles_list = []
    for diameter in args:
        surface = (math.pi * (diameter / 2) ** 2) * multiplier
        circles_list.append(surface)
        
    return circles_list
        


#%%
calc_multiple_circles(1,2,3,4, 4, 5, 6, 7, 2, 1, 3, 4)

# %%
def describe_object(**kwargs):
    print(f"{kwargs}")
    for key, value in kwargs.items():
        print(f"My {key} is {value}")
    
#%% 
describe_object(name="Arie", age=50, city="Enschede")

# %%
