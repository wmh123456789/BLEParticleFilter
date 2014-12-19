import math
# import pandas as pd
import numpy as np
import scipy as sc
import scipy.special as special
import scipy.io as io 
import matplotlib.pyplot as plt


a = [1,2,3,4]
b = np.array([[1,2],[3,4]])
c = np.array(list(xrange(1,10)))
d = np.array([1,2,3,2.5,2.2,3.1,4,5])
e = np.array([4,3,3,2.5,4.2,3.1,4,5])

bins = [1,2,3,4,5]
histd = np.histogram(d,[1,2,3,4,5])
histe = np.histogram(e,[1,2,3,4,5])
print histd[0],histe[0]
print histd[0]/(histe[0]+0.0001)
m = {}
m0 = {}
for x in a:
	m0 = {}
	for i,rssi in enumerate(bins[0:-1]):
		print i , rssi
		m0.update({rssi:x+histd[0][i]})
	m.update({x:m0})

print histd[0],histe[0]
print histe[0]/(histd[0]+0.00001) 


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
