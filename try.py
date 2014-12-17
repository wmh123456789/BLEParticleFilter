import math
# import pandas as pd
import numpy as np
import scipy as sc
import scipy.special as special
import scipy.io as io 
import matplotlib.pyplot as plt


a = np.ones((2,2))
b = np.array([[1,2],[3,4]])
c = np.array(list(xrange(1,10)))
d = np.array([1,2,3,2.5,2.2,3.1,4,5])

hist= np.histogram(d,[1,2,3,4,5])
print hist[0]


# Save mat related
# dic = {
# 	'x':[1,2,3,4],
# 	'y':[5,6,7,8],
# 	'a':a,
# 	'b':b
# }
# io.savemat('test.mat',dic)

# plt.bar(left = (0,1),height = (1,0.5),width = 0.35)
# plt.show()

# print special.gamma([1,2,3])
