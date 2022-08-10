import math
import time
import multiprocessing as mp

def calc_circle(diameter):
    radius = diameter / 2
    circle_size = math.pow(radius, 2) * math.pi
    print(mp.current_process())
    time.sleep(10)
    return circle_size, radius