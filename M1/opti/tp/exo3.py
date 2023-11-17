import matplotlib.pyplot as plt
import numpy as np
from exo2 import *

v0 =  np.array([1, 1])
rho = 1.9999/1000
tol = 0.001
NitMax = 10000


def f2(x):
    [x1, x2] = x
    return x1*x1 + 100*x2*x2
    
def GradF2(x):
     [x1, x2] = x
     return np.array([2*x1, 200*x2])
     
     
def plot_xk(GradF2, f, v0, rho, tol, NitMax):
    (v, Lv, n, b) = gf(GradF2, v0, rho, tol, NitMax)
    Ln = np.array(NitMax)
    plt.plot( Lv)
    plt.show()
    plt.clf()
    plt.plot(list(map(f,  Lv)))
    plt.show()
    plt.plot(list(map(np.linalg.norm,  Lv)))
    plt.show()
    
def gf2(f, GradF, v0, rho, tol, NitMax):
    n = 0
    v = v0
    nv = v0 + [1, 1]
    Lv = list()
    Lv.append(v0)
    b = 1
    while( n<NitMax and np.linalg.norm(GradF(v)) > tol and np.linalg.norm(nv-v) > tol and np.linalg.norm(f2(nv-v))) :
    
        nv = v - rho*GradF(v)
        Lv.append(v)
        v = nv
        n = n+ 1
    if (np.linalg.norm(GradF(v)) > tol):
        b =0 
    return( v, Lv, n, b)
    
     
     
# plot_xk(GradF2, v0, rho, tol, NitMax)
(v, Lv, n, b) = gf(GradF2, v0, rho, tol, NitMax)
(v2, Lv2, n2, b2) = gf2(f, GradF2, v0, rho, tol, NitMax)
print(v, v2)
print(np.linalg.norm(v - v2))
     
    
    
