#%%
import pandas as pd
import requests
from sqlalchemy import create_engine



#%%
brand = "TESLA"
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand}"

#%%
response = requests.get(endpoint)
# %%
cars_list = response.json()

# %%
cars_df = pd.DataFrame(cars_list)
# %%
cars_df.head()

# %%
con = create_engine("sqlite:///cars.db")
cars_df.to_sql("cars", con=con, if_exists='append')

# %% importing data from a database
model_type = 'MODEL S'

# using params to prevent sql injection
qry = '''
      select kenteken, merk, handelsbenaming, catalogusprijs
      from cars
      where catalogusprijs > 100000
        and handelsbenaming = ?
      '''

#%%
selected_cars_df = pd.read_sql_query(qry, con=con, params=(model_type,) )

# %%
