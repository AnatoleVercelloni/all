import matplotlib.pyplot as plt
import numpy as np

p = 3


def f(x):
    return np.cos(p*np.pi*x)

def matrix_assembly(N):
    h = 1/N
    K = np.diag(2*N*np.ones(N)) + np.diag(-N*np.ones(N-1),1) + np.diag(-N*np.ones(N-1),-1)
    K[0][0] = N
    K[-1][-1] = N
    
    M = np.diag(h*2/3*N*np.ones(N)) + np.diag(-h/6*np.ones(N-1),1) + np.diag(-h/6*np.ones(N-1),-1)
    K[0][0] = h/3
    K[-1][-1] = h/3
    F = M.dot([f(j*h) for j in range(N+1)])

    
    return K, M, F
    
    
    
    
matrix_assembly(17)

 # a = 1/2*abs(np.cross((x0-x1), (x1-x2)))