import matplotlib.pyplot as plt
import numpy as np




def Refine(vtx, elt):
    print(vtx)
    print(elt)
    refined_elt = list()
    refined_vtx = vtx
    k = len(vtx)
    for e in elt:
        (v1, v2, v3) = e
        
        v4 = k
        cv4 = [(vtx[v1][0] + vtx[v2][0])/2, (vtx[v1][1] + vtx[v2][1])/2]

        if cv4 not in refined_vtx:
            refined_vtx.append(cv4)
        else:
            v4 = refined_vtx.index(cv4)
            k = k-1
            
        v5 = k+1
        cv5 = [(vtx[v1][0] + vtx[v3][0])/2, (vtx[v1][1] + vtx[v3][1])/2]
        if cv5 not in refined_vtx:
            refined_vtx.append(cv5)
        else:
            v5 = refined_vtx.index(cv5)
            k = k-1
            
        v6 = k+2
        cv6 =[(vtx[v2][0] + vtx[v3][0])/2, (vtx[v2][1] + vtx[v3][1])/2]
        if cv6 not in refined_vtx:
           refined_vtx.append(cv6)
        else:
            v6 = refined_vtx.index(cv6)
            k = k-1
           
        refined_elt.append([v1, v4, v5])
        refined_elt.append([v2, v4, v6])
        refined_elt.append([v5, v4, v6])
        refined_elt.append([v5, v3, v6])
        
        k = k+3
    return refined_vtx, refined_elt


