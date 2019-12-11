import numpy as np

def f(x):
	return(np.sin(np.cos(np.exp(x))))
	

def df(x):
	return(-np.exp(x)*np.cos(np.cos(np.exp(x)))*np.sin(np.exp(x)))

from scipy import optimize

root = optimize.newton(f,-.1,fprime = df)

print("The obtained root is",root)
print("The value of the function at the calculated root",f(root))

print("The answer change if we change our initial guess beacuse Newton-Raphson method converge to a root depending on the initial guess")
