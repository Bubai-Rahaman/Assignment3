import numpy as np

def f(x):
	return(np.exp(x))

from scipy import integrate


result = integrate.fixed_quad(f,0,1,n=5)

print("The value of the integral is",result)
