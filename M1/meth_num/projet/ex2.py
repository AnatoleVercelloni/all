import matplotlib.pyplot as plt
import numpy as np

from scipy import linalg
from numpy.linalg import *


Nxmax = 999
Ntmax = 999
nu = 0.01
gamma = 10

def matrix_b(nt, dt, Uh):
    #building of the matrix B
	b = np.diag(dt*gamma*Uh)
	return b

def matrix_af(nt, Uh):
    #building of A and F
	nx = len(Uh)
	dx = 1/(nx+1)
	dt = 1/nt
	l = nu*dt/(dx*dx)
	a = np.zeros((nx,nx))
	f = np.zeros(nx)
	a = np.diag(np.ones(nx)*(1+2*l-gamma*dt)) + np.diag(np.ones(nx-1)*-l, k=1) + np.diag(np.ones(nx-1)*-l, k=-1)

	return a, f
	


def u0(x):
    #initial condition
	return 0.25*np.sin(np.pi*x)*np.exp(-20*(x-0.5)**2)
    
   

def scheme1(Nt, Nx):
    #numerical solving of the problem
    dx = 1/(Nx+1)
    dt = 1/(Nt)
    X = np.array([dx*i for i in range(Nx+1)])
    #X: space discretization
    Uh = u0(X) #at t= 0 Uh = u0(X)
    (A,F) = matrix_af(Nt, Uh) 
    for t in range(Nt+1): # at each time we update B (depend of Uh) and Uh
        if (t%5 == 0):
             plt.plot(X, Uh)
        B = matrix_b(Nt, dt, Uh)
        nUh = linalg.solve((A+B),Uh) #this solve (A+B)X = Uh
        Uh = nUh
    plt.plot(X, Uh)
    plt.show()
    plt.savefig("approximation.png")        
    return (X,Uh)    

    
def solve1():
    #we applied the scheme with a large Nt and Nx
    #and we assume that this is the exact solution
    Nt = Ntmax
    _Nx = Nxmax
    _dx = 1/(_Nx+1)
    dt = 1/(Nt)
    _X = np.array([_dx*i for i in range(_Nx+1)])
    _Uh = u0(_X)
    (_A,_F) = matrix_af(Nt, _Uh)
    for t in range(Nt+1):
        print(" tour ",t,"\n")
        _B = matrix_b(Nt, dt, _Uh)
        _nUh = linalg.solve((_A+_B),_Uh)
        _Uh = _nUh    
    return (_X,_Uh)    
    


def errorspace1():
    #We want to study the convergence of the scheme
    #this function compute the 2,delta and the inf,delta norm
    #for different value of Nx 
    L = [ 4, 49, 99, 199, 499]
    E_inf = list()
    E_2 = list()
    Nt = Ntmax
    dt = 1/(Nt)
    for nx in L: #we compute the error for ech nx
        print("nx: ",nx)
        einf = 0.0
        e2 = 0.0
        step = (int)((Nxmax+1)/(nx+1)) #this is to compare the to vector of different sizes
        print ("step: ",step,"\n")
        dx = 1/(nx+1)
        #_x is for something related to the "exact solution"
        _Nx = Nxmax
        _dx = 1/(_Nx+1)
        X = np.array([dx*i for i in range(nx+1)])
        Uh = u0(X)
        nUh= Uh
        (A,F) = matrix_af(Nt, Uh)
        _X = np.array([_dx*i for i in range(_Nx+1)])
        _Uh = u0(_X)
        _nUh = _Uh
        (_A,_F) = matrix_af(Nt, _Uh)
        for i in range (Nt+1):  #for each time, we update Uh and _UhS
            dif = np.zeros(len(Uh))
            for j in range(nx+1):
                dif[j] = Uh[j] - _Uh[j*step]  #this is to compute the norm of the difference
            # print("diff", dif)
            B = matrix_b(Nt, dt, Uh)
            nUh = linalg.solve((A+B),Uh)
            Uh = nUh
            _B = matrix_b(Nt, dt, _Uh)
            _nUh = linalg.solve((_A+_B),_Uh)
            _Uh = _nUh   
            N2 = np.sqrt(dx)*np.linalg.norm(dif,2) #for the 2, delta norm
            Ninf = np.linalg.norm(dif,np.inf)       #for the inf,delta norm
            print("Ninf", Ninf)
            if (N2>e2):     #we take the max over all the time step
                e2 = N2
            if (Ninf>einf): #same here
                einf = Ninf
        E_2.append(e2)
        E_inf.append(einf)
        #the comment part just here is to plot 
        #the comparaison with the "exact" solution for each nx
        # plt.plot(_X, _Uh)
        # plt.plot(X, Uh)
        # plt.show()
        # plt.savefig("comp sol with nmax= "+str(nx)) #
        # plt.clf()
    print("E_2  = ",E_2, "\n")
    print("E_inf  = : ",E_inf, "\n")
    plt.plot(L,E_2)
    plt.plot(L,E_inf)
    plt.show()
    plt.savefig("error.png") #and here we plot the evolution of the error
                
            
