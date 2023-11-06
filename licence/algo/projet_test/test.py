from algo import*
nomf='cap_rand.txt'

def test():
    s=100
    k=10
    d=3
    genere_cap_rand(nomf,s,k)
    print(algo1(nomf))
    print(algo2(nomf))
    print(glouton(nomf))
    
    
test()