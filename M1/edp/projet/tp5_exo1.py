import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import coo_matrix



def Mloc(vtx, e):
    if (len(e) == 3):
        [x0, y0] = vtx[e[0]]
        [x1, y1] = vtx[e[1]]
        [x2, y2] = vtx[e[2]]
        
        a0 = np.array([x0, y0 ,0])
        a1 = np.array([x1, y1 ,0])
        a2 = np.array([x2, y2 ,0])
        
        
        a = 1/2*np.linalg.norm(np.cross((a0-a1), (a1-a2)), 1)

        
        Mloc = a/12*np.ones((3,3))
        Mloc = Mloc + np.diag(a/12*np.ones(3))
        
    if (len(e) == 2):
        gamma = np.sqrt(e[0]*e[0] + e[1]*e[1])
        Mloc = gamma/6*np.ones((2,2))
        Mloc = Mloc + np.diag(gamma/6*np.ones(2))
     
    
    return Mloc
    
    
    
def Mass(vtx, elt):
    M = np.zeros((len(vtx), len(vtx)))
    i = 0
    j = 0
    
    for e in elt:
        i = 0
        Ml = Mloc(vtx, e)
        for v1 in e:
            j = 0
            for v2 in e:
                M[v1][v2] += Ml[i][j]
                j = j+1
            i = i+1
    Mcoo = coo_matrix(M)
    return Mcoo
        
        
    
    
    
 

 
    
