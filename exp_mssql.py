#%%
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import requests
import pandas as pd

load_dotenv()

#%%




# %%
# 1. Constants
DBSERVER=os.environ.get('DBSERVER')
DBUSER=os.environ.get('DBUSER')
DBPWD=os.environ.get('DBPWD')
DATABASE  = 'Cars'                       #
DRIVER   = 'ODBC Driver 17 for SQL Server'        # ODBC Driver

#%%
name = "Arie"
sentence = f"My name is {name}"
print(sentence)

#%%
name = "Arie"
sentence = "My name is {}".format(name)
print(sentence)


#%%
connectionstring = 'mssql+pyodbc://{uid}:{password}@{server}:1433/{database}?driver={driver}'.format(
        uid=DBUSER,
        password=DBPWD,
        server=DBSERVER,
        database=DATABASE,
        driver=DRIVER.replace(' ', '+'))

#%% 
con = create_engine(connectionstring)

# %%
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
cars_df.to_sql("cars_from_python", con=con, if_exists='append')
# %%
