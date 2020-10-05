# coding: utf-8
import numpy as np
import sys, os

sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
from common.function import sigmoid, softmax


def equation(x, cont):
    return x[0] ** 2 + x[1] ** 2 + cont


def teach_data(samplenumber, cont, randmax, randmin):
    teachx = np.array([(randmax - randmin) * np.random.rand(samplenumber) + randmin,
                       (randmax - randmin) * np.random.rand(samplenumber) + randmin])
    teachf = equation(teachx, cont)
    teach = {"teachx": teachx, "teachf": teachf}

    return teach


def init_network(fv):
    network = {}
    network["W1"] = np.ones((fv.W1size[0], fv.W1size[1]))
    network["W2"] = np.ones((fv.W2size[0], fv.W2size[1]))
    network["W3"] = np.ones((fv.W3size[0], fv.W3size[1]))
    network["b1"] = fv.b1
    network["b2"] = fv.b2
    network["b3"] = fv.b3

    return network


def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


