import numpy as np

dir = "./se_res/data/2body_data/"
val_names = ["t", "rx", "ry", "rz", "vx", "vy", "vz", "ax", "ay", "az", "sx", "sy", "sz", "axt"]
inds = {val_names[i]:i for i in range(len(val_names))}
for i in range(50):
    f = open(dir+"trial_"+str(i)+".npy", 'rb')
    data = np.load(f)
    n = np.shape(data)[1]
    ind =int(3*n/5)
    omega = np.sqrt(data[inds["sz"],ind]**2 + data[inds["sy"],ind]**2 + data[inds["sx"],ind]**2)
    if np.degrees(np.arccos(data[inds["sz"],ind]/omega)) > 70:
        print(i)
        break