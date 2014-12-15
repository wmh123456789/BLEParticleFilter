import numpy as np
import scipy as sc
import scipy.io as io 
import matplotlib.pyplot as plt  


a = np.ones((2,2))
b = np.array([[1,2],[3,4]])
print b

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

bm = [np.mean(b[i]) for i in [0,1]]
print bm