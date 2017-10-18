#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @description:
        二次规划的小例子


 @Time       : 17/10/18 下午7:12
 @Author     : guomianzhuang
"""
from cvxopt import solvers, matrix
import numpy as np

P = matrix(np.diag([1.0, 0]))
q = matrix(np.array([3.0, 4]))
G = matrix(np.array([[-1.0, 0], [0, -1], [-1, -3], [2, 5], [3, 4]]))
h = matrix(np.array([0.0, 0, -15, 100, 80]))

sol = solvers.qp(P, q, G, h)
print(sol['x'])
