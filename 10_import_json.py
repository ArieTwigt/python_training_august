#%%
import json

#%%
with open("configuration.json", "r") as file:
    configuration = file.read()
    
#%%
configuration_dict = json.loads(configuration)
# %%
configuration_dict['city']
# %%
