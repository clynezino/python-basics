import numpy
import matplotlib.pyplot as plt 

x = numpy.random.uniform(0.0, 100.0, 1000000)

plt.hist(x, 100)
plt.show()