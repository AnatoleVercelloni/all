from random import*
import os
from numpy  import *
from math import *
from pylab import *
import timeit
import sys

sys.setrecursionlimit(5000)



MAX = 10**8


def lecture(f):
    L=f.readlines()
    V=[]
    S=(int)(L[0].strip())
    k=(int)(L[1].strip())
    for j in range(2,2+k):
        V.append((int)(L[j].strip()))
    print ("S="+str(S)+"    V="+str(V))
    return (S,k,V)

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

def algo1(S,k,V):
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




def algo2(S,k,V):
	tab = zeros((S+1,k+1))

	#print(tab)
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




def glouton(S,k,V):
    res = 0
    i = k-1
    while (S != 0):
    
        res = res + S//V[i]
        S = S%V[i]
        i = i-1
    #print(res)
    return res
    
    
def genere_cap_rand(f,S,k):
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
    return f
    

def test_glouton_compatible(k,V):
    if (k>=3):
        for S in range(V[3]+2,V[k-1]+V[k]-1):
            for j in range(0,k):
                if ((V[j]<S) and (glouton(S,k,V)>1+glouton(S-V[j],k,V))):
                    return 0
    return 1

   
    
def genere_cap_ex(f,S,k,d):
    f.write(str(S)+'\n')
    f.write(str(k)+'\n')
    L=[]
    for i in range(k-1):
        L.append(d**(i+1))
    L=sorted(L)
    f.write(str(1)+'\n')
    for i in range(k-1):
        f.write(str(L[i])+'\n')
    return f
    
PMAX=100

def test(): 
    
    f= open('cap_rand.txt','w')
    genere_cap_rand(f,PMAX,10)
    f= open('cap_rand.txt','r')
    (S,k,V)=lecture(f)
    
    """f1= open('cap_ex.txt','w+')
    genere_cap_ex(f1,10,5,2)
    f1= open('cap_ex.txt','r')
    (S1,k1,V1)=lecture(f1)"""
    print(test_glouton_compatible(k-1,V))
    starttime1 = timeit.default_timer()
    res1=algo1(S,k,V)
    print("The time difference is :", timeit.default_timer() - starttime1)
    print("resalgoI: "+str(res1))
    starttime2 = timeit.default_timer()
    res2=algo2(S,k,V)
    print("The time difference is :", timeit.default_timer() - starttime2)
    print("resalgoII: "+str(res2))
    starttime3 = timeit.default_timer()
    res3=glouton(S,k,V)
    print("The time difference is :", timeit.default_timer() - starttime3)
    print("resalgoIII: "+str(res3))
    f.close()
    #f1.close()
   
    os.remove("cap_rand.txt")
    #os.remove("cap_ex.txt")
    
    
def tempsS():
    S1=10
    k1=10
    d1=2
    s=10
   
    L=[]
    L1=[]
    L2=[]
    L3=[]
    for s in range(S1,S1**4,100):
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,s,k1,d1)
        f1= open('cap_ex.txt','r')
        (S,k,V)=lecture(f1)
        
        L.append(s)
        """if(s<101):
            starttime1 = timeit.default_timer()
            algo1(S,k,V)
            L1.append(np.log(timeit.default_timer() - starttime1))
        else :
            L1.append(0)"""
        
        starttime2 = timeit.default_timer()
        algo2(s,k1,V)
        L2.append(np.log(timeit.default_timer() - starttime2))
        
        """starttime3 = timeit.default_timer()
        glouton(S,k,V)
        L3.append(np.log(timeit.default_timer() - starttime3))"""
      
     
    #model=make_interp_spline(L, L1)
    #plt.plot(L,L1)
    plt.plot(L,L2)
    #plt.plot(L,L3)
  
    plt.xlabel('quantité de confiture S (en dg)')
    plt.ylabel('temps(en ms)')
    plt.show()

def tempsk():
    #S=2**30+15
    k1= 100
    d1=2
    s=500
   
    L=[]
    L1=[]
    L2=[]
    L3=[]
    for k in range(1,k1,5):
        #S=d1**(k-1)
        S=500
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d1)
        f1= open('cap_ex.txt','r')
        (S,k,V)=lecture(f1)
        
        L.append(k)

        
        if(S<101):
            starttime1 = timeit.default_timer()
            algo1(S,k,V)
            L1.append((timeit.default_timer() - starttime1))
        else :
            L1.append(0)
        starttime2 = timeit.default_timer()
        algo2(S,k,V)
        L2.append((timeit.default_timer() - starttime2))
        
        starttime3 = timeit.default_timer()
        glouton(S,k,V)
        L3.append((timeit.default_timer() - starttime3))
      
     
    #model=make_interp_spline(L, L1)
    plt.plot(L,L1,'b')
    plt.plot(L,L2,'r')
    plt.plot(L,L3,'g')
    plt.xlabel('taille du tableau de capaité k')
    plt.ylabel('temps(en ms)')
    plt.show()

