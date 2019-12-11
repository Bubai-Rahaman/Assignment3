import numpy as np
from scipy import integrate

def f(x):
	return(np.exp(x))

x = np.linspace(0,1,100)

result = integrate.simps(f(x),x)

print("The value of the integration is",result)
