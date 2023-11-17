import matplotlib.pyplot as plt
import numpy as np
from exo1 import *

n = 10

v0 =  [0.5, 0.5]
rho = 0.5
tol = 0.001
NitMax = 10000


xl = [-5, 5]
yl = [-5, 5]


def f(x, y):
    return x*x + y*y

def GradF(x):
    [x1, x2] = x
    return np.array([2*x1, 2*x2])
    


def gf(GradF, v0, rho, tol, NitMax):
    n = 0
    v = v0
    Lv = list()
    Lv.append(v0)
    b = 1
    while( n<NitMax and np.linalg.norm(GradF(v)) > tol):
    
        nv = v - rho*GradF(v)
        Lv.append(v)
        v = nv
        n = n+ 1
    if (np.linalg.norm(GradF(v)) > tol):
        b =0 
    return( v, Lv, n, b)
    
# level_ligne(f, n, xl, yl)

# print(gf(GradF, v0, rho, tol, NitMax))