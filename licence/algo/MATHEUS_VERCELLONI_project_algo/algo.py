from random import*
import os
from numpy  import *
from math import *
from pylab import *
import timeit
import sys

sys.setrecursionlimit(5000)
MAX = 10**8
PMAX=100

def m(s,i,V,starttime):
	#if(i == 1 and s==1):
		#print("Appel récursif s = " + str(s)+ " i = "+ str(i))
    if (s == 0):
        return 0;
    if (i == 0):
        return MAX
    if (s < 0):
        return MAX
    else:
        #print(timeit.default_timer() - starttime)
        if (timeit.default_timer() - starttime>60):
            print("trop long")
            return 0
        return min(m(s,i-1,V,starttime), (m(s-V[i-1],i,V,starttime)+1)) 

def algo1(nomf):
    (S,k,V)=lecture(nomf)
    starttime = timeit.default_timer()
    res = MAX
    for i in range(1,k+1) : 
        #print(timeit.default_timer() - starttime)
        if (timeit.default_timer() - starttime>60):
            print("trop long")
            break
        #print("for indice = " + str(i))
        res = min(res,m(S,i,V,starttime))
    return res
    
def algo2(nomf):
    (S,k,V)=lecture(nomf)
    tab = zeros((S+1,k+1))
    for i in range(1,S+1):
        for j in range(k+1):
            if (j == 0) :
                tab[i][j] = MAX
            else : 	 
                if(i-V[j-1] < 0) :
                    tab[i][j]=int(min((tab[i][j-1]),MAX+1))
                else : 
                    tab[i][j] = int(min((tab[i][j-1]),tab[i-V[j-1]][j]+1))
    return((int)(tab[S][k]))
    
def glouton(nomf):
    (S,k,V)=lecture(nomf)
    res = 0
    i = k-1
    while (S != 0):
    
        res = res + S//V[i]
        S = S%V[i]
        i = i-1
    #print(res)
    return res
    
    
def lecture(nomf):
    f= open(nomf,'r')
    L=f.readlines()
    V=[]
    S=(int)(L[0].strip())
    k=(int)(L[1].strip())
    for j in range(2,2+k):
        V.append((int)(L[j].strip()))
    #print ("S="+str(S)+"    V="+str(V))
    f.close()
    return (S,k,V)
    
    
def genere_cap_ex(nomf,S,k,d):
    f=open(nomf,'w')
    f.write(str(S)+'\n')
    f.write(str(k)+'\n')
    L=[]
    for i in range(k-1):
        L.append(d**(i+1))
    L=sorted(L)
    f.write(str(1)+'\n')
    for i in range(k-1):
        f.write(str(L[i])+'\n')
    f.close
    
def genere_cap_rand(nomf,S,k):
    f= open(nomf,'w')
    f.write(str(S)+'\n')
    f.write(str(k)+'\n')
    L=[]
    while (len(L)!=k):
        x=2+(int)((PMAX-2)*random())
        if x not in L:
            L.append(x)
    L=sorted(L)
    f.write(str(1)+'\n')
    for i in range(k-1):
        f.write(str(L[i])+'\n')
    f.close()
    
    

def test_glouton_compatible(k,V):
    if (k>=3):
        for S in range(V[3]+2,V[k-1]+V[k]-1):
            for j in range(0,k):
                if ((V[j]<S) and (glouton(S,k,V)>1+glouton(S-V[j],k,V))):
                    return 0
    return 1