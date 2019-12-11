import numpy as np

def f(x):
	return(np.exp(x))

x = np.linspace(0,1,100)

result = np.trapz(f(x),x)

print("The value of the integral is",result)
