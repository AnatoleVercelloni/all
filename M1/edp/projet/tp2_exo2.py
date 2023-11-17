import matplotlib.pyplot as plt
import numpy as np


def GenerateMesh(filename, nx, ny, lx, ly):
    x = np.linspace(0, lx, nx+1)
    y = np.linspace(0, ly, ny + 1)
    file = open(filename, "w")
    file.write('$Noeuds\n')
    file.write(str(2*nx*ny) +"\n")
    n = 0
    for j in y:
        for i in x:
            file.write(str(n) + " ")
            file.write(str(i)+ " ")
            file.write(str(j) + "\n")
            n = n+1
    file.write('$FinNoeuds\n')
    file.write('$Elements\n')
    file.write(str(2*nx*ny) +"\n")
    j = 0
    k = -1
    for i in range(2*nx*ny):
        if (i%(nx*ny) == 0):
            k= k +1
        if (i%2==0):
            file.write(str(i)+" "+str(j + k) + " " + str(j + k + 1) + " " + str(j + k + 2 + nx) + "\n")
           
        else:
            file.write(str(i)+" "+str(j + k ) + " " +str(j + k  + 1 + nx) + " " + str(j + k + 2 + nx) + "\n")
            j = j+1
    file.write('$FinElements\n')
    
# GenerateMesh("mechtest.msh", 3, 2, 3, 2)