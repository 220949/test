# coding: utf-8

import numpy as np
import matplotlib.pylab as plt
import fixed_value
from mpl_toolkits.mplot3d import Axes3D
import function as func

fv = fixed_value.fixed_value()
samplenumber = fv.test_samplenumber
cont = fv.cont
randmax = fv.randmax
randmin = fv.randmin
teach = func.teach_data(samplenumber, cont, randmax, randmin)

network = func.init_network(fv)

batch_size = fv.batch_size
train_size = teach["teachf"].shape[0]
batch_mask = np.random.choice(train_size, batch_size)
x_train = teach["teachx"]
f_train = teach["teachf"]
x_batch = np.array([x_train[0,batch_mask],x_train[1,batch_mask]])
t_batch = f_train[batch_mask]