def errortime1():
    #We want to study the convergence of the scheme
    #this function compute the 2,delta and the inf,delta norm
    #for different value of Nx 
    L = [ 9,49, 99, 199, 499]
    E_inf = list()
    E_2 = list()
    Nx = Nxmax
    dx = 1/(Nx+1)
    _Nt = Ntmax
    for nt in L: #we compute the error for ech nt
        print("nt: ",nt)
        einf = 0.0
        e2 = 0.0
        step = (int)((Ntmax+1)/(nt+1)) #this is to update Uh only once over step time
        print ("step: ",step,"\n")
        dt = 1/(nt+1)
        #_x is for something related to the "exact solution"
        _Nt = Ntmax
        _Nx = Nxmax
        _dx = 1/(_Nx+1)
        _dt = 1/(_Nt)
        X = np.array([dx*i for i in range(Nx+1)])
        Uh = u0(X)
        nUh= Uh
        (A,F) = matrix_af(nt, Uh)
        _X = np.array([_dx*i for i in range(_Nx+1)])
        _Uh = u0(_X)
        _nUh = _Uh
        (_A,_F) = matrix_af(_Nt, _Uh)
        for i in range (_Nt+1):  #for each time, we update Uh and _UhS
            dif = np.zeros(len(Uh))
            if (i%step == 0): #we update Uh only if the time correspond to an equivalent time for _Uh
                for j in range(Nx+1):
                    dif[j] = Uh[j] - _Uh[j]  #this is to compute the norm of the difference
                    # print("diff", dif)
                N2 = np.sqrt(dx)*np.linalg.norm(dif,2) #for the 2, delta norm
                Ninf = np.linalg.norm(dif,np.inf)       #for the inf,delta norm
                if (N2>e2):     #we take the max over all the time step
                    e2 = N2
                if (Ninf>einf): #same here
                    einf = Ninf
                print("Ninf", Ninf)
                B = matrix_b(nt, dt, Uh)
                nUh = linalg.solve((A+B),Uh)
                Uh = nUh
            _B = matrix_b(_Nt, _dt, _Uh)
            _nUh = linalg.solve((_A+_B),_Uh)
            _Uh = _nUh   
           
        E_2.append(e2)
        E_inf.append(einf)
        #the comment part just here is to plot 
        #the comparaison with the "exact" solution for each nx
        # plt.plot(_X, _Uh)
        # plt.plot(X, Uh)
        # plt.show()
        # plt.savefig("comp sol with nmax= "+str(nx)) #
        # plt.clf()
    print("E_2  = ",E_2, "\n")
    print("E_inf  = : ",E_inf, "\n")
    plt.plot(L,E_2)
    plt.plot(L,E_inf)
    plt.show()
    plt.savefig("errortime1.png") #and here we plot the evolution of the error            
        
        
 

def error1():
    #We want to study the convergence of the scheme
    #this function compute the 2,delta and the inf,delta norm
    #for different value of Nx 
    #this function is a union of errortime and errorspace
    Lx = [ 4, 49, 99, 199, 499]
    Lt = [ 49, 99, 199, 499]
    _Nx = Nxmax
    _dx = 1/(_Nx+1)
    _Nt = Ntmax
    _dt = 1/_Nt
    for nt in Lt:
        E_inf = list()
        E_2 = list()
        dt = 1/(nt)
        print("nt: ", nt)
        stept = (int)((Ntmax+1)/(nt+1)) 
        print ("stept: ",stept,"\n")
        for nx in Lx: #we compute the error for ech nx
            print("nx: ",nx)
            einf = 0.0
            e2 = 0.0
            stepx = (int)((Nxmax+1)/(nx+1)) #this is to compare the to vector of different sizes
            print ("stepx: ",stepx,"\n")
            dx = 1/(nx+1)
            #_x is for something related to the "exact solution"
            X = np.array([dx*i for i in range(nx+1)])
            Uh = u0(X)
            nUh= Uh
            (A,F) = matrix_af(nt, Uh)
            _X = np.array([_dx*i for i in range(_Nx+1)])
            _Uh = u0(_X)
            _nUh = _Uh
            (_A,_F) = matrix_af(_Nt, _Uh)
            for i in range (_Nt+1):  #for each time, we update Uh and _UhS
                dif = np.zeros(len(Uh))
                if (i%stept == 0):
                    for j in range(nx+1):
                        dif[j] = Uh[j] - _Uh[j*stepx]  #this is to compute the norm of the difference
                    # print("diff", dif)
                    N2 = np.sqrt(dx)*np.linalg.norm(dif,2) #for the 2, delta norm
                    Ninf = np.linalg.norm(dif,np.inf)       #for the inf,delta norm
                    print("Ninf", Ninf)
                    if (N2>e2):     #we take the max over all the time step
                        e2 = N2
                    if (Ninf>einf): #same here
                        einf = Ninf
                    B = matrix_b(nt, dt, Uh)
                    nUh = linalg.solve((A+B),Uh)
                    Uh = nUh
                _B = matrix_b(_Nt, _dt, _Uh)
                _nUh = linalg.solve((_A+_B),_Uh)
                _Uh = _nUh   
               
            E_2.append(e2)
            E_inf.append(einf)
            #the comment part just here is to plot 
            #the comparaison with the "exact" solution for each nx
            # plt.plot(_X, _Uh)
            # plt.plot(X, Uh)
            # plt.show()
            # plt.savefig("comp sol with nmax= "+str(nx)) #
            # plt.clf()
        print("E_2  = ",E_2, "\n")
        print("E_inf  = : ",E_inf, "\n")
        plt.plot(Lx,E_2)
        # plt.plot(Lx, E_inf)
    plt.legend(Lt)
    plt.show()
    plt.savefig("error1.png") #and here we plot the evolution of the error 
# scheme1(100,100)
# errorspace1()
# errortime1()
# error1()
# solve1()