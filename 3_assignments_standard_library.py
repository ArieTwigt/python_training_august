## Assignments
#%%
import math
import os

## Assignment 1.

#%%
import datetime

# %%
today_date         = datetime.date.today()
next_birthday_date = datetime.date(2022, 4, 1)


# %%
days_until_birthday = (next_birthday_date - today_date).days


print(f"Days until next birthday: {days_until_birthday} days.")

# %%
## b. When the next year of your birthday is not hard-coded
birthday_month = 4
birthday_day   = 1
current_year   = datetime.date.today().year
current_year_birthday = datetime.date(current_year, birthday_month, birthday_day)


#%%
current_date = datetime.date.today()
birthday_passed = current_date > current_year_birthday


if birthday_passed:
    next_year           = current_year + 1
    next_birthday       = datetime.date(next_year, birthday_month, birthday_day)
    days_until_birthday = next_birthday - current_date
    print(f"Days until next birthday: {days_until_birthday} days.")
else:
    next_birthday       = datetime.date(current_year, birthday_month, birthday_day)
    days_until_birthday = next_birthday - current_date
    print(f"Days until next birthday: {days_until_birthday} days.")


## Assignment 2
# %%
diameter = 10
radius   = diameter / 2

surface_circle =  round(math.pow(radius, 2) * math.pi, 2)
print(surface_circle)


#%%
math.pi

## Assignment 3


# %%
os.getcwd()


# %%
files_folders_list = os.listdir()

#%%
print(files_folders_list)

## Assignment 4

# %%
os.mkdir("our_functions")


## Extra. It is also possible to create sub-folders --> 'os.makedirs()' method
#%%
os.makedirs("folder/subfolder")



# %%
