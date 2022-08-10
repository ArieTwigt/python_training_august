# %% define a decorator that will correct for the inflation
def inflation_adjust(func):
    def wrapper(amount, rate, years):
        return func(amount, rate / 2, years)
    
    return wrapper


#%% define a decorator that prints the intermediate results
def print_interest(func):
    def wrapper(amount, rate, years):
        for year in range(years):
            amount = func(amount, rate, 1)
            print(amount)
        return amount
    return wrapper
        

# %%
@inflation_adjust
@print_interest
def calc_interest(amount, rate, years):
    return amount * (1 + rate) ** years


#%%]
def calc_interest(amount, rate, years):
    return amount * (1 + rate) ** years

if __name__ == '__name__':
    calc_interest(1000, 0.05, 5)


# %%
