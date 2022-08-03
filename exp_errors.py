#%%
numbers_list = [1,2,3,4]

#%% 
numbers_list[5]
# %%


# %%
try:
    numbers_list / numbers_list
except IndexError:
    print("Does not exist, creating it")
    numbers_list.append(1)


# %%
import os

try:
    os.mkdir("folder")
except FileExistsError:
    print("Folder already exists")



# %%
