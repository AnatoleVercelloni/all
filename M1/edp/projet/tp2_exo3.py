
import matplotlib
import colorsys
import matplotlib.tri as mtri
import numpy as np
import random
from  tp2_exo2 import *
from  tp2_exo1 import *
from  tp3_exo2 import *





def PlotMesh(vtx, elt, val = list(), eltb = list()):
    x = np.array([(vtx[i])[0] for i in range(len(vtx))])
    y = np.array([(vtx[i])[1] for i in range(len(vtx))])
    

    if (len(val) == 0):
        triang = mtri.Triangulation(x, y, elt)
        plt.triplot(triang)
    else:
        z = val
        colorNames = list(matplotlib.colors.cnames.keys())
        n_components, label = CCmpt(elt)
        Ltri = [[] for _ in range(n_components)]
        triangi = [[]]*n_components
        i = 0
        # print(label)
        for k in label:
            Ltri[k].append(elt[i])
            i = i+1
        # print(Ltri[0])
        for j in range(n_components):
            if (len(val) != 0):
                z = val + 100*i
            triangi[j] = mtri.Triangulation(x, y, Ltri[j])
            plt.tricontour(triangi[j], z, 500, colors=colorNames[random.randint(0, len(colorNames)- 1)] )
        
    # plt.tricontour(triang, z, 500, colors=colorNames[0])
     #plotting the boundary
    if (len(eltb) != 0):
        for e in eltb:
            plt.plot((vtx[e[0]][0], vtx[e[1]][0]), (vtx[e[0]][1], vtx[e[1]][1]), 'r-')
            
    plt.title('mesh')
    plt.show()
    

# a = np.random.rand(2)
# d = a/np.linalg.norm(a)
# filename = "maillage1.msh"
# vtx = loadVTX(filename)
# elt = loadELT(filename)
# val = np.array([4* np.pi* (d[0]*(vtx[i])[0] + d[1]*(vtx[i])[1]) for i in range(len(vtx))])
# print(val)

# PlotMesh(vtx, elt, val)
 # plt.tricontourf(triang, z)