import matplotlib.pyplot as plt
import numpy as np
from tp3_exo1 import *


def normal(vtx, elt, b):
    (eltb, be2e) = b
    X = list()
    Y = list()
    U = list()
    V = list()
    z = np.array([0, 0, 1])
    i = 0
    for bi in eltb:
        k = be2e[i]%3
        j = 0
        v3= elt[k][j]
        
        while(v3 in bi):
            v3 = elt[k][j]
            j = j + 1
        
        [v1, v2] = bi
        [x1, y1] = vtx[v1] 
        [x2, y2] = vtx[v2]
        a= np.array([x1 - x2, y1 - y2, 0])
        n = np.cross(a, z)
        g1 = (x1 + x2)/2 - vtx[v3][0]
        g2 = (y1 + y2)/2 - vtx[v3][1]
        X.append((x1 + x2)/2 )
        Y.append((y1 + y2)/2 )
        
        if k%3 == 2:#(np.sign(g1) >=np.sign(n[0]) and np.sign(g2) >=np.sign(n[1])):
            U.append(n[0])
            V.append(n[1])
        else:
            # U.append(n[0]*-1)
            U.append(0)
            # V.append(n[1]*-1)
            V.append(0)
        print(U[i], V[i], X[i], Y[i], k)
        i = i + 1
    plt.quiver(X, Y, U, V)
    PlotMesh(vtx, elt,  eltb=eltb)
    
    
    
filename = "maillage2.msh"
vtx = loadVTX(filename)
elt = loadELT(filename)

# vtx = [[0., 0, ], [1., 0.], [0.5, 0.5], [0., 1.], [1., 1.]]
# elt = [[0, 1, 2], [1, 2, 4], [2, 3, 4], [0, 2, 3]]
b = Boundary(elt)

# PlotMesh(vtx, elt,  eltb=eltb)
normal(vtx, elt, b)