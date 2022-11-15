import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(projection='3d')



r = [-3, 3]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s,e), color="black")

colors = ['b', 'g', 'r', 'c', 'm', 'y']
for i, (z, zdir) in enumerate(product([-3,3], ['x','y','z'])):
    #print(f"color : {colors[i]}    z: {z}    zdir: {zdir}")
    side = Rectangle((-3, -3), 2, 2, facecolor=colors[i])
    ax.add_patch(side)
    art3d.pathpatch_2d_to_3d(side, z=z, zdir=zdir)

plt.show()
