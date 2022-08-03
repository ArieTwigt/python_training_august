### Assignments

## 1

#%%
from typing import Iterable


person_1 = {"name": "Arie", 
            "age": 35,
            "hobbies": ['mountainbike', 'football', 'cooking']}

#%%
person_1 = {}
person_1['name']    = "Arie"
person_1['age']     = 35
person_1['hobbies'] = ['mountainbike', 'football', 'cooking']


## 2
#%%
person_2 = {}
person_2['name']    = "Mary"
person_2['age']     = 33
person_2['hobbies'] = ['history', 'tennis', 'cooking']

family_dict            = {}
family_dict['name']    = 'Twigt'
family_dict['members'] = [person_1, person_2]



## Bonus
# %% # bonus 1 --> Add another person
person_3 = {}
person_3['name']    = "Baby"
person_3['age']     = 0
person_3['hobbies'] = ['crawling', 'crying', 'eeting']


# code?
#%%
family_dict['members'].append(person_3)


#%% # bonus 2 --> remove a hobby of a person
family_dict['members'][0]['hobbies'].remove("football")

#%%
family_dict['members'][0]['hobbies'][0]


my_list = ['history', 'tennis', 'cooking']
# %%
my_list.pop(0)


#%% # bonus 3 --> Increase the age of a person
family_dict['members'][0]['age'] += 2

# %%


### Dict comprehension
#%%
name_list = ['Arie', 'Mary', 'Jane']
age_list  = [30, 40, 50]
city_list = ['Amsterdam', 'Rotterdam', 'Utrecht']
# %%

# %% Dict comprehension
people_dict = { # constructing the keys and values
                name :{"person_name": name, 
                       "person_age": age,
                       "person_city": city}

                # loop trough the items
                for name, age, city

                # the iterables (list) to look for the values
                in zip(name_list, age_list, city_list)
                }



