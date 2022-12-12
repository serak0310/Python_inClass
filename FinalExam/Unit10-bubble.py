import matplotlib.pyplot as plt

plt.scatter([1, 2,3,4], [10,30,20,40], s=[30,60,90,120], c=range(4), cmap='jet')
plt.colorbar()
plt.show()