#%%
from sqlalchemy import create_engine

#%%
engine = create_engine('sqlite:///cars.db')

# %%
engine 

# %%
# create a table in the database
qry = '''
      CREATE TABLE stocks
      (date text, 
      trans text, 
      symbol text, 
      qty real, 
      price real)
               '''

#%% Insert a row of data
engine.execute(qry)

# %% Add data to the table
qry_insert = '''
            INSERT INTO stocks 
            VALUES ('2006-01-05','BUY','APPL',80,35.14)
'''

#%%
engine.execute(qry_insert)

# %%
engine.table_names()

# %% fetch data from a database
qry_select = "select * from stocks"

#%%
result = engine.execute(qry_select)

#%%
results = result.fetchall()

# %%
colnames = result.keys()

# %%
