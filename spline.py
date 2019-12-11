import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([1.0,2.0,1.0,0.5,4.0,8.0])
'''
spline fiting'''

spl1 = scipy.interpolate.UnivariateSpline(x,y,k=1)
spl2 = scipy.interpolate.UnivariateSpline(x,y,k=2)
spl3 = scipy.interpolate.UnivariateSpline(x,y,k=3)

xs = np.linspace(0,6,1000)
'''
lagrange
'''
poly = scipy.interpolate.lagrange(x,y)
f = poly(xs)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(xs,f,color = 'pink', label = 'Lagrange interpolate')

plt.plot(xs,spl1(xs),'r-',label = 'linear spline')
plt.plot(xs,spl2(xs),'g-',label = 'Quadratic spline')
plt.plot(xs,spl3(xs),'b-',label = 'Cubic spline')

plt.plot(x,y,'o',color = 'black',label = 'Data point')

plt.legend()
plt.show()
