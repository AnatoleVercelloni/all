import matplotlib.pyplot as plt
import numpy as np



u = np.array([1, 2, 3, 4])
v = np.array([-1, 0, 1, 2])
w = np.array([2, -2, 1, 0])

# print("uv^t = ")
# print( np.outer(u, np.transpose(v)))


# print("u^tw = ")
# print( np.outer(np.transpose(u), w))


# print("norm2(u) = "+ "", np.linalg.norm(u,2))

# print("norm1(u) = "+ "", np.linalg.norm(v,1))


# print("norm1(u) = "+ "", np.linalg.norm(u-v,np.inf))

n = 4

zeros = np.zeros(n)
ide = np.eye(n)
ones = np.ones(n)
diag = np.diag(u)

A = np.diag(np.ones(4)*2) + np.diag(-1*np.ones(3), -1) + np.diag(-1*np.ones(3), 1)
B = np.diag(-1*np.ones(3), -1) + np.diag(1*np.ones(3), 1) + np.diag(-2*np.ones(2), -2) + np.diag(2*np.ones(2), 2) + np.diag(-3*np.ones(1), -3) + np.diag(3*np.ones(1), 3)


# for i in range(0, int(n/2)):
    # B += np.diag(i*np.ones(n-i), i) 
    # B += np.diag(-i*np.ones(n-i), -i) 

# print(B)

detA = np.linalg.det(A)
detB = np.linalg.det(B)


detA = np.linalg.eig(A)
detB = np.linalg.eig(B)

C = np.block([[A, B],[ np.transpose(B), A]])

detC = np.linalg.det(C)

# print(np.block([[A, B],[ np.transpose(B), A]]))

def X_ij(n):
    X = np.zeros(n)
    for i in range(n):
        for j in range(n):
            X[i,j] = 2**(i-j)
    return X
    

def X_ij2(n):
    X = np.zeros(n)
    for i in range(n):
        for j in range(n):
            X[i,j] = 1/(i + j + 1)
    return X
    

un = np.random.rand(n)
for i in range(20):
   a = np.linalg.norm(A.dot(un))
   # print(a)
   nun = 1/a*A.dot(un)
   un = nun
   
   

t = 5

def ft(x):
    return np.sin(x - t)
n = 100
L = np.linspace(0, 2*np.pi, n)
# plt.plot(L, ft(L))


# for t in range(4): 
    # plt.plot(L, ft(L))
# plt.show()


h = 1/(n + 1)

def buildAh(n):
    h = 1/(n + 1)
    return 1/h**2*np.diag(2*np.ones(n)) + np.diag(-1*np.ones(n-1), -1)+ np.diag(-1*np.ones(n-1), 1)

Ah = buildAh(n)

e = np.linalg.eig(Ah)

Lc = np.zeros(n)

for i in range(2, n):
    Ah = buildAh(i)

    Lc[i] = np.linalg.cond(Ah)

# plt.loglog(Lc)
# plt.show()






# for i in range(5, 20, 5):
    # Lk = np.array(i)
    # b = np.ones((i,1))
    # Ah = buildAh(i)
    # u = np.linalg.solve(Ah, b)
    # plt.plot(Lk*h, u)

# plt.show() 



def f(x):
    return np.sin(2*np.pi*x)
 
def df(x):
    return 2*np.pi*np.cos(2*np.pi*x)
    
def dfplus(x):
    return (f(x + h) - f(x))/h
    
def dfmoins(x):
    return (f(x - h) - f(x))/h
    
def dfzero(x):
    return (f(x + h) - f(x - h))/2*h
    
X = np.linspace(-1, 1, 1000)

h = 0.05

Lh = np.linspace(0.001, 0.1, 20)

plt.plot(X, df(X))
plt.plot(X, dfplus(X))
plt.plot(X, dfmoins(X))
plt.plot(X, dfzero(X))

plt.show()
def maxe()
    e = 0
    for x in X:
        em = (abs(df(x) - dfplus(x)))
        if em > e:
            e = em

for h in Lh:
    maxe
    