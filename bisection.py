import numpy as np

def f(x):
	return(np.sin(np.cos(np.exp(x))))


from scipy import optimize

root = optimize.bisect(f,-1,1)

print("One root of the given equation is",root)

print("The value of the function at the calculated root",f(root))


print("Functional value at calculated root is not zero because bisection method does not give exact root. It gives a value close to the actual root depending on the preceission we want. Also computer can not differenciate number between 0 and smallest machine number")
