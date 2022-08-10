#%%
import multiprocessing as mp
from custom_modules.calculation_functions import calc_circle


def main():
    pool = mp.Pool(4)
    result = pool.map(calc_circle, [1,2,3,4,5,6,7,8,9,0,9,8,7,67,56,4,2,2])
    print(result)
    
    
if __name__ == "__main__":
    main()