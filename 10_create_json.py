#%%
import json


#%%
configuration_dict = {'city': "UTRECHT",
                      'export': "csv"}

#%%
configuration_str = json.dumps(configuration_dict)


#%%
with open("configuration.json", "w") as file:
    file.write(configuration_str)
# %%
