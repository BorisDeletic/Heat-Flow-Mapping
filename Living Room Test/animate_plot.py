import numpy as np
import matplotlib.pyplot as plt

Heatintensity=np.random.rand(6) #Values controlling scatter colormap
Xs=np.random.rand(6)
Ys=np.random.rand(6)

plt.ion()
fig, ax = plt.subplots()

norm = plt.Normalize(Heatintensity.min(), Heatintensity.max())
sc = ax.scatter(Xs, Ys, c=Heatintensity, s=500, cmap=plt.cm.jet, norm=norm)

plt.draw()
for i in range(20):
    # set coordinates
    sc.set_offsets(np.c_[Xs[(i):(i)+1],\
                        Ys[(i):(i)+1]])
    # set colors
    sc.set_array(Heatintensity[(i):(i)+1])
    # draw and make pause
    plt.pause(1)

plt.ioff()
plt.show()
