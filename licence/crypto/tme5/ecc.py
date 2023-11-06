# Sorbonne Université LU3IN024 2021-2022
# TME 5 : Cryptographie à base de courbes elliptiques
#
# Etudiant.e 1 : NOM ET NUMERO D'ETUDIANT
# Etudiant.e 2 : NOM ET NUMERO D'ETUDIANT

from math import sqrt
import matplotlib.pyplot as plt
from random import randint

# Fonctions utiles

def exp(a, N, p):
    """Renvoie a**N % p par exponentiation rapide."""
    def binaire(N):
        L = list()
        while (N > 0):
            L.append(N % 2)
            N = N // 2
        L.reverse()
        return L
    res = 1
    for Ni in binaire(N):
        res = (res * res) % p
        if (Ni == 1):
            res = (res * a) % p
    return res


def factor(n):
    """ Return the list of couples (p, a_p) where p is a prime divisor of n and
    a_p is the p-adic valuation of n. """
    def factor_gen(n):
        j = 2
        while n > 1:
            for i in range(j, int(sqrt(n)) + 1):
                if n % i == 0:
                    n //= i
                    j = i
                    yield i
                    break
            else:
                if n > 1:
                    yield n
                    break

    factors_with_multiplicity = list(factor_gen(n))
    factors_set = set(factors_with_multiplicity)

    return [(p, factors_with_multiplicity.count(p)) for p in factors_set]


def inv_mod(x, p):
    """Renvoie l'inverse de x modulo p."""
    return exp(x, p-2, p)


def racine_carree(a, p):
    """Renvoie une racine carrée de a mod p si p = 3 mod 4."""
    assert p % 4 == 3, "erreur: p != 3 mod 4"

    return exp(a, (p + 1) / 4, p)


# Fonctions demandées dans le TME

def est_elliptique(E):
    """
    Renvoie True si la courbe E est elliptique et False sinon.

    E : un triplet (p, a, b) représentant la courbe d'équation
    y^2 = x^3 + ax + b sur F_p, p > 3
    """
    (p,a,b) = E
    return ((4*(exp(a,3,p)) + 27*(exp(b, 2, p))))%p!= 0 and p>3


def point_sur_courbe(P, E):
    """Renvoie True si le point P appartient à la courbe E et False sinon."""
    (p,a,b) = E
    if P == () :
        return True
    (x,y) = P
    return (y*y) % p== (x*x*x + a*x+b) %p

