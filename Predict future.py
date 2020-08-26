# Now we can use the information we have gathered to predict future values.
# Predict the speed of a 10 years old car:
from scipy import stats 

x = [6,7,8,9,16,15,5,8,2,10,11,12,18]
y = [99,86,85,86,87,76,66,90,91,111,112,103,95]

slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope * x + intercept 

speed = myfunc(10)

print(speed)