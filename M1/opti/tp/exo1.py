import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 1

xl = [-5, 5]
yl = [-5, 5]

x0 = 2
y0 = 2

n = 10

def f(x,y):
    return 1/2*a*x*x + 1/2*b*y*y
    
def values_f(f, n, xl, yl):
    [x1, x2] = xl
    [y1, y2] = yl
    x = np.linspace(x1, x2, n)
    y = np.linspace(y1, y2, n)
    [X, Y] = np.meshgrid(x, y)
    Z = f(X, Y)
    return (X,Y,Z)
    
def level_ligne(f, n, xl, yl):
    
    (X,Y,Z) = values_f(f, n, xl, yl)
    plt.contour(X, Y, Z)
    plt.show()

def gradient_f(Z):
     return np.gradient(Z)



def plot_grad(f, n, xl, yl, x0, y0):
    (X,Y,Z) = values_f(f, n, xl, yl)
    g =  gradient_f(Z)
    plt.contour(X, Y, Z)
    plt.quiver(X, Y, g[1], g[0])
    plt.show()
    
    
# level_ligne(f, n, xl, yl)
# plot_grad(f, n, xl, yl, x0, y0)