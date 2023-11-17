import matplotlib.pyplot as plt
import numpy as np
from exo3 import *


v0 =  np.array([0, np.sqrt(2)])
tol = 0.001
NitMax = 10000

a = 1
b = 100


def f3(x):
    [x1, x2] = x
    return a*x1*x1 + b*x2*x2
    

def GradF3(x):
      [x1, x2] = x
      return np.array([2*a*x1, 2*b*x2]) 
 
def gopt(GradF3, v0, tol, NitMax):
    n = 0
    v = v0
    nv = v0 + np.array([1, 1])
    Lv = list()
    Lv.append(v0)
    bo = 1
    while( n<NitMax and np.linalg.norm(GradF3(v)) > tol ) :
        [x1, x2] = v
        pk = (a*a*x1*x1 + b*b*x2*x2)/(2*(a*a*a*x1*x1 + b*b*b*x2*x2))
        nv = v - pk*GradF3(v)
        Lv.append(v)
        v = nv
        n = n+ 1
    if (np.linalg.norm(GradF3(v)) > tol):
        bo =0 
    return( v, Lv, n, b)
    

( v, Lv, n, b) = gopt(GradF3, v0, tol, NitMax)
print(v)


