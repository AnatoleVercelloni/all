import matplotlib.pyplot as plt
import numpy as np

from scipy import linalg
from numpy.linalg import *
from ex2 import *

Nxmax = 999
Ntmax = 999
nu = 0.01
gamma = 10

def matrix(Nt, Uh):
    #building of the matrix A (for the diffusion step)
    Nx = len(Uh)
    dt = 1/(Nt)
    dx = 1/(Nx+1)
    l = nu*dt/(4*dx*dx)
    A = np.zeros((Nx,Nx))
    A = np.diag(np.ones(Nx)*(1+2*l)) + np.diag(np.ones(Nx-1)*-l, k=1) + np.diag(np.ones(Nx-1)*-l, k=-1)
    return A
    


def diffusion_step(Uh, A):
    #the diffusion step
     return np.linalg.solve(A, Uh)
     
def reaction_step(Uh, dt):
    #the reaction step
    nUh = np.zeros(len(Uh))
    for i in range(len(Uh)):
        #we take y s.t. Uh[i] = dt*gamma*x^2 + x(-dt*gamma+1) 
        nUh[i] = (dt*gamma - 1 + np.sqrt(dt*dt*gamma*gamma+1-2*dt*gamma+4*Uh[i]*dt*gamma))/(2*dt*gamma)
    return nUh
        
    
def scheme2(Nx, Nt):
    #numerical solving of the problem with strang splitting
    dx = 1/(Nx+1)
    X = np.array([dx*i for i in range(Nx+1)])
    Uh = u0(X)
    A = matrix(Nt, Uh)
    nUh = Uh
    dt = 1/(Nt)
    for t in range(Nt+1):	
        if (t%5 == 0):
             plt.plot(X, Uh)
        nUh = diffusion_step(Uh, A)#one half diffusion step
        Uh = nUh
        nUh = reaction_step(Uh, dt)#one reaction step
        Uh = nUh
        nUh = diffusion_step(Uh, A)#one half diffusion step
        Uh = nUh
    plt.plot(X, Uh)
    plt.show()
    plt.savefig("approximation3.png")
    return (X, Uh)
    
def solve2():
    #we applied the scheme with a large Nt and Nx
    #and we assume that this is the exact solution
    Nt = Ntmax
    _Nx = Nxmax
    _dx = 1/(_Nx+1)
    dt = 1/(Nt)
    _X = np.array([_dx*i for i in range(_Nx+1)])
    _Uh = u0(_X)
    _A = matrix(Nt, _Uh)
    for t in range(Nt+1):
        print(" tour ",t,"\n")
        _nUh = diffusion_step(_Uh, _A)#one half diffusion step
        _Uh = _nUh
        _nUh = reaction_step(_Uh, dt)#one reaction step
        _Uh = _nUh
        _nUh = diffusion_step(_Uh, _A)#one half diffusion step
        _Uh = _nUh
    return (_X,_Uh)    
    
def errorspace2():
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
        A = matrix(Nt, Uh)
        _X = np.array([_dx*i for i in range(_Nx+1)])
        _Uh = u0(_X)
        _nUh = _Uh
        _A = matrix(Nt, _Uh)
        for i in range (Nt+1):  #for each time, we update Uh and _UhS
            dif = np.zeros(len(Uh))
            for j in range(nx+1):
                dif[j] = Uh[j] - _Uh[j*step]  #this is to compute the norm of the difference
            # print("diff", dif)
            nUh = diffusion_step(Uh, A)#one half diffusion step
            Uh = nUh
            nUh = reaction_step(Uh, dt)#one reaction step
            Uh = nUh
            nUh = diffusion_step(Uh, A)#one half diffusion step
            Uh = nUh
            _nUh = diffusion_step(_Uh, _A)#one half diffusion step
            _Uh = _nUh
            _nUh = reaction_step(_Uh, dt)#one reaction step
            _Uh = _nUh
            _nUh = diffusion_step(_Uh, _A)#one half diffusion step
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


def errortime2():
    #We want to study the convergence of the scheme
    #this function compute the 2,delta and the inf,delta norm
    #for different value of Nx 
    L = [ 49, 99, 199, 499]
    E_inf = list()
    E_2 = list()
    Nx = Nxmax
    dx = 1/(Nx+1)
    _Nt = Ntmax
    for nt in L: #we compute the error for ech nx
        print("nt: ",nt)
        einf = 0.0
        e2 = 0.0
        step = (int)((Ntmax+1)/(nt+1)) 
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
        A = matrix(nt, Uh)
        _X = np.array([_dx*i for i in range(_Nx+1)])
        _Uh = u0(_X)
        _nUh = _Uh
        _A= matrix(_Nt, _Uh)
        for i in range (_Nt+1):  #for each time, we update Uh and _UhS
            dif = np.zeros(len(Uh))
            if (i%step == 0):
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
                nUh = diffusion_step(Uh, A)#one half diffusion step
                Uh = nUh
                nUh = reaction_step(Uh, dt)#one reaction step
                Uh = nUh
                nUh = diffusion_step(Uh, A)#one half diffusion step
                Uh = nUh
            _nUh = diffusion_step(_Uh, _A)#one half diffusion step
            _Uh = _nUh
            _nUh = reaction_step(_Uh, _dt)#one reaction step
            _Uh = _nUh
            _nUh = diffusion_step(_Uh, _A)#one half diffusion step
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
    plt.loglog(L,E_2)
    plt.loglog(L,E_inf)
    plt.show()
    plt.savefig("errortime2.png") #and here we plot the evolution of the error            
    
def error2():
    #We want to study the convergence of the scheme
    #this function compute the 2,delta and the inf,delta norm
    #for different value of Nx and Nt 
    #this function is an union of errortime and errorspace
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
        stept = (int)((Ntmax+1)/(nt+1)) #this is to update Uh only all the step time
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
            A = matrix(nt, Uh)
            _X = np.array([_dx*i for i in range(_Nx+1)])
            _Uh = u0(_X)
            _nUh = _Uh
            _A = matrix(_Nt, _Uh)
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
                    nUh = diffusion_step(Uh, A)#one half diffusion step
                    Uh = nUh
                    nUh = reaction_step(Uh, dt)#one reaction step
                    Uh = nUh
                    nUh = diffusion_step(Uh, A)#one half diffusion step
                    Uh = nUh
                _nUh = diffusion_step(_Uh, _A)#one half diffusion step
                _Uh = _nUh
                _nUh = reaction_step(_Uh, _dt)#one reaction step
                _Uh = _nUh
                _nUh = diffusion_step(_Uh, _A)#one half diffusion step
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
        # plt.plot(Lx,E_2)
        plt.plot(Lx, E_inf)
    plt.legend(Lt)
    plt.show()
    plt.savefig("error2norminf.png") #and here we plot the evolution of the error 
                        

    
    



# scheme2(100,100)
# solve2()
error2()