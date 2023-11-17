import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from tp2_exo1 import *
from tp5_exo1 import *
from tp5_exo2 import *


def CCmpt(elt):
    # print(elt)
    d = dict()
    i  = 0
    graph = [[0 for e in elt  ] for e in elt]
    for e in elt:
        (v1, v2, v3) = e
        if (v1 not in d):
            d[v1] = [i]
        else:
            d[v1].append(i)
            
        if (v2 not in d):
            d[v2] =  [i]
        else:
            d[v2].append(i)
            
        if (v3 not in d):
            d[v3] =  [i]
        else:
            d[v3].append(i)
            
        i = i+1
    
    for k in d:
        for u in d[k]:
            for v in d[k]:
                graph[u][v] = 1
            
    
    graph = csr_matrix(graph)
    # print(graph)
    cc = n_components, labels = connected_components(csgraph=graph, directed=False, return_labels=True)
    # print(cc)
    return n_components, labels
    
    
    
    
# a = np.random.rand(2)
# d = a/np.linalg.norm(a)
# filename = "maillage1.msh"
# vtx = loadVTX(filename)
# elt = loadELT(filename)
# vtx = [[0., 0.], [1., 0.], [1., 1.], [0., 1.]]
# elt = [[0,3,2],  [0, 2,1]]

# K = Rig(vtx, elt)


# print(K.todense())

