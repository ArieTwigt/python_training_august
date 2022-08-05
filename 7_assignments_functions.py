## Assignment 1

#%%
def calc_contents(length, width, hight):
    return length * width * hight

#%% 
calc_contents(2,3,4)    

## Assignment 2

# %%
def capitalize_names(names_list):
    capitalized_names_list = [name.capitalize() for name in names_list]
    return capitalized_names_list

#%%
# define a list of 10 lowercase names
my_names_list = ['aaron', 'bob', 'charlie', 'david', 'erin', 'frank', 'gloria', 'harry', 'ian', 'jane']

capitalize_names(my_names_list)
# %%
