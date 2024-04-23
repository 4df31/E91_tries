from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter,MultipleLocator,LinearLocator

from matplotlib import cm
from numpy import pi
import numpy as np

result = np.loadtxt("./data_aer_simulator_12_04_2024_14_56_shift_0.csv",delimiter=',')

n_phase = int(1e2)
phase = np.linspace(0,2,n_phase)
angle = phase


X,Y = np.meshgrid(angle,phase)
f,axs = plt.subplots(subplot_kw={'projection':'3d'},figsize=(8,8))
surf = axs.plot_surface(X,Y,np.array(result),cmap=cm.magma)
axs.set_xlabel("Angle between polarizers",fontsize=10)
axs.set_ylabel("Relative Phase of Bell State",fontsize=10)
axs.set_zlabel("N_anticorrelations/N_same_basis",fontsize=10)
axs.set_zlim([0,1.3])
axs.xaxis.set_major_formatter(FormatStrFormatter('%g $\\pi$'))
axs.xaxis.set_major_locator(MultipleLocator(base=.25))
axs.yaxis.set_major_formatter(FormatStrFormatter('%g $\\pi$'))
axs.yaxis.set_major_locator(MultipleLocator(base=.25))
f.colorbar(surf, shrink=0.5, aspect=5)
plt.show()