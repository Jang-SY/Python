#rbm의 probability 구현
'''
vis->hid , hid->vis 확률 구현
'''

import numpy as np
import math as m

class RBM:
    def __init__(self, n_vis, n_hid, W = None, v_bias = None, h_bias = None, numpy_rd = None, frequency = None):
        self.n_vis = n_vis
        self.n_hid = n_hid
        if numpy_rd == None:
            numpy_rd = np.random.RandomState(1234)  # numpy random 객체 생성
        if W == None:
            W = numpy.asarray(
            numpy_rd.poisson(lam=frequency, size=(n_vis, n_hid)), dtype = float)  # poisson distribution 에 의한 weight 초기화
        if v_bias == None:
            v_bias = np.zeros(n_vis)    # v_bias 0으로 초기화
        if h_bias == None:
            h_bias = np.zeros(n_hid)    # h_bias 0으로 초기화

        self.W = W
        self.n_vis = n_vis
        self.n_hid = n_hid

    # sigmoid function
    def sigmoid(self, arr):
        for i in range(len(arr)):
            arr[i] = 1/(1+m.exp(-arr[i]))
        return arr

    # visible -> hidden 의 확률
    def propup(self, vis):
        pre_activation = np.dot(vis, self.W) + self.h_bias
        return [pre_activation, sigmoid(pre_activation)]

    # hidden -> visible 의 확률
    def propdown(self, hid):
        pre_activation = np.dot(hid, self.W.T) + self.v_bias
        return [pre_activation, sigmoid(pre_activation)]
