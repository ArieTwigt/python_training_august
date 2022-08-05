#%% Defining a function
import math
from typing import Tuple

#%%
def calc_circle(diameter: float, rounding: int=1, multiplier: float=1) -> Tuple[float, float]:
    '''
    This is a function that calculates the surface of a circle
    
    parameters:
    * diameter (float/int), required
    
    '''
    
    # verify the inserted data type
    required_types = [int, float]
    if type(diameter) not in required_types:
        raise TypeError("Param 'diameter' should be of type 'int' or 'float'")
    
    # verify the rounding
    if rounding < 0 or type(rounding) != int:
        raise ValueError("Rounding should be larger than 0 and an int")
    
    radius = diameter / 2
    surface_circle = (radius ** 2) * math.pi
    surface_circle_rounde = round(surface_circle, rounding) * multiplier
    return surface_circle_rounde, radius


#%%
my_circle = calc_circle(40,rounding=2)
print(my_circle)

# %%
my_doc_string = '''

This 
is the story of my life

Yours truly

Arie Twigt

'''

#%%
print(my_doc_string)

# %%
help(calc_circle)

# %%