def symbole_legendre(a, p):
    """Renvoie le symbole de Legendre de a mod p."""


    
    return exp(a,(p-1)//2,p)


def cardinal(E):
    """Renvoie le cardinal du groupe de points de la courbe E."""
    (p,a,b) = E
    cpt  = 1
    for i in range(p):
        temp = symbole_legendre((i*i*i+a*i+b)%p,p)
        if(temp==1):
            cpt = cpt+2
        elif (temp==0):
            cpt = cpt+1

    return cpt


def liste_points(E):
    """Renvoie la liste des points de la courbe elliptique E."""
    p, a, b = E

   # assert p % 4 == 3, "erreur: p n'est pas congru à 3 mod 4."
    Lres = [()]
    for i in range(p) :
        y_square = (i*i*i+a*i+b)%p
        temp = symbole_legendre(y_square,p)
        if (temp ==1) :
            y = exp(y_square,(p+1)//4,p)
            Lres.append((i,y))
            Lres.append((i,-y))
        elif (temp==0):
            Lres.append((i,0))
    return Lres


def cardinaux_courbes(p):
    """
    Renvoie la distribution des cardinaux des courbes elliptiques définies sur F_p.

    Renvoie un dictionnaire D où D[i] contient le nombre de courbes elliptiques
    de cardinal i sur F_p.
    """
    D = {}
    for i in range((int)(1+p+1-2*sqrt(p)),(int)(p+1+2*sqrt(p)+1)):
        D[i] = 0
   
    for a in range(p) :
        for b in range(p) :
            if est_elliptique((p,a,b)) :
                E = (p,a,b)
                
                j = cardinal((p,a,b))
                if j in D:
                    D[j] += 1#D[j]+1
                else:
                    D[j]=1
    print(D)
    return D


def dessine_graphe(p):
    """Dessine le graphe de répartition des cardinaux des courbes elliptiques définies sur F_p."""
    bound = int(2 * sqrt(p))
    C = [c for c in range(p + 1 - bound, p + 1 + bound + 1)]
    D = cardinaux_courbes(p)

    plt.bar(C, [D[c] for c in C], color='b')
    plt.show()


def moins(P, p):
    """Retourne l'opposé du point P mod p."""
    x1,y1 = P
    if x1<0:
        x1 = x1 - p*x1
    if y1<0:
        x2 = x2 - p*x2
    return x1%p,-(y1%p)


def est_egal(P1, P2, p):
    """Teste l'égalité de deux points mod p."""
    if (P1==() and P2 == ()):
            return True
    else:
        if P1==():
            return False
        if P2==():
            return False
    x1,y1 = P1
    x2,y2 = P2
    if x1<0:
        x1 = x1 - p*x1
    if x2<0:
        x2 = x2 - p*x2
    if y1<0:
        y1 = y1 - p*y1
    if y2<0:
        y2 = y2 - p*y2
    return (x1%p == x2%p) and (y1%p == y2%p)


def est_zero(P):
    """Teste si un point est égal au point à l'infini."""
    
    return P==()


def addition(P1, P2, E):
    """Renvoie P1 + P2 sur la courbe E."""
    p, a, b = E
    if est_zero(P1):
        return P2
    if est_zero(P2):
        return P1
    print("p1")
    print(P1)
    x1,y1 = P1
    x2,y2 = P2
    P3 = (x2,-y2)
    if est_egal(P1,P3,p):
        return ()
    x2,y2 = P2
    if est_egal(P1,P2,p):
        L = (((3*x1*x1)+a))*inv_mod((2*y1),p)
        
    else:
        L = (y2-y1)*inv_mod((x2-x1),p)
    
    x3 = L*L-x1-x2
    if x3<0:
        x3 = x3 - p*x3
    x3 = x3%p
    y3 = L*(x1-x3)-y1
    if y3<0:
        y3 = y3 - p*y3
    return (x3,y3%p)


def multiplication_scalaire(k, P, E):
    """Renvoie la multiplication scalaire k*P sur la courbe E."""
    res = ()
    p, a, b = E
    if k<0:
        P = moins(P,p)
    k = abs(k)
    cpt = 0
    for ki in bin(abs(k)):
        if cpt>=2:
            print(res)
            print(cpt)
            res = addition(res,res,E)
            if ki=='1':
                res = addition(res,P,E)
        cpt = cpt+1

    return res




def diviseur (L, L_tmp):

    if L == []:
        res = 1
        for elt in L_tmp :
            res = res* elt[0]**elt[1]
        return [res]
    else :
        L_res = []
        (n,p) = L[0]
        for i in range(p+1):
            L_res = L_res+diviseur(L[1:],L_tmp+[(n,i)])
        return L_res


def ordre(N, factors_N, P, E):
    """Renvoie l'ordre du point P dans les points de la courbe E mod p. 
    N est le nombre de points de E sur Fp.
    factors_N est la factorisation de N en produit de facteurs premiers."""

    Lfactor = list(factors_N)
    if(est_zero(P)):
        return 1
    ordre = 0 
   
    Ld = diviseur(Lfactor,[])
    temp = 0
    vu = False
    mult = 0

    Ld.sort()
    for elt in Ld :
    
        if vu:
            
            k = elt-temp
            mult = addition(mult,multiplication_scalaire(k,P,E),E)
            temp = elt
           
            
        else :
            mult = multiplication_scalaire(elt,P,E)
            temp = elt
            vu = True 
        
        if est_zero(mult) :
            print("fini")
            return elt
            
    print("erreur, pas d'ordre trouvé")

    return -1
def point_aleatoire_naif(E):
    """Renvoie un point aléatoire (différent du point à l'infini) sur la courbe E."""
    p, a, b = E
    x = randint()
    y = randint()
    P = (x,y)
    while point_sur_courbe(P,E)==False:
        x = randint()
        y = randint()
        P = (x,y)
    
    return P


def point_aleatoire(E):
    """Renvoie un point aléatoire (différent du point à l'infini) sur la courbe E."""
    temp = -1
    p, a, b = E
    while True :
        i = randint(0,p-1)
        y_square = (i*i*i+a*i+b)%p
        temp = symbole_legendre(y_square,p)
        if (temp ==1) :
            y = exp(y_square,(p+1)//4,p)
            e = randint(1,2)
            if e==1:
                return (i,y)
            else:
                return (i,-y)
        elif (temp==0):
            return (i,0)
    


def point_ordre(E, N, factors_N, n):
    """Renvoie un point aléatoire d'ordre N sur la courbe E.
    Ne vérifie pas que n divise N."""
    L = []
    Lfactor=list(factors_N)
    print("f")
    P = point_aleatoire(E)
    print(P)
    l=N
    print("f")
    while (ordre(N, Lfactor, P, E)!=n) and (len(L)!=l):
        print("f")
        if P not in L: 
            L.append(P)
        P = point_aleatoire(E)
    if ordre(N, Lfactor, P, E)!=n:
        print("pas de point d'ordre n")
        return ()
    return P

def keygen_DH(P, E, n):
    """Génère une clé publique et une clé privée pour un échange Diffie-Hellman.
    P est un point d'ordre n sur la courbe E.
    """
    p, a, b = E
    sec = randint(1,n-1)
    pub = multiplication_scalaire(sec,P,E)
    
    return (sec, pub)

def echange_DH(sec_A, pub_B, E):
    """Renvoie la clé commune à l'issue d'un échange Diffie-Hellman.
    sec_A est l'entier secret d'Alice et pub_b est l'entier public de Bob."""
    

    return multiplication_scalaire(sec_A,pub_B,E)
