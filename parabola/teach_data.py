# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
import fixed_value as fv

fixed_value = fv.fixed_value()
samplenumber = fixed_value.test_samplenumber
gravity = fixed_value.gravity

teacht = np.random.rand(samplenumber)
teachv0x = 5*np.random.rand(samplenumber)
teachv0z = 5*np.random.rand(samplenumber)
# teachv0x = [5] * samplenumber
# teachv0z = [3] * samplenumber
teachx0 = [0] * samplenumber
teachz0 = teachx0

teachxt = teachx0 + teacht * teachv0x
teachzt = teachz0 + teacht * teachv0z - gravity * teacht*teacht / 2

plt.plot(teachxt,teachzt,"o")
plt.show()