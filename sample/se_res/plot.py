import numpy as np
import matplotlib.pyplot as plt

dat = np.loadtxt('/Users/henryyuan/Documents/Github/GRIT/sample/se_res/data_in_mat/Planet', skiprows=1).T
t, a, e, i, W, w, f, ax, ay, az, sx, sy, sz, obl, axt = dat
omegas = np.sqrt(sx**2 + sy**2 + sz**2)
P = 0.4**(3/2)

fig, axs = plt.subplots(3, 1,figsize=(6, 15), sharex=True)
axs[0].scatter(t/P/(10**6),omegas/(2*np.pi/P), color="black",s=1)
axs[0].set_ylabel(r"$\Omega/n$")
axs[1].scatter(t/P/(10**6), np.degrees(obl), color="black",s=1)
axs[1].set_ylabel(r"$\theta$ ($^{\circ}$)")
axs[2].scatter(t/P/(10**6), np.degrees(np.arccos((ax*sx+ay*sy+az*sz)/omegas)), color="black",s=1)
axs[2].set_ylabel(r"$\beta$ ($^{\circ}$)")
axs[2].set_xlabel(r"Time ($10^6$ P)")

plt.savefig("grit_2:1_res.png", dpi=300)