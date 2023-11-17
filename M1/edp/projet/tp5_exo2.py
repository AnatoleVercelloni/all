import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import coo_matrix



def Kloc(vtx, e):

    [x0, y0] = vtx[e[0]]
    [x1, y1] = vtx[e[1]]
    [x2, y2] = vtx[e[2]]
        
    a0 = np.array([x0, y0 ,0])
    a1 = np.array([x1, y1 ,0])
    a2 = np.array([x2, y2 ,0])
   
    n0 = np.cross(a1 - a2, np.zeros(3))
    n1 = np.cross(a0 - a2, np.zeros(3))
    n2 = np.cross(a1 - a0, np.zeros(3))
    
    d20 = a2 - a0
    d12 = a1-a2
    d01 = a0 - a1
    a = 1/2*np.linalg.norm(np.cross((a0-a1), (a1-a2)), 1)
    
    v0 = np.array([np.dot(d12, d12),  np.dot(d20, d12), np.dot(d01, d12)])
    v1 = np.array([np.dot(d12, d20), np.dot(d20, d20), np.dot(d20, d01)])
    v2 = np.array([np.dot(d12, d01), np.dot(d20, d01), np.dot(d01, d01)])

    Kloc = 1/(4*a)*np.array([v0, v1, v2])
        
    return Kloc
    
    
    
def Rig(vtx, elt):
    K = np.zeros((len(vtx), len(vtx)))
    i = 0
    j = 0
    
    for e in elt:
        i = 0
        Kl = Kloc(vtx, e)
        for v1 in e:
            j = 0
            for v2 in e:
                K[v1][v2] += Kl[i][j]
                j = j+1
            i = i+1
    Kcoo = coo_matrix(K)
    return Kcoo
        
        
    
    
    
# a = np.random.rand(2)
# d = a/np.linalg.norm(a)
# filename = "maillage6.msh"
# vtx = loadVTX(filename)
# elt = loadELT(filename)

# K = rig(vtx, elt)

# alpha1 = np.random.rand(2)
# alpha2 = np.random.rand(2)
# beta = np.random.rand(1)

# x = np.random.rand(2)

# alpha1