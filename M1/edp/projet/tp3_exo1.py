from tp2_exo3 import *
from tp3_exo3 import *
from tp2_exo1 import *


def Boundary(elt):
    B = list()
    A = list()
    d = dict()
    i = 0
    be2e = list()
    for e in elt:
        (v1, v2, v3) = e
        e1 = set([v2, v3])
        e2 = set([v3, v1])
        e3 = set([v1, v2])
        d[(v1, v2)] = 3*i + 2
        d[(v2, v3)] = 3*i + 0
        d[(v3, v1)] = 3*i + 1
        if e1 not in B:
            B.append(e1)
        else:
            del(B[B.index(e1)])
            
        if e2 not in B:
            B.append(e2)
        else:
           del(B[B.index(e2)])
            
        if e3 not in B:
            B.append(e3)
        else:
            del(B[B.index(e3)])
        i = i +1   
        
    for k in d:
        l = set(k)
        if l in B:
            be2e.append(d[k])
            
    for b in B:
        a = list(b)
        A.append(a)
  
    return A, be2e
        
      
      
      
# a = np.random.rand(2)
# d = a/np.linalg.norm(a)
# filename = "maillage1.msh"
# vtx = loadVTX(filename)
# elt = loadELT(filename)
# val = np.array([4* np.pi* (d[0]*(vtx[i])[0] + d[1]*(vtx[i])[1]) for i in range(len(vtx))])
# print(val)
# eltb, be2 = Boundary(elt)
# PlotMesh(vtx, elt,  eltb=eltb)
# PlotMesh(vtx, elt,  val = val)
# refine_vtx, refine_elt = Refine(vtx, elt)
# PlotMesh(refine_vtx, refine_elt,  eltb=eltb)
