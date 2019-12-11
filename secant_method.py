import numpy as np

def f(x):
	return(np.sin(np.cos(np.exp(x))))

from scipy import optimize

root = optimize.newton(f,-.1)

print("The obtained root is",root)
print("The value of the function at the calculated root",f(root))


