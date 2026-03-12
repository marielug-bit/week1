import numpy as np
from scipy import integrate
import random
import time

def integrand(x):
    return x**2

# Compute the integral of the function
result, _ = integrate.quad(integrand, 0, 1)
print("Integral of x^2 from 0 to 1:", result)

arr = np.random.rand(1000000)
print(arr)
start = time.time()
mean = arr.mean()
print(np.mean(arr))
std_np = np.std(arr)
print(std_np)
end = time.time()
print(f'with numpy it took {end -start} seconds ')

from scipy import stats
start = time.time()
mean_scipy = stats.tmean(arr)
std_scipy = stats.tstd(arr)
end = time.time()
print(f'with spicy it took {end -start} seconds ')