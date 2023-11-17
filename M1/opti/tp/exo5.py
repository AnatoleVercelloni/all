import matplotlib.pyplot as plt
import numpy as np
from exo2 import *
from exo3 import *
from exo4 import *

v0 =  np.array([0, np.sqrt(2)])
tol = 0.001
NitMax = 10000

def g(x):
    [x1, x2] = x
    return x1*x1 + 2*x2*x2
    
def GradG(x):
    [x1, x2] = x
    return np.array([2*x1, 2*x2])



L = {1/3 - 0.01, 1/3, 1/3 + 0.01, 0.9999}
for itol in L:
    plot_xk(GradG, g, v0, rho, tol, NitMax)
