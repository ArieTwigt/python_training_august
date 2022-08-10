#%%
import pytest
from exp_decorators import calc_interest, print_interest, inflation_adjust


#%%
def test_calc_interest():
    assert calc_interest(100, 0.05, 1) == 105.0
    assert round(calc_interest(100, 0.05, 5), 2) == 127.63
    
    
#%%
def test_inflation_adjusted():
    assert inflation_adjust(calc_interest(100, 0.05, 1)) == 102.49999999999999
    assert inflation_adjust(calc_interest(100, 0.05, 1)) == 10000