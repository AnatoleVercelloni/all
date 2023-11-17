import matplotlib.pyplot as plt
import numpy as np

N = 3
y = np.array([0]*N)
l= 1


def D_mat(N):
    return np.diag(np.concatenate((np.ones(N-1)*-1,np.array([0])))) + np.diag(np.ones(N-1), 1)




def f(x):
    D = np.diag(np.concatenate((np.ones(N-1)*-1,np.array([0])))) + np.diag(np.ones(N-1), 1)
    return 0.5 * np.linalg.norm(x - y)**2 + l * 0.5  *np.linalg.norm(D*x)**2
    
    
    
    
x = np.random.rand(N)

print(f(x))
