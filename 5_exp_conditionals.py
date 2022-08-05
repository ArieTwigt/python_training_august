#%%
names_list = ['John', 'Jane', 'Jack', 'Jill']
name = "Arie"
age = 21

#%%
if name in names_list or age > 18:
    print("You are welcome")
    print("Welcome")
else:
    print("Youre are not in the list yet")
    names_list.append(name)
    
#%%
print("Proceed with the rest of the code")

#%%
for name in names_list:
    print(name)

# %%
for idx, name in enumerate(names_list):
    print(f"The name {name} is at index {idx}")

# %%
new_names_list = []

for name in names_list:
    new_name = name.replace("J", "X")
    new_names_list.append(new_name)
    
print(new_names_list)

# %%
new_names_list = [name.replace("J", "X") 
                  for name in names_list]
print(new_names_list)

# %%
names_list = ['Dohn', 'Jane', 'Dack', 'Jill']
new_names_list = []

for name in names_list:
    if name[0] == 'D':
        new_name = name.replace('D', 'J')
        new_names_list.append(new_name)
    else:
        new_name = name.replace('J', 'D')
        new_names_list.append(new_name)



#%%
new_names_list = [name.replace('D', 'J')   
                  if name[0] == 'D' 
                  else name.replace('J', 'D') 
                  for name in names_list]

# %%
new_names_list = [name.replace('D', 'J')   
                  for name in names_list
                  if name[0] == 'D' ]

#%%
