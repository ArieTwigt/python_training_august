#%%
my_list = [5, 6, 9, 10, 4, 8]

#%% .sort() is a method of a <list> instance
my_list.sort()


# %% sorted() is a global Python function
my_list = [5, 6, 9, 10, 4, 8]
sorted(my_list)

# %%
my_list_double = [x * 2 for x in my_list]
my_list_double

# %%
my_filtered_list = [x for x in my_list if x > 6]
my_filtered_list

# %% Impirative
person = {}
person['name'] = 'arie'
person['age'] = 50
print(person)

# %% Declaritive
person = {"name": "arie",
          "age": 50}
person

# %%
person['age']
# %% dict, to prevent KeyErrors you can use a DefaultDic
person['city']

# %%
person.keys()
# %%
person.values()
# %%
names_list = ['arie', 'joe', 'jane', 'jim']
ages_list = [50, 40, 30, 20]

#%% zip the lists to a dictonary
person_ages_dict = dict(zip(names_list, ages_list))

# %%
person_ages_dict.keys()
# %%
