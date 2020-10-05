# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
import fixed_value as fv
import equation as eq
from mpl_toolkits.mplot3d import Axes3D

def teach_data(samplenumber, cont, randmax, randmin)

    teachx0 = (randmax - randmin) * np.random.rand(samplenumber) + randmin
    teachx1 = (randmax - randmin) * np.random.rand(samplenumber) + randmin
    teachf = eq.equation(teachx0, teachx1, cont)

    return teachf

# fixed_value = fv.fixed_value()
# samplenumber = fixed_value.test_samplenumber
# cont = fixed_value.cont
# randmax = fixed_value.randmax
# randmin = fixed_value.randmin
#
# teachx0 = (randmax - randmin) * np.random.rand(samplenumber) + randmin
# teachx1 = (randmax - randmin) * np.random.rand(samplenumber) + randmin
# # teachx0 = np.arange(-3,3,0.1)
# # teachx1 = np.arange(-3,3,0.1)
#
# teachf = eq.equation(teachx0, teachx1, cont)
#
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot(teachx0, teachx1, teachf, marker="o", linestyle="none")
# plt.show()