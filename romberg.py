import numpy as np

def f(x):
	return(np.exp(x))

from scipy import integrate


result = integrate.romberg(f,0,1)

print("The value of the integral is",result)
