# Code conventions

# Main convention
# Explicit is better than implicit
# PEP8
# "Zen of Python"

#%% avoid spaces, underscore
my_name = "Arie"

#%% descriptive variable names
amount = 10
country = "Holland"

#%%
type(amount)

# %%
"-"  * 10
# %%
numbers_list = [1,2,3,4]


## Object has 'methods' and 'attributes'

# %% method, chaining
my_name.upper().replace("A", "U")
# %%
help(str)

## List operations

# %%

# %%
len(numbers_list)
# %%
len(my_name)
# %%
names_list = ["Arie", "Bart", "Cindy", "Arie", "Bart"]

#%% get the unique names
list(set(names_list))
# %%
names_list[0][0]
# %%
'''
Objects:
[] : lists
{} : dictionaries
() : tuples

Operations:
[] : Data section, indexing
{} : String operations
() : Calling an object, using it in a function

'''

#%%
f"My name is {my_name}"

# %%
names_list = ["Arie", "Bart", "Cindy", "Arie", "Bart"]

# %%
names_tuple = ("Arie", "Bart", "Cindy", "Arie", "Bart")


# %%
names_list[0] = "Jim"
print(names_list)
# %%
names_tuple[0] = "Jim"
print(names_tuple)
# %%
names_list.remove("Arie")
# %%
names_list
# %%
my_name.upper()
# %%
