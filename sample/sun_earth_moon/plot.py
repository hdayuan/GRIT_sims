import numpy as np
import matplotlib.pyplot as plt

dat = np.loadtxt('/Users/henryyuan/Documents/Github/GRIT/sample/sun_earth_moon/data_in_mat/Earth', skiprows=1).T

t, a, e, i, W, w, f, obl = dat
plt.scatter(t, np.degrees(obl))
plt.show()

plt.clf()
plt.scatter(t,a)
plt.show()