import matplotlib.pyplot as plt
import numpy as np


def printFile(filename):
    fichier = open(filename, "r")
    print (fichier.read())
    fichier.close()
    
def loadVTX(filename):
    fichier = open(filename, "r")
    s =  fichier.read()
    L = s.split()
    if (L[0] != '$Noeuds'):
        print("format error")
        return -1
    n = int(L[1])
    T =  [[float(L[3 + i]), float(L[i+4])] for i in range(0, 3*n, 3)]
    return T
      
     
def loadELT(filename):
    fichier = open(filename, "r")
    s =  fichier.read()
    L = s.split()
    if (L[0] != '$Noeuds'):
        return -1
        print("format error")
    n = int(L[1])
    p = 4 + 3*n
    N = int(L[4 + 3*n] )
    T =  [[int(L[p + 2 + i]), int(L[i+p+3]), int(L[i+p+4])] for i in range(0, 4*N, 4)]
    return T
    
    
# printFile("maillage1.msh")
# loadVTX("maillage1.msh")
# loadELT("maillage1.msh")




