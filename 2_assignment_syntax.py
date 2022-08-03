## Assignments

# Assignment 1.

#%%
first_name = "Erling"
last_name  = "Haaland"

# (using + instead of an f-string)
#%% a.
full_name = first_name + " " + last_name + " Jr."
print(full_name)

#%% b. Using an f-string
full_name = f"{first_name} {last_name} Jr."
print(full_name)
# %%


## Assignment 2.

#%% a.
full_name_new = f"{first_name[0]}. {last_name} Jr."
print(full_name_new)

# %% b. (in case the seperate variables first_name and last_name are not available)
full_name_list =  full_name.split(" ")
print(full_name_list)
full_name_new = f"{full_name_list[0][0]}. {full_name_list[1]} {full_name_list[2]}"
print(full_name_new)


## Assignment 3

# %% Set the variables
flower_list_1 = ['rose', 'tulip', 'lily']
flower_list_2 = ['dandelion', 'gerbera']

combined_flower_list = flower_list_1 + flower_list_2
print(combined_flower_list)

# %% a
print(combined_flower_list)
combined_flower_list[1] = "daisy"
print(combined_flower_list)

# %% b. In situations in which you are not sure in which position "tulip" is
print(combined_flower_list)
idx = combined_flower_list.index("tulip")
combined_flower_list[idx] = "daisy"
print(combined_flower_list)

# %% c. List comprehension (Best solution) In situations where there are more tulips or there is no tulip at all
combined_flower_list
# %%

# %%