def tempsd(f):
    S=4**10+7
    k1= 10
    d3 = 4
    d1=2
    d2 = 3
    
   
    L=[]
    L1=[]
    L2=[]
    L3=[]
    for k in range(1,k1):
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d1)
        f1= open('cap_ex.txt','r')
        (S,k,V)=lecture(f1)
        
        L.append(k)
        
 
        
        starttime2 = timeit.default_timer()
        f(S,k,V)
        L1.append((timeit.default_timer() - starttime2))
        
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d2)
        f1= open('cap_ex.txt','r')
        
        (S,k,V)=lecture(f1)
        starttime3 = timeit.default_timer()
        f(S,k,V)
        L2.append((timeit.default_timer() - starttime3))
      
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d3)
        f1= open('cap_ex.txt','r')
        
        (S,k,V)=lecture(f1)
        starttime3 = timeit.default_timer()
        f(S,k,V)
        L3.append((timeit.default_timer() - starttime3))
     
    #model=make_interp_spline(L, L1)
    plt.plot(L,L1,'r')
    plt.plot(L,L2,'g')
    plt.plot(L,L3,'b')
    plt.xlabel('taille du tableau de capaité k')
    plt.ylabel('temps(en ms)')
    plt.show()
    
    
    
    
def tempsd1(f):
    S1=3000
    k= 6
    d3 = 4
    d1=2
    d2 = 3
    
   
    L=[]
    L1=[]
    L2=[]
    L3=[]
    for S in range(1,S1,20):
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d1)
        f1= open('cap_ex.txt','r')
        (S,k,V)=lecture(f1)
        
        L.append(S)
        
 
        
        starttime2 = timeit.default_timer()
        f(S,k,V)
        L1.append((timeit.default_timer() - starttime2))
        
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d2)
        f1= open('cap_ex.txt','r')
        
        (S,k,V)=lecture(f1)
        starttime3 = timeit.default_timer()
        f(S,k,V)
        L2.append((timeit.default_timer() - starttime3))
      
        f1= open('cap_ex.txt','w+')
        genere_cap_ex(f1,S,k,d3)
        f1= open('cap_ex.txt','r')
        
        (S,k,V)=lecture(f1)
        starttime3 = timeit.default_timer()
        f(S,k,V)
        L3.append((timeit.default_timer() - starttime3))
     
    #model=make_interp_spline(L, L1)
    plt.plot(L,L1,'r')
    plt.plot(L,L2,'g')
    plt.plot(L,L3,'b')
    plt.xlabel('quantité de confiture S')
    plt.ylabel('temps(en ms)')
    plt.show()
    
    
    

def prop_glouton():
    L=[]
    M=100
    K=30
    Lk=[]
    Lp=[]
    L1=[]
    for ki in range(K):
        Lk.append(ki)
        
        L=[]
        for i in range(M):
            f= open('cap_rand.txt','w')
            genere_cap_rand(f,s,ki)
            f= open('cap_rand.txt','r')
            (S,ki,V)=lecture(f)
            L.append(test_glouton_compatible(ki-1,V))
        Lp.append(L.count(1)/100.0)
    plt.xlabel('taille du tableau de capacité k')
    plt.ylabel('proportion de tableau glouton-compatible')
    plt.plot(Lk,Lp)
    
    plt.show()
    
    

def derniere_question():
    Lk=[]
    pmax=10
    fo=20
    k=25
    m=0
    
    moy=0.0
    Lmax=[]
    Lmoy=[]
    d=(float)(fo*pmax-pmax)
    #for ki in range (1,k):
    for s in range(pmax,fo*pmax,1):
        Lk.append(s)
        f= open('cap_rand.txt','w')
        genere_cap_rand(f,s,k)
        f= open('cap_rand.txt','r')
        (s,k,V)=lecture(f)
        for i in range(100):
            
            if (test_glouton_compatible(k-1,V)==0):
                x =glouton(s,k,V)-algo2(s,k,V)
                if x>m:
                    m=x
                moy = moy+x
            #print(m)
        Lmax.append(m)
        Lmoy.append(moy/d)
        print(moy/d)
    #plt.plot(Lk,Lmax)
    plt.xlabel('S')
    plt.ylabel('moyenne des différences entre algoII et glouton')
    plt.plot(Lk,Lmoy)
    plt.show()
        
 
            
            

#test()
#tempsS()
#tempsk()
#tempsd1(algo2)
#prop_glouton()
derniere_question()
