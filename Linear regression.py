# The term regression is used when you try to find the relationship between variables.


import matplotlib.pyplot as plt 
from scipy import stats 

x = [6,7,8,9,16,15,5,8,2,10,11,12,18]
y = [99,86,85,86,87,76,66,90,91,111,112,103,95]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept 

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()